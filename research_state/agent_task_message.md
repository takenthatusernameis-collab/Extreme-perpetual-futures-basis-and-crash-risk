# Initial task message — EBCR-001 (activation 14 successor)

Read AGENTS.md, SKILLS.md, research_state/agent_task_message.md, research_state/agent_handoff.md, prompts/continuous_research_operating_contract_v1.md, docs/research_protocol.md, configs/basis_crash_grid_v1.json.

## What was done this activation (activation 14)
- Required checks re-run and pass: grid manifest 324 cells (config_sha256=55caedf84ac723289f70f49bbed4712c8195425feb4a95e737f3e8929479a0e0 matches frozen config); 11 unittest tests pass (python3 -m unittest discover -s tests); git diff --check clean.
- Coverage-cohort audit complete: all 13 symbols consistent across pit_universe_verification_v1.json, data_coverage_ledger.json, candidate_perp_mapping_v1.json (listing_verified=true, rank_verified=false, coverage 1.0, meets_gate true). Artifact inconsistency noted (not fabricated): 7 symbols have verified retrieved_at_utc but null sha256_last_page — documented, no hashes synthesized.
- PIT rank line of inquiry remains closed (all formation dates definitively checked; 7 confirmed no capture; 0 rate-limited/unconfirmed; rank_verified=false; coverage-cohort approach final).
- No frozen anchor/config/Q1/extended artifacts modified. H002/H003 remain registered_secondary_not_tested. No preregistration from grid hits.

## Verified state
- Anchor null preserved: crash_incidence_15pct adj p 0.248, expected_shortfall_5pct_forward_mae adj p 0.949.
- 2,592 registered tests; 2,451 with p-values; 141 blocked; 424 Holm-significant with dependence caveats.
- PIT listing: 13/13 symbols listing_verified=true; 0/13 rank_verified=true.
- PIT rank evidence: Wayback Machine CMC historical snapshots at 25 snapshot dates (2019-12-31 .. 2024-04-01); snapshot-based coverage, not continuous. All formation dates definitively checked (7 confirmed no capture). rank_verified=false. Coverage-cohort approach is final.
- H002 (cheap_negative) and H003 (absolute_extreme) remain registered_secondary_not_tested.

## Your task
1. Audit extended evaluation artifacts for any unaddressed data gaps: research_state/evaluation_report_extended_v1.json, research_state/negative_results_report_v1.json, research_state/red_team_audit_extended_v1.json. Verify exclusions preserved (336), blocked cells documented (141), statuses complete, no silent data changes. Document findings without modifying frozen artifacts.
2. Do not preregister cheap-negative or absolute-extreme from grid hits. Any separate preregistration needs its own anchor/config, independent predeclared rationale, and new experiment ID. Do not modify frozen anchor/config or Q1/extended artifacts.
3. Re-run required checks before any further change: manifest, unittest, git diff --check. Update handoff and task message with verified findings only. A concrete next task must always remain.

## Boundary
Free public data only. No fabrication. Preserve null/failed/exclusions. Complete horizons only.
