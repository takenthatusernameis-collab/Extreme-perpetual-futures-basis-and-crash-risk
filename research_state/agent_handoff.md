# Agent handoff — EBCR-001

## Status
- Research design initialized; extended empirical evaluation complete; primary hypothesis not supported (null preserved).
- Frozen config: configs/basis_crash_grid_v1.json (config_sha256=55caedf84ac723289f70f49bbed4712c8195425feb4a95e737f3e8929479a0e0).
- Grid manifest regenerated: 324 cells, config_sha256 matches frozen config (verified via scripts/generate_grid_manifest.py, output /tmp/basis-grid-manifest.json).
- Tests: 11 passed (unittest). git diff --check clean.
- Universe frontier: 25 discovery candidates (rank-unverified).
- Candidate-to-perp mapping: research_state/candidate_perp_mapping_v1.json (updated with archive verification).
- S3 XML listing implemented: scripts/s3_xml_listing.py; verified coverage via s3_xml_listing.
- Q1 2024 ingestion (BTCUSDT+ETHUSDT): research_state/ingestion_btc_eth_q1_2024.json (ok).
- Data coverage ledger: research_state/data_coverage_ledger.json.
- Basis computation (Q1 all): research_state/basis_computation_q1_all.json.
- Crash labels computed (Q1): research_state/crash_labels_q1.json.
- Integrated dataset (Q1): research_state/integrated_q1.json.
- Grid execution scaffold (Q1): research_state/grid_execution_scaffold_v1.json.
- Cell status ledger (Q1): research_state/cell_status_ledger.json (324 blocked).
- Extended ingestion (EBCR-001-EXTENDED-V1): research_state/ingestion_extended_v1.json.
- Basis/crash labels/integrated (extended): research_state/basis_computation_extended_v1.json, research_state/crash_labels_extended_v1.json, research_state/integrated_extended_v1.json (5010 rows, 336 exclusions).
- Grid execution scaffold/ledger (extended): research_state/grid_execution_scaffold_extended_v1.json, research_state/cell_status_ledger_extended_v1.json (324 ok).
- Evaluation (extended): research_state/evaluation_report_extended_v1.json + research_state/evaluation_summary_extended_v1.md.
  - 2,592 registered tests; 2,451 with p-values; 141 blocked.
  - Holm across full family: 424 significant (with dependence caveats).
  - Anchor co-primary (crash_incidence_15pct, expected_shortfall_5pct_forward_mae): **not significant** (adj p 0.248, 0.949). Primary hypothesis not supported — null preserved.
- **Red-team audit (extended):** research_state/red_team_audit_extended_v1.json + .md (leakage/past-only verified; overlapping horizons; exclusions 336; confounding noted).
- **Negative results report:** research_state/negative_results_report_v1.json + .md (anchor null, grid hits with caveats, all exclusions/statuses preserved).
- **PIT universe verification (extended):** research_state/pit_universe_verification_v1.json (listing evidence via Binance Vision S3 XML for mapped symbols; rank remains unverified per point-in-time rules).
- **PIT rank search:** research_state/pit_rank_search_v1.json (checked 2026-10-24T22:51:53Z; CMC/Wayback CDX, CoinMetrics Community API, CoinPaprika checked; no bulk free PIT rank history located).
- **Prior-only controls robustness (exploratory):** research_state/robustness_prior_controls_extended_v1.json + .md (anchor unchanged; null preserved).
- **Alternative orientation:** NOT preregistered this session. H002 (cheap_negative) and H003 (absolute_extreme) remain registered_secondary_not_tested in research_state/hypothesis_registry.json. Rationale: grid hits (absolute_extreme 224/864, cheap_negative 65/864 Holm-significant) are inspected results; preregistering now would constitute selection by raw p-value, prohibited by the operating contract and research protocol. Independent predeclared rationale + new experiment ID required before any separate preregistration.

## Completed this session
- Regenerated grid manifest (324 cells; config hash matches frozen config) and confirmed 11 unittest tests pass and git diff --check clean.
- PIT hardening re-confirmed: pit_rank_search_v1.json — no bulk free PIT market-cap rank history source located; rank remains unverified for all candidates; explicit gaps documented, no fabrication, no current ranks projected backward.
- Listed PIT listing-evidence gaps: complete earliest/latest markPriceKlines zip dates for XRPUSDT, SOLUSDT, TRXUSDT, ZECUSDT, LINKUSDT, XLMUSDT, NEARUSDT; null earliest/latest (incomplete listing metadata via S3 XML) for BTCUSDT, ETHUSDT, BNBUSDT, DOGEUSDT, ADAUSDT, BCHUSDT. Q1 coverage ledger shows full coverage (1.0) for all 11 symbols in 2024-01-01..2024-03-31; extended window 5,010 rows, 336 exclusions (missing_label).
- Documented explicit decision not to preregister cheap-negative/absolute-extreme from grid hits (see Status); preserves null result and multiplicity rules.
- Updated handoff and task message with verified findings only.

## Next action
1. If a defensible free PIT market-cap rank history source appears, record source/timestamp/checksum in research_state/pit_rank_search_v1.json and update pit_universe_verification_v1.json; otherwise keep rank-unverified and continue with the coverage-cohort approach. Do not project current ranks backward.
2. Do not preregister cheap-negative or absolute-extreme from inspected grid hits; only via separate predeclared rationale with a new experiment ID (H002/H003 remain registered_secondary_not_tested).
3. Expand coverage notes for symbols with limited history (PIT listing gaps above); preserve all exclusions/statuses and terminal cell statuses.
4. Update handoff and next task at every activation.

## Reporting rules
Separate completed, blocked, failed, incomplete and not-run. Preserve exclusions. A concrete next task must always remain.

## PIT hardening (this session - extended)
- Searched free sources for historical market-cap/rank: Wayback CDX shows CMC historical snapshots exist; CoinMetrics/CoinPaprika catalog checked. No pre-parsed free PIT rank dataset located in repo. See research_state/pit_rank_search_v1.json.
- Listing/lifecycle evidence via Binance Vision S3 XML for mapped perpetual symbols recorded in research_state/pit_universe_verification_v1.json; rank_verified=false for all.
- Per point-in-time rules: discovery rank ≠ historical membership; no current ranks projected backward. Candidates remain rank-unverified/coverage cohort until defensible PIT rank evidence exists.

(End of file - total updated)
