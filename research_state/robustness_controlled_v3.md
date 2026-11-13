# Controlled Re-estimation (EBCR-H004) — EBCR-001-ROBUST-CTRL-V3
Generated: 2026-11-13T17:55:18.328821+00:00

Preregistration: h004_controlled_rereg_v1.json (sha256 f7a0a9c2268477f0...)
Anchor (unchanged): {"basis_aggregation_days": 1, "rolling_reference_days": 90, "orientation": "rich_positive", "tail_quantile": 0.95, "horizon_days": 14}
Frozen config sha256: 55caedf84ac723289f70f49bbed4712c8195425feb4a95e737f3e8929479a0e0
Integrated: integrated_extended_v1.json (sha256 8c826687da2fa91c...) exclusions 336
Panel: 4014 obs, 11 symbols, 156 clusters
Controls: ret7, ret30, vol30, mdd30, btc_ret, btc_vol30, market_ret, funding

## Notes
- Controlled re-estimation per EBCR-H004 preregistration (EBCR-001-ROBUST-CTRL-V3).
- All controls lagged (t-1); complete-case analysis (no missing controls).
- Liquidity/turnover and open interest not available in derived data; only funding_median used.
- Cluster-robust SEs by symbol-month for logistic; bootstrap for ES5.
- Holm correction applied across the two co-primary endpoints within registered family.

## Co-primary Endpoints (Controlled vs Uncontrolled)
### crash_incidence_15pct
```json
{
  "uncontrolled": {
    "n_signal": 301,
    "n_nosignal": 3713,
    "rate_signal": 0.2159468438538206,
    "rate_nosignal": 0.19175868569889576,
    "rd": 0.024188158154924838,
    "logit_coef": 0.149178398898417,
    "logit_p": 0.3073842707678488
  },
  "controlled": {
    "logit_coef": -0.1824762852091558,
    "logit_p_model": 0.31181785247143057,
    "logit_se_cluster": 0.03360841292840813,
    "logit_p_cluster": 5.6517738045158694e-08,
    "n_obs": 4014,
    "n_clusters": 156
  }
}
```

### expected_shortfall_5pct_forward_mae
```json
{
  "uncontrolled": {
    "n_signal": 301,
    "n_nosignal": 3713,
    "es_signal": -0.3084027011669326,
    "es_nosignal": -0.312623945247935,
    "diff": 0.00422124408100244
  },
  "controlled": {
    "ols_coef_signal": 0.004828674086176744,
    "ols_p_model": 0.29052529254097065,
    "ols_se_cluster": 0.006494248368350821,
    "ols_p_cluster": 0.45720396969691945,
    "bootstrap_se_es5_diff": 0.018531845855094615,
    "n_obs": 4014,
    "n_clusters": 156
  }
}
```

## Holm Correction (Family: 2 Co-primary Endpoints)
```json
{
  "crash_incidence_15pct": {
    "raw_p": 5.6517738045158694e-08,
    "holm_threshold": 0.025,
    "holm_significant": true
  },
  "expected_shortfall_5pct_forward_mae": {
    "raw_p": 0.45720396969691945,
    "holm_threshold": 0.05,
    "holm_significant": false
  }
}
```

## Anchor Co-primary (Frozen, Uncontrolled)
```json
{
  "cell_id": "EBCR-GRID-001-0005",
  "crash_incidence_15pct_adj_p": 0.24830545694889028,
  "expected_shortfall_5pct_forward_mae_adj_p": 0.9485,
  "both_not_significant": true
}
```

## Conclusion
- crash_incidence_15pct: Holm SIGNIFICANT (p=5.6517738045158694e-08)
- expected_shortfall_5pct_forward_mae: Holm NOT significant (p=0.45720396969691945)
- Null result preserved: anchor co-primary remains not significant (consistent with EBCR-H001).
- No frozen artifacts modified; new experiment ID and output paths used.