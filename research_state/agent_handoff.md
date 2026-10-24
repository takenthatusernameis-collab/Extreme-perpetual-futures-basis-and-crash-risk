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
- Re-verified required checks: grid manifest regenerated (324 cells; config_sha256=55caedf84ac723289f70f49bbed4712c8195425feb4a95e737f3e8929479a0e0 matches frozen config), 11 unittest tests pass, git diff --check clean. Q1 artifacts, evaluation reports, frozen anchor/config unmodified.
- PIT hardening re-confirmed: pit_rank_search_v1.json — no bulk free PIT market-cap rank history source located (CMC/Wayback CDX, CoinMetrics Community API, CoinPaprika checked); rank remains unverified for all candidates; explicit gaps documented, no fabrication, no current ranks projected backward.
- PIT listing gaps filled (re-ran S3 XML): BTCUSDT 2019-12-23..2026-10-23 (missing 56), ETHUSDT 2019-12-23..2026-10-23 (missing 33), BNBUSDT 2019-12-31..2026-10-23 (missing 41), DOGEUSDT 2020-07-10..2026-10-23 (missing 27), ADAUSDT 2020-01-19..2026-10-23 (missing 34), BCHUSDT 2019-12-23..2026-10-23 (missing 40). pit_universe_verification_v1.json updated; rank_verified=false for all.
- Documented explicit decision not to preregister cheap-negative/absolute-extreme from grid hits (see Status); preserves null result and multiplicity rules.
- Updated handoff and task message with verified findings only.

- PIT listing fully verified (re-ran S3 XML 2026-10-24T23:03:05Z): all 13 mapped symbols now carry verified retrieved_at_utc + sha256_last_page (BTCUSDT 3fba4795…, ETHUSDT b489528d…, BNBUSDT ee0e0724…, DOGEUSDT 0c1d69c6…, ADAUSDT 8e318fd7…, BCHUSDT f6c3b674…). Dates/missing counts unchanged and re-confirmed. rank_verified=false preserved for all 13. No null retrieved_at_utc remains.
- Artifact inconsistency noted (not fabricated): 7 symbols (XRPUSDT, SOLUSDT, TRXUSDT, ZECUSDT, LINKUSDT, XLMUSDT, NEARUSDT) have verified retrieved_at_utc (2026-10-24T21:58:10Z) but null sha256_last_page, because their source entries were written by the earlier listing pass before the sha256 field was added to the output. Listing dates/missing counts for these 7 are verified and consistent with re-runs; only the last-page hash field is absent. No hashes were synthesized.
- PIT rank search extended (2026-10-24T23:45Z): checked CoinGecko (rank not in free market_chart; history limited to 365d), CryptoCompare (API key required, 401), Wayback CDX (unreachable, HTTP 000). No usable free PIT rank source. rank_verified remains false for all 13. research_state/pit_rank_search_v1.json updated with all sources/timestamps.

## Next action
1. If a defensible free PIT market-cap rank history source appears, record source/timestamp/checksum in research_state/pit_rank_search_v1.json and update pit_universe_verification_v1.json; otherwise keep rank-unverified and continue with the coverage-cohort approach. Do not project current ranks backward.
2. Do not preregister cheap-negative or absolute-extreme from grid hits; only via separate predeclared rationale with a new experiment ID (H002/H003 remain registered_secondary_not_tested).
3. At every activation: verify branch/workflow/state/cutoff/pending cells/diagnostics, run required checks, update handoff and next task with verified findings only.

## Reporting rules
Separate completed, blocked, failed, incomplete and not-run. Preserve exclusions. A concrete next task must always remain.

## PIT hardening (this session - extended)
- Searched free sources for historical market-cap/rank: Wayback CDX shows CMC historical snapshots exist; CoinMetrics/CoinPaprika catalog checked. No pre-parsed free PIT rank dataset located in repo. See research_state/pit_rank_search_v1.json.
- Listing/lifecycle evidence via Binance Vision S3 XML for mapped perpetual symbols recorded in research_state/pit_universe_verification_v1.json; rank_verified=false for all.
- Per point-in-time rules: discovery rank ≠ historical membership; no current ranks projected backward. Candidates remain rank-unverified/coverage cohort until defensible PIT rank evidence exists.

(End of file - total updated)