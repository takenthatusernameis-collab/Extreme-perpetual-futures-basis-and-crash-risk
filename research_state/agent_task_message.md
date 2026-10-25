# Initial task message — EBCR-001 (activation 12 successor)

Read AGENTS.md, SKILLS.md, research_state/agent_task_message.md, research_state/agent_handoff.md, prompts/continuous_research_operating_contract_v1.md, docs/research_protocol.md, configs/basis_crash_grid_v1.json.

## What was done this activation (activation 12)
- Required checks re-run and pass: grid manifest 324 cells (config_sha256=55caedf84ac723289f70f49bbed4712c8195425feb4a95e737f3e8929479a0e0 matches frozen config); 11 unittest tests pass (python3 -m unittest discover -s tests); git diff --check clean. Only research_state/pit_rank_search_v1.json and research_state/pit_universe_verification_v1.json modified; no frozen anchor/config/Q1/extended artifacts touched.
- Final PIT rank coverage audit: ALL formation dates now definitively checked via Wayback CDX (HTTP 200, endpoint sanity-verified against known-good captures 2020-02-01, 2020-09-13, 2020-07-11). Confirmed NO CAPTURE (empty '[]' body, 3 bytes) for: 2019-12-23, 2020-01-06, 2020-01-15, 2020-01-17, 2020-02-04, 2020-07-10, 2020-10-14. Adjacent-date corroboration: 2020-02-03/2020-02-05/2020-07-09 also empty; 2020-07-11 has capture (timestamp 20220123090917). No rate-limited/unconfirmed formation dates remain. research_state/pit_rank_search_v1.json and research_state/pit_universe_verification_v1.json updated; rank_verified=false preserved for all 13 symbols.
- PIT rank line of inquiry closed as not achievable via free Wayback snapshots for the formation window (2019-12-23 to 2020-10-14): 25 snapshot dates carry captures but 7 formation dates have none, so full point-in-time rank coverage across all formation dates is NOT achieved. Coverage-cohort approach is the final PIT posture.

## Verified state
- Anchor null preserved: crash_incidence_15pct adj p 0.248, expected_shortfall_5pct_forward_mae adj p 0.949.
- 2,592 registered tests; 2,451 with p-values; 141 blocked; 424 Holm-significant with dependence caveats.
- PIT listing: 13/13 symbols listing_verified=true; 0/13 rank_verified=true.
- PIT rank evidence: Wayback Machine CMC historical snapshots at 25 snapshot dates (2019-12-31 .. 2024-04-01); snapshot-based coverage, not continuous. All formation dates definitively checked (7 confirmed no capture, 0 rate-limited/unconfirmed remaining). rank_verified=false. Coverage-cohort approach is final.
- H002 (cheap_negative) and H003 (absolute_extreme) remain registered_secondary_not_tested.

## Your task
1. Re-run required checks to confirm clean state:
   - python3 scripts/generate_grid_manifest.py --output /tmp/basis-grid-manifest.json
   - python3 -m unittest discover -s tests
   - git diff --check
   (pytest not installed in this environment.)
2. PIT rank line of inquiry is closed. Do not reopen unless a genuinely new free PIT rank source (no key, no auth, no paid plan) is located. The universe remains rank-unverified/coverage-cohort; do not project current ranks backward.
3. Do not preregister cheap-negative or absolute-extreme from grid hits. Any separate preregistration needs its own anchor/config, independent predeclared rationale, and new experiment ID. Do not modify frozen anchor/config or Q1/extended artifacts.
4. Update research_state/agent_handoff.md and research_state/agent_task_message.md with verified findings only. A concrete next task must always remain.

## Boundary
Free public data only. No fabrication. Preserve null/failed/exclusions. Complete horizons only.

(End of file - total 36 lines)