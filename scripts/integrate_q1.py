#!/usr/bin/env python3
import json, hashlib, datetime
from pathlib import Path

root = Path("/home/runner/work/Extreme-perpetual-futures-basis-and-crash-risk/Extreme-perpetual-futures-basis-and-crash-risk")
basis = json.load(open(root/"research_state/basis_computation_q1_all.json"))
labels = json.load(open(root/"research_state/crash_labels_q1.json"))

bmap = {(r["symbol"], r["date"]): r for r in basis["basis_computations"]}
lmap = {(r["symbol"], r["date"]): r for r in labels["labels"]}

rows = []
exclusions = []
for key in sorted(bmap):
    if key not in lmap:
        exclusions.append({"key": list(key), "reason": "missing_label"})
        continue
    b = bmap[key]; l = lmap[key]
    if b.get("status") != "ok" or l.get("status") != "ok":
        exclusions.append({"key": list(key), "reason": "non_ok_status", "basis_status": b.get("status"), "label_status": l.get("status")})
        continue
    rows.append({
        "symbol": key[0], "date": key[1],
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

# unmatched labels
for key in lmap:
    if key not in bmap:
        exclusions.append({"key": list(key), "reason": "missing_basis"})

def sha(obj):
    return hashlib.sha256(json.dumps(obj, sort_keys=True).encode()).hexdigest()

out = {
  "schema_version": "1.0",
  "program_id": "EBCR-001",
  "generated_at_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(),
  "source_basis": "research_state/basis_computation_q1_all.json",
  "source_labels": "research_state/crash_labels_q1.json",
  "join_key": ["symbol","date"],
  "window": {"start":"2024-01-01","end":"2024-03-31"},
  "horizons_days": labels["horizons_days"],
  "schema": {
    "symbol": "str", "date": "str (YYYY-MM-DD UTC)",
    "basis_pct": "float (UM median / spot median -1)",
    "spot_median": "float", "um_kline_median": "float", "mark_median": "float", "index_median": "float", "funding_median": "float",
    "ref_close": "float (spot close proxy)",
    "mae": "dict horizon_days->float (min low/ref_close -1)",
    "horizons_days": "list[int]"
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
  "status": "ok" if len(exclusions)==0 else "incomplete"
}
Path(root/"research_state/integrated_q1.json").write_text(json.dumps(out, indent=2))
print("rows", len(rows), "exclusions", len(exclusions))
print("symbols", sorted(set(r["symbol"] for r in rows)))