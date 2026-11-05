# Agent task message (EBCR-001) — activation 2613

## Read first (required)
- `research_state/agent_handoff.md` (activation 2612 completed — NO-OP; latest verified research state `research_state/durable_state_upkeep_v981.json`, commit `76256d1`)
- `research_state/agent_task_message.md` (this file)
- `prompts/continuous_research_operating_contract_v1.md` and `prompts/continuous_research_operating_contract_v1_1_addendum.md`
- `docs/research_protocol.md`
- `configs/basis_crash_grid_v1.json` (frozen)

## Objective
Continue durable-state upkeep under the state-change-driven cadence. Activation 2612 exited NO-OP: post-v981 diff limited to `.github/workflows/main.yml` (operational) and harness checkpoint files; no research-material code/test/config/grid/source/registry/frontier/audit change detected.

## Required action (activation 2613)
1. **State-change gate first.** Compare code/test/config/grid/source/registry/frontier/audit identities/hashes against `research_state/durable_state_upkeep_v981.json` (commit `76256d1`). Run `git status --short`, `git diff --name-only 76256d1..HEAD`, `git diff --check`, and `git ls-files --others --exclude-standard`. Verify `configs/basis_crash_grid_v1.json` literal sha256 `753d9357e1d535ef4229a901e25ef059a751e4c4d56188247f5f2e0ef1debd16` on disk. If unchanged from verified material state and no new admissible source data or dated research event, exit NO-OP: no repeated full tests, no in-repo grid manifest regeneration, no new upkeep artifact, no timestamp-only handoff/task refresh, no empty commit.
2. **If changed:** run targeted affected tests first; full required gates only at a material milestone or relevant input change. `tests/test_controller_progress_accounting.py` contains function-style tests (not always collected by `unittest discover`); run it explicitly when controller progress code changes.
3. **Preserve invariants.** Exclusions n=336 (v981), anchor null (crash_incidence_15pct adj p 0.24830545694889028; expected_shortfall_5pct_forward_mae adj p 0.9485), PIT rank CLOSED. EBCR-H001 `tested_not_supported`; EBCR-H002/EBCR-H003/EBCR-H004 `registered_secondary_not_tested`; `next_hypothesis_sequence` 5. No preregistration from grid hits; do not modify frozen anchor/config artifacts.
4. **Durable upkeep (changed path only).** Re-verify hypothesis registry consistency and re-review on-disk audits for any new unaddressed items. Create a successor upkeep artifact only if state changed and no gaps found; do not create on NO-OP.
5. **Report only verified findings.** Do not commit changes unless explicitly asked.

## Verified baseline (activation 2612, 2026-11-05)
- State-change gate: no research-material change since v981 (`76256d1`). `git diff --name-only 76256d1..HEAD` limited to `.github/workflows/main.yml` (operational) and harness checkpoint files (`research_state/agent_handoff.md`, `research_state/agent_task_message.md`, `research_state/durable_state_upkeep_v981.json`). `git status --short` clean; `git diff --check` clean; no untracked files.
- No new admissible source data or dated research event (last research-input `52b3e49`, 2026-10-27). No research artifacts newer than `durable_state_upkeep_v981.json` (excluding harness checkpoints).
- Frozen config literal sha256 `753d9357e1d535ef4229a901e25ef059a751e4c4d56188247f5f2e0ef1debd16` verified on disk via `sha256sum`.
- Hypothesis registry consistent (`research_state/hypothesis_registry.json`): EBCR-H001 `tested_not_supported`; EBCR-H002/EBCR-H003/EBCR-H004 `registered_secondary_not_tested`; `next_hypothesis_sequence` 5.
- Invariants preserved (v981): exclusions n=336; anchor null (crash_incidence_15pct adj p 0.24830545694889028; expected_shortfall_5pct_forward_mae adj p 0.9485); PIT rank CLOSED. No audits newer than `durable_state_upkeep_v981.json`.
- Pre-existing UNRESOLVED preserved: contract listing/delisting/migration history; data revision behavior. No new unaddressed audit items.
- Tests not re-run per NO-OP (unchanged since activation 2541). `pytest` unavailable.
- Latest verified upkeep: `research_state/durable_state_upkeep_v981.json`. No commit made (not requested).
