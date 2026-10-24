# Initial task message — EBCR-001 (activation 8)

Read AGENTS.md, SKILLS.md, research_state/agent_task_message.md, research_state/agent_handoff.md, prompts/continuous_research_operating_contract_v1.md, docs/research_protocol.md, configs/basis_crash_grid_v1.json.

## What was done this activation
- Required checks pass: grid manifest 324 cells, config_sha256=55caedf84ac723289f70f49bbed4712c8195425feb4a95e737f3e8929479a0e0 matches frozen config; 11 unittest tests pass; git diff --check clean.
- Expanded PIT rank snapshot coverage: CDX queried for 7 formation/listing dates. Only 2020-01-19 yielded a capture (sha256 520b694b…, capture 2020-11-26T21:13:11Z), saved under /tmp/pit_rank_evidence/cmc_20200119.html. 2019-12-23, 2020-01-17, 2020-02-04, 2020-07-10, 2020-10-14 have no archived capture. Total captures now 7 dates (2019-12-31, 2020-01-01, 2020-01-19, 2020-09-13, 2022-01-01, 2023-01-01, 2024-01-01). rank_verified remains false. research_state/pit_rank_search_v1.json updated.
- No artifacts modified (frozen anchor/config and Q1/extended artifacts untouched). H002/H003 remain registered_secondary_not_tested.

## Verified state
- Anchor null preserved: crash_incidence_15pct adj p 0.248, expected_shortfall_5pct_forward_mae adj p 0.949.
- 2,592 registered tests; 2,451 with p-values; 141 blocked; 424 Holm-significant with dependence caveats.
- PIT listing: 13/13 symbols listing_verified=true; 0/13 rank_verified=true.
- PIT rank evidence: Wayback Machine CMC historical snapshots at 7 dates across 2019-2024; snapshot-based coverage, not continuous. rank_verified=false.
- H002 (cheap_negative) and H003 (absolute_extreme) remain registered_secondary_not_tested.

## Your task
1. Optional: continue expanding PIT rank snapshot coverage by attempting additional Wayback CMC historical dates (e.g., around 2020-03-01, 2020-06-01, 2021-01-01, 2021-07-01, 2022-07-01, 2023-07-01). Record source, timestamp, checksum in research_state/pit_rank_search_v1.json for every source checked. Do not fabricate ranks.
2. If full point-in-time rank coverage across all formation dates is achieved, update research_state/pit_universe_verification_v1.json (rank_verified may become true only with full point-in-time evidence) and update handoff. Otherwise keep rank_verified=false and continue coverage-cohort approach. Do not project current ranks backward.
3. Do not preregister cheap-negative/absolute-extreme from grid hits. Any separate preregistration needs its own anchor/config, independent predeclared rationale, and new experiment ID. Do not modify frozen anchor/config or Q1/extended artifacts.
4. Run required checks after any change: python3 scripts/generate_grid_manifest.py --output /tmp/basis-grid-manifest.json ; python3 -m unittest discover -s tests ; git diff --check.
5. Update handoff and task message with verified findings only. A concrete next task must always remain.

## Boundary
Free public data only. No fabrication. Preserve null/failed/exclusions. Complete horizons only.
" filePath">
research_state/agent_task_message.md