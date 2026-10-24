#!/usr/bin/env python3
import csv, hashlib, io, json, urllib.request, zipfile, os, re
from datetime import datetime, timezone, timedelta
from xml.etree import ElementTree as ET

BASE = "https://data.binance.vision/data"
BUCKET_S3 = "https://s3-ap-northeast-1.amazonaws.com/data.binance.vision"

def fetch(url):
    req = urllib.request.Request(url, headers={'User-Agent': 'EBCR-001'})
    with urllib.request.urlopen(req, timeout=30) as r:
        return r.read()

def list_keys_xml(prefix, max_keys=1000):
    keys = []
    marker = ""
    while True:
        url = f"{BUCKET_S3}?prefix={prefix}&max-keys={max_keys}"
        if marker:
            url += f"&marker={urllib.parse.quote(marker)}" if False else f"&marker={marker}"
        try:
            data = fetch(url)
        except Exception as e:
            raise
        h = hashlib.sha256(data).hexdigest()
        root = ET.fromstring(data)
        ns = "{http://s3.amazonaws.com/doc/2006-03-01/}"
        for c in root.findall(f"{ns}Contents"):
            key = c.find(f"{ns}Key").text
            keys.append(key)
        truncated = root.find(f"{ns}IsTruncated")
        if truncated is not None and truncated.text == "true":
            marker_elem = root.find(f"{ns}NextMarker")
            if marker_elem is None or marker_elem.text is None:
                marker = keys[-1] if keys else None
            else:
                marker = marker_elem.text
            if not marker:
                break
        else:
            break
    return keys

def get_zip_dates_for_prefix(prefix):
    try:
        keys = list_keys_xml(prefix)
        dates = set()
        for k in keys:
            m = re.search(r'-(\d{4}-\d{2}-\d{2})\.zip$', k)
            if m:
                dates.add(m.group(1))
        return sorted(dates)
    except Exception as e:
        return [], str(e)

def fetch_kline_csv(data_zip):
    z = zipfile.ZipFile(io.BytesIO(data_zip))
    name = z.namelist()[0]
    txt = z.read(name).decode()
    rows = list(csv.reader(io.StringIO(txt)))
    data_rows = [r for r in rows if r and len(r) > 0 and r[0].lstrip('-').isdigit()]
    return data_rows, rows[0] if rows else []

def process_day(symbol, day):
    result = {"symbol": symbol, "date": day, "status": "ok", "components": {}}
    try:
        # spot
        url_spot = f"{BASE}/spot/daily/klines/{symbol}/1d/{symbol}-1d-{day}.zip"
        d_spot = fetch(url_spot)
        rows_spot, hdr_spot = fetch_kline_csv(d_spot)
        closes_spot = [float(r[4]) for r in rows_spot]
        result["components"]["spot"] = {
            "n_bars": len(rows_spot),
            "close_median": sorted(closes_spot)[len(closes_spot)//2] if closes_spot else None,
            "raw_sha256": hashlib.sha256(d_spot).hexdigest()
        }
    except Exception as e:
        result["components"]["spot"] = {"status": "failed", "error": str(e)}
        result["status"] = "incomplete"

    try:
        # um kline
        url_um = f"{BASE}/futures/um/daily/klines/{symbol}/1d/{symbol}-1d-{day}.zip"
        d_um = fetch(url_um)
        rows_um, hdr_um = fetch_kline_csv(d_um)
        closes_um = [float(r[4]) for r in rows_um]
        result["components"]["um_kline"] = {
            "n_bars": len(rows_um),
            "close_median": sorted(closes_um)[len(closes_um)//2] if closes_um else None,
            "raw_sha256": hashlib.sha256(d_um).hexdigest()
        }
    except Exception as e:
        result["components"]["um_kline"] = {"status": "failed", "error": str(e)}
        result["status"] = "incomplete"

    try:
        # mark
        url_mark = f"{BASE}/futures/um/daily/markPriceKlines/{symbol}/1d/{symbol}-1d-{day}.zip"
        d_mark = fetch(url_mark)
        rows_mark, hdr_mark = fetch_kline_csv(d_mark)
        closes_mark = [float(r[4]) for r in rows_mark]
        result["components"]["mark"] = {
            "n_bars": len(rows_mark),
            "close_median": sorted(closes_mark)[len(closes_mark)//2] if closes_mark else None,
            "raw_sha256": hashlib.sha256(d_mark).hexdigest()
        }
    except Exception as e:
        result["components"]["mark"] = {"status": "failed", "error": str(e)}
        result["status"] = "incomplete"

    try:
        # index
        url_idx = f"{BASE}/futures/um/daily/indexPriceKlines/{symbol}/1d/{symbol}-1d-{day}.zip"
        d_idx = fetch(url_idx)
        rows_idx, hdr_idx = fetch_kline_csv(d_idx)
        closes_idx = [float(r[4]) for r in rows_idx]
        result["components"]["index"] = {
            "n_bars": len(rows_idx),
            "close_median": sorted(closes_idx)[len(closes_idx)//2] if closes_idx else None,
            "raw_sha256": hashlib.sha256(d_idx).hexdigest()
        }
    except Exception as e:
        result["components"]["index"] = {"status": "failed", "error": str(e)}
        result["status"] = "incomplete"

    try:
        ym = day[:7]
        furl = f"{BASE}/futures/um/monthly/fundingRate/{symbol}/{symbol}-fundingRate-{ym}.zip"
        fdata = fetch(furl)
        fz = zipfile.ZipFile(io.BytesIO(fdata))
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
                d = datetime.fromtimestamp(ts/1000, tz=timezone.utc).date().isoformat()
                if d == day:
                    day_funding.append(float(r[fi]))
            except:
                pass
        result["components"]["funding"] = {
            "rates_on_day": day_funding,
            "median": sorted(day_funding)[len(day_funding)//2] if day_funding else None,
            "raw_sha256": hashlib.sha256(fdata).hexdigest()
        }
    except Exception as e:
        result["components"]["funding"] = {"status": "failed", "error": str(e)}
        result["status"] = "incomplete"

    # compute basis
    try:
        mark_med = result["components"].get("mark", {}).get("close_median")
        idx_med = result["components"].get("index", {}).get("close_median")
        if mark_med is not None and idx_med is not None:
            result["basis_pct"] = 100*(mark_med/idx_med - 1)
    except:
        pass

    return result

def main():
    symbols = ["BTCUSDT", "ETHUSDT"]
    # Find overlapping complete window - use a recent window where data is likely complete
    # Try a window
    start_date = "2024-01-01"
    end_date = "2024-01-10"  # small window for testing

    out = {
        "schema_version": "1.0",
        "program_id": "EBCR-001",
        "generated_at_utc": datetime.now(timezone.utc).isoformat(),
        "symbols": symbols,
        "window": {"start": start_date, "end": end_date},
        "coverage_gate": 0.95,
        "days": [],
        "coverage": {},
        "status": "ok"
    }

    for sym in symbols:
        sym_days = []
        for i in range(10):  # 10 days
            d = (datetime.strptime(start_date, "%Y-%m-%d") + timedelta(days=i)).strftime("%Y-%m-%d")
            res = process_day(sym, d)
            sym_days.append(res)
        out["days"].append({sym: sym_days})

        # compute coverage
        total_components = 0
        ok_components = 0
        for dayres in sym_days:
            comps = dayres.get("components", {})
            for k, v in comps.items():
                total_components += 1
                if isinstance(v, dict) and v.get("status") != "failed" and "close_median" in v:
                    ok_components += 1
                elif isinstance(v, dict) and v.get("median") is not None:  # funding
                    ok_components += 1
                elif isinstance(v, dict) and "rates_on_day" in v and v.get("rates_on_day") is not None:
                    ok_components += 1
        cov = ok_components / total_components if total_components > 0 else 0
        out["coverage"][sym] = {"ok_components": ok_components, "total_components": total_components, "coverage": cov, "meets_gate": cov >= 0.95}

    # overall gate check
    all_meet = all(out["coverage"][s]["meets_gate"] for s in symbols)
    if not all_meet:
        out["status"] = "blocked"
        out["reason"] = "coverage_below_gate"

    path = "research_state/ingestion_multi_day_sample.json"
    with open(path, "w") as f:
        json.dump(out, f, indent=2)
    print(json.dumps({"status": out["status"], "coverage": out["coverage"], "path": path}, indent=2))

if __name__ == "__main__":
    main()
