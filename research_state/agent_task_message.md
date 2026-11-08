# Agent task message (EBCR-001) — activation 2739

## Read first (required)
- `research_state/agent_handoff.md` (activation 2738 completed — NO-OP; latest verified upkeep `research_state/durable_state_upkeep_v981.json`, commit `76256d1`)
- `research_state/agent_task_message.md` (this file)
- `prompts/continuous_research_operating_contract_v1.md` and `prompts/continuous_research_operating_contract_v1_1_addendum.md`
- `docs/research_protocol.md`
- `configs/basis_crash_grid_v1.json` (frozen)

## Objective
Continue durable-state upkeep under the state-change-driven cadence. Activation 2738 exited NO-OP after verifying no research-material changes since v981/`76256d1`.

## Required action (activation 2739)
1. **State-change gate first.** Compare code/test/config/grid/source/registry/frontier/audit identities/hashes against `research_state/durable_state_upkeep_v981.json` (commit `76256d1`). Run `git status --short`, `git diff --name-only 76256d1..HEAD`, `git diff --check`, and `git ls-files --others --exclude-standard`. Verify `configs/basis_crash_grid_v1.json` literal sha256 `753d9357e1d535ef4229a901e25ef059a751e4c4d56188247f5f2e0ef1debd16` on disk. If unchanged from verified material state and no new admissible source data or dated research event, exit NO-OP: no repeated full tests, no in-repo grid manifest regeneration, no new upkeep artifact, no timestamp-only handoff/task refresh, no empty commit.
2. **If changed:** run targeted affected tests first; full required gates only at a material milestone or relevant input change. `tests/test_controller_progress_accounting.py` contains function-style tests (not always collected by `unittest discover`); run it explicitly when controller progress code changes — with isolated temp dirs per test, since `python3 -m unittest tests.test_controller_progress_accounting` collects 0 tests.
3. **Preserve invariants.** Exclusions n=336 (v981), anchor null (crash_incidence_15pct adj p 0.24830545694889028; expected_shortfall_5pct_forward_mae adj p 0.9485), PIT rank CLOSED. EBCR-H001 `tested_not_supported`; EBCR-H002/EBCR-H003/EBCR-H004 `registered_secondary_not_tested`; `next_hypothesis_sequence` 5. No preregistration from grid hits; do not modify frozen anchor/config artifacts.
4. **Durable upkeep (changed path only).** Re-verify hypothesis registry consistency and re-review on-disk audits for any new unaddressed items. Create a successor upkeep artifact only if state changed and no gaps found; do not create on NO-OP.
5. **Report only verified findings.** Do not commit changes unless explicitly asked.

## Verified baseline (activation 2738, 2026-11-08)
- State-change gate vs `research_state/durable_state_upkeep_v981.json` / commit `76256d1`: `git status --short` clean before handoff/task updates; `git diff --name-only 76256d1..HEAD` limited to `.github/workflows/main.yml`, `research_state/agent_handoff.md`, `research_state/agent_task_message.md`, `research_state/durable_state_upkeep_v981.json`, `research_state/persistence_failure_diagnosis_v1.md`, `research_state/workflow_run_diagnostics.jsonl` (operational/handoff only). Research-material diff check (`scripts/`, `tests/`, `configs/`, `data/`, `results/`, `docs/`, `prompts/`, `schemas/`, `research_state/hypothesis_registry.json`, `research_state/grid_manifest_v1.json`) → empty. `git diff --check` clean; `git ls-files --others --exclude-standard` empty.
- Frozen config literal sha256 `753d9357e1d535ef4229a901e25ef059a751e4c4d56188247f5f2e0ef1debd16` verified on disk (sha256sum).
- No new admissible source data or dated research event. Last research-input change remains commit `52b3e49` (2026-10-27). `workflow_run_diagnostics.jsonl` is a harness artifact, not a research source.
- Hypothesis registry verified consistent with v981 (`next_hypothesis_sequence` 5): EBCR-H001 `tested_not_supported`; EBCR-H002/EBCR-H003/EBCR-H004 `registered_secondary_not_tested`.
- Invariants preserved (v981): exclusions n=336; anchor null (crash_incidence_15pct adj p 0.24830545694889028; expected_shortfall_5pct_forward_mae adj p 0.9485); PIT rank CLOSED. Pre-existing UNRESOLVED: contract listing/delisting/migration history; data revision behavior. No new unaddressed audit items.
- Tests/manifest: not re-run per NO-OP cadence (no code/test/config change). `pytest` unavailable. Latest verified upkeep: `research_state/durable_state_upkeep_v981.json` (commit `76256d1`). No new upkeep artifact created. No frozen artifacts modified.
