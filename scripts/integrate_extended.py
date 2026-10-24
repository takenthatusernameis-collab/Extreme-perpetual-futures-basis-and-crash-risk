#!/usr/bin/env python3
"""Integrate extended basis and crash labels into one formation-day dataset.

Mirror of scripts/integrate_q1.py but parameterised over paths so Q1 artifacts
are never touched. Output: research_state/integrated_extended_v1.json
"""
import argparse, hashlib, json, datetime
from pathlib import Path


def sha(obj):
    return hashlib.sha256(json.dumps(obj, sort_keys=True).encode()).hexdigest()


def main():
    parser = argparse.ArgumentParser(description="Integrate extended basis + labels into formation-day rows.")
    parser.add_argument("--basis", type=Path, default=Path("research_state/basis_computation_extended_v1.json"))
    parser.add_argument("--labels", type=Path, default=Path("research_state/crash_labels_extended_v1.json"))
    parser.add_argument("--out", type=Path, default=Path("research_state/integrated_extended_v1.json"))
    parser.add_argument("--window-start", default="2023-01-01")
    parser.add_argument("--window-end", default="2024-04-30")
    args = parser.parse_args()

    basis = json.loads(args.basis.read_text(encoding="utf-8"))
    labels = json.loads(args.labels.read_text(encoding="utf-8"))
    bmap = {(r["symbol"], r["date"]): r for r in basis["basis_computations"]}
    lmap = {(r["symbol"], r["date"]): r for r in labels["labels"]}

    rows = []
    exclusions = []
    for key in sorted(bmap):
        if key not in lmap:
            exclusions.append({"key": list(key), "reason": "missing_label"})
            continue
        b = bmap[key]
        l = lmap[key]
        if b.get("status") != "ok" or l.get("status") != "ok":
            exclusions.append({"key": list(key), "reason": "non_ok_status", "basis_status": b.get("status"), "label_status": l.get("status")})
            continue
        rows.append({
            "symbol": key[0],
            "date": key[1],
            "basis_pct": b["basis_pct"],
            "spot_median": b["spot_median"],
            "um_kline_median": b["um_kline_median"],
            "mark_median": b["mark_median"],
            "index_median": b["index_median"],
            "funding_median": b["funding_median"],
            "ref_close": l["ref_close"],
            "mae": l["mae"],
            "horizons_days": labels["horizons_days"],
        })
    for key in lmap:
        if key not in bmap:
            exclusions.append({"key": list(key), "reason": "missing_basis"})

    out = {
        "schema_version": "1.0",
        "program_id": "EBCR-001",
        "experiment_id": "EBCR-001-EXTENDED-V1",
        "generated_at_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "source_basis": str(args.basis),
        "source_labels": str(args.labels),
        "join_key": ["symbol", "date"],
        "window": {"start": args.window_start, "end": args.window_end},
        "horizons_days": labels["horizons_days"],
        "schema": {
            "symbol": "str",
            "date": "str (YYYY-MM-DD UTC)",
            "basis_pct": "float (mark median / index median - 1)",
            "spot_median": "float",
            "um_kline_median": "float",
            "mark_median": "float",
            "index_median": "float",
            "funding_median": "float",
            "ref_close": "float (spot close at t else index close at t)",
            "mae": "dict horizon_days->float (min low/ref_close - 1)",
            "horizons_days": "list[int]",
        },
        "n_basis_obs": len(basis["basis_computations"]),
        "n_labels": len(labels["labels"]),
        "n_rows": len(rows),
        "n_exclusions": len(exclusions),
        "exclusions": exclusions,
        "rows": rows,
        "hashes": {
            "basis_sha256": sha(basis["basis_computations"]),
            "labels_sha256": sha(labels["labels"]),
            "integrated_rows_sha256": sha(rows),
        },
        "status": "ok" if len(exclusions) == 0 else "incomplete",
    }
    args.out.write_text(json.dumps(out, indent=2), encoding="utf-8")
    print("rows", len(rows), "exclusions", len(exclusions), "path", args.out)


if __name__ == "__main__":
    main()
