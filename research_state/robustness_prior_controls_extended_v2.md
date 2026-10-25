# Robustness prior-only controls (EBCR-001) — EBCR-001-ROBUST-PRIOR-V2
Generated: 2026-10-25T01:52:33.455489+00:00

Anchor (unchanged): {"basis_aggregation_days": 1, "rolling_reference_days": 90, "orientation": "rich_positive", "tail_quantile": 0.95, "horizon_days": 14}
Frozen config sha256: 55caedf84ac723289f70f49bbed4712c8195425feb4a95e737f3e8929479a0e0
Integrated: integrated_extended_v1.json (sha256 8c826687da2fa91c...) exclusions 336

## Notes
- Bounded prior-only controls on fixed anchor. No anchor/config change.
- Controls lagged (t-1); no forward fill.
- No holdout unblinding; no parameter search.

## Controlled vs uncontrolled (anchor co-primary)
### crash_incidence_15pct
```json
{
  "uncontrolled": {
    "n_signal": 301,
    "n_nosignal": 4737,
    "rate_signal": 0.2159468438538206,
    "rate_nosignal": 0.17943846316233902,
    "rd": 0.03650838069148157,
    "p_fisher": 0.12269124087221213
  }
}
```

### expected_shortfall_5pct_forward_mae
```json
{
  "uncontrolled": {
    "n_signal": 301,
    "n_nosignal": 4709,
    "es_signal": -0.3084027011669326,
    "es_nosignal": -0.30962961612827994,
    "diff": 0.0012269149613473584
  }
}
```

## Conclusion
- Controlled specification remains descriptive (prior-only lags). Anchor estimates reported without changing anchor/selection/holdout.
- Null result preserved consistent with prior robustness (anchor not significant).