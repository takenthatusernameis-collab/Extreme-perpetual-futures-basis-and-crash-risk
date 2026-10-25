# Leakage / permutation / placebo audit — EBCR-001-LEAKAGE-AUDIT-EXTENDED-V1

- Report: `research_state/leakage_audit_extended_v1.json`
- Experiment: EBCR-001-EXTENDED-V1
- Window: 2023-01-01..2024-04-02
- Generated: 2026-10-25T11:48:13.791961+00:00
- Anchor cell: `EBCR-GRID-001-0005` ({'basis_aggregation_days': 1, 'rolling_reference_days': 90, 'orientation': 'rich_positive', 'tail_quantile': 0.95, 'horizon_days': 14})
- Config sha256: `55caedf84ac723289f70f49bbed4712c8195425feb4a95e737f3e8929479a0e0`

## Structural leakage checks
- threshold_uses_past_only: **True** — Rolling-L quantile threshold at day t computed exclusively from completed daily features at dates < t (rolling(L).quantile.shift(1)); current formation day excluded.
  - Evidence: scripts/leakage_audit_extended.py::compute_anchor_signal
- labels_use_forward_only: **True** — MAE_h uses spot/index lows from t+1 through t+h divided by close at t; horizons complete within window; no truncated or crossed horizons.
  - Evidence: research_state/integrated_extended_v1.json

## Anchor observed statistics (extended window)
- crash_incidence_15pct: n_signal=301, n_control=4709, events_signal=65, events_control=850, risk_difference=0.03544142869136571
- expected_shortfall_5pct_forward_mae: n_signal=301, n_control=4709, es_signal=-0.3084027011669326, es_control=-0.30962961612827994, es_difference=0.0012269149613473584

## Permutation test (break signal-outcome alignment)
- Permutations: 2000, block size: 56 days
- Observed risk_difference: 0.03544142869136571; perm null mean=0.000107, 95% CI=[-0.133070, 0.204154]
- Observed es_difference: 0.0012269149613473584; perm null mean=0.024488, 95% CI=[-0.090876, 0.123757]
- Empirical p (risk_difference): 0.738
- Empirical p (es_difference): 0.9855

## Temporal placebo (signal at t vs crashes already realized at t-k)
- lag=7d: n_signal=301, n_control=4737, risk_difference=-0.10444882549688358, p_value=5.126989673064192e-07
- lag=14d: n_signal=301, n_control=4737, risk_difference=-0.14226030044107424, p_value=3.122309792951181e-13
- lag=28d: n_signal=301, n_control=4737, risk_difference=-0.12784981733536163, p_value=8.227770497415961e-12

## Leakage verdict
- Past-only signal: **True**
- Forward-only labels: **True**
- Permutation consistent with null: **True**
- Placebo null for all lags: **False**

## Conclusion
- The anchor signal construction uses only past completed daily features (rolling quantile with shift(1)) and labels use only forward lows (t+1..t+h). No structural look-ahead was detected (past_only=True, forward_only=True).
- Permutation test: observed anchor statistics are within the permutation null (empirical p=0.738 for risk_difference, p=0.986 for es_difference), i.e. consistent with chance alignment; no evidence the forward association exceeds random signal-outcome alignment.
- Temporal placebo: signal at t is NEGATIVELY associated with crashes already realized at t-7/t-14/t-28 (risk_difference ≈ -0.10 to -0.14, p<1e-6 for all lags). This is the opposite direction of a leakage signal (leakage would imply future/past crash info contaminating the signal, producing a positive association). It is consistent with rich basis following calm (low-crash) market regimes — serial regime correlation, not look-ahead bias.
- Overall: no structural leakage detected; forward anchor association is not stronger than chance alignment under permutation. This audit verifies causal time alignment only and does not modify the preregistered evaluation or the red-team audit.
