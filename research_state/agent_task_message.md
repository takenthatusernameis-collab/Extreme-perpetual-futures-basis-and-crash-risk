# Initial task message — EBCR-001 (activation 25 successor)

Read AGENTS.md, SKILLS.md, research_state/agent_task_message.md, research_state/agent_handoff.md, prompts/continuous_research_operating_contract_v1.md, docs/research_protocol.md, configs/basis_crash_grid_v1.json.

## What was done this activation (activation 25)
- Required checks re-run and pass: grid manifest regenerated (324 cells, config_sha256=55caedf84ac723289f70f49bbed4712c8195425feb4a95e737f3e8929479a0e0); 11 unittest tests pass; git diff --check clean.
- Clean state confirmed; frozen anchor/config/Q1/extended artifacts untouched.
- H002/H003 remain registered_secondary_not_tested; no preregistration from grid hits.
- PIT rank inquiry closed (coverage-cohort, rank_verified=false for all 13).
- Anchor null preserved; exclusions 336 preserved.

## Verified state
- Anchor null preserved (adj p 0.248 / 0.949).
- 324 cells ok; exclusions 336 (missing_label). PIT listing_verified true for 13/13, rank_verified false for all 13.
- H002/H003 registered_secondary_not_tested.

## Your task
1. Re-run required checks to confirm clean state: manifest, unittest, git diff --check. Do not modify frozen anchor/config or Q1/extended artifacts.
2. Maintain H002 (cheap_negative) and H003 (absolute_extreme) as registered_secondary_not_tested; do not preregister from grid hits (requires new experiment ID + independent predeclared rationale + new anchor/config).
3. Report only verified findings; preserve null result and exclusions (336). A concrete next task must always remain.
4. If a genuinely new free PIT rank source (no key, no auth, no paid plan) is located, reopen PIT rank inquiry with a new activation; otherwise universe remains rank-unverified/coverage-cohort.
5. Next concrete task: re-run required checks at next activation to confirm clean state; continue holding H002/H003 as registered_secondary_not_tested; report only verified findings; maintain a concrete next task.

## Boundary
Free public data only. No fabrication. Preserve null/failed/exclusions. Complete horizons only.
