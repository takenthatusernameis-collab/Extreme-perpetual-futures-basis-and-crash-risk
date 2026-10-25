# Initial task message — EBCR-001 (activation 11 successor)

Read AGENTS.md, SKILLS.md, research_state/agent_task_message.md, research_state/agent_handoff.md, prompts/continuous_research_operating_contract_v1.md, docs/research_protocol.md, configs/basis_crash_grid_v1.json.

## What was done this activation (activation 11)
- PIT rank snapshot coverage expanded: Wayback CDX + direct snapshot page fetch both reachable (HTTP 200). 11 new capture dates with page-level sha256: 2020-02-01, 2020-08-01, 2020-11-01, 2021-02-01, 2021-05-01, 2021-06-01, 2021-08-01, 2021-09-01, 2021-12-01, 2022-05-01, 2023-12-01 (pages saved under /tmp/pit_rank_evidence/). Total 25 snapshot dates with captures (up from 14); page-level sha256 for 18 dates, CDX capture timestamps only for 7. 2019-12-23 and 2020-10-14 confirmed no capture; 2020-02-04 and 2020-07-10 rate-limited/unconfirmed (not treated as no-capture). research_state/pit_rank_search_v1.json and research_state/pit_universe_verification_v1.json updated; rank_verified=false preserved for all 13 symbols.
- Required checks re-run and pass: grid manifest 324 cells (config_sha256=55caedf84ac723289f70f49bbed4712c8195425feb4a95e737f3e8929479a0e0 matches frozen config); 11 unittest tests pass; git diff --check clean.
- No frozen anchor/config/Q1/extended artifacts modified. H002/H003 remain registered_secondary_not_tested.

## Verified state
- Anchor null preserved: crash_incidence_15pct adj p 0.248, expected_shortfall_5pct_forward_mae adj p 0.949.
- 2,592 registered tests; 2,451 with p-values; 141 blocked; 424 Holm-significant with dependence caveats.
- PIT listing: 13/13 symbols listing_verified=true; 0/13 rank_verified=true.
- PIT rank evidence: Wayback Machine CMC historical snapshots at 25 snapshot dates (2019-12-31 .. 2024-04-01); snapshot-based coverage, not continuous. rank_verified=false. Formation dates span 2019-12-23 to 2020-10-14; several lack captures. Page-level sha256 for 18 dates under /tmp/pit_rank_evidence/.
- H002 (cheap_negative) and H003 (absolute_extreme) remain registered_secondary_not_tested.

## Your task
1. Re-run required checks to confirm clean state:
   - python3 scripts/generate_grid_manifest.py --output /tmp/basis-grid-manifest.json
   - python3 -m unittest discover -s tests
   - git diff --check
   (pytest not installed in this environment.)
2. (Optional, bounded) After a cooldown, retry the 2 unconfirmed formation dates (2020-02-04, 2020-07-10) via Wayback CDX. Do not treat rate-limit errors as no-capture; if still no capture, document as confirmed no-capture. Record source/timestamp in research_state/pit_rank_search_v1.json.
3. PIT rank coverage-cohort approach stands: rank_verified=false, snapshot-based not continuous across every formation date; do not project current ranks backward. Full PIT rank coverage across all formation dates is not achievable via free Wayback snapshots for the formation window (2019-12-23 to 2020-10-14).
4. Do not preregister cheap-negative or absolute-extreme from grid hits. Any separate preregistration needs its own anchor/config, independent predeclared rationale, and new experiment ID. Do not modify frozen anchor/config or Q1/extended artifacts.
5. Update research_state/agent_handoff.md and research_state/agent_task_message.md with verified findings only. A concrete next task must always remain.

## Boundary
Free public data only. No fabrication. Preserve null/failed/exclusions. Complete horizons only.
