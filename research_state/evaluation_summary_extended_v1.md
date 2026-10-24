# Evaluation summary — EBCR-001-EXTENDED-V1

Full report: `research_state/evaluation_report_extended_v1.json`
Script: `scripts/evaluate_grid_extended.py`

## Inputs
- Integrated data: `research_state/integrated_extended_v1.json` — 5,010 rows, 336 recorded exclusions, 11 symbols, 2023-01-01..2024-04-30.
- Config: `configs/basis_crash_grid_v1.json` (immutable).

## Registered inference
- Family: 324 cells × 8 endpoints = **2,592** registered grid tests.
- Tests with a computable p-value: **2,451**; blocked/no-p: **141** (minimum-history or forward-horizon gate; no p-value invented).
- Correction: Holm step-down across the full family; anchor co-primary Holm separately across 2 endpoints.

## Anchor (fixed: 1-day agg, 90-day ref, rich-positive, q95, 14-day)
| endpoint | n_signal | n_control | p | adj (anchor) | sig |
|---|---|---|---|---|---|
| crash_incidence_15pct | 301 | 4,709 | 0.124 | 0.248 | no |
| expected_shortfall_5pct_forward_mae | 301 | 4,709 | 0.949 | 0.949 | no |

Anchor co-primary: **no significant effect** after correction. This is the preregistered primary test; it is a negative/null result and is preserved as such.

## Grid family
- Holm-significant tests: **424 / 2,451** (17.3%).
- Stratified by orientation: absolute_extreme 224/864, rich_positive 135/864, cheap_negative 65/864.
- Stratified by horizon: 7d 186/864, 14d 129/864, 28d 109/864.

## Red-team caveats (not conclusions)
1. **Non-independent tests.** The 2,592 tests share 108 underlying signal configurations and 8 correlated endpoints per cell; overlapping 7/14/28-day horizons and common market shocks induce dependence. Holm does not model this, so the 424 count overstates independent evidence. The registered procedure is applied as specified; dependence is reported, not corrected away.
2. **No leakage check performed here.** Signal thresholds use only preceding completed daily features (rolling(...).shift(1)); labels start at t+1. This was the design; a permutation/placebo audit is the next unblocked task.
3. **Selection rule.** No selection by raw p-value. Estimates and intervals are reported regardless of significance.
4. **Anchor negative.** The primary hypothesis is not supported on the extended window. Rich-positive extreme basis at the fixed anchor does not raise 15% crash incidence or worsen 5% expected shortfall after correction.

## Status accounting
- ok: 324 cells (all evaluated on extended window).
- blocked/failed/incomplete/invalid: 0.
- not_run: 0.
- Exclusions preserved: 336 (recorded in integrated source; reasons in report).