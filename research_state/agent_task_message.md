# Agent task message (EBCR-001) — activation 2542

## Read first (required)
- `research_state/agent_handoff.md` (latest: activation 2541 completed — material state-change verification, no gaps found)
- `research_state/agent_task_message.md` (this file)
- `prompts/continuous_research_operating_contract_v1.md` and `prompts/continuous_research_operating_contract_v1_1_addendum.md`
- `docs/research_protocol.md`
- `configs/basis_crash_grid_v1.json` (frozen)

## Objective
Continue durable-state upkeep under the state-change-driven cadence. Activation 2541 detected material code/test changes since baseline `d9e5fec` (controller progress accounting scripts/tests) and completed targeted verification; this is activation 2542.

## Required action (activation 2542)
1. **State-change gate first.** Compare code/test/config/grid/source/registry/frontier/audit identities/hashes against latest verified state (`research_state/durable_state_upkeep_v981.json`, HEAD at 2541 verification: `76256d1`, gate baseline `d9e5fec`). Run `git status --short`, `git diff --name-only d9e5fec..HEAD` (or against latest verified commit if a new research-relevant commit exists), `git diff --check`, and `git ls-files --others --exclude-standard`. If unchanged from verified material state and no new admissible source data or dated research event, exit NO-OP: no repeated full tests, no grid manifest regeneration in-repo, no new upkeep artifact, no timestamp-only handoff/task refresh beyond the durable record, no empty commit.
2. **If changed:** run targeted affected tests first; full required gates only at material milestone or relevant input change. Note: `tests/test_controller_progress_accounting.py` contains function-style tests (not discovered by `unittest discover` default pattern in prior runs); run it explicitly when controller progress code changes.
3. **Preserve invariants.** Maintain null/exclusions (336, v981); preserve `registered_secondary_not_tested` for EBCR-H002/EBCR-H003/EBCR-H004; preserve anchor null. PIT rank CLOSED. No preregistration from grid hits; do not modify frozen anchor/config artifacts.
4. **Durable upkeep (changed path only).** Re-verify hypothesis registry consistency and re-review on-disk audits for any new unaddressed items. Create a successor upkeep artifact only if state changed and no gaps found; do not create on NO-OP.
5. **Report only verified findings.** Do not commit changes unless explicitly asked.

## Verified baseline (activation 2541, 2026-11-05)
- State-change gate: material change detected — `git diff --name-only d9e5fec..HEAD` includes `scripts/controller_progress.py` (new) and `tests/test_controller_progress_accounting.py` (new) plus harness checkpoint files. `git diff --check` clean; no untracked files.
- No new admissible source data or dated research event (last research-input change remains commit 52b3e49, 2026-10-27). `research_state/workflow_run_diagnostics.jsonl` remains harness workflow artifacts only (latest recorded: run 41998331220, conclusion failure, 2026-11-05T17:06:07Z).
- Frozen config literal sha256 `753d9357e1d535ef4229a901e25ef059a751e4c4d56188247f5f2e0ef1debd16` verified on disk; grid manifest regenerated to `/tmp` -> 324 cells, 324 unique per-cell `configuration_hash_sha256`, config_sha256 `55caedf84ac723289f70f49bbed4712c8195425feb4a95e737f3e8929479a0e0` matches frozen canonical.
- Tests: `python3 -m unittest discover -s tests` -> 11 OK. Controller progress accounting function tests (7) executed directly -> OK, including workflow wiring contract. `pytest` unavailable.
- Hypothesis registry consistent: EBCR-H001 `tested_not_supported`; EBCR-H002/EBCR-H003/EBCR-H004 `registered_secondary_not_tested`; next seq 5. Exclusions n=336 (v981). Anchor null preserved (crash_incidence_15pct adj p 0.24830545694889028; expected_shortfall_5pct_forward_mae adj p 0.9485). PIT rank CLOSED.
- Pre-existing UNRESOLVED (preserved): contract listing/delisting/migration history; data revision behavior. No new unaddressed audit items.
- Latest verified upkeep: `research_state/durable_state_upkeep_v981.json`. No commit made (not requested).
