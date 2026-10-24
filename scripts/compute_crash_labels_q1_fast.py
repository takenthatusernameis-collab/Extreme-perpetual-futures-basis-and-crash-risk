#!/usr/bin/env python3
import csv, hashlib, io, json, urllib.request, zipfile
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

_cache = {}
def get_spot_low(symbol, day):
    key = ('spot', symbol, day)
    if key in _cache: return _cache[key]
    try:
        url = f"{BASE}/spot/daily/klines/{symbol}/1d/{symbol}-1d-{day}.zip"
        d = fetch(url)
        rows = fetch_kline_csv(d)
        if not rows:
            _cache[key] = None
            return None
        r = rows[0]
        low = float(r[3])
        _cache[key] = low
        return low
    except Exception:
        _cache[key] = None
        return None

def get_index_low(symbol, day):
    key = ('idx', symbol, day)
    if key in _cache: return _cache[key]
    try:
        url = f"{BASE}/futures/um/daily/indexPriceKlines/{symbol}/1d/{symbol}-1d-{day}.zip"
        d = fetch(url)
        rows = fetch_kline_csv(d)
        if not rows:
            _cache[key] = None
            return None
        r = rows[0]
        low = float(r[3])
        _cache[key] = low
        return low
    except Exception:
        _cache[key] = None
        return None

def main():
    with open('research_state/basis_computation_q1_all.json') as f:
        basis = json.load(f)
    comps = basis.get('basis_computations') or []
    horizons = [7,14,28]
    labels = []
    exclusions = []
    for comp in comps:
        sym = comp['symbol']
        t = comp['date']
        t_dt = datetime.strptime(t, '%Y-%m-%d')
        ref_close = comp.get('spot_median') or comp.get('index_median')
        if ref_close is None:
            exclusions.append({"symbol": sym, "date": t, "reason": "no_ref_close"})
            continue
        mae = {}
        ok_all = True
        for h in horizons:
            min_low = None
            missing = False
            for d in range(1, h+1):
                fday = (t_dt + timedelta(days=d)).strftime('%Y-%m-%d')
                lowv = get_spot_low(sym, fday)
                if lowv is None:
                    lowv = get_index_low(sym, fday)
                if lowv is None:
                    missing = True
                    break
                if min_low is None or lowv < min_low:
                    min_low = lowv
            if missing or min_low is None:
                ok_all = False
                break
            mae[f'h{h}'] = min_low / ref_close - 1.0
        if not ok_all:
            exclusions.append({"symbol": sym, "date": t, "reason": "incomplete_forward_horizon"})
            continue
        labels.append({
            "symbol": sym,
            "date": t,
            "ref_close": ref_close,
            "mae": mae,
            "status": "ok"
        })
    out = {
        "schema_version": "1.0",
        "program_id": "EBCR-001",
        "generated_at_utc": datetime.now(timezone.utc).isoformat(),
        "horizons_days": horizons,
        "method": "MAE = min(spot/index low over t+1..t+h) / ref_close_t - 1 (ref_close_t = spot_median close proxy)",
        "source": "S3 spot/index daily klines (free public)",
        "window_basis": basis['window'],
        "n_basis_obs": len(comps),
        "n_labels_ok": len(labels),
        "n_exclusions": len(exclusions),
        "labels": labels,
        "exclusions": exclusions
    }
    path = "research_state/crash_labels_q1.json"
    with open(path, 'w') as f:
        json.dump(out, f)
    print(json.dumps({"n_labels_ok": len(labels), "n_exclusions": len(exclusions), "path": path}, indent=2))

if __name__ == '__main__':
    main()
