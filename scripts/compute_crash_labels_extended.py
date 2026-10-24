#!/usr/bin/env python3
"""Compute forward crash labels on the extended window (experiment EBCR-001-EXTENDED-V1).

MAE_h = min(spot/index low over t+1..t+h) / ref_close_t - 1, ref_close_t =
spot close at t else index close at t. Horizons 7/14/28; full horizon required.
Reads ingestion checkpoints (offline). Output: research_state/crash_labels_extended_v1.json
"""
import hashlib, json
from datetime import datetime, timedelta, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
STATE = ROOT / "research_state"
CKPT_DIR = STATE / "ingest_extended_window"
OUT = STATE / "crash_labels_extended_v1.json"
HORIZONS = [7, 14, 28]


def sha_obj(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True).encode("utf-8")).hexdigest()


def atomic_write(path, obj):
    rendered = json.dumps(obj, indent=2, sort_keys=True) + "\n"
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text(rendered, encoding="utf-8")
    tmp.replace(path)


def main():
    price = {}
    basis_by_key = {}
    for ckpt in sorted(CKPT_DIR.glob("*.json")):
        d = json.loads(ckpt.read_text(encoding="utf-8"))
        sym = d["symbol"]
        for rec in d["days"]:
            key = (sym, rec["date"])
            c = rec.get("components", {})
            spot = c.get("spot", {})
            index = c.get("index", {})
            price[key] = {
                "spot_close": spot.get("close"),
                "spot_low": spot.get("low"),
                "index_close": index.get("close"),
                "index_low": index.get("low"),
            }
            if rec.get("basis_pct") is not None:
                basis_by_key[key] = rec["basis_pct"]

    labels = []
    exclusions = []
    for key in sorted(basis_by_key):
        sym, t = key
        t_dt = datetime.strptime(t, "%Y-%m-%d")
        p = price.get(key, {})
        ref_close = p.get("spot_close") if p.get("spot_close") is not None else p.get("index_close")
        if ref_close is None:
            exclusions.append({"symbol": sym, "date": t, "reason": "no_ref_close"})
            continue
        mae = {}
        ok_all = True
        for h in HORIZONS:
            min_low = None
            missing = False
            for offset in range(1, h + 1):
                fday = (t_dt + timedelta(days=offset)).strftime("%Y-%m-%d")
                fp = price.get((sym, fday), {})
                low = fp.get("spot_low") if fp.get("spot_low") is not None else fp.get("index_low")
                if low is None:
                    missing = True
                    break
                if min_low is None or low < min_low:
                    min_low = low
            if missing or min_low is None:
                ok_all = False
                break
            mae[f"h{h}"] = min_low / ref_close - 1.0
        if not ok_all:
            exclusions.append({"symbol": sym, "date": t, "reason": "incomplete_forward_horizon"})
            continue
        labels.append({"symbol": sym, "date": t, "ref_close": ref_close, "mae": mae, "status": "ok"})

    out = {
        "schema_version": "1.0",
        "program_id": "EBCR-001",
        "experiment_id": "EBCR-001-EXTENDED-V1",
        "generated_at_utc": datetime.now(timezone.utc).isoformat(),
        "horizons_days": HORIZONS,
        "method": "MAE = min(spot/index low over t+1..t+h) / ref_close_t - 1; ref_close_t = spot close at t else index close at t; full horizon required",
        "source": "research_state/ingestion_extended_v1.json (Binance Public Data Archive, free public)",
        "window": {"start": "2023-01-01", "end": "2024-04-30"},
        "n_basis_obs": len(basis_by_key),
        "n_labels_ok": len(labels),
        "n_exclusions": len(exclusions),
        "labels": labels,
        "exclusions": exclusions[:500],
    }
    atomic_write(OUT, out)
    print(json.dumps({"n_labels_ok": len(labels), "n_exclusions": len(exclusions), "path": str(OUT)}, indent=2))


if __name__ == "__main__":
    main()
