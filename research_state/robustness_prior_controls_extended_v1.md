# Robustness: prior-only controls (exploratory)
Generated: 2026-10-24T21:59:55.091934+00:00

Anchor (unchanged): {"basis_aggregation_days": 1, "rolling_reference_days": 90, "orientation": "rich_positive", "tail_quantile": 0.95, "horizon_days": 14}

## Notes
- Exploratory only - no anchor/config change. Controls are predeclared (lagged). No holdout unblinded.

## Results
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
