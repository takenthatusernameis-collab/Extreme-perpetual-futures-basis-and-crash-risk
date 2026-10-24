#!/usr/bin/env python3
import csv, hashlib, io, json, urllib.request, zipfile, os
from datetime import datetime, timezone, timedelta

BASE = "https://data.binance.vision/data"

def fetch(url):
    req = urllib.request.Request(url, headers={'User-Agent': 'EBCR-001'})
    with urllib.request.urlopen(req, timeout=30) as r:
        return r.read()

def fetch_kline_csv(data_zip):
    z = zipfile.ZipFile(io.BytesIO(data_zip))
    name = z.namelist()[0]
    txt = z.read(name).decode()
    rows = list(csv.reader(io.StringIO(txt)))
    data_rows = [r for r in rows if r and len(r) > 0 and r[0].lstrip('-').isdigit()]
    return data_rows

def median(xs):
    if not xs: return None
    s = sorted(xs)
    n = len(s)
    if n % 2 == 1:
        return s[n//2]
    return (s[n//2-1]+s[n//2])/2

def process_day(symbol, day):
    out = {"symbol": symbol, "date": day, "status": "ok", "hashes": {}}
    mark_med = idx_med = spot_med = um_med = None
    funding_med = None
    # spot
    try:
        url = f"{BASE}/spot/daily/klines/{symbol}/1d/{symbol}-1d-{day}.zip"
        d = fetch(url)
        rows = fetch_kline_csv(d)
        closes = [float(r[4]) for r in rows]
        spot_med = median(closes)
        out["spot_median"] = spot_med
        out["hashes"]["spot_sha256"] = hashlib.sha256(d).hexdigest()
    except Exception as e:
        out["spot_median"] = None; out["status"] = "incomplete"
        out["hashes"]["spot_sha256"] = None
    # um kline
    try:
        url = f"{BASE}/futures/um/daily/klines/{symbol}/1d/{symbol}-1d-{day}.zip"
        d = fetch(url)
        rows = fetch_kline_csv(d)
        closes = [float(r[4]) for r in rows]
        um_med = median(closes)
        out["um_kline_median"] = um_med
        out["hashes"]["um_sha256"] = hashlib.sha256(d).hexdigest()
    except Exception as e:
        out["um_kline_median"] = None; out["status"] = "incomplete"
        out["hashes"]["um_sha256"] = None
    # mark
    try:
        url = f"{BASE}/futures/um/daily/markPriceKlines/{symbol}/1d/{symbol}-1d-{day}.zip"
        d = fetch(url)
        rows = fetch_kline_csv(d)
        closes = [float(r[4]) for r in rows]
        mark_med = median(closes)
        out["mark_median"] = mark_med
        out["hashes"]["mark_sha256"] = hashlib.sha256(d).hexdigest()
    except Exception as e:
        out["mark_median"] = None; out["status"] = "incomplete"
        out["hashes"]["mark_sha256"] = None
    # index
    try:
        url = f"{BASE}/futures/um/daily/indexPriceKlines/{symbol}/1d/{symbol}-1d-{day}.zip"
        d = fetch(url)
        rows = fetch_kline_csv(d)
        closes = [float(r[4]) for r in rows]
        idx_med = median(closes)
        out["index_median"] = idx_med
        out["hashes"]["index_sha256"] = hashlib.sha256(d).hexdigest()
    except Exception as e:
        out["index_median"] = None; out["status"] = "incomplete"
        out["hashes"]["index_sha256"] = None
    # funding
    try:
        ym = day[:7]
        url = f"{BASE}/futures/um/monthly/fundingRate/{symbol}/{symbol}-fundingRate-{ym}.zip"
        d = fetch(url)
        fz = zipfile.ZipFile(io.BytesIO(d))
        ftxt = fz.read(fz.namelist()[0]).decode()
        frows = list(csv.reader(io.StringIO(ftxt)))
        header = frows[0]
        ci = header.index("calc_time") if "calc_time" in header else 0
        fi = header.index("last_funding_rate") if "last_funding_rate" in header else None
        day_funding = []
        for r in frows[1:]:
            if not r: continue
            try:
                ts = int(r[ci])
                dd = datetime.fromtimestamp(ts/1000, tz=timezone.utc).date().isoformat()
                if dd == day:
                    day_funding.append(float(r[fi]))
            except:
                pass
        funding_med = median(day_funding)
        out["funding_median"] = funding_med
        out["hashes"]["funding_sha256"] = hashlib.sha256(d).hexdigest()
    except Exception as e:
        out["funding_median"] = None; out["status"] = "incomplete"
        out["hashes"]["funding_sha256"] = None
    # basis
    if mark_med is not None and idx_med is not None:
        out["basis_pct"] = 100*(mark_med/idx_med - 1)
    else:
        out["basis_pct"] = None
    return out

def main():
    symbols = ["BNBUSDT","XRPUSDT","SOLUSDT","TRXUSDT","ZECUSDT","DOGEUSDT","LINKUSDT","ADAUSDT","XLMUSDT","NEARUSDT","BCHUSDT"]
    start = "2024-01-01"
    end = "2024-03-31"
    days = []
    cur = datetime.strptime(start,"%Y-%m-%d")
    endd = datetime.strptime(end,"%Y-%m-%d")
    alldates = []
    while cur <= endd:
        alldates.append(cur.strftime("%Y-%m-%d"))
        cur += timedelta(days=1)
    n = len(alldates)
    computations = []
    coverage = {}
    for sym in symbols:
        sym_ok = 0
        sym_total = 0
        for day in alldates:
            r = process_day(sym, day)
            computations.append(r)
            # count components
            for comp in ["mark_median","index_median","spot_median","um_kline_median","funding_median"]:
                sym_total += 1
                if r.get(comp) is not None:
                    sym_ok += 1
        coverage[sym] = {"ok_components": sym_ok, "total_components": sym_total, "coverage": sym_ok/sym_total if sym_total else 0, "meets_gate": (sym_ok/sym_total if sym_total else 0) >= 0.95}
    out = {
        "schema_version": "1.0",
        "program_id": "EBCR-001",
        "generated_at_utc": datetime.now(timezone.utc).isoformat(),
        "source": "S3 daily klines + monthly funding (free public)",
        "symbols": symbols,
        "window": {"start": start, "end": end},
        "coverage_gate": 0.95,
        "basis_computations": computations,
        "coverage": coverage,
        "status": "ok" if all(coverage[s]["meets_gate"] for s in symbols) else "blocked",
    }
    path = "research_state/basis_computation_q1_all.json"
    with open(path,"w") as f:
        json.dump(out, f)
    print(json.dumps({"status": out["status"], "coverage": {s: coverage[s]["coverage"] for s in symbols}, "n": len(computations), "path": path}, indent=2))

if __name__ == "__main__":
    main()
