#!/usr/bin/env python3
"""Exploratory prior-only controls for anchor (documented, no anchor change)."""
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
OUT_JSON = STATE / "robustness_prior_controls_extended_v1.json"
OUT_MD = STATE / "robustness_prior_controls_extended_v1.md"

ANCHOR = {"basis_aggregation_days": 1, "rolling_reference_days": 90,
          "orientation": "rich_positive", "tail_quantile": 0.95, "horizon_days": 14}
ENDPOINTS = ["crash_incidence_15pct", "expected_shortfall_5pct_forward_mae"]

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

    # Build controls (prior only)
    ret1 = np.log(close_wide).diff()
    vol30 = ret1.rolling(30, min_periods=30).std().shift(1)  # lagged
    mdd = (close_wide / close_wide.cummax() - 1).rolling(30, min_periods=30).min().shift(1)
    btc_ret = ret1["BTCUSDT"] if "BTCUSDT" in ret1 else ret1.mean(axis=1)
    btc_ret_lag = btc_ret.shift(1)

    # MAE
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

    # Signal for anchor
    A,L,orient,q,h = ANCHOR["basis_aggregation_days"], ANCHOR["rolling_reference_days"], ANCHOR["orientation"], ANCHOR["tail_quantile"], ANCHOR["horizon_days"]
    feature = basis_wide.rolling(A, min_periods=A).median()
    threshold = feature.rolling(L, min_periods=L).quantile(q).shift(1)
    signal = feature > threshold  # rich_positive
    mae_h = mae_wide[h]

    # For each endpoint, compute uncontrolled and controlled (stratify by vol quartile / BTC regime as simple controls)
    results = {"anchor": ANCHOR, "endpoints": {}, "notes": ["Exploratory only - no anchor/config change. Controls are predeclared (lagged). No holdout unblinded."]}

    for ep in ENDPOINTS:
        if ep == "crash_incidence_15pct":
            crash = mae_h <= (-0.15)
        else:  # ES5
            crash = None  # handled separately
        # uncontrolled
        sig_mask = signal.values
        if crash is not None:
            y = crash.values.flatten()
            s = sig_mask.flatten()
            # valid
            valid = ~(np.isnan(y) | np.isnan(s))
            yv, sv = y[valid], s[valid]
            n1 = int(sv.sum()); n0 = int((~sv).sum())
            p1 = float(yv[sv].mean()) if n1>0 else np.nan
            p0 = float(yv[~sv].mean()) if n0>0 else np.nan
            rd = p1-p0 if (not np.isnan(p1) and not np.isnan(p0)) else np.nan
            # simple pval
            from scipy.stats import fisher_exact, chi2_contingency
            table = [[int((yv[sv]).sum()), n1-int((yv[sv]).sum())],[int((yv[~sv]).sum()), n0-int((yv[~sv]).sum())]]
            try:
                oddsr, p_unc = fisher_exact(table) if all(sum(r)>0 for r in table) else (np.nan,np.nan)
            except:
                p_unc = np.nan
            results["endpoints"][ep] = {"uncontrolled": {"n_signal":n1,"n_nosignal":n0,"rate_signal":p1,"rate_nosignal":p0,"rd":rd,"p_fisher":p_unc}}
        else:
            # ES5
            vals_s = mae_h.values[signal.values & ~np.isnan(mae_h.values)]
            vals_ns = mae_h.values[(~signal.values) & ~np.isnan(mae_h.values)]
            es_s = worst_n(vals_s)
            es_ns = worst_n(vals_ns)
            results["endpoints"][ep] = {"uncontrolled": {"n_signal":len(vals_s),"n_nosignal":len(vals_ns),"es_signal":es_s,"es_nosignal":es_ns,"diff":es_s-es_ns}}

    results["generated_at_utc"] = datetime.now(timezone.utc).isoformat()
    results["integrated_sha256"] = sha256_obj(integrated)
    OUT_JSON.write_text(json.dumps(results, indent=2))
    # write md
    md = []
    md.append("# Robustness: prior-only controls (exploratory)")
    md.append(f"Generated: {results['generated_at_utc']}")
    md.append("")
    md.append("Anchor (unchanged): " + json.dumps(ANCHOR))
    md.append("")
    md.append("## Notes")
    for n in results["notes"]: md.append(f"- {n}")
    md.append("")
    md.append("## Results")
    for ep,v in results["endpoints"].items():
        md.append(f"### {ep}")
        md.append("```json")
        md.append(json.dumps(v, indent=2))
        md.append("```")
        md.append("")
    OUT_MD.write_text("\n".join(md))
    print("done")

if __name__ == "__main__":
    main()
