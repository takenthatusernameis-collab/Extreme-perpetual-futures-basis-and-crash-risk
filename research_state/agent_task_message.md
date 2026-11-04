# Agent task message (EBCR-001) — activation 2117
1:
2: ## Read first (required)
3: - `research_state/agent_handoff.md` (latest verified upkeep v980, commit d9e5fec; activation 2116 completed NO-OP)
4: - `research_state/agent_task_message.md` (this file)
5: - `prompts/continuous_research_operating_contract_v1.md` and `prompts/continuous_research_operating_contract_v1_1_addendum.md`
6: - `docs/research_protocol.md`
7: - `configs/basis_crash_grid_v1.json` (frozen)
8:
9: ## Objective
10: Continue durable-state upkeep under the state-change-driven cadence. Activation 2116 completed as NO-OP (no research state/code/config/grid/source changes; only harness checkpoint/handoff/task/upkeep/diagnostics files). Proceed to activation 2117.
11:
12: ## Required action (activation 2117)
13: 1. State-change gate first. Compare code/test/config/grid/source/registry/frontier/audit identities/hashes against latest verified state (`research_state/durable_state_upkeep_v980.json`, commit d9e5fec). If unchanged and no new admissible source data or dated event, exit NO-OP (no repeated full tests, no grid manifest regeneration, no new upkeep artifact, no timestamp-only handoff update beyond this record, no empty commit).
14: 2. If changed, run targeted affected tests first; full required gates only at material milestone or relevant input change.
15: 3. Preserve invariants. Maintain null/exclusions (336); preserve registered_secondary_not_tested for EBCR-H002/EBCR-H003/EBCR-H004; preserve anchor null. PIT rank CLOSED. No preregistration from grid hits; do not modify frozen anchor/config artifacts.
16: 4. Durable upkeep. Re-verify hypothesis registry consistency and re-review on-disk audits for any new unaddressed items. If changed and no gaps found, create successor upkeep artifact only if changed; do not create on NO-OP.
17: 5. Report only verified findings. Do not commit changes unless explicitly asked.
18:
19: ## Verified baseline
20: - Frozen config canonical sha256 `55caedf84ac723289f70f49bbed4712c8195425feb4a95e737f3e8929479a0e0`; literal file sha256 `753d9357e1d535ef4229a901e25ef059a751e4c4d56188247f5f2e0ef1debd16`. Grid 324/324 unique hashes. unittest 11 OK; pytest unavailable. git diff --check clean; git status clean.
21: - Exclusions n=336. Anchor null preserved (crash_incidence_15pct adj p 0.24830545694889028; expected_shortfall_5pct_forward_mae adj p 0.9485). PIT rank CLOSED. Pre-existing UNRESOLVED: contract listing/delisting/migration history; data revision behavior.
