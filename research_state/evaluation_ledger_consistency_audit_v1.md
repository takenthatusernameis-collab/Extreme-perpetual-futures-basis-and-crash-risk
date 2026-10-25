# Evaluation report vs cell status ledger consistency audit

- Evaluation report: `research_state/evaluation_report_extended_v1.json`
- Cell status ledger: `research_state/cell_status_ledger_extended_v1.json`

## Counts
- n_cells (eval): 324; n_cells (ledger): 324 → match.
- n_endpoints_per_cell: 8 → registered tests 324×8 = 2,592; eval n_registered_grid_tests = 2,592 → match.
- Ledger: 324 ok, 0 blocked/failed/incomplete/invalid/not_run → all cells terminal `ok`.
- Family tests: 2,592 total; 2,451 with p-value; 141 blocked (no p) → 2,451 + 141 = 2,592 → match.
- family_size_tests (inference): 2,592 → match.
- family_holm_significant: 424 (raw Holm, dependence caveats).
- Anchor co-primary adjusted p: crash_incidence_15pct 0.2483, expected_shortfall_5pct_forward_mae 0.9485 → both not significant.

## Verdict
No discrepancy. Evaluation report test counts are fully consistent with the cell status ledger (324 cells × 8 endpoints = 2,592 registered tests; 2,451 with p-values; 141 blocked without p). All 324 cells terminal `ok`. Anchor null preserved.
