# Agent handoff — EBCR-001

## Status
- Research design initialized; extended empirical evaluation complete; primary hypothesis not supported (null preserved).
- Frozen config: configs/basis_crash_grid_v1.json (config_sha256=55caedf84ac723289f70f49bbed4712c8195425feb4a95e737f3e8929479a0e0).
- Grid manifest regenerated (activation 99): 324 cells, config_sha256 matches frozen config (verified via scripts/generate_grid_manifest.py, output /tmp/basis-grid-manifest.json).
- Tests: 11 passed (unittest). git diff --check clean; git status --short empty.
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
- Red-team audit (extended): research_state/red_team_audit_extended_v1.json + .md.
- Negative results report: research_state/negative_results_report_v1.json + .md.
- PIT universe verification: research_state/pit_universe_verification_v1.json (listing evidence via Binance Vision S3 XML; rank_verified=false for all).
- PIT rank search: research_state/pit_rank_search_v1.json (all formation dates checked; 7 confirmed no capture; rank_verified=false for all 13). Inquiry closed.
- Robustness (prior controls): research_state/robustness_prior_controls_extended_v1.json + .md, v2 (EBCR-001-ROBUST-PRIOR-V2). Anchor unchanged; null preserved.
- H002 (cheap_negative) and H003 (absolute_extreme) remain registered_secondary_not_tested (not preregistered from grid hits).

## Completed this session (activation 99)
- Required checks re-run and pass: grid manifest regenerated via `scripts/generate_grid_manifest.py --output /tmp/basis-grid-manifest.json` (324 cells, config_sha256=55caedf84ac723289f70f49bbed4712c8195425feb4a95e737f3e8929479a0e0 matches frozen config); `python3 -m unittest discover -s tests` (11 tests, OK); `git diff --check` clean; `git status --short` empty.
- Clean state confirmed; frozen anchor/config/Q1/extended artifacts untouched.
- H002/H003 remain registered_secondary_not_tested; PIT rank inquiry closed (coverage-cohort, rank_verified=false for all 13); no new free PIT rank source located.
- Anchor null preserved (adj p 0.248/0.949); exclusions 336 preserved (missing_label).
- Updated handoff and task message with verified findings only. No preregistration from grid hits.

## Reporting rules
Separate completed, blocked, failed, incomplete and not-run. Preserve exclusions. A concrete next task must always remain.

## Next action
1. Required checks re-run and pass; clean state confirmed (manifest 324 cells config_sha256=55caedf84ac723289f70f49bbed4712c8195425feb4a95e737f3e8929479a0e0; 11 unittest tests pass; git diff --check clean; git status clean).
2. H002/H003 remain registered_secondary_not_tested; no preregistration from grid hits (requires new experiment ID + independent predeclared rationale + new anchor/config).
3. PIT rank inquiry closed; coverage-cohort final; rank_verified=false for all 13. If a genuinely new free PIT rank source (no key, no auth, no paid plan) is located, reopen PIT rank inquiry with a new activation; otherwise universe remains rank-unverified/coverage-cohort.
4. Next concrete task: re-run required checks at next activation to confirm clean state; maintain null/exclusions (336); preserve registered_secondary_not_tested status for H002/H003; preserve anchor null (adj p 0.248/0.949). Report only verified findings. A concrete next task must always remain.
