# Initial task message — EBCR-001 (activation 10)

Read AGENTS.md, SKILLS.md, research_state/agent_task_message.md, research_state/agent_handoff.md, prompts/continuous_research_operating_contract_v1.md, docs/research_protocol.md, configs/basis_crash_grid_v1.json.

## What was done this activation
- Required checks pass: grid manifest 324 cells, config_sha256=55caedf84ac723289f70f49bbed4712c8195425feb4a95e737f3e8929479a0e0 matches frozen config; 11 unittest tests pass (python3 -m unittest discover -s tests); git diff --check clean. pytest not installed in this environment.
- Expanded PIT rank snapshot coverage via Wayback CDX: captures now located at 10 distinct dates across 2019-2024 (2019-12-31, 2020-01-01, 2020-01-19, 2020-03-01, 2020-06-01, 2020-09-13, 2021-01-01, 2022-01-01, 2023-01-01, 2024-01-01). New captures: 2020-03-01 (earliest capture 20201129230859), 2020-06-01 (capture 20250818090759), 2021-01-01 (earliest capture 20210301163118). No captures for 2019-12-23, 2020-10-14, 2021-07-01, 2022-07-01, 2023-07-01. research_state/pit_rank_search_v1.json updated with source/timestamp evidence for every source checked.
- Direct Wayback snapshot page fetch returns HTTP 000 (unreachable) in this environment; page-level sha256 checksums not recomputable for new dates. Existing page evidence for 7 dates preserved under /tmp/pit_rank_evidence/.
- Updated research_state/pit_universe_verification_v1.json (retrieved_at_utc, snapshot date lists); rank_verified=false preserved for all 13 symbols. No frozen anchor/config/Q1/extended artifacts modified. H002/H003 remain registered_secondary_not_tested.

## Verified state
- Anchor null preserved: crash_incidence_15pct adj p 0.248, expected_shortfall_5pct_forward_mae adj p 0.949.
- 2,592 registered tests; 2,451 with p-values; 141 blocked; 424 Holm-significant with dependence caveats.
- PIT listing: 13/13 symbols listing_verified=true; 0/13 rank_verified=true.
- PIT rank evidence: Wayback Machine CMC historical snapshots at 10 dates across 2019-2024; snapshot-based coverage, not continuous. rank_verified=false. Snapshot page fetch blocked (HTTP 000).
- H002 (cheap_negative) and H003 (absolute_extreme) remain registered_secondary_not_tested.

## Your task
1. Optional: continue expanding PIT rank snapshot coverage by attempting additional Wayback CMC historical dates (e.g., 2020-12-01, 2021-04-01, 2021-10-01, 2022-04-01, 2022-10-01, 2023-04-01, 2023-10-01, 2024-04-01). Record source, timestamp, checksum in research_state/pit_rank_search_v1.json for every source checked. Note: direct snapshot page fetch returns HTTP 000 (unreachable) in this environment; only the CDX API is reachable, so record capture timestamps as evidence and do not fabricate page sha256 checksums.
2. If full point-in-time rank coverage across all formation dates is achieved, update research_state/pit_universe_verification_v1.json (rank_verified may become true only with full point-in-time evidence) and update handoff. Otherwise keep rank_verified=false and continue coverage-cohort approach. Do not project current ranks backward.
3. Do not preregister cheap-negative/absolute-extreme from grid hits. Any separate preregistration needs its own anchor/config, independent predeclared rationale, and new experiment ID. Do not modify frozen anchor/config or Q1/extended artifacts.
4. Run required checks after any change: python3 scripts/generate_grid_manifest.py --output /tmp/basis-grid-manifest.json ; python3 -m unittest discover -s tests ; git diff --check. (pytest not installed in this environment.)
5. Update handoff and task message with verified findings only. A concrete next task must always remain.

## Boundary
Free public data only. No fabrication. Preserve null/failed/exclusions. Complete horizons only.
