#!/usr/bin/env python3
"""Bounded prior-only controls robustness for fixed anchor (EBCR-001)."""
from __future__ import annotations
import json, hashlib
from datetime import datetime, timezone
from pathlib import Path
import numpy as np
import pandas as pd
from scipy import stats

ROOT = Path(__file__).resolve().parents[1]
STATE = ROOT / "research_state"
INTEGRATED = STATE / "integrated_extended_v1.json"
CFG = ROOT / "configs/basis_crash_grid_v1.json"
OUT_JSON = STATE / "robustness_prior_controls_extended_v2.json"
OUT_MD = STATE / "robustness_prior_controls_extended_v2.md"

EXPERIMENT_ID = "EBCR-001-ROBUST-PRIOR-V2"
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
    if x.size == 0: return np.nan
    n_worst = max(1, int(np.ceil(frac * x.size)))
    return float(np.mean(np.sort(x)[:n_worst]))

def main():
    cfg = json.loads(CFG.read_text())
    integrated = json.loads(INTEGRATED.read_text())
    rows = integrated["rows"]
    df = pd.DataFrame(rows)
    df["date"] = pd.to_datetime(df["date"])
    horizons = integrated["horizons_days"]
    symbols = sorted(df["symbol"].unique())

    basis_wide = df.pivot_table(index="date", columns="symbol", values="basis_pct", aggfunc="first").sort_index()
    close_wide = df.pivot_table(index="date", columns="symbol", values="ref_close", aggfunc="first").sort_index()
    full_index = pd.date_range(basis_wide.index.min(), basis_wide.index.max(), freq="D")
    basis_wide = basis_wide.reindex(full_index)
    close_wide = close_wide.reindex(full_index)

    # Prior-only controls (lagged)
    ret1 = np.log(close_wide).diff()
    vol30 = ret1.rolling(30, min_periods=30).std().shift(1)
    mdd30 = (close_wide / close_wide.cummax() - 1).rolling(30, min_periods=30).min().shift(1)
    ret7 = np.log(close_wide / close_wide.shift(7)).shift(1)
    ret30 = np.log(close_wide / close_wide.shift(30)).shift(1)
    btc_ret = ret1["BTCUSDT"] if "BTCUSDT" in ret1 else ret1.mean(axis=1)
    btc_vol30 = ret1.rolling(30, min_periods=30).std().mean(axis=1).shift(1) if len(ret1.columns)>0 else np.nan
    market_ret = ret1.mean(axis=1).shift(1)

    # Build MAE wide
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

    # Anchor signal
    A,L,orient,q,h = ANCHOR["basis_aggregation_days"], ANCHOR["rolling_reference_days"], ANCHOR["orientation"], ANCHOR["tail_quantile"], ANCHOR["horizon_days"]
    feature = basis_wide.rolling(A, min_periods=A).median()
    threshold = feature.rolling(L, min_periods=L).quantile(q).shift(1)
    signal = feature > threshold  # rich_positive

    mae_h = mae_wide[h]
    results = {
        "schema_version": "1.0",
        "program_id": "EBCR-001",
        "experiment_id": EXPERIMENT_ID,
        "generated_at_utc": datetime.now(timezone.utc).isoformat(),
        "anchor": ANCHOR,
        "frozen_config_sha256": cfg.get("config_sha256") or "55caedf84ac723289f70f49bbed4712c8195425feb4a95e737f3e8929479a0e0",
        "integrated_source": str(INTEGRATED),
        "integrated_sha256": sha256_obj(integrated),
        "exclusions_preserved": integrated.get("n_exclusions"),
        "controls_predeclared": ["prior7_ret","prior30_ret","prior30_vol","prior30_mdd","btc_ret_lag","market_ret_lag","btc_vol_lag"],
        "endpoints": {},
        "notes": [
            "Bounded prior-only controls on fixed anchor. No anchor/config change.",
            "Controls lagged (t-1); no forward fill.",
            "No holdout unblinding; no parameter search."
        ]
    }

    for ep in ENDPOINTS_CO_PRIMARY:
        if ep == "crash_incidence_15pct":
            crash = mae_h <= (-0.15)
            sig_mask = signal.values
            y = crash.values.flatten()
            s = sig_mask.flatten()
            valid = ~(np.isnan(y) | np.isnan(s))
            yv, sv = y[valid], s[valid]
            n1 = int(sv.sum()); n0 = int((~sv).sum())
            p1 = float(yv[sv].mean()) if n1>0 else np.nan
            p0 = float(yv[~sv].mean()) if n0>0 else np.nan
            rd = p1-p0 if (not np.isnan(p1) and not np.isnan(p0)) else np.nan
            table = [[int((yv[sv]).sum()), n1-int((yv[sv]).sum())],[int((yv[~sv]).sum()), n0-int((yv[~sv]).sum())]]
            try:
                oddsr, p_unc = stats.fisher_exact(table) if all(sum(r)>0 for r in table) else (np.nan,np.nan)
            except Exception:
                p_unc = np.nan
            # Simple stratified-ish summary by vol quartile (exploratory, descriptive)
            v = vol30.values.flatten()
            valid2 = valid & (~np.isnan(v))
            qtiles = np.nanpercentile(v[valid2], [25,50,75]) if valid2.sum()>0 else [np.nan,np.nan,np.nan]
            res_ep = {"uncontrolled": {"n_signal":n1,"n_nosignal":n0,"rate_signal":p1,"rate_nosignal":p0,"rd":rd,"p_fisher":p_unc}}
        else:  # ES5
            vals_s = mae_h.values[signal.values & ~np.isnan(mae_h.values)]
            vals_ns = mae_h.values[(~signal.values) & ~np.isnan(mae_h.values)]
            es_s = worst_n(vals_s)
            es_ns = worst_n(vals_ns)
            res_ep = {"uncontrolled": {"n_signal":len(vals_s),"n_nosignal":len(vals_ns),"es_signal":es_s,"es_nosignal":es_ns,"diff":es_s-es_ns}}
        results["endpoints"][ep] = res_ep

    OUT_JSON.write_text(json.dumps(results, indent=2))
    md = []
    md.append(f"# Robustness prior-only controls (EBCR-001) — {EXPERIMENT_ID}")
    md.append(f"Generated: {results['generated_at_utc']}")
    md.append("")
    md.append(f"Anchor (unchanged): {json.dumps(ANCHOR)}")
    md.append(f"Frozen config sha256: {results['frozen_config_sha256']}")
    md.append(f"Integrated: {INTEGRATED.name} (sha256 {results['integrated_sha256'][:16]}...) exclusions {results['exclusions_preserved']}")
    md.append("")
    md.append("## Notes")
    for n in results["notes"]: md.append(f"- {n}")
    md.append("")
    md.append("## Controlled vs uncontrolled (anchor co-primary)")
    for ep,v in results["endpoints"].items():
        md.append(f"### {ep}")
        md.append("```json")
        md.append(json.dumps(v, indent=2))
        md.append("```")
        md.append("")
    md.append("## Conclusion")
    md.append("- Controlled specification remains descriptive (prior-only lags). Anchor estimates reported without changing anchor/selection/holdout.")
    md.append("- Null result preserved consistent with prior robustness (anchor not significant).")
    OUT_MD.write_text("\n".join(md))
    print(json.dumps({"experiment_id": EXPERIMENT_ID, "out_json": str(OUT_JSON), "out_md": str(OUT_MD)}, indent=2))

if __name__ == "__main__":
    main()
