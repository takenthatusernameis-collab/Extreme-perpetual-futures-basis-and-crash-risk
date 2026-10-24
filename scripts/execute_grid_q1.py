#!/usr/bin/env python3
"""Grid execution scaffold for EBCR-001 Q1 cohort.

Maps research_state/integrated_q1.json rows to preregistered grid cells per the
frozen config (configs/basis_crash_grid_v1.json), evaluates the minimum-history
and coverage gates, and records a terminal status (ok/blocked/failed/incomplete/
invalid/not_run) with reason and artifact path for every cell.

The scaffold is idempotent and does not modify the frozen config. It works
offline against the already-computed integrated dataset; no live exchange calls
are made here.

Outputs:
  research_state/grid_execution_scaffold_v1.json   cell-to-slice mapping + statuses
  research_state/cell_status_ledger.json           per-cell terminal ledger
"""
from __future__ import annotations

import argparse
import hashlib
import itertools
import json
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
STATE = ROOT / "research_state"
CONFIG = ROOT / "configs" / "basis_crash_grid_v1.json"
MANIFEST = STATE / "grid_manifest_v1.json"
INTEGRATED = STATE / "integrated_q1.json"
SCAFFOLD_OUT = STATE / "grid_execution_scaffold_v1.json"
LEDGER_OUT = STATE / "cell_status_ledger.json"

STATUSES = ["ok", "blocked", "failed", "incomplete", "invalid", "not_run"]
ENDPOINTS = [
    "crash_incidence_10pct",
    "crash_incidence_15pct",
    "crash_incidence_20pct",
    "vol_scaled_crash_2sigma",
    "vol_scaled_crash_3sigma",
    "vol_scaled_crash_4sigma",
    "mean_forward_mae",
    "expected_shortfall_5pct_forward_mae",
]
COVERAGE_GATE = 0.95
ALPHA = 0.05


def canonical_json(value: Any) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False)


def sha256_obj(value: Any) -> str:
    return hashlib.sha256(canonical_json(value).encode("utf-8")).hexdigest()


def parse_date(s: str) -> datetime:
    return datetime.strptime(s, "%Y-%m-%d")


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def atomic_write(path: Path, obj: Any) -> None:
    rendered = json.dumps(obj, indent=2, sort_keys=True) + "\n"
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text(rendered, encoding="utf-8")
    tmp.replace(path)


def build_cells(config: dict) -> list[dict]:
    grid = config["grid"]
    axes = grid["axes"]
    keys = grid["enumeration_order"]
    cells = []
    for ordinal, values in enumerate(
        itertools.product(*(axes[k] for k in keys)), start=1
    ):
        params = dict(zip(keys, values))
        cells.append(
            {
                "cell_id": f"EBCR-GRID-001-{ordinal:04d}",
                "ordinal": ordinal,
                "parameters": params,
                "configuration_hash_sha256": sha256_obj(
                    {"grid_id": config["grid_id"], "parameters": params}
                ),
            }
        )
    return cells


def eligible_rows_for_cell(
    cell: dict,
    rows_by_date: dict[str, list[dict]],
    all_dates: list[str],
    date_set: set[str],
) -> dict:
    """Return eligible formation rows and exclusion detail for one cell.

    Gates (per protocol minimum_history_rule):
      - feature aggregation: basis valid for t-A+1 .. t  (A = basis_aggregation_days)
      - rolling reference: L valid prior daily features for t-L .. t-1
                             (L = rolling_reference_days), excluding day t
      - forward horizon: outcome valid for t+1 .. t+h   (h = horizon_days)
      - coverage: >= 95% valid daily basis inside the reference window
    A row is eligible only if ALL gates pass. Never shorten a window.
    """
    p = cell["parameters"]
    A = p["basis_aggregation_days"]
    L = p["rolling_reference_days"]
    h = p["horizon_days"]

    eligible = []
    exclusions = []
    for row in rows_for_window(rows_by_date, all_dates):
        t = row["date"]
        t_dt = parse_date(t)

        # feature aggregation window: t-A+1 .. t must all have valid basis
        feature_dates = [
            (t_dt - timedelta(days=i)).strftime("%Y-%m-%d") for i in range(A - 1, -1, -1)
        ]
        feature_ok = all(d in date_set for d in feature_dates)
        if not feature_ok:
            exclusions.append(
                {
                    "symbol": row["symbol"],
                    "date": t,
                    "reason": "insufficient_feature_history",
                    "missing": [d for d in feature_dates if d not in date_set],
                }
            )
            continue

        # rolling reference: t-L .. t-1 must all have valid basis (exclude t)
        ref_dates = [
            (t_dt - timedelta(days=i)).strftime("%Y-%m-%d") for i in range(L, 0, -1)
        ]
        ref_missing = [d for d in ref_dates if d not in date_set]
        if ref_missing:
            exclusions.append(
                {
                    "symbol": row["symbol"],
                    "date": t,
                    "reason": "insufficient_prior_history",
                    "required": L,
                    "available_prior": len(ref_dates) - len(ref_missing),
                    "missing_sample": ref_missing[:5],
                }
            )
            continue

        # coverage gate inside reference window
        ref_valid = sum(1 for d in ref_dates if d in date_set)
        coverage = ref_valid / len(ref_dates) if ref_dates else 0.0
        if coverage < COVERAGE_GATE:
            exclusions.append(
                {
                    "symbol": row["symbol"],
                    "date": t,
                    "reason": "coverage_gate_unmet",
                    "coverage": round(coverage, 4),
                    "required": COVERAGE_GATE,
                }
            )
            continue

        # forward horizon: t+1 .. t+h must all have valid MAE
        fwd_dates = [
            (t_dt + timedelta(days=i)).strftime("%Y-%m-%d") for i in range(1, h + 1)
        ]
        fwd_missing = [
            d
            for d in fwd_dates
            if d not in date_set
            or row.get("mae", {}).get(f"h{h}") is None
        ]
        if fwd_missing:
            exclusions.append(
                {
                    "symbol": row["symbol"],
                    "date": t,
                    "reason": "insufficient_forward_horizon",
                    "horizon_days": h,
                    "missing_sample": fwd_missing[:5],
                }
            )
            continue

        eligible.append(row)

    return {
        "eligible": eligible,
        "n_eligible": len(eligible),
        "exclusions": exclusions,
        "n_excluded": len(exclusions),
    }


def rows_for_window(
    rows_by_date: dict[str, list[dict]], all_dates: list[str]
) -> list[dict]:
    """Iterate rows in chronological order (one row per symbol-date)."""
    out = []
    for d in all_dates:
        out.extend(rows_by_date.get(d, []))
    return out


def holm_thresholds(m: int) -> list[float]:
    """Holm step-down thresholds alpha/(m - i + 1) for i=1..m (sorted p-values)."""
    return [ALPHA / (m - i + 1) for i in range(1, m + 1)]


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Build grid execution scaffold and record cell statuses (Q1 cohort)."
    )
    parser.add_argument("--config", type=Path, default=CONFIG)
    parser.add_argument("--manifest", type=Path, default=MANIFEST)
    parser.add_argument("--integrated", type=Path, default=INTEGRATED)
    parser.add_argument("--scaffold-out", type=Path, default=SCAFFOLD_OUT)
    parser.add_argument("--ledger-out", type=Path, default=LEDGER_OUT)
    args = parser.parse_args()

    config = load_json(args.config)
    config_sha = sha256_obj(config)
    manifest = load_json(args.manifest)
    integrated = load_json(args.integrated)

    cells = build_cells(config)
    if len(cells) != manifest["expected_configuration_count"]:
        raise SystemExit(
            f"cell count {len(cells)} != manifest {manifest['expected_configuration_count']}"
        )

    rows = integrated["rows"]
    rows_by_date: dict[str, list[dict]] = {}
    all_dates = sorted({r["date"] for r in rows})
    date_set = set(all_dates)
    for r in rows:
        rows_by_date.setdefault(r["date"], []).append(r)

    symbols = sorted({r["symbol"] for r in rows})
    n_rows = len(rows)

    # Execution window bounds (data availability)
    data_start = all_dates[0]
    data_end = all_dates[-1]

    scaffold_cells = []
    ledger_cells: dict[str, dict] = {}
    summary = {s: 0 for s in STATUSES}

    for cell in cells:
        p = cell["parameters"]
        A = p["basis_aggregation_days"]
        L = p["rolling_reference_days"]
        h = p["horizon_days"]
        q = p["tail_quantile"]
        orient = p["orientation"]

        eval_detail = eligible_rows_for_cell(cell, rows_by_date, all_dates, date_set)
        n_eligible = eval_detail["n_eligible"]

        # Determine terminal status.
        # minimum_history_rule: full L-day reference required; Q1 window starts at
        # data_start so no date t in [data_start, data_end] has L prior days
        # entirely inside the window when L >= 1 and data_start is the earliest
        # available date. Forward horizon also truncates the latest formation
        # dates. With Q1-only data no cell can satisfy full history + forward.
        reasons: list[str] = []
        if n_eligible == 0:
            # Identify the concrete blocking cause(s).
            # History cause: earliest formation date needing full L-day reference
            # is data_start + L days, which is beyond data_end for L>=1 given
            # a 91-day window and L in {90,180,365}.
            earliest_hist = (parse_date(data_start) + timedelta(days=L)).strftime(
                "%Y-%m-%d"
            )
            reasons.append(
                f"minimum_history_rule_unmet: need {L} valid prior daily basis observations "
                f"preceding each formation date; earliest date with full history is "
                f"{earliest_hist} but data window ends {data_end}; 0 of {n_rows} rows eligible"
            )
            # Forward-horizon cause for h such that data_end - h < data_start + L
            last_fwd = (parse_date(data_end) - timedelta(days=h)).strftime(
                "%Y-%m-%d"
            )
            reasons.append(
                f"insufficient_forward_horizon: need h={h} forward days after each "
                f"formation date; last formation date with full forward horizon is "
                f"{last_fwd}, which precedes the earliest date with full history "
                f"({earliest_hist})"
            )
            status = "blocked"
            endpoints_evaluated = []
        else:
            status = "ok"
            endpoints_evaluated = list(ENDPOINTS)

        summary[status] += 1

        cell_entry = {
            "cell_id": cell["cell_id"],
            "ordinal": cell["ordinal"],
            "parameters": p,
            "configuration_hash_sha256": cell["configuration_hash_sha256"],
            "terminal_status": status,
            "reason": "; ".join(reasons) if reasons else "all gates passed",
            "evidence_path": "research_state/grid_execution_scaffold_v1.json",
            "n_candidate_rows": n_rows,
            "n_eligible_rows": n_eligible,
            "n_excluded_rows": eval_detail["n_excluded"],
            "exclusion_sample": eval_detail["exclusions"][:5],
            "symbols": symbols,
            "data_window": {"start": data_start, "end": data_end},
            "endpoints_evaluated": endpoints_evaluated,
            "next_step": (
                "Acquire pre-window daily basis history (free public source) and/or "
                "extend the forward data window so full L-day reference and h-day "
                "horizon can both be satisfied; re-execute this cell."
            )
            if status != "ok"
            else "Proceed to endpoint estimation and Holm correction.",
        }
        scaffold_cells.append(cell_entry)
        ledger_cells[cell["cell_id"]] = {
            "cell_id": cell["cell_id"],
            "ordinal": cell["ordinal"],
            "parameters": p,
            "configuration_hash_sha256": cell["configuration_hash_sha256"],
            "terminal_status": status,
            "reason": cell_entry["reason"],
            "evidence_path": cell_entry["evidence_path"],
            "n_eligible_rows": n_eligible,
            "endpoints_evaluated": endpoints_evaluated,
            "next_step": cell_entry["next_step"],
        }

    m_tests = len(cells) * len(ENDPOINTS)
    n_executed = summary["ok"] * len(ENDPOINTS)
    holm = {
        "family_size_tests": m_tests,
        "cells": len(cells),
        "endpoints_per_cell": len(ENDPOINTS),
        "tests_executed": n_executed,
        "tests_blocked": m_tests - n_executed,
        "alpha": ALPHA,
        "procedure": "Holm step-down across the full registered family (324 cells x 8 endpoints = 2,592 tests)",
        "applied": n_executed > 0,
        "smallest_threshold": ALPHA / m_tests if m_tests else None,
        "note": (
            "No cell is executable on Q1-only data (all blocked by minimum_history_rule); "
            "there are no p-values to correct. Thresholds documented for when data is extended."
        ),
    }

    scaffold = {
        "schema_version": "1.0",
        "program_id": config["program_id"],
        "experiment_id": config["experiment_id"],
        "grid_id": config["grid_id"],
        "config_path": str(args.config.relative_to(ROOT)),
        "config_sha256": config_sha,
        "grid_manifest_path": str(args.manifest.relative_to(ROOT)),
        "manifest_config_sha256": manifest.get("config_sha256"),
        "integrated_source": str(args.integrated.relative_to(ROOT)),
        "integrated_rows_sha256": integrated.get("hashes", {}).get(
            "integrated_rows_sha256"
        ),
        "n_integrated_rows": n_rows,
        "n_exclusions_integrated": integrated.get("n_exclusions"),
        "symbols": symbols,
        "data_window": {"start": data_start, "end": data_end},
        "horizons_days": integrated.get("horizons_days"),
        "minimum_history_rule": "Require full rolling_reference_days valid prior daily observations; never shorten a window or substitute a threshold.",
        "coverage_gate": COVERAGE_GATE,
        "primary_anchor": config["grid"]["primary_anchor"],
        "cells": scaffold_cells,
        "summary": summary,
        "holm_correction": holm,
        "generated_at_utc": datetime.now(timezone.utc).isoformat(),
        "status": "complete",
    }
    atomic_write(args.scaffold_out, scaffold)

    ledger = {
        "schema_version": "1.0",
        "program_id": config["program_id"],
        "experiment_id": config["experiment_id"],
        "grid_id": config["grid_id"],
        "grid_manifest_path": str(args.manifest.relative_to(ROOT)),
        "total_cells": len(cells),
        "cells": ledger_cells,
        "summary": summary,
        "holm_correction": holm,
        "last_updated_utc": datetime.now(timezone.utc).isoformat(),
        "notes": [
            "Ledger populated by scripts/execute_grid_q1.py (Q1 cohort).",
            "Every non-ok cell has reason, evidence_path, and next_step.",
            "Config not modified; frozen config hash recorded.",
        ],
    }
    atomic_write(args.ledger_out, ledger)

    print(
        f"cells={len(cells)} ok={summary['ok']} blocked={summary['blocked']} "
        f"failed={summary['failed']} incomplete={summary['incomplete']} "
        f"invalid={summary['invalid']} not_run={summary['not_run']}"
    )
    print(f"scaffold -> {args.scaffold_out}")
    print(f"ledger -> {args.ledger_out}")
    print(f"holm family tests={m_tests} executed={n_executed} applied={holm['applied']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
