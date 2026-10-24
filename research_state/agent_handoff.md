# Agent handoff — EBCR-001

## Status
- Research design initialized; no empirical finding verified.
- Frozen config: configs/basis_crash_grid_v1.json (config_sha256=55caedf84ac723289f70f49bbed4712c8195425feb4a95e737f3e8929479a0e0).
- Grid manifest generated: research_state/grid_manifest_v1.json (324 cells).
- Tests: 11 passed (unittest).
- Universe frontier: 25 discovery candidates (rank-unverified).
- Candidate-to-perp mapping: research_state/candidate_perp_mapping_v1.json (updated with archive verification).
- S3 XML listing implemented: scripts/s3_xml_listing.py; verified coverage via s3_xml_listing.
- Q1 2024 ingestion (BTCUSDT+ETHUSDT): research_state/ingestion_btc_eth_q1_2024.json (ok, coverage 1.0 for both, 91 days each).
- Data coverage ledger: research_state/data_coverage_ledger.json (all verified symbols audited for Q1 2024).
- Basis computation (Q1 all): research_state/basis_computation_q1_all.json (1001 obs, coverage 1.0 all symbols, 91 days each, 2024-01-01..2024-03-31).
- Crash labels computed (Q1): research_state/crash_labels_q1.json (1001 labels ok, 0 exclusions; horizons 7/14/28d).
- Integrated dataset (Q1): research_state/integrated_q1.json (1001 rows, 0 exclusions, 11 symbols).
- Grid execution scaffold (Q1): research_state/grid_execution_scaffold_v1.json (324 cells mapped).
- Cell status ledger (Q1): research_state/cell_status_ledger.json (324 blocked, 0 ok) — minimum history unmet / insufficient forward horizon in Q1 window.
- Extended ingestion (EBCR-001-EXTENDED-V1): research_state/ingestion_extended_v1.json + checkpoints in research_state/ingest_extended_window/ (11 symbols, 2023-01-01..2024-04-30; basis coverage >=0.997).
- Basis computation (extended): research_state/basis_computation_extended_v1.json (5346 computations; coverage >=0.997).
- Crash labels (extended): research_state/crash_labels_extended_v1.json (5010 ok, 308 exclusions).
- Integrated dataset (extended): research_state/integrated_extended_v1.json (5010 rows, 336 exclusions).
- Grid execution scaffold (extended): research_state/grid_execution_scaffold_extended_v1.json (324 cells mapped).
- Cell status ledger (extended): research_state/cell_status_ledger_extended_v1.json (324 ok, 0 blocked).
- **Evaluation (extended): research_state/evaluation_report_extended_v1.json + research_state/evaluation_summary_extended_v1.md.**
  - 2,592 registered tests; 2,451 with p-values; 141 blocked (no p-value invented).
  - Holm across full family: 424 significant.
  - Anchor co-primary (crash_incidence_15pct, expected_shortfall_5pct_forward_mae): **not significant** (adj p 0.248, 0.949). Primary hypothesis not supported on this window — preserved as a null/negative finding.

## Completed this session
- Reran extended ingestion via background process; generated all 11 symbol checkpoints and summary ingestion_extended_v1.json.
- Computed basis/crash labels/integrated for extended window (5010 rows).
- Executed full grid for extended window: all 324 cells ok (8 endpoints each; family 2592). Recorded in grid_execution_scaffold_extended_v1.json and cell_status_ledger_extended_v1.json.
- Ran required checks: grid manifest regenerated (324 cells), unittest 11 passed, git diff --check clean.
- **Applied Holm correction across all 2592 grid cell-endpoint tests and anchor co-primary Holm separately (m=2). Generated evaluation report with point estimates, intervals, event counts, exclusions and stratified summaries.**

## Next action
1. Run statistical red-team audit on the extended results: leakage/permutation/placebo checks, overlapping-horizon dependence quantification, survivorship/missingness selection, confounding vs prior-only controls. Use the `statistical-red-team` skill.
2. Produce a formal negative-results report (EBCR-001-NEGATIVE-V1) documenting the anchor null, the 424/2451 grid hits with dependence caveats, exclusions (336) and all blocked states.
3. Update handoff/next task with red-team findings; keep Q1 artifacts unchanged.

## Reporting rules
Separate completed, blocked, failed, incomplete and not-run. Preserve exclusions. A concrete next task must always remain.