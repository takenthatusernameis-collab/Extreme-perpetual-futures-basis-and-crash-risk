# Leakage audit verification (EBCR-001-LEAKAGE-AUDIT-EXTENDED-V1)

- JSON: research_state/leakage_audit_extended_v1.json (schema_version 1.0, report_id EBCR-001-LEAKAGE-AUDIT-EXTENDED-V1)
- Markdown: research_state/leakage_audit_extended_v1.md
- Config: configs/basis_crash_grid_v1.json (sha256 55caedf84ac723289f70f49bbed4712c8195425feb4a95e737f3e8929479a0e0) — matches
- Anchor: EBCR-GRID-001-0005 (rich_positive, tail_quantile 0.95, horizon_days 14, rolling_reference_days 90, basis_aggregation_days 1)
- Window: 2023-01-01..2024-04-02, 5010 rows, 11 symbols
- Integrated source: research_state/integrated_extended_v1.json (sha256 e8a3ebab4baf151337a1de93313316f72a63da735f04cdd5d7f36abe37a50861)

## Structural checks
- past_only_signal: true (threshold uses rolling quantile with shift(1), past-only)
- forward_only_labels: true (MAE_h uses t+1..t+h lows)
- Evidence present in both JSON and MD.

## Permutation test (2000 permutations, 56-day blocks)
- risk_difference_perm_p: 0.738 (JSON) vs report states "Empirical p (risk_difference): 0.738" — match
- es_difference_perm_p: 0.9855 (JSON) vs report states "Empirical p (es_difference): 0.9855" — match
- Observed values match: RD 0.03544142869136571, ES diff 0.0012269149613473584
- Null means/CI present and consistent.

## Temporal placebo
- lag 7/14/28 all negative RD (-0.104 to -0.142), p<1e-6 — reported in both, consistent.

## Schema validity
- Required top-level fields present: anchor, anchor_cell_id, config_path/sha256, experiment_id/grid_id/program_id/report_id, generated_at_utc, integrated_*, leakage_verdict, n_rows/n_symbols, permutation_test, structural_checks, symbols, temporal_placebo, window.
- leakage_verdict flags consistent with findings.
- No structural schema issues observed.

## Discrepancy
- None found. Permutation p-values cross-check cleanly; structural checks and placebo results consistent across JSON and Markdown.
