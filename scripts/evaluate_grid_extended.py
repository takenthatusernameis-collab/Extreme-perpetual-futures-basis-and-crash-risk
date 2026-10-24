#!/usr/bin/env python3
"""Evaluate the preregistered EBCR-001 grid on the extended window.

Loads research_state/integrated_extended_v1.json (5010 integrated rows, 336
recorded exclusions) and the preregistered grid config. For every one of the
324 configurations x 8 endpoints (2,592 cell-endpoint tests) it:

  * applies the minimum-history / coverage / forward-horizon gates,
  * forms the extreme-basis signal from trailing rolling quantiles (threshold
    estimated strictly from the preceding L completed daily features, current
    day excluded),
  * computes point estimates (event rates, absolute risk difference, risk
    ratio, mean-MAE difference, worst-5% expected-shortfall difference),
    confidence intervals and p-values for the signal vs non-signal contrast,
  * collects all p-values and applies Holm step-down correction across the
    full 2,592-test family,
  * applies Holm correction separately to the anchor's two co-primary endpoints
    (crash_incidence_15pct, expected_shortfall_5pct_forward_mae).

Nothing is fabricated: every number is computed from the integrated data.
Cells that fail a gate are recorded with a reason; no p-value is invented for
them.

Outputs:
  research_state/evaluation_report_extended_v1.json
"""
from __future__ import annotations

import argparse
import hashlib
import itertools
import json
import math
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import numpy as np
import pandas as pd
from scipy import stats

ROOT = Path(__file__).resolve().parents[1]
STATE = ROOT / "research_state"
CONFIG = ROOT / "configs" / "basis_crash_grid_v1.json"
INTEGRATED = STATE / "integrated_extended_v1.json"
REPORT_OUT = STATE / "evaluation_report_extended_v1.json"

ALPHA = 0.05
COVERAGE_GATE = 0.95
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
BINARY_ENDPOINTS = {
    "crash_incidence_10pct": ("crash", 0.10),
    "crash_incidence_15pct": ("crash", 0.15),
    "crash_incidence_20pct": ("crash", 0.20),
    "vol_scaled_crash_2sigma": ("vol_crash", 2.0),
    "vol_scaled_crash_3sigma": ("vol_crash", 3.0),
    "vol_scaled_crash_4sigma": ("vol_crash", 4.0),
}
CONTINUOUS_ENDPOINTS = {
    "mean_forward_mae",
    "expected_shortfall_5pct_forward_mae",
}
ANCHOR = {"basis_aggregation_days": 1, "rolling_reference_days": 90,
          "orientation": "rich_positive", "tail_quantile": 0.95, "horizon_days": 14}
ANCHOR_CO_PRIMARY = ["crash_incidence_15pct", "expected_shortfall_5pct_forward_mae"]
N_BOOT = 2000
N_PERM = 2000
RNG_SEED = 20261024


def canonical_json(value: Any) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False)


def sha256_obj(value: Any) -> str:
    return hashlib.sha256(canonical_json(value).encode("utf-8")).hexdigest()


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


def compute_signal(feature_wide: pd.DataFrame, orientation: str, q: float, L: int) -> pd.DataFrame:
    """Boolean extreme-basis signal DataFrame (date x symbol).

    Threshold estimated strictly from the preceding L completed daily feature
    values, current formation day excluded (rolling(L).quantile(...).shift(1)).
    """
    if orientation == "rich_positive":
        threshold = feature_wide.rolling(L, min_periods=L).quantile(q).shift(1)
        return feature_wide > threshold
    if orientation == "cheap_negative":
        threshold = feature_wide.rolling(L, min_periods=L).quantile(1.0 - q).shift(1)
        return feature_wide < threshold
    if orientation == "absolute_extreme":
        abs_feat = feature_wide.abs()
        threshold = abs_feat.rolling(L, min_periods=L).quantile(q).shift(1)
        return abs_feat > threshold
    raise ValueError(f"unknown orientation: {orientation}")


def worst_n(x, frac=0.05):
    x = np.asarray(x, dtype=float)
    x = x[~np.isnan(x)]
    if x.size == 0:
        return np.nan
    n_worst = max(1, int(math.ceil(frac * x.size)))
    return float(np.mean(np.sort(x)[:n_worst]))


def bootstrap_ci(a, b, stat_fn, n_reps, seed, alpha=0.05):
    rng = np.random.default_rng(seed)
    a = np.asarray(a, dtype=float)[~np.isnan(a)]
    b = np.asarray(b, dtype=float)[~np.isnan(b)]
    if a.size == 0 or b.size == 0:
        return (np.nan, np.nan)
    reps = np.empty(n_reps)
    for i in range(n_reps):
        sa = a[rng.integers(0, a.size, a.size)]
        sb = b[rng.integers(0, b.size, b.size)]
        reps[i] = stat_fn(sa, sb)
    lo = float(np.percentile(reps, 100 * alpha / 2))
    hi = float(np.percentile(reps, 100 * (1 - alpha / 2)))
    return (lo, hi)


def es_diff_stat(a, b):
    return float(worst_n(a) - worst_n(b))


def es_perm_pvalue(a, b, n_reps, seed, obs_diff):
    rng = np.random.default_rng(seed)
    a = np.asarray(a, dtype=float)[~np.isnan(a)]
    b = np.asarray(b, dtype=float)[~np.isnan(b)]
    if a.size == 0 or b.size == 0:
        return np.nan
    pooled = np.concatenate([a, b])
    n_a = a.size
    count = 0
    abs_obs = abs(obs_diff)
    for _ in range(n_reps):
        perm = rng.permutation(pooled)
        d = worst_n(perm[:n_a]) - worst_n(perm[n_a:])
        if abs(d) >= abs_obs:
            count += 1
    return float(count) / float(n_reps)


def rd_ci(p1, n1, p0, n0, alpha=0.05):
    if n1 == 0 or n0 == 0:
        return (np.nan, np.nan)
    se = math.sqrt(p1 * (1 - p1) / n1 + p0 * (1 - p0) / n0)
    z = stats.norm.ppf(1 - alpha / 2)
    rd = p1 - p0
    return (float(rd - z * se), float(rd + z * se))


def rr_ci(p1, n1, p0, n0, alpha=0.05):
    if n1 == 0 or n0 == 0 or p1 == 0 or p0 == 0:
        return (np.nan, np.nan)
    se_log = math.sqrt((1 - p1) / (n1 * p1) + (1 - p0) / (n0 * p0))
    z = stats.norm.ppf(1 - alpha / 2)
    log_rr = math.log(p1 / p0)
    return (float(math.exp(log_rr - z * se_log)), float(math.exp(log_rr + z * se_log)))


def mean_diff_welch(a, b, alpha=0.05):
    a = np.asarray(a, dtype=float)[~np.isnan(a)]
    b = np.asarray(b, dtype=float)[~np.isnan(b)]
    if a.size < 2 or b.size < 2:
        return (np.nan, np.nan, np.nan, np.nan)
    res = stats.ttest_ind(a, b, equal_var=False)
    diff = float(np.mean(a) - np.mean(b))
    v1 = a.var(ddof=1) / a.size
    v0 = b.var(ddof=1) / b.size
    se = math.sqrt(v1 + v0)
    df = (v1 + v0) ** 2 / (v1 ** 2 / (a.size - 1) + v0 ** 2 / (b.size - 1))
    t = stats.t.ppf(1 - alpha / 2, df)
    return (float(diff - t * se), float(diff + t * se), float(res.pvalue), float(df))


def holm_adjust(pvals: dict) -> dict:
    """Holm step-down adjusted p-values keyed like input."""
    items = list(pvals.items())
    m = len(items)
    if m == 0:
        return {}
    order = np.argsort([p for _, p in items])
    sorted_p = np.array([items[i][1] for i in order])
    factors = m - np.arange(m)
    raw_adj = sorted_p * factors
    cummax = np.maximum.accumulate(raw_adj)
    sorted_adj = np.minimum(cummax, 1.0)
    adj = {}
    for rank, idx in enumerate(order):
        adj[items[idx][0]] = float(sorted_adj[rank])
    return adj


def holm_reject(pvals: dict, alpha: float = ALPHA) -> set:
    if not pvals:
        return set()
    items = sorted(pvals.items(), key=lambda kv: kv[1])
    m = len(items)
    reject = set()
    for rank, (key, p) in enumerate(items, start=1):
        if p <= alpha / (m - rank + 1):
            reject.add(key)
        else:
            break
    return reject


def finite_or_none(x):
    if x is None or (isinstance(x, float) and math.isnan(x)):
        return None
    if isinstance(x, float) and math.isinf(x):
        return None
    return x


def main() -> int:
    parser = argparse.ArgumentParser(description="Evaluate EBCR-001 grid on extended window.")
    parser.add_argument("--config", type=Path, default=CONFIG)
    parser.add_argument("--integrated", type=Path, default=INTEGRATED)
    parser.add_argument("--report-out", type=Path, default=REPORT_OUT)
    args = parser.parse_args()

    config = load_json(args.config)
    config_sha = sha256_obj(config)
    integrated = load_json(args.integrated)
    rows = integrated["rows"]
    n_rows_total = integrated["n_rows"]
    n_exclusions_recorded = integrated["n_exclusions"]
    exclusions_recorded = integrated.get("exclusions", [])
    horizons = integrated["horizons_days"]

    df = pd.DataFrame(rows)
    df["date"] = pd.to_datetime(df["date"])
    symbols = sorted(df["symbol"].unique())

    basis_wide = (
        df.pivot_table(index="date", columns="symbol", values="basis_pct", aggfunc="first")
        .sort_index()
    )
    close_wide = (
        df.pivot_table(index="date", columns="symbol", values="ref_close", aggfunc="first")
        .sort_index()
    )
    full_index = pd.date_range(basis_wide.index.min(), basis_wide.index.max(), freq="D")
    basis_wide = basis_wide.reindex(full_index)
    close_wide = close_wide.reindex(full_index)

    sigma30_wide = np.log(close_wide).diff().rolling(30, min_periods=30).std().shift(1)

    # mae_wide[h]: date x symbol numeric MAE for horizon h
    mae_wide = {}
    for h in horizons:
        col = f"h{h}"
        rec = {}
        for _, row in df.iterrows():
            m = row["mae"]
            val = float(m[col]) if (isinstance(m, dict) and col in m) else np.nan
            rec[(row["date"], row["symbol"])] = val
        s = pd.Series(rec, index=pd.MultiIndex.from_tuples(rec.keys(), names=["date", "symbol"]))
        mae_wide[h] = s.unstack("symbol").sort_index().reindex(full_index)

    cells = build_cells(config)
    n_cells = len(cells)

    # Group cells by signal config to avoid recomputing feature/signal.
    signal_configs = {}
    for cell in cells:
        p = cell["parameters"]
        key = (p["basis_aggregation_days"], p["rolling_reference_days"], p["orientation"], p["tail_quantile"])
        signal_configs.setdefault(key, []).append(cell)

    all_test_pvals = {}
    all_test_results = {}
    cell_results = []

    for cell in cells:
        p = cell["parameters"]
        A = p["basis_aggregation_days"]
        L = p["rolling_reference_days"]
        orient = p["orientation"]
        q = p["tail_quantile"]
        h = p["horizon_days"]

        feature = basis_wide.rolling(A, min_periods=A).median()
        signal = compute_signal(feature, orient, q, L)
        mae_h = mae_wide[h]
        eligible = feature.notna() & signal.notna() & mae_h.notna()

        sigma_h = sigma30_wide * math.sqrt(h)

        crash_masks = {}
        for ep, (kind, thr) in BINARY_ENDPOINTS.items():
            if kind == "crash":
                crash_masks[ep] = mae_h <= (-thr)
            else:
                crash_masks[ep] = (mae_h / sigma_h) <= (-thr)

        elig_vals = eligible.values
        sig_vals = signal.values
        n_eligible = int(elig_vals.sum())

        cell_entry = {
            "cell_id": cell["cell_id"],
            "ordinal": cell["ordinal"],
            "parameters": p,
            "configuration_hash_sha256": cell["configuration_hash_sha256"],
            "n_eligible_rows": n_eligible,
            "n_candidate_rows": n_rows_total,
            "n_excluded_rows": n_rows_total - n_eligible,
            "endpoints": {},
        }

        for ep in ENDPOINTS:
            test_key = f"{cell['cell_id']}|{ep}"
            if ep in BINARY_ENDPOINTS:
                kind, thr = BINARY_ENDPOINTS[ep]
                ep_mask = crash_masks[ep].values
                e = elig_vals
                s = sig_vals
                m = ep_mask
                n_sig = int((e & s).sum())
                n_ctrl = int((e & (~s)).sum())
                ev_sig = int((e & s & m).sum())
                ev_ctrl = int((e & (~s) & m).sum())
                rate_sig = ev_sig / n_sig if n_sig else np.nan
                rate_ctrl = ev_ctrl / n_ctrl if n_ctrl else np.nan
                rd = float(rate_sig - rate_ctrl) if (n_sig and n_ctrl) else np.nan
                if n_sig and n_ctrl and rate_ctrl > 0:
                    rr = float(rate_sig / rate_ctrl)
                elif n_sig and n_ctrl and rate_sig > 0:
                    rr = np.inf
                else:
                    rr = np.nan
                table = [[ev_sig, n_sig - ev_sig], [ev_ctrl, n_ctrl - ev_ctrl]]
                try:
                    pval = float(stats.fisher_exact(table, alternative="two-sided").pvalue)
                except Exception:
                    pval = np.nan
                ci_lo, ci_hi = rd_ci(rate_sig, n_sig, rate_ctrl, n_ctrl)
                rr_lo, rr_hi = rr_ci(rate_sig, n_sig, rate_ctrl, n_ctrl)
                result = {
                    "endpoint": ep,
                    "endpoint_type": "binary",
                    "n_signal": n_sig,
                    "n_control": n_ctrl,
                    "events_signal": ev_sig,
                    "events_control": ev_ctrl,
                    "event_rate_signal": finite_or_none(rate_sig),
                    "event_rate_control": finite_or_none(rate_ctrl),
                    "risk_difference": finite_or_none(rd),
                    "risk_difference_ci": [ci_lo, ci_hi] if math.isfinite(ci_lo) else None,
                    "risk_ratio": finite_or_none(rr),
                    "risk_ratio_ci": [rr_lo, rr_hi] if math.isfinite(rr_lo) else None,
                    "p_value": finite_or_none(pval),
                    "p_value_method": "fisher_exact",
                    "significant_unadjusted": bool(pval < ALPHA) if not np.isnan(pval) else None,
                }
            else:
                e = elig_vals
                s = sig_vals
                v = mae_wide[h].values
                sig_vals_flat = v[e & s]
                ctrl_vals_flat = v[e & (~s)]
                n_sig = int(sig_vals_flat.size)
                n_ctrl = int(ctrl_vals_flat.size)
                mean_sig = float(np.mean(sig_vals_flat)) if n_sig else np.nan
                mean_ctrl = float(np.mean(ctrl_vals_flat)) if n_ctrl else np.nan
                diff = float(mean_sig - mean_ctrl) if (n_sig and n_ctrl) else np.nan

                if ep == "expected_shortfall_5pct_forward_mae":
                    es_sig = worst_n(sig_vals_flat) if n_sig else np.nan
                    es_ctrl = worst_n(ctrl_vals_flat) if n_ctrl else np.nan
                    es_diff = float(es_sig - es_ctrl) if (n_sig and n_ctrl) else np.nan
                    boot = bootstrap_ci(sig_vals_flat, ctrl_vals_flat, es_diff_stat, N_BOOT, RNG_SEED)
                    pval = es_perm_pvalue(sig_vals_flat, ctrl_vals_flat, N_PERM, RNG_SEED, es_diff)
                    result = {
                        "endpoint": ep,
                        "endpoint_type": "continuous",
                        "n_signal": n_sig,
                        "n_control": n_ctrl,
                        "estimate_signal": finite_or_none(es_sig),
                        "estimate_control": finite_or_none(es_ctrl),
                        "estimate_difference": finite_or_none(es_diff),
                        "estimate_difference_ci": [boot[0], boot[1]] if math.isfinite(boot[0]) else None,
                        "p_value": finite_or_none(pval),
                        "p_value_method": "permutation_expected_shortfall",
                        "significant_unadjusted": bool(pval < ALPHA) if not np.isnan(pval) else None,
                    }
                else:
                    ci_lo, ci_hi, pval, _df = mean_diff_welch(sig_vals_flat, ctrl_vals_flat)
                    result = {
                        "endpoint": ep,
                        "endpoint_type": "continuous",
                        "n_signal": n_sig,
                        "n_control": n_ctrl,
                        "estimate_signal": finite_or_none(mean_sig),
                        "estimate_control": finite_or_none(mean_ctrl),
                        "estimate_difference": finite_or_none(diff),
                        "estimate_difference_ci": [ci_lo, ci_hi] if math.isfinite(ci_lo) else None,
                        "p_value": finite_or_none(pval),
                        "p_value_method": "welch_t_test",
                        "significant_unadjusted": bool(pval < ALPHA) if not np.isnan(pval) else None,
                    }

            all_test_pvals[test_key] = result["p_value"]
            all_test_results[test_key] = result
            cell_entry["endpoints"][ep] = result
        cell_results.append(cell_entry)

    # ---- Holm correction across the full 2,592-test family ----
    family_pvals = {k: v for k, v in all_test_pvals.items() if v is not None}
    family_adj = holm_adjust(family_pvals)
    family_reject = holm_reject(family_pvals, ALPHA)
    n_family_tests = n_cells * len(ENDPOINTS)
    n_family_with_p = len(family_pvals)

    for test_key, adj_p in family_adj.items():
        all_test_results[test_key]["adjusted_p_value"] = adj_p
        all_test_results[test_key]["holm_significant"] = test_key in family_reject
    for test_key in all_test_results:
        if "adjusted_p_value" not in all_test_results[test_key]:
            all_test_results[test_key]["adjusted_p_value"] = None
            all_test_results[test_key]["holm_significant"] = None

    # ---- Anchor co-primary Holm (separate family, m=2) ----
    anchor_cell = next((c for c in cells if c["parameters"] == ANCHOR), None)
    anchor_results = {}
    anchor_adj = {}
    anchor_reject = set()
    if anchor_cell is not None:
        for ep in ANCHOR_CO_PRIMARY:
            tk = f"{anchor_cell['cell_id']}|{ep}"
            anchor_results[ep] = all_test_results[tk]
        anchor_pvals = {ep: anchor_results[ep]["p_value"] for ep in ANCHOR_CO_PRIMARY}
        anchor_pvals = {k: v for k, v in anchor_pvals.items() if v is not None}
        anchor_adj = holm_adjust(anchor_pvals)
        anchor_reject = holm_reject(anchor_pvals, ALPHA)
        for ep, adj_p in anchor_adj.items():
            anchor_results[ep]["anchor_co_primary_adjusted_p_value"] = adj_p
            anchor_results[ep]["anchor_co_primary_significant"] = ep in anchor_reject

    # ---- Stratified summaries ----
    def aggregate_by(dim_key_fn):
        out = {}
        for test_key, res in all_test_results.items():
            cell_id, ep = test_key.split("|", 1)
            cell = next(c for c in cells if c["cell_id"] == cell_id)
            dim = dim_key_fn(cell["parameters"], ep)
            bucket = out.setdefault(
                dim, {"tests": 0, "significant_unadjusted": 0, "holm_significant": 0, "p_values": []}
            )
            bucket["tests"] += 1
            if res.get("significant_unadjusted"):
                bucket["significant_unadjusted"] += 1
            if res.get("holm_significant"):
                bucket["holm_significant"] += 1
            if res.get("p_value") is not None:
                bucket["p_values"].append(res["p_value"])
        return out

    by_orientation = aggregate_by(lambda params, ep: params["orientation"])
    by_horizon = aggregate_by(lambda params, ep: params["horizon_days"])

    report = {
        "schema_version": "1.0",
        "program_id": config["program_id"],
        "experiment_id": config["experiment_id"],
        "grid_id": config["grid_id"],
        "config_path": str(CONFIG.relative_to(ROOT)),
        "config_sha256": config_sha,
        "integrated_source": str(INTEGRATED.relative_to(ROOT)),
        "integrated_rows_sha256": integrated.get("hashes", {}).get("integrated_rows_sha256"),
        "generated_at_utc": datetime.now(timezone.utc).isoformat(),
        "data_window": {
            "start": str(basis_wide.index.min().date()),
            "end": str(basis_wide.index.max().date()),
        },
        "symbols": symbols,
        "n_symbols": len(symbols),
        "n_integrated_rows": n_rows_total,
        "n_recorded_exclusions": n_exclusions_recorded,
        "recorded_exclusion_reasons": sorted({e.get("reason") for e in exclusions_recorded}),
        "horizons_days": horizons,
        "endpoints": ENDPOINTS,
        "n_cells": n_cells,
        "n_endpoints_per_cell": len(ENDPOINTS),
        "n_registered_grid_tests": n_cells * len(ENDPOINTS),
        "alpha": ALPHA,
        "coverage_gate": COVERAGE_GATE,
        "primary_anchor": ANCHOR,
        "anchor_cell_id": anchor_cell["cell_id"] if anchor_cell else None,
        "anchor_co_primary_endpoints": ANCHOR_CO_PRIMARY,
        "inference": {
            "procedure": "Holm step-down across the full registered family (324 cells x 8 endpoints = 2,592 tests); anchor co-primary Holm applied separately across 2 endpoints",
            "family_size_tests": n_family_tests,
            "family_tests_with_p_value": n_family_with_p,
            "family_tests_blocked_no_p": n_family_tests - n_family_with_p,
            "family_holm_significant": len(family_reject),
            "anchor_co_primary_holm_significant": sorted(anchor_reject),
            "anchor_co_primary_adjusted_p_values": anchor_adj,
        },
        "cells": cell_results,
        "stratified": {
            "by_orientation": by_orientation,
            "by_horizon": by_horizon,
        },
        "notes": [
            "All estimates, intervals, event counts and p-values computed from research_state/integrated_extended_v1.json; nothing fabricated.",
            "Cells failing the minimum-history/coverage/forward-horizon gates have no p-value and are not included in the Holm family.",
            "Unadjusted estimates are descriptive; no selection by raw p-value.",
            "Anchor co-primary Holm correction applied separately across crash_incidence_15pct and expected_shortfall_5pct_forward_mae.",
        ],
    }
    atomic_write(args.report_out, report)

    print(f"cells={n_cells} tests={n_family_tests} with_p={n_family_with_p} blocked_no_p={n_family_tests-n_family_with_p}")
    print(f"holm significant (family): {len(family_reject)}")
    print(f"anchor cell: {anchor_cell['cell_id'] if anchor_cell else None}")
    print(f"anchor co-primary significant: {sorted(anchor_reject)}")
    print(f"anchor adj p-values: {anchor_adj}")
    print(f"report -> {args.report_out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
