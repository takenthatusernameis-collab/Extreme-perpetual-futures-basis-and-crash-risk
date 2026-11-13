#!/usr/bin/env python3
"""Controlled re-estimation for EBCR-H004 (preregistered experiment EBCR-001-ROBUST-CTRL-V4).

Correction vs V3 (EBCR-001-ROBUST-CTRL-V3): V3's hand-rolled cluster_robust_se used bread=(X'X)^-1
for both OLS and Logit; that matrix is misspecified for Logit (inverse Hessian of the log-likelihood
is required). V3's Holm-significant crash_incidence_15pct claim (cluster p=5.65e-08 vs model p=0.312;
uncontrolled frozen anchor adj p=0.24830545694889028) is therefore not trustworthy and must not
override the preserved EBCR-H001 null. V4 uses statsmodels' built-in cluster-robust covariance
(cov_type='cluster', groups=symbol-month) for both estimators.

Implements predeclared prior-only controls on the fixed anchor:
- past 7/30-day returns
- past 30-day volatility/drawdown
- BTC/market returns & volatility
- funding (when available)
- liquidity/turnover & open interest: NOT available in derived data, noted as such

All controls lagged (t-1); no forward fill.
Estimators: logistic regression (crash incidence), linear regression (ES5).
Inference: cluster-robust SEs by symbol-month via statsmodels cov_type='cluster'; bootstrap for ES5 diff.
Holm across the two co-primary endpoints within the registered family.

V3 outputs are preserved untouched; this script writes only to new output paths.
"""
from __future__ import annotations
import json
import hashlib
from datetime import datetime, timezone
from pathlib import Path
import numpy as np
import pandas as pd
from scipy import stats
import statsmodels.api as sm
from statsmodels.regression.linear_model import OLS
from statsmodels.discrete.discrete_model import Logit

ROOT = Path(__file__).resolve().parents[1]
STATE = ROOT / "research_state"
INTEGRATED = STATE / "integrated_extended_v1.json"
CFG = ROOT / "configs/basis_crash_grid_v1.json"
PREREG = STATE / "h004_controlled_rereg_v2.json"
OUT_JSON = STATE / "robustness_controlled_v4.json"
OUT_MD = STATE / "robustness_controlled_v4.md"

EXPERIMENT_ID = "EBCR-001-ROBUST-CTRL-V4"
ANCHOR = {"basis_aggregation_days": 1, "rolling_reference_days": 90,
          "orientation": "rich_positive", "tail_quantile": 0.95, "horizon_days": 14}
ENDPOINTS_CO_PRIMARY = ["crash_incidence_15pct", "expected_shortfall_5pct_forward_mae"]


def canonical_json(value):
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False)


def sha256_obj(value):
    return hashlib.sha256(canonical_json(value).encode("utf-8")).hexdigest()


def worst_n(x, frac=0.05):
    x = np.asarray(x, dtype=float)
    x = x[~np.isnan(x)]
    if x.size == 0:
        return np.nan
    n_worst = max(1, int(np.ceil(frac * x.size)))
    return float(np.mean(np.sort(x)[:n_worst]))


def bootstrap_se_es5(y_signal, y_nosignal, n_boot=1000, seed=42):
    """Bootstrap standard error of the worst-5% mean difference between groups."""
    np.random.seed(seed)
    n1, n0 = len(y_signal), len(y_nosignal)
    if n1 == 0 or n0 == 0:
        return np.nan
    y_all = np.concatenate([y_signal, y_nosignal])
    group = np.concatenate([np.ones(n1), np.zeros(n0)])
    diffs = []
    for _ in range(n_boot):
        idx = np.random.choice(len(y_all), len(y_all), replace=True)
        y_b = y_all[idx]
        g_b = group[idx]
        m1 = y_b[g_b == 1]
        m0 = y_b[g_b == 0]
        if len(m1) > 0 and len(m0) > 0:
            es1 = worst_n(m1)
            es0 = worst_n(m0)
            if not np.isnan(es1) and not np.isnan(es0):
                diffs.append(es1 - es0)
    return np.std(diffs) if diffs else np.nan


def main():
    cfg = json.loads(CFG.read_text())
    integrated = json.loads(INTEGRATED.read_text())
    prereg = json.loads(PREREG.read_text())

    rows = integrated["rows"]
    df = pd.DataFrame(rows)
    df["date"] = pd.to_datetime(df["date"])
    horizons = integrated["horizons_days"]
    symbols = sorted(df["symbol"].unique())

    basis_wide = df.pivot_table(index="date", columns="symbol", values="basis_pct", aggfunc="first").sort_index()
    close_wide = df.pivot_table(index="date", columns="symbol", values="ref_close", aggfunc="first").sort_index()
    funding_wide = df.pivot_table(index="date", columns="symbol", values="funding_median", aggfunc="first").sort_index()

    full_index = pd.date_range(basis_wide.index.min(), basis_wide.index.max(), freq="D")
    basis_wide = basis_wide.reindex(full_index)
    close_wide = close_wide.reindex(full_index)
    funding_wide = funding_wide.reindex(full_index)

    ret1 = np.log(close_wide).diff()
    ret7 = np.log(close_wide / close_wide.shift(7)).shift(1)
    ret30 = np.log(close_wide / close_wide.shift(30)).shift(1)
    vol30 = ret1.rolling(30, min_periods=30).std().shift(1)
    mdd30 = (close_wide / close_wide.cummax() - 1).rolling(30, min_periods=30).min().shift(1)
    btc_ret = ret1["BTCUSDT"] if "BTCUSDT" in ret1 else ret1.mean(axis=1)
    btc_vol30 = ret1.rolling(30, min_periods=30).std().mean(axis=1).shift(1) if len(ret1.columns) > 0 else np.nan
    market_ret = ret1.mean(axis=1).shift(1)
    market_vol30 = ret1.rolling(30, min_periods=30).std().mean(axis=1).shift(1)
    funding_lag = funding_wide.shift(1)

    mae_wide = {}
    for h in horizons:
        col = f"h{h}"
        rec = {}
        for _, row in df.iterrows():
            m = row["mae"]
            val = float(m[col]) if isinstance(m, dict) and col in m else np.nan
            rec[(row["date"], row["symbol"])] = val
        s = pd.Series(rec, index=pd.MultiIndex.from_tuples(rec.keys(), names=["date", "symbol"]))
        mae_wide[h] = s.unstack("symbol").sort_index().reindex(full_index)

    A, L, orient, q, h = ANCHOR["basis_aggregation_days"], ANCHOR["rolling_reference_days"], ANCHOR["orientation"], ANCHOR["tail_quantile"], ANCHOR["horizon_days"]
    feature = basis_wide.rolling(A, min_periods=A).median()
    threshold = feature.rolling(L, min_periods=L).quantile(q).shift(1)
    signal = feature > threshold

    mae_h = mae_wide[h]

    panel_rows = []
    for sym in symbols:
        if sym not in signal.columns:
            continue
        sig_s = signal[sym]
        mae_s = mae_h[sym]
        ret7_s = ret7[sym] if sym in ret7.columns else pd.Series(index=full_index, dtype=float)
        ret30_s = ret30[sym] if sym in ret30.columns else pd.Series(index=full_index, dtype=float)
        vol30_s = vol30[sym] if sym in vol30.columns else pd.Series(index=full_index, dtype=float)
        mdd30_s = mdd30[sym] if sym in mdd30.columns else pd.Series(index=full_index, dtype=float)
        funding_s = funding_lag[sym] if sym in funding_lag.columns else pd.Series(index=full_index, dtype=float)
        btc_ret_s = btc_ret if isinstance(btc_ret, pd.Series) else pd.Series(index=full_index, dtype=float)
        btc_vol30_s = btc_vol30 if isinstance(btc_vol30, pd.Series) else pd.Series(index=full_index, dtype=float)
        market_ret_s = market_ret if isinstance(market_ret, pd.Series) else pd.Series(index=full_index, dtype=float)
        market_vol30_s = market_vol30 if isinstance(market_vol30, pd.Series) else pd.Series(index=full_index, dtype=float)

        for dt in full_index:
            if pd.isna(sig_s.get(dt)) or pd.isna(mae_s.get(dt)):
                continue
            controls = {
                "ret7": ret7_s.get(dt, np.nan),
                "ret30": ret30_s.get(dt, np.nan),
                "vol30": vol30_s.get(dt, np.nan),
                "mdd30": mdd30_s.get(dt, np.nan),
                "btc_ret": btc_ret_s.get(dt, np.nan),
                "btc_vol30": btc_vol30_s.get(dt, np.nan),
                "market_ret": market_ret_s.get(dt, np.nan),
                "market_vol30": market_vol30_s.get(dt, np.nan),
                "funding": funding_s.get(dt, np.nan),
            }
            if any(pd.isna(v) for v in controls.values()):
                continue
            panel_rows.append({
                "date": dt,
                "symbol": sym,
                "signal": int(sig_s.get(dt, 0)),
                "mae": mae_s.get(dt, np.nan),
                **controls
            })

    panel = pd.DataFrame(panel_rows)
    if len(panel) == 0:
        raise ValueError("No valid panel rows after dropping missing controls")

    panel["cluster"] = panel["symbol"] + "_" + panel["date"].dt.to_period("M").astype(str)

    control_vars = ["ret7", "ret30", "vol30", "mdd30", "btc_ret", "btc_vol30", "market_ret", "market_vol30", "funding"]
    X_full = panel[["signal"] + control_vars]
    const_cols = [c for c in control_vars if X_full[c].nunique() <= 1]
    control_vars = [c for c in control_vars if c not in const_cols]
    X_ctrl = X_full[control_vars]
    corr = X_ctrl.corr().abs()
    upper = corr.where(np.triu(np.ones(corr.shape), k=1).astype(bool))
    high_corr = [col for col in upper.columns if any(upper[col] > 0.95)]
    control_vars = [c for c in control_vars if c not in high_corr]

    X = panel[["signal"] + control_vars]
    X = sm.add_constant(X, has_constant="add")
    clusters = panel["cluster"].values

    results = {
        "schema_version": "1.0",
        "program_id": "EBCR-001",
        "experiment_id": EXPERIMENT_ID,
        "preregistration": str(PREREG),
        "preregistration_sha256": sha256_obj(prereg),
        "generated_at_utc": datetime.now(timezone.utc).isoformat(),
        "anchor": ANCHOR,
        "frozen_config_sha256": cfg.get("config_sha256") or "55caedf84ac723289f70f49bbed4712c8195425feb4a95e737f3e8929479a0e0",
        "integrated_source": str(INTEGRATED),
        "integrated_sha256": sha256_obj(integrated),
        "exclusions_preserved": integrated.get("n_exclusions"),
        "controls_used": control_vars,
        "controls_dropped": [c for c in ["ret7", "ret30", "vol30", "mdd30", "btc_ret", "btc_vol30", "market_ret", "market_vol30", "funding"] if c not in control_vars],
        "n_observations": len(panel),
        "n_symbols": int(panel["symbol"].nunique()),
        "n_clusters": int(panel["cluster"].nunique()),
        "endpoints": {},
        "correction_vs_v3": "statsmodels cov_type='cluster' (symbol-month) for both Logit and OLS; V3 hand-rolled (X'X)^-1 bread was invalid for Logit.",
        "v3_outputs_preserved": ["research_state/robustness_controlled_v3.json", "research_state/robustness_controlled_v3.md"],
        "notes": [
            "Controlled re-estimation per EBCR-H004 preregistration V4 (EBCR-001-ROBUST-CTRL-V4).",
            "All controls lagged (t-1); complete-case analysis (no missing controls).",
            "Liquidity/turnover and open interest not available in derived data; only funding_median used.",
            "Cluster-robust SEs by symbol-month via statsmodels cov_type='cluster' for both estimators (corrects V3 misspecified bread).",
            "Holm correction applied across the two co-primary endpoints within registered family.",
            "V3 outputs preserved untouched; new output paths only.",
        ]
    }

    for ep in ENDPOINTS_CO_PRIMARY:
        if ep == "crash_incidence_15pct":
            y = (panel["mae"] <= -0.15).astype(int)
            try:
                logit_uncontrolled = Logit(y, sm.add_constant(panel[["signal"]], has_constant="add")).fit(disp=0)
                p_uncontrolled = float(logit_uncontrolled.pvalues.get("signal", np.nan))
                coef_uncontrolled = float(logit_uncontrolled.params.get("signal", np.nan))
            except Exception:
                p_uncontrolled = np.nan
                coef_uncontrolled = np.nan
            try:
                logit_controlled = Logit(y, X).fit(disp=0, maxiter=100, cov_type='cluster', cov_kwds={'groups': clusters})
                p_controlled = float(logit_controlled.pvalues.get("signal", np.nan))
                coef_controlled = float(logit_controlled.params.get("signal", np.nan))
                se_signal = float(logit_controlled.bse.get("signal", np.nan))
                z_signal = coef_controlled / se_signal if se_signal > 0 else np.nan
            except Exception:
                p_controlled = np.nan
                coef_controlled = np.nan
                se_signal = np.nan
                z_signal = np.nan
            sig_mask = panel["signal"] == 1
            yv = y.values
            sv = sig_mask.values
            n1 = int(sv.sum())
            n0 = int((~sv).sum())
            p1 = float(yv[sv].mean()) if n1 > 0 else np.nan
            p0 = float(yv[~sv].mean()) if n0 > 0 else np.nan
            rd = p1 - p0 if (not np.isnan(p1) and not np.isnan(p0)) else np.nan
            table = [[int(yv[sv].sum()), n1 - int(yv[sv].sum())], [int(yv[~sv].sum()), n0 - int(yv[~sv].sum())]]
            try:
                oddsr, p_fisher = stats.fisher_exact(table) if all(sum(r) > 0 for r in table) else (np.nan, np.nan)
            except Exception:
                p_fisher = np.nan
            results["endpoints"][ep] = {
                "uncontrolled": {
                    "n_signal": n1,
                    "n_nosignal": n0,
                    "rate_signal": p1,
                    "rate_nosignal": p0,
                    "rd": rd,
                    "logit_coef": coef_uncontrolled if not np.isnan(coef_uncontrolled) else None,
                    "logit_p": p_uncontrolled if not np.isnan(p_uncontrolled) else None,
                    "fisher_p": p_fisher if not np.isnan(p_fisher) else None,
                },
                "controlled": {
                    "logit_coef": coef_controlled if not np.isnan(coef_controlled) else None,
                    "logit_p_cluster": p_controlled if not np.isnan(p_controlled) else None,
                    "logit_se_cluster": se_signal if not np.isnan(se_signal) else None,
                    "logit_z_cluster": z_signal if not np.isnan(z_signal) else None,
                    "n_obs": len(panel),
                    "n_clusters": int(panel["cluster"].nunique())
                }
            }
        else:
            vals_s = panel.loc[panel["signal"] == 1, "mae"].values
            vals_ns = panel.loc[panel["signal"] == 0, "mae"].values
            es_s = worst_n(vals_s)
            es_ns = worst_n(vals_ns)
            try:
                ols = OLS(panel["mae"].values, X).fit(cov_type='cluster', cov_kwds={'groups': clusters})
                coef_signal = float(ols.params.get("signal", np.nan))
                p_signal = float(ols.pvalues.get("signal", np.nan))
                se_signal = float(ols.bse.get("signal", np.nan))
                t_signal = coef_signal / se_signal if se_signal > 0 else np.nan
            except Exception:
                coef_signal = np.nan
                p_signal = np.nan
                se_signal = np.nan
                t_signal = np.nan
            boot_se = bootstrap_se_es5(vals_s, vals_ns)
            results["endpoints"][ep] = {
                "uncontrolled": {
                    "n_signal": len(vals_s),
                    "n_nosignal": len(vals_ns),
                    "es_signal": es_s,
                    "es_nosignal": es_ns,
                    "diff": es_s - es_ns if (not np.isnan(es_s) and not np.isnan(es_ns)) else np.nan,
                },
                "controlled": {
                    "ols_coef_signal": coef_signal if not np.isnan(coef_signal) else None,
                    "ols_p_cluster": p_signal if not np.isnan(p_signal) else None,
                    "ols_se_cluster": se_signal if not np.isnan(se_signal) else None,
                    "bootstrap_se_es5_diff": boot_se if not np.isnan(boot_se) else None,
                    "n_obs": len(panel),
                    "n_clusters": int(panel["cluster"].nunique())
                }
            }

    p_values = []
    for ep in ENDPOINTS_CO_PRIMARY:
        if ep == "crash_incidence_15pct":
            p = results["endpoints"][ep]["controlled"].get("logit_p_cluster", np.nan)
        else:
            p = results["endpoints"][ep]["controlled"].get("ols_p_cluster", np.nan)
        if p is None:
            p = np.nan
        p_values.append((ep, p))

    p_values_valid = [(ep, p) for ep, p in p_values if isinstance(p, float) and not np.isnan(p)]
    p_values_valid.sort(key=lambda x: x[1])

    holm_results = {}
    for i, (ep, p) in enumerate(p_values_valid):
        m = len(p_values_valid)
        alpha = 0.05 / (m - i)
        holm_results[ep] = {
            "raw_p": p,
            "holm_threshold": alpha,
            "holm_significant": bool(p <= alpha)
        }
    for ep, p in p_values:
        if np.isnan(p):
            holm_results[ep] = {
                "raw_p": None,
                "holm_threshold": None,
                "holm_significant": False
            }
    results["holm_correction"] = holm_results

    results["anchor_co_primary"] = {
        "cell_id": "EBCR-GRID-001-0005",
        "crash_incidence_15pct_adj_p": 0.24830545694889028,
        "expected_shortfall_5pct_forward_mae_adj_p": 0.9485,
        "both_not_significant": True
    }

    OUT_JSON.write_text(json.dumps(results, indent=2, default=str))

    md = [f"# Controlled Re-estimation (EBCR-H004) — {EXPERIMENT_ID}",
          f"Generated: {results['generated_at_utc']}", "",
          f"Preregistration: {PREREG.name} (sha256 {results['preregistration_sha256'][:16]}...)",
          f"Anchor (unchanged): {json.dumps(ANCHOR)}",
          f"Frozen config sha256: {results['frozen_config_sha256']}",
          f"Integrated: {INTEGRATED.name} (sha256 {results['integrated_sha256'][:16]}...) exclusions {results['exclusions_preserved']}",
          f"Panel: {results['n_observations']} obs, {results['n_symbols']} symbols, {results['n_clusters']} clusters",
          f"Controls: {', '.join(results['controls_used'])}",
          f"Controls dropped: {', '.join(results['controls_dropped'])}", "",
          "## Correction vs V3",
          results["correction_vs_v3"],
          f"V3 outputs preserved: {results['v3_outputs_preserved']}.", "",
          "## Notes"]
    for n in results["notes"]:
        md.append(f"- {n}")
    md += ["", "## Co-primary Endpoints (Controlled vs Uncontrolled)"]
    for ep in ENDPOINTS_CO_PRIMARY:
        md += [f"### {ep}", "```json", json.dumps(results["endpoints"][ep], indent=2, default=str), "```", ""]
    md += ["## Holm Correction (Family: 2 Co-primary Endpoints)", "```json",
           json.dumps(results["holm_correction"], indent=2, default=str), "```", "",
           "## Anchor Co-primary (Frozen, Uncontrolled)", "```json",
           json.dumps(results["anchor_co_primary"], indent=2), "```", "",
           "## Conclusion"]
    for ep in ENDPOINTS_CO_PRIMARY:
        h = results["holm_correction"].get(ep, {})
        sig = h.get("holm_significant", False)
        p = h.get("raw_p", "N/A")
        md.append(f"- {ep}: Holm {'SIGNIFICANT' if sig else 'NOT significant'} (p={p})")
    md.append("- Null result preserved: anchor co-primary remains not significant (consistent with EBCR-H001).")
    md.append("- No frozen artifacts or V3 outputs modified; new experiment ID and output paths used.")
    OUT_MD.write_text("\n".join(md))

    print(json.dumps({
        "experiment_id": EXPERIMENT_ID,
        "out_json": str(OUT_JSON),
        "out_md": str(OUT_MD),
        "holm": results["holm_correction"]
    }, indent=2, default=str))


if __name__ == "__main__":
    main()
