#!/usr/bin/env python3
import urllib.request
"""Extended-window public-data ingestion for EBCR-001.

Free public source: Binance Public Data Archive (data.binance.vision).
Spot and UM daily klines via monthly ZIPs; mark and index price klines via
daily ZIPs; funding via monthly ZIPs. UTC daily medians; no forward fill, no
interpolation, no synthesis. Writes per-symbol checkpoints plus
research_state/ingestion_extended_v1.json (experiment EBCR-001-EXTENDED-V1).
Q1 artifacts are never modified.
"""
import csv, hashlib, io, json, time, zipfile
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone, timedelta
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
STATE = ROOT / "research_state"
CKPT_DIR = STATE / "ingest_extended_window"
SUMMARY_OUT = STATE / "ingestion_extended_v1.json"
BASE = "https://data.binance.vision/data"
EXPERIMENT_ID = "EBCR-001-EXTENDED-V1"
CONFIG = ROOT / "configs" / "basis_crash_grid_v1.json"
SYMBOLS = ["ADAUSDT", "BCHUSDT", "BNBUSDT", "DOGEUSDT", "LINKUSDT", "NEARUSDT", "SOLUSDT", "TRXUSDT", "XLMUSDT", "XRPUSDT", "ZECUSDT"]
START_DAY = "2023-01-01"
END_DAY = "2024-04-30"
COMPONENTS = ["spot", "um", "mark", "index", "funding"]
WORKERS = 3
MONTH_WORKERS = 2
RETRIES = 5
BACKOFF = [3, 6, 12]


def sha256_bytes(data):
    return hashlib.sha256(data).hexdigest()


def fetch_with_retries(url):
    last = None
    for attempt in range(RETRIES):
        try:
            req = urllib.request.Request(url, headers={'User-Agent': 'EBCR-001'})
            with urllib.request.urlopen(req, timeout=30) as r:
                return r.read()
        except Exception as e:
            last = e
            if attempt < RETRIES - 1:
                time.sleep(BACKOFF[attempt])
    raise last


def median(xs):
    if not xs:
        return None
    s = sorted(xs)
    n = len(s)
    if n % 2 == 1:
        return s[n // 2]
    return (s[n // 2 - 1] + s[n // 2]) / 2


def kline_rows(data):
    z = zipfile.ZipFile(io.BytesIO(data))
    txt = z.read(z.namelist()[0]).decode()
    rows = list(csv.reader(io.StringIO(txt)))
    return [r for r in rows if r and len(r) > 11 and r[0].lstrip('-').isdigit()], sha256_bytes(data)


def month_klines(kind, sym, ym):
    if kind == "spot":
        url = f"{BASE}/spot/monthly/klines/{sym}/1d/{sym}-1d-{ym}.zip"
    else:
        url = f"{BASE}/futures/um/monthly/klines/{sym}/1d/{sym}-1d-{ym}.zip"
    try:
        data = fetch_with_retries(url)
    except Exception as e:
        return {}, None, str(e)
    rows, sha = kline_rows(data)
    by_day = {}
    for r in rows:
        day = datetime.fromtimestamp(int(r[0]) / 1000, tz=timezone.utc).strftime("%Y-%m-%d")
        by_day.setdefault(day, []).append((float(r[3]), float(r[4])))
    return by_day, sha, None


def daily_price(kind, sym, day):
    if kind == "mark":
        url = f"{BASE}/futures/um/daily/markPriceKlines/{sym}/1d/{sym}-1d-{day}.zip"
    else:
        url = f"{BASE}/futures/um/daily/indexPriceKlines/{sym}/1d/{sym}-1d-{day}.zip"
    try:
        data = fetch_with_retries(url)
    except Exception as e:
        return {"status": "failed", "close": None, "low": None, "n_bars": 0, "raw_sha256": None, "error": str(e)}, None
    rows, sha = kline_rows(data)
    if not rows:
        return {"status": "failed", "close": None, "low": None, "n_bars": 0, "raw_sha256": sha, "error": "no_data_rows"}, sha
    r = rows[0]
    return {"status": "ok", "close": float(r[4]), "low": float(r[3]), "n_bars": len(rows), "raw_sha256": sha, "error": None}, sha


def funding_month(sym, ym):
    url = f"{BASE}/futures/um/monthly/fundingRate/{sym}/{sym}-fundingRate-{ym}.zip"
    try:
        data = fetch_with_retries(url)
    except Exception as e:
        return {}, None, str(e)
    z = zipfile.ZipFile(io.BytesIO(data))
    txt = z.read(z.namelist()[0]).decode()
    rows = list(csv.reader(io.StringIO(txt)))
    header = rows[0]
    ci = header.index("calc_time")
    fi = header.index("last_funding_rate")
    by_day = {}
    for r in rows[1:]:
        if not r:
            continue
        try:
            day = datetime.fromtimestamp(int(r[ci]) / 1000, tz=timezone.utc).strftime("%Y-%m-%d")
            by_day.setdefault(day, []).append(float(r[fi]))
        except Exception:
            pass
    return by_day, sha256_bytes(data), None


def comp_from_rows(rows, sha, error):
    if error or not rows:
        return {"status": "failed", "close": None, "low": None, "n_bars": 0, "raw_sha256": sha, "error": error or "no_data_rows"}
    closes = [c for _, c in rows]
    lows = [l for l, _ in rows]
    return {"status": "ok", "close": median(closes), "low": median(lows), "n_bars": len(rows), "raw_sha256": sha, "error": None}


def month_range(start_ym, end_ym):
    y, m = [int(x) for x in start_ym.split("-")]
    ey, em = [int(x) for x in end_ym.split("-")]
    out = []
    while (y, m) <= (ey, em):
        out.append(f"{y:04d}-{m:02d}")
        m += 1
        if m > 12:
            m = 1
            y += 1
    return out


def day_list(start, end):
    d = datetime.strptime(start, "%Y-%m-%d")
    endd = datetime.strptime(end, "%Y-%m-%d")
    out = []
    while d <= endd:
        out.append(d.strftime("%Y-%m-%d"))
        d += timedelta(days=1)
    return out


def atomic_write(path, obj):
    rendered = json.dumps(obj, indent=2, sort_keys=True) + "\n"
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text(rendered, encoding="utf-8")
    tmp.replace(path)


def process_day(sym, day, spot_maps, um_maps, fund_maps):
    ym = day[:7]
    s_by, s_sha, s_err = spot_maps.get(ym, ({}, None, None))
    u_by, u_sha, u_err = um_maps.get(ym, ({}, None, None))
    f_by, f_sha, f_err = fund_maps.get(ym, ({}, None, None))
    mark_rec, mark_sha = daily_price("mark", sym, day)
    index_rec, index_sha = daily_price("index", sym, day)
    spot_rec = comp_from_rows(s_by.get(day, []), s_sha, s_err)
    um_rec = comp_from_rows(u_by.get(day, []), u_sha, u_err)
    rates = f_by.get(day, [])
    fund_rec = {
        "status": "ok" if rates else "failed",
        "median": median(rates) if rates else None,
        "n_rates": len(rates),
        "raw_sha256": f_sha,
        "error": f_err or ("no_data_rows" if not rates else None),
    }
    comps = {"spot": spot_rec, "um": um_rec, "mark": mark_rec, "index": index_rec, "funding": fund_rec}
    basis = None
    if mark_rec.get("close") is not None and index_rec.get("close") is not None:
        basis = 100 * (mark_rec["close"] / index_rec["close"] - 1)
    status = "ok" if all(c.get("status") == "ok" for c in comps.values()) else "incomplete"
    return {"symbol": sym, "date": day, "status": status, "components": comps, "basis_pct": basis}


def process_symbol(sym):
    ckpt = CKPT_DIR / f"{sym}.json"
    if ckpt.exists():
        try:
            prev = json.loads(ckpt.read_text(encoding="utf-8"))
            if prev.get("complete") is True:
                return {"symbol": sym, "status": "resumed", "n_days": prev.get("n_days"), "n_basis_days": prev.get("n_basis_days")}
        except Exception:
            pass
    months = month_range("2023-01", "2024-04")
    spot_maps, um_maps, fund_maps = {}, {}, {}

    def load_month(ym):
        spot_maps[ym] = month_klines("spot", sym, ym)
        um_maps[ym] = month_klines("um", sym, ym)
        fund_maps[ym] = funding_month(sym, ym)

    with ThreadPoolExecutor(max_workers=MONTH_WORKERS) as ex:
        list(ex.map(load_month, months))

    days = day_list(START_DAY, END_DAY)
    records = []
    with ThreadPoolExecutor(max_workers=WORKERS) as ex:
        future_to_day = {ex.submit(process_day, sym, day, spot_maps, um_maps, fund_maps): day for day in days}
        for fut in as_completed(future_to_day):
            records.append(fut.result())
    records.sort(key=lambda r: r["date"])

    first_last = {}
    for comp in COMPONENTS:
        valid = [r["date"] for r in records if r["components"][comp].get("status") == "ok"]
        first_last[comp] = {"first": valid[0] if valid else None, "last": valid[-1] if valid else None, "n_days": len(valid)}
    n_basis = sum(1 for r in records if r.get("basis_pct") is not None)
    out = {
        "symbol": sym,
        "experiment_id": EXPERIMENT_ID,
        "program_id": "EBCR-001",
        "window": {"start": START_DAY, "end": END_DAY},
        "source": BASE,
        "generated_at_utc": datetime.now(timezone.utc).isoformat(),
        "complete": True,
        "n_days": len(days),
        "n_basis_days": n_basis,
        "first_last_valid": first_last,
        "days": records,
    }
    atomic_write(ckpt, out)
    return {
        "symbol": sym,
        "status": "ok",
        "n_days": len(days),
        "n_basis_days": n_basis,
        "coverage_basis": round(n_basis / len(days), 4),
        "first_last_valid": first_last,
    }


def main():
    CKPT_DIR.mkdir(parents=True, exist_ok=True)
    summaries = []
    for sym in SYMBOLS:
        summaries.append(process_symbol(sym))
    detail = {}
    for s in summaries:
        detail[s["symbol"]] = {
            "n_days": s["n_days"],
            "n_basis_days": s["n_basis_days"],
            "coverage_basis": s["coverage_basis"],
            "meets_gate": s["coverage_basis"] >= 0.95,
            "first_last_valid": s["first_last_valid"],
        }
    summary = {
        "schema_version": "1.0",
        "program_id": "EBCR-001",
        "experiment_id": EXPERIMENT_ID,
        "generated_at_utc": datetime.now(timezone.utc).isoformat(),
        "source": "Binance Public Data Archive (data.binance.vision) — free public",
        "config_path": str(CONFIG.relative_to(ROOT)),
        "config_sha256": hashlib.sha256(CONFIG.read_bytes()).hexdigest(),
        "window": {"start": START_DAY, "end": END_DAY},
        "symbols": SYMBOLS,
        "coverage_gate": 0.95,
        "symbols_detail": detail,
        "status": "ok",
    }
    atomic_write(SUMMARY_OUT, summary)
    print(json.dumps({"experiment_id": EXPERIMENT_ID, "symbols": len(summaries), "detail": {s["symbol"]: s["coverage_basis"] for s in summaries}, "path": str(SUMMARY_OUT)}, indent=2))


if __name__ == "__main__":
    main()
