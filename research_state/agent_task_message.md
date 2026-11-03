# Agent task message (EBCR-001) — activation 1888

## Read first (required)
- `research_state/agent_handoff.md` (activation 1887 completed; latest verified upkeep v979)
- `research_state/agent_task_message.md` (this file)
- `prompts/continuous_research_operating_contract_v1.md` and `prompts/continuous_research_operating_contract_v1_1_addendum.md`
- `docs/research_protocol.md`
- `configs/basis_crash_grid_v1.json` (frozen)

## Objective
Continue durable-state upkeep under the state-change-driven cadence. Activation 1887 was NO-OP. Latest verified upkeep is v979 (commit fc6f76d, created 2026-11-03T03:49:39Z). Proceed to activation 1888.

## Required action (activation 1888)
1. **State-change gate first.** Compare code/test/config/grid/source/registry/frontier/audit identities/hashes against latest verified state (`research_state/durable_state_upkeep_v979.json`, created 2026-11-03T03:49:39Z, commit fc6f76d). If unchanged and no new admissible source data or dated event, exit NO-OP (no repeated full tests, no grid manifest regeneration, no new upkeep artifact, no timestamp-only handoff update, no empty commit).
2. **If changed**, run targeted affected tests first; full required gates only at material milestone or relevant input change.
3. **Preserve invariants.** Maintain null/exclusions (336); preserve registered_secondary_not_tested for EBCR-H002/EBCR-H003/EBCR-H004; preserve anchor null (crash_incidence_15pct adj p 0.24830545694889028; expected_shortfall_5pct_forward_mae adj p 0.9485). PIT rank CLOSED — do not reopen without genuinely new free PIT rank source. No preregistration from grid hits; do not modify frozen anchor/config/Q1/extended artifacts.
4. **Durable upkeep.** Re-verify hypothesis registry consistency (EBCR-H001 tested_not_supported; EBCR-H002/EBCR-H003/EBCR-H004 registered_secondary_not_tested; next_hypothesis_sequence 5) and re-review on-disk audits for any new unaddressed items. If changed and no gaps found, create `research_state/durable_state_upkeep_v980.json` with verdict `no_gaps_found`. If gaps found, document explicitly with artifact paths and concrete next steps. Do not create v980 on NO-OP.
5. **Report only verified findings.** Do not commit changes unless explicitly asked.

## Verified baseline
- Frozen config canonical sha256 `55caedf84ac723289f70f49bbed4712c8195425feb4a95e737f3e8929479a0e0`. Grid 324/324 unique hashes. unittest 11 OK; pytest unavailable. git diff --check clean; git status clean.
- Exclusions n=336. Anchor null preserved. PIT rank CLOSED (verified free Wayback-CMC). Pre-existing UNRESOLVED: contract listing/delisting/migration history; data revision behavior.
