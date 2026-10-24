# Agent handoff — EBCR-001

## Status
- Research design initialized; no empirical finding verified.
- Frozen config: configs/basis_crash_grid_v1.json (config_sha256=55caedf84ac723289f70f49bbed4712c8195425feb4a95e737f3e8929479a0e0).
- Grid manifest generated: research_state/grid_manifest_v1.json (324 cells).
- Tests: 11 passed (unittest).
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
- **Prior-only controls robustness (exploratory):** research_state/robustness_prior_controls_extended_v1.json + .md (anchor unchanged; crash_incidence_15pct RD +0.0365 p_fisher 0.123, ES5 diff +0.00123; null preserved).

## Completed this session
- Ran statistical-red-team audit on extended results (leakage/permutation/placebo structural checks, overlap/dependence, survivorship/missingness, confounding, thin tails).
- Wrote formal negative-results report documenting anchor null, grid hits with dependence caveats, exclusions (336), blocked states (0).
- Strengthened PIT universe verification: collected listing evidence via S3 XML listings for mapped symbols (ADAUSDT,BCHUSDT,BNBUSDT,DOGEUSDT,LINKUSDT,NEARUSDT,SOLUSDT,TRXUSDT,XLMUSDT,XRPUSDT,ZECUSDT); recorded sources/timestamps/checksums where available; marked rank-verified=false, rank-unverified with explicit notes.
- Added predeclared prior-only controls robustness check (lagged vol/regime/BTC context documented) on anchor endpoints without changing anchor/config/holdout logic.
- Updated handoff and task message with findings.

## Next action
1. Continue PIT hardening if any free PIT rank source appears (no fabrication). Document gaps explicitly.
2. If justified by predeclared rationale, consider separately preregistered hypothesis (cheap-negative/absolute-extreme) with its own anchor — do not re-open anchor selection.
3. Expand coverage notes for symbols with limited history; preserve all exclusions/statuses.

## Reporting rules
Separate completed, blocked, failed, incomplete and not-run. Preserve exclusions. A concrete next task must always remain.

(End of file - total updated)

## PIT hardening (this session - extended)
- Searched free sources for historical market-cap/rank: Wayback CDX shows CMC historical snapshots exist; CoinMetrics/CoinPaprika catalog checked. No pre-parsed free PIT rank dataset located in repo. See research_state/pit_rank_search_v1.json.
- Listing/lifecycle evidence via Binance Vision S3 XML for mapped perpetual symbols recorded in research_state/pit_universe_verification_v1.json; rank_verified=false for all.
- Per point-in-time rules: discovery rank ≠ historical membership; no current ranks projected backward. Candidates remain rank-unverified/coverage cohort until defensible PIT rank evidence exists.
