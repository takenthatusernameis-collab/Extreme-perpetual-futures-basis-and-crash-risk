# Initial task message — EBCR-001 (activation 16 successor)

Read AGENTS.md, SKILLS.md, research_state/agent_task_message.md, research_state/agent_handoff.md, prompts/continuous_research_operating_contract_v1.md, docs/research_protocol.md, configs/basis_crash_grid_v1.json.

## What was done this activation (activation 16)
- Required checks re-run and pass: grid manifest 324 cells (config_sha256=55caedf84ac723289f70f49bbed4712c8195425feb4a95e737f3e8929479a0e0 matches frozen config); 11 unittest tests pass (python3 -m unittest discover -s tests); git diff --check clean.
- Prior task message (activation 14 successor) completed: extended evaluation artifact audit verified (no unaddressed data gaps; exclusions 336 preserved; 141 blocked cell-endpoint tests documented; 324 cells ok; no silent data changes). Null result preserved. H002/H003 remain registered_secondary_not_tested.
- No frozen anchor/config/Q1/extended artifacts modified. No preregistration from grid hits.

## Verified state
- Anchor null preserved: crash_incidence_15pct adj p 0.248, expected_shortfall_5pct_forward_mae adj p 0.949.
- 2,592 registered tests; 2,451 with p-values; 141 blocked (cell-endpoint, not cells); 424 Holm-significant with dependence caveats.
- PIT listing: 13/13 symbols listing_verified=true; 0/13 rank_verified=true.
- PIT rank evidence: Wayback Machine CMC historical snapshots at 25 snapshot dates; snapshot-based coverage, not continuous. All formation dates definitively checked (7 confirmed no capture). rank_verified=false. Coverage-cohort approach is final.
- H002 (cheap_negative) and H003 (absolute_extreme) remain registered_secondary_not_tested.

## Your task
1. Re-run required checks to confirm clean state: manifest (scripts/generate_grid_manifest.py --output /tmp/basis-grid-manifest.json), unittest (python3 -m unittest discover -s tests), git diff --check. Do not modify frozen anchor/config or Q1/extended artifacts.
2. Maintain H002 (cheap_negative) and H003 (absolute_extreme) as registered_secondary_not_tested; do not preregister from grid hits (would require new experiment ID + independent predeclared rationale + new anchor/config).
3. Report only verified findings; preserve null result and exclusions (336). A concrete next task must always remain.
4. If a genuinely new free PIT rank source (no key, no auth, no paid plan) is located, reopen PIT rank inquiry with a new activation; otherwise universe remains rank-unverified/coverage-cohort.

## Boundary
Free public data only. No fabrication. Preserve null/failed/exclusions. Complete horizons only.

(End of file)