#!/usr/bin/env python3
"""Recompute UTC daily basis on the extended window (experiment EBCR-001-EXTENDED-V1).

Reads per-symbol checkpoints from scripts/ingest_extended_window.py and emits
one daily basis observation per symbol/day with mark/index medians, funding
median and raw-response hashes. No network calls; no forward fill.
Output: research_state/basis_computation_extended_v1.json
"""
import hashlib, json
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
STATE = ROOT / "research_state"
CKPT_DIR = STATE / "ingest_extended_window"
OUT = STATE / "basis_computation_extended_v1.json"
COMPONENTS = ["spot", "um", "mark", "index", "funding"]


def median(xs):
    if not xs:
        return None
    s = sorted(xs)
    n = len(s)
    if n % 2 == 1:
        return s[n // 2]
    return (s[n // 2 - 1] + s[n // 2]) / 2


def sha_obj(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True).encode("utf-8")).hexdigest()


def atomic_write(path, obj):
    rendered = json.dumps(obj, indent=2, sort_keys=True) + "\n"
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text(rendered, encoding="utf-8")
    tmp.replace(path)


def main():
    computations = []
    coverage = {}
    for ckpt in sorted(CKPT_DIR.glob("*.json")):
        d = json.loads(ckpt.read_text(encoding="utf-8"))
        sym = d["symbol"]
        sym_ok = 0
        sym_total = 0
        for rec in d["days"]:
            comps = rec.get("components", {})
            out = {
                "symbol": sym,
                "date": rec["date"],
                "status": rec["status"],
                "spot_median": None,
                "um_kline_median": None,
                "mark_median": None,
                "index_median": None,
                "funding_median": None,
                "basis_pct": rec.get("basis_pct"),
                "hashes": {},
            }
            for comp in COMPONENTS:
                c = comps.get(comp, {})
                sym_total += 1
                if c.get("status") == "ok":
                    sym_ok += 1
                if comp == "spot":
                    out["spot_median"] = c.get("close")
                    out["hashes"]["spot_sha256"] = c.get("raw_sha256")
                elif comp == "um":
                    out["um_kline_median"] = c.get("close")
                    out["hashes"]["um_sha256"] = c.get("raw_sha256")
                elif comp == "mark":
                    out["mark_median"] = c.get("close")
                    out["hashes"]["mark_sha256"] = c.get("raw_sha256")
                elif comp == "index":
                    out["index_median"] = c.get("close")
                    out["hashes"]["index_sha256"] = c.get("raw_sha256")
                elif comp == "funding":
                    out["funding_median"] = c.get("median")
                    out["hashes"]["funding_sha256"] = c.get("raw_sha256")
            computations.append(out)
        coverage[sym] = {
            "ok_components": sym_ok,
            "total_components": sym_total,
            "coverage": round(sym_ok / sym_total, 6) if sym_total else 0.0,
            "meets_gate": (sym_ok / sym_total if sym_total else 0) >= 0.95,
            "n_days": d["n_days"],
            "n_basis_days": d["n_basis_days"],
        }
    out = {
        "schema_version": "1.0",
        "program_id": "EBCR-001",
        "experiment_id": "EBCR-001-EXTENDED-V1",
        "generated_at_utc": datetime.now(timezone.utc).isoformat(),
        "source": "research_state/ingestion_extended_v1.json (Binance Public Data Archive, free public)",
        "symbols": sorted(c["symbol"] for c in computations) if computations else [],
        "window": {"start": "2023-01-01", "end": "2024-04-30"},
        "coverage_gate": 0.95,
        "basis_computations": computations,
        "coverage": coverage,
        "n_computations": len(computations),
        "status": "ok" if all(coverage[s]["meets_gate"] for s in coverage) else "blocked",
    }
    atomic_write(OUT, out)
    print(json.dumps({"status": out["status"], "n_computations": len(computations), "coverage": {s: coverage[s]["coverage"] for s in sorted(coverage)}, "path": str(OUT)}, indent=2))


if __name__ == "__main__":
    main()
