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
- **PIT rank search:** research_state/pit_rank_search_v1.json (checked 2026-10-24T23:59:00Z; CDX located captures at 10 snapshot dates incl. 2020-03-01, 2020-06-01, 2021-01-01; snapshot page fetch HTTP 000 unreachable; no bulk free PIT rank history located; rank_verified=false).
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
- PIT rank search extended (2026-10-24T23:48Z): checked CoinMarketCap listings/historical (API key required), Coinranking rank-history (paid), Kaggle daily tracker (2026 only), Zenodo single-date snapshot. No usable free no-key bulk PIT rank source. rank_verified remains false for all 13. research_state/pit_rank_search_v1.json updated.

## This activation (verification + PIT search expansion)
- Required checks re-run and pass: grid manifest 324 cells, config_sha256=55caedf84ac723289f70f49bbed4712c8195425feb4a95e737f3e8929479a0e0 matches frozen config; 11 unittest tests pass (python3 -m unittest discover -s tests); git diff --check clean.
- PIT rank search expanded (2026-10-24T23:59Z): Wayback Machine CMC historical snapshots confirmed directly accessible and contain full point-in-time ranking tables (rank, name, symbol, market cap, price, circulating supply, volume) at snapshot dates: 2019-12-31 (sha256 0ca492a4…, capture 2021-04-18T13:34:18Z), 2020-01-01 (sha256 90f8ceca…, capture 2021-01-02T05:52:18Z), 2020-09-13 (sha256 c10348af…, capture 2020-12-04T09:08:11Z), 2022-01-01 (sha256 e2c52f63…, capture 2022-03-01T21:53:30Z), 2023-01-01 (sha256 385a5cde…, capture 2023-12-04T06:21:44Z), 2024-01-01 (sha256 79a88bd8…, capture 2026-05-21T10:48:15Z). Evidence pages saved under /tmp/pit_rank_evidence/ with sha256 checksums. 2019-12-23 and 2020-10-14 returned 404 (no capture). Defensible free PIT market-cap rank source at snapshot dates; coverage is snapshot-based, not continuous across every formation date. rank_verified remains false pending full point-in-time coverage across all formation dates. research_state/pit_rank_search_v1.json and research_state/pit_universe_verification_v1.json updated.
- No artifacts modified (frozen anchor/config and Q1/extended artifacts untouched). H002/H003 remain registered_secondary_not_tested.

## Completed this session (activation 10)
- Required checks re-run and pass: grid manifest 324 cells, config_sha256=55caedf84ac723289f70f49bbed4712c8195425feb4a95e737f3e8929479a0e0 matches frozen config; 11 unittest tests pass (python3 -m unittest discover -s tests); git diff --check clean. pytest not installed in this environment.
- Expanded PIT rank snapshot coverage via Wayback CDX: captures now located at 14 distinct dates across 2019-2024 (2019-12-31, 2020-01-01, 2020-01-19, 2020-03-01, 2020-06-01, 2020-09-13, 2020-12-01, 2021-01-01, 2021-04-01, 2022-01-01, 2023-01-01, 2023-10-01, 2024-01-01, 2024-04-01). New captures: 2020-12-01, 2021-04-01, 2023-10-01, 2024-04-01. No captures for 2019-12-23, 2020-02-04, 2020-07-10, 2020-10-14, 2021-07-01, 2021-10-01, 2022-04-01, 2022-07-01, 2022-10-01, 2023-04-01, 2023-07-01. research_state/pit_rank_search_v1.json updated.
- Direct Wayback snapshot page fetch returns HTTP 000 (unreachable) in this environment; page-level sha256 checksums not recomputable for newly located dates. Existing page evidence for 7 dates preserved under /tmp/pit_rank_evidence/.
- Updated research_state/pit_universe_verification_v1.json (retrieved_at_utc, snapshot date lists); rank_verified=false preserved for all 13 symbols. No frozen anchor/config/Q1/extended artifacts modified. H002/H003 remain registered_secondary_not_tested.

## Completed this session (activation 12)
- Required checks re-run and pass: grid manifest 324 cells (config_sha256=55caedf84ac723289f70f49bbed4712c8195425feb4a95e737f3e8929479a0e0 matches frozen config); 11 unittest tests pass (python3 -m unittest discover -s tests); git diff --check clean. Only research_state/pit_rank_search_v1.json and research_state/pit_universe_verification_v1.json modified; no frozen anchor/config/Q1/extended artifacts touched.
- Final PIT rank coverage audit: ALL formation dates now definitively checked via Wayback CDX (HTTP 200, endpoint sanity-verified against known-good captures 2020-02-01, 2020-09-13, 2020-07-11). Confirmed NO CAPTURE (empty '[]' body, 3 bytes) for: 2019-12-23, 2020-01-06, 2020-01-15, 2020-01-17, 2020-02-04, 2020-07-10, 2020-10-14. Adjacent-date corroboration: 2020-02-03/2020-02-05/2020-07-09 also empty; 2020-07-11 has capture (timestamp 20220123090917). No rate-limited/unconfirmed formation dates remain. research_state/pit_rank_search_v1.json and research_state/pit_universe_verification_v1.json updated; rank_verified=false preserved for all 13 symbols.
- PIT rank line of inquiry closed as not achievable via free Wayback snapshots for the formation window (2019-12-23 to 2020-10-14): 25 snapshot dates carry captures but 7 formation dates have none, so full point-in-time rank coverage across all formation dates is NOT achieved. Coverage-cohort approach stands. No current ranks projected backward.
- H002 (cheap_negative) and H003 (absolute_extreme) remain registered_secondary_not_tested.

## Next action
1. PIT rank line of inquiry is closed (activation 12): all formation dates definitively checked; 7 confirmed no capture; rank_verified=false for all 13 symbols. Coverage-cohort approach is the final PIT posture. No further free PIT rank sources located (see research_state/pit_rank_search_v1.json).
2. No unblocked PIT work remains. If a genuinely new free PIT rank source (no key, no auth, no paid plan) is located, reopen with a new activation; otherwise the universe remains rank-unverified/coverage-cohort.
3. H002 (cheap_negative) and H003 (absolute_extreme) remain registered_secondary_not_tested; not preregistered from grid hits.
4. Required checks re-run and pass: grid manifest 324 cells config_sha256=55caedf84ac723289f70f49bbed4712c8195425feb4a95e737f3e8929479a0e0 matches frozen config; 11 unittest tests pass; git diff --check clean.
5. Next concrete task: re-run required checks to confirm clean state (manifest, unittest, git diff --check). Do not modify frozen anchor/config or Q1/extended artifacts. Do not preregister H002/H003 from grid hits. Update handoff and task message with verified findings only. A concrete next task must always remain.

## Completed this session (activation 11)
- PIT rank snapshot coverage expanded: Wayback CDX + direct snapshot page fetch reachable (HTTP 200). 11 new capture dates with page-level sha256: 2020-02-01, 2020-08-01, 2020-11-01, 2021-02-01, 2021-05-01, 2021-06-01, 2021-08-01, 2021-09-01, 2021-12-01, 2022-05-01, 2023-12-01 (pages under /tmp/pit_rank_evidence/). Total 25 snapshot dates (up from 14); page sha256 for 18, CDX timestamps only for 7. 2019-12-23 and 2020-10-14 confirmed no capture; 2020-02-04 and 2020-07-10 rate-limited/unconfirmed. research_state/pit_rank_search_v1.json and research_state/pit_universe_verification_v1.json updated; rank_verified=false preserved for all 13 symbols.
- Required checks re-run and pass: grid manifest 324 cells (config_sha256=55caedf84ac723289f70f49bbed4712c8195425feb4a95e737f3e8929479a0e0 matches frozen config); 11 unittest tests pass; git diff --check clean.
- No frozen anchor/config/Q1/extended artifacts modified. H002/H003 remain registered_secondary_not_tested.

## Next action
1. PIT rank snapshot coverage expanded (activation 11): Wayback CDX + direct snapshot page fetch both reachable (HTTP 200). 11 new capture dates with page-level sha256: 2020-02-01, 2020-08-01, 2020-11-01, 2021-02-01, 2021-05-01, 2021-06-01, 2021-08-01, 2021-09-01, 2021-12-01, 2022-05-01, 2023-12-01 (pages saved under /tmp/pit_rank_evidence/). Total 25 snapshot dates with captures (up from 14); page-level sha256 for 18 dates, CDX capture timestamps only for 7. 2019-12-23 and 2020-10-14 confirmed no capture; 2020-02-04 and 2020-07-10 rate-limited/unconfirmed (not treated as no-capture). research_state/pit_rank_search_v1.json and research_state/pit_universe_verification_v1.json updated; rank_verified=false preserved for all 13 symbols.
2. Full point-in-time rank coverage across all formation dates NOT achieved (formation dates span 2019-12-23 to 2020-10-14; several lack captures). rank_verified remains false for all 13 symbols; coverage-cohort approach continues. Do not project current ranks backward.
3. H002 (cheap_negative) and H003 (absolute_extreme) remain registered_secondary_not_tested; not preregistered from grid hits.
4. Required checks re-run and pass: grid manifest 324 cells config_sha256=55caedf84ac723289f70f49bbed4712c8195425feb4a95e737f3e8929479a0e0 matches frozen config; 11 unittest tests pass; git diff --check clean.
5. Next concrete task: re-run required checks to confirm clean state (manifest, unittest, git diff --check). Optionally, after a cooldown, retry the 2 unconfirmed formation dates (2020-02-04, 2020-07-10) via Wayback CDX — do not treat rate-limit errors as no-capture; if still no capture, document as confirmed no-capture and finalize the coverage-cohort PIT rank line of inquiry. Do not modify frozen anchor/config or Q1/extended artifacts. Do not preregister H002/H003 from grid hits. Update handoff and task message with verified findings only. A concrete next task must always remain.

## Completed this session (activation 9)
- Required checks re-run and pass: grid manifest 324 cells, config_sha256=55caedf84ac723289f70f49bbed4712c8195425feb4a95e737f3e8929479a0e0 matches frozen config; 11 unittest tests pass (python3 -m unittest discover -s tests); git diff --check clean. pytest not installed in this environment.
- Expanded PIT rank snapshot coverage via Wayback CDX: captures now located at 10 distinct dates (2019-12-31, 2020-01-01, 2020-01-19, 2020-03-01, 2020-06-01, 2020-09-13, 2021-01-01, 2022-01-01, 2023-01-01, 2024-01-01). New captures: 2020-03-01 (earliest 20201129230859), 2020-06-01 (20250818090759), 2021-01-01 (earliest 20210301163118). No captures for 2019-12-23, 2020-10-14, 2021-07-01, 2022-07-01, 2023-07-01. research_state/pit_rank_search_v1.json updated with source/timestamp evidence for every source checked.
- Direct Wayback snapshot page fetch returns HTTP 000 (unreachable) in this environment; page-level sha256 checksums not recomputable for new dates. Existing page evidence for 7 dates preserved under /tmp/pit_rank_evidence/.
- Updated research_state/pit_universe_verification_v1.json (retrieved_at_utc, snapshot date lists); rank_verified=false preserved for all 13 symbols. No frozen anchor/config/Q1/extended artifacts modified. H002/H003 remain registered_secondary_not_tested.

## Reporting rules
Separate completed, blocked, failed, incomplete and not-run. Preserve exclusions. A concrete next task must always remain.

## PIT hardening (this session - extended)
- Searched free sources for historical market-cap/rank: Wayback CDX shows CMC historical snapshots exist; CoinMetrics/CoinPaprika catalog checked. No pre-parsed free PIT rank dataset located in repo. See research_state/pit_rank_search_v1.json.
- Listing/lifecycle evidence via Binance Vision S3 XML for mapped perpetual symbols recorded in research_state/pit_universe_verification_v1.json; rank_verified=false for all.
- Per point-in-time rules: discovery rank ≠ historical membership; no current ranks projected backward. Candidates remain rank-unverified/coverage cohort until defensible PIT rank evidence exists.

(End of file - total updated)
## PIT rank coverage expanded (2026-10-24T23:55Z)
- CDX queried for 2019-12-23, 2020-01-17, 2020-01-19, 2020-02-04, 2020-07-10, 2020-09-13, 2020-10-14. Only 2020-01-19 had a capture (timestamp 2020-11-26T21:13:11Z, sha256 520b694b…); saved as /tmp/pit_rank_evidence/cmc_20200119.html. Other six dates have no archived capture. Total captures now 7 dates. rank_verified remains false pending full point-in-time coverage across all formation dates. research_state/pit_rank_search_v1.json updated.

## Completed this session (activation 14)
- Required checks re-run and pass: grid manifest 324 cells (config_sha256=55caedf84ac723289f70f49bbed4712c8195425feb4a95e737f3e8929479a0e0 matches frozen config); 11 unittest tests pass (python3 -m unittest discover -s tests); git diff --check clean.
- Coverage-cohort audit complete: all 13 symbols consistent across pit_universe_verification_v1.json, data_coverage_ledger.json, and candidate_perp_mapping_v1.json. listing_verified=true, rank_verified=false for all 13; coverage 1.0, meets_gate true, 0 missing days across components for all symbols in Q1 ledger. Artifact inconsistency noted (not fabricated): 7 symbols (XRPUSDT, SOLUSDT, TRXUSDT, ZECUSDT, LINKUSDT, XLMUSDT, NEARUSDT) have verified retrieved_at_utc but null sha256_last_page (earlier listing pass before sha256 field added) — documented, no hashes synthesized.
- PIT rank line of inquiry remains closed: all formation dates definitively checked; 7 confirmed no capture; 0 rate-limited/unconfirmed remaining; rank_verified=false for all 13 symbols; coverage-cohort approach is final.
- No frozen anchor/config/Q1/extended artifacts modified. H002/H003 remain registered_secondary_not_tested. No preregistration from grid hits. Null result preserved.

## Next action
1. PIT rank line of inquiry closed (all formation dates checked, 7 no-capture). Coverage-cohort approach final; no further free PIT rank sources located.
2. H002 (cheap_negative) and H003 (absolute_extreme) remain registered_secondary_not_tested; not preregistered from grid hits (would require new experiment ID + predeclared rationale).
3. Required checks re-run and pass: manifest, unittest, git diff --check.
4. Next concrete task: audit extended evaluation artifacts for any unaddressed data gaps (research_state/evaluation_report_extended_v1.json, research_state/negative_results_report_v1.json) — verify exclusions preserved, blocked cells documented, no silent data changes. Do not modify frozen anchor/config/Q1/extended artifacts. Update handoff and task message with verified findings only. A concrete next task must always remain.
