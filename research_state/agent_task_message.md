# Agent task message (EBCR-001) — activation 2506

## Read first (required)
- `research_state/agent_handoff.md` (latest relevant: activation 2505 completed NO-OP)
- `research_state/agent_task_message.md` (this file)
- `prompts/continuous_research_operating_contract_v1.md` and `prompts/continuous_research_operating_contract_v1_1_addendum.md`
- `docs/research_protocol.md`
- `configs/basis_crash_grid_v1.json` (frozen)

## Objective
Continue durable-state upkeep under the state-change-driven cadence. Activation 2505 completed as NO-OP; this is activation 2506.

## Required action (activation 2506)
1. **State-change gate first.** Compare code/test/config/grid/source/registry/frontier/audit identities/hashes against latest verified state (`research_state/durable_state_upkeep_v980.json`, commit d9e5fec baseline). If unchanged and no new admissible source data or dated event, exit NO-OP: no repeated full tests, no grid manifest regeneration in-repo, no new upkeep artifact, no timestamp-only handoff/task refresh beyond the durable record, no empty commit.
2. **If changed:** run targeted affected tests first; full required gates only at material milestone or relevant input change.
3. **Preserve invariants.** Maintain null/exclusions (336); preserve `registered_secondary_not_tested` for EBCR-H002/EBCR-H003/EBCR-H004; preserve anchor null. PIT rank CLOSED. No preregistration from grid hits; do not modify frozen anchor/config artifacts.
4. **Durable upkeep (changed path only).** Re-verify hypothesis registry consistency and re-review on-disk audits for any new unaddressed items. Create a successor upkeep artifact only if state changed and no gaps found; do not create on NO-OP.
5. **Report only verified findings.** Do not commit changes unless explicitly asked.

## Verified baseline (activation 2505, 2026-11-05)
- State-change gate: `d9e5fec..HEAD` limited to harness checkpoint files (`agent_handoff.md`, `agent_task_message.md`, `durable_state_upkeep_v980.json`, `workflow_run_diagnostics.jsonl`); no code/test/config/grid/source/registry/frontier/audit/results/docs source changes. Working tree clean at gate. Frozen config literal sha256 `753d9357e1d535ef4229a901e25ef059a751e4c4d56188247f5f2e0ef1debd16` verified. Grid manifest regenerated to /tmp -> 324 cells, config_sha256 `55caedf84ac723289f70f49bbed4712c8195425feb4a95e737f3e8929479a0e0` matches. No new admissible source data or dated research event (last research-input change commit 52b3e49, 2026-10-27). Latest verified upkeep: `research_state/durable_state_upkeep_v980.json`.
- `python3 -m unittest discover -s tests` -> 11 OK (Ran 11 tests in 0.007s, OK).
- Hypothesis registry consistent: EBCR-H001 `tested_not_supported`; EBCR-H002/EBCR-H003/EBCR-H004 `registered_secondary_not_tested`; next seq 5. Exclusions n=336 (v980). Anchor null preserved (crash_incidence_15pct adj p 0.24830545694889028; expected_shortfall_5pct_forward_mae adj p 0.9485). PIT rank CLOSED.
- Pre-existing UNRESOLVED (preserved): contract listing/delisting/migration history; data revision behavior. No new unaddressed audit items.

(End of file - total 23 lines)