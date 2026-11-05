# Agent task message (EBCR-001) — activation 2572

## Read first (required)
- `research_state/agent_handoff.md` (activation 2571 completed — NO-OP; latest verified research state `research_state/durable_state_upkeep_v981.json`, commit `76256d1`)
- `research_state/agent_task_message.md` (this file)
- `prompts/continuous_research_operating_contract_v1.md` and `prompts/continuous_research_operating_contract_v1_1_addendum.md`
- `docs/research_protocol.md`
- `configs/basis_crash_grid_v1.json` (frozen)

## Objective
Continue durable-state upkeep under the state-change-driven cadence. Activation 2571 exited NO-OP: post-v981 changes remain limited to operational harness/session control and harness checkpoint files; no research-material code/test/config/grid/source/registry/frontier/audit change detected.

## Required action (activation 2572)
1. **State-change gate first.** Compare code/test/config/grid/source/registry/frontier/audit identities/hashes against latest verified research state (`research_state/durable_state_upkeep_v981.json`, commit `76256d1`). Run `git status --short`, `git diff --name-only 76256d1..HEAD`, `git diff --check`, and `git ls-files --others --exclude-standard`. If unchanged from verified material state and no new admissible source data or dated research event, exit NO-OP: no repeated full tests, no in-repo grid manifest regeneration, no new upkeep artifact, no timestamp-only handoff/task refresh beyond the durable record, no empty commit.
2. **If changed:** run targeted affected tests first; full required gates only at material milestone or relevant input change. `tests/test_controller_progress_accounting.py` contains function-style tests (not always collected by `unittest discover`); run it explicitly when controller progress code changes.
3. **Preserve invariants.** Maintain exclusions n=336 (v981), anchor null, PIT rank CLOSED. Preserve EBCR-H001 `tested_not_supported`; EBCR-H002/EBCR-H003/EBCR-H004 `registered_secondary_not_tested`. No preregistration from grid hits; do not modify frozen anchor/config artifacts.
4. **Durable upkeep (changed path only).** Re-verify hypothesis registry consistency and re-review on-disk audits for any new unaddressed items. Create a successor upkeep artifact only if state changed and no gaps found; do not create on NO-OP.
5. **Report only verified findings.** Do not commit changes unless explicitly asked.

## Verified baseline (activation 2571, 2026-11-05)
- State-change gate (HEAD `e58809a`): no research-material change since v981 (`76256d1`). `git diff --name-only 76256d1..HEAD` limited to `.github/workflows/main.yml` (operational, `64f77cc`) and harness checkpoint files. `git status --short` clean; `git diff --check` clean; no untracked files.
- No new admissible source data or dated research event (last research-input change remains commit `52b3e49`, 2026-10-27). `research_state/workflow_run_diagnostics.jsonl` entries are harness workflow artifacts only (latest: run 41998331220, conclusion failure, captured 2026-11-05T17:06:07Z).
- Frozen config literal sha256 `753d9357e1d535ef4229a901e25ef059a751e4c4d56188247f5f2e0ef1debd16` verified on disk. Tests not re-run per NO-OP (unchanged since v981: `unittest discover -s tests` → 11 OK at 2541; controller progress function tests → 7 OK at 2541). `pytest` unavailable.
- Hypothesis registry consistent: EBCR-H001 `tested_not_supported`; EBCR-H002/EBCR-H003/EBCR-H004 `registered_secondary_not_tested`; `next_hypothesis_sequence` 5. v981 exclusions_n 336. Anchor null preserved (crash_incidence_15pct adj p 0.24830545694889028; expected_shortfall_5pct_forward_mae adj p 0.9485). PIT rank CLOSED.
- Pre-existing UNRESOLVED preserved: contract listing/delisting/migration history; data revision behavior. No new unaddressed audit items.
- Latest verified upkeep: `research_state/durable_state_upkeep_v981.json`. No commit made (not requested).

(End of file - total 26 lines)