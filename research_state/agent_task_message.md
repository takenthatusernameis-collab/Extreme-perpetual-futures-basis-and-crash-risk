# Agent task message (EBCR-001) — activation 2467

## Read first (required)
- `research_state/agent_handoff.md` (latest)
- `research_state/agent_task_message.md` (this file)
- `prompts/continuous_research_operating_contract_v1.md` and `prompts/continuous_research_operating_contract_v1_1_addendum.md`
- `docs/research_protocol.md`
- `configs/basis_crash_grid_v1.json` (frozen)

## Objective
Continue durable-state upkeep under the state-change-driven cadence. Activation 2466 completed as NO-OP; this is activation 2467.

## Required action (activation 2467)
1. State-change gate first. Compare code/test/config/grid/source/registry/frontier/audit identities/hashes against latest verified state (`research_state/durable_state_upkeep_v980.json`, commit d9e5fec baseline). If unchanged and no new admissible source data or dated event, exit NO-OP (no repeated full tests, no grid manifest regeneration in-repo, no new upkeep artifact, no timestamp-only handoff/task refresh beyond this durable record, no empty commit).
2. If changed, run targeted affected tests first; full required gates only at material milestone or relevant input change.
3. Preserve invariants. Maintain null/exclusions (336); preserve registered_secondary_not_tested for EBCR-H002/EBCR-H003/EBCR-H004; preserve anchor null. PIT rank CLOSED. No preregistration from grid hits; do not modify frozen anchor/config artifacts.
4. Durable upkeep. Re-verify hypothesis registry consistency and re-review on-disk audits for any new unaddressed items. If changed and no gaps found, create a successor upkeep artifact only if changed; do not create on NO-OP.
5. Report only verified findings. Do not commit changes unless explicitly asked.

## Verified baseline (activation 2466)
- Frozen config: literal sha256 `753d9357e1d535ef4229a901e25ef059a751e4c4d56188247f5f2e0ef1debd16`. Grid manifest check (to /tmp) -> 324 cells, 324 unique per-cell configuration_hash_sha256, config_sha256 `55caedf84ac723289f70f49bbed4712c8195425feb4a95e737f3e8929479a0e0`. `python3 -m unittest discover -s tests` -> 11 OK.
- Exclusions n=336. Anchor null preserved (crash_incidence_15pct adj p 0.24830545694889028; expected_shortfall_5pct_forward_mae adj p 0.9485). PIT rank CLOSED. EBCR-H001 tested_not_supported; EBCR-H002-H004 registered_secondary_not_tested (next seq 5). Pre-existing UNRESOLVED: contract listing/delisting/migration history; data revision behavior.
- Last research-input change: commit 52b3e49 (2026-10-27). Latest verified upkeep: `research_state/durable_state_upkeep_v980.json`. HEAD diff from d9e5fec: harness checkpoint/handoff/task/upkeep/diagnostics files only.
- Activation 2466: state-change gate NO-OP (no research-input/code/config/grid/source/registry/frontier/audit changes). No upkeep artifact created.