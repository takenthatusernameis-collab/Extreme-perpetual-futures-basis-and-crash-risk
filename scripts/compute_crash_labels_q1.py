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

def get_spot_low_high_close(symbol, day):
    try:
        url = f"{BASE}/spot/daily/klines/{symbol}/1d/{symbol}-1d-{day}.zip"
        d = fetch(url)
        rows = fetch_kline_csv(d)
        if not rows: return None, None, None, None
        r = rows[0]
        low = float(r[3])
        high = float(r[2])
        close = float(r[4])
        return low, high, close, hashlib.sha256(d).hexdigest()
    except Exception:
        return None, None, None, None

def get_index_low_close(symbol, day):
    try:
        url = f"{BASE}/futures/um/daily/indexPriceKlines/{symbol}/1d/{symbol}-1d-{day}.zip"
        d = fetch(url)
        rows = fetch_kline_csv(d)
        if not rows: return None, None, None
        r = rows[0]
        low = float(r[3])
        close = float(r[4])
        return low, close, hashlib.sha256(d).hexdigest()
    except Exception:
        return None, None, None

def main():
    with open('research_state/basis_computation_q1_all.json') as f:
        basis = json.load(f)
    comps = basis.get('basis_computations') or []
    symbols = basis['symbols']
    horizons = [7,14,28]
    labels = []
    exclusions = []
    # build lookup
    # need forward data
    for comp in comps:
        sym = comp['symbol']
        t = comp['date']
        t_dt = datetime.strptime(t, '%Y-%m-%d')
        # get close at t for reference - prefer spot median/index median; use spot median close? protocol says "spot/index close at t" - in our data we have spot_median/index_median as median of closes; use spot_median as close proxy
        ref_close = comp.get('spot_median') or comp.get('index_median')
        if ref_close is None:
            exclusions.append({"symbol": sym, "date": t, "reason": "no_ref_close"})
            continue
        mae = {}
        ok_all = True
        for h in horizons:
            # need all days t+1 to t+h
            min_low = None
            missing = False
            for d in range(1, h+1):
                fday = (t_dt + timedelta(days=d)).strftime('%Y-%m-%d')
                # try spot first
                slow, shigh, sclose, shash = get_spot_low_high_close(sym, fday)
                if slow is None:
                    # try index
                    ilow, iclose, ihash = get_index_low_close(sym, fday)
                    if ilow is None:
                        missing = True
                        break
                    lowv = ilow
                else:
                    lowv = slow
                if min_low is None or lowv < min_low:
                    min_low = lowv
            if missing or min_low is None:
                ok_all = False
                break
            mae[f'h{h}'] = min_low / ref_close - 1.0  # MAE = min low / close_t - 1
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
        "exclusions": exclusions[:100]  # truncate for size
    }
    path = "research_state/crash_labels_q1.json"
    with open(path, 'w') as f:
        json.dump(out, f)
    print(json.dumps({"n_labels_ok": len(labels), "n_exclusions": len(exclusions), "path": path}, indent=2))

if __name__ == '__main__':
    main()
