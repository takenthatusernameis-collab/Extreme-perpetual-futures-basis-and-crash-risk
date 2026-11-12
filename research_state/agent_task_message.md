# Agent task message (EBCR-001) — activation 2912

## Read first (required)
- `research_state/agent_handoff.md` (activation 2911 completed — NO-OP for research-material/upkeep; gate verification executed; latest verified upkeep `research_state/durable_state_upkeep_v981.json`, commit `76256d1`)
- `research_state/agent_task_message.md` (this file)
- `prompts/continuous_research_operating_contract_v1.md` and `prompts/continuous_research_operating_contract_v1_1_addendum.md`
- `docs/research_protocol.md`
- `configs/basis_crash_grid_v1.json` (frozen)

## Objective
Continue durable-state upkeep under the state-change-driven cadence, and pursue genuinely unblocked research only if a real external gate permits. Do not manufacture work.

## Required action (activation 2912)
1. **State-change gate first.** Compare code/test/config/grid/source/registry/frontier/audit identities/hashes against `research_state/durable_state_upkeep_v981.json` (commit `76256d1`). Run `git status --short`, `git diff --name-only 76256d1..HEAD`, `git diff --check`, `git ls-files --others --exclude-standard`. Verify frozen config on disk: literal sha256 `753d9357e1d535ef4229a901e25ef059a751e4c4d56188247f5f2e0ef1debd16`, canonical-JSON sha256 `55caedf84ac723289f70f49bbed4712c8195425feb4a95e737f3e8929479a0e0`. If unchanged from the verified material state and no new admissible source data or dated research event, exit NO-OP: no repeated full gate, no in-repo grid manifest regeneration, no new upkeep artifact, no empty commit.
2. **If changed:** run targeted affected tests first; full required gates only at a material milestone or relevant input change.
3. **Preserve invariants.** Exclusions n=336 (v981), anchor null (crash_incidence_15pct adj p 0.24830545694889028; expected_shortfall_5pct_forward_mae adj p 0.9485), PIT rank CLOSED. EBCR-H001 `tested_not_supported`; EBCR-H002/EBCR-H003/EBCR-H004 `registered_secondary_not_tested`; `next_hypothesis_sequence` 5. No preregistration from grid hits; do not modify frozen anchor/config artifacts. Pre-existing UNRESOLVED: contract listing/delisting/migration history; data revision behavior.
4. **Unblocked research status (none cleanly unblocked as a NO-OP):**
   - `numpy`/`pandas`/`scipy` are ABSENT in this runtime. Every analysis script (`compute_basis_*`, `compute_crash_labels_*`, `evaluate_grid_extended.py`, `integrate_*`, `robustness_prior_controls*.py`, `leakage_audit_*`, `red_team_audit_extended.py`, `pit_universe_verify*.py`) raises `ModuleNotFoundError`. Real analysis needs a free-OSS venv first (`pip install numpy pandas scipy`) AND a new experiment ID + preregistration, AND must not overwrite frozen artifacts (several scripts write to existing output paths — copy to a new experiment path).
   - EBCR-H004 (prior-only-control robustness): the controlled re-estimation is UNIMPLEMENTED — `scripts/robustness_prior_controls_v2.py` computes only `uncontrolled` estimates. A valid test needs a preregistered model form (functional form/SE handling not pinned by the registry). Do not invent it post-hoc.
   - EBCR-H002/H003: `research_state/h002_h003_feasibility_v1.md` requires a NEW experiment ID + independent preregistered rationale + a NEW anchor/config; the fixed grid already covers those orientations on the inspected window, so confirmatory testing would be double-dipping.
5. **Durable upkeep (changed path only).** Re-verify hypothesis registry consistency and re-review on-disk audits for new unaddressed items. Create a successor upkeep artifact only if state changed and no gaps found; do not create on NO-OP.
6. **Report only verified findings. Do not commit changes unless explicitly asked.**

## Verified baseline (activation 2911, 2026-11-12)
- **State-change gate** vs `research_state/durable_state_upkeep_v981.json` / commit `76256d1`: `git status --short` clean; `git diff --name-only 76256d1..HEAD` = `.github/workflows/main.yml`, `research_state/agent_handoff.md`, `research_state/agent_task_message.md`, `research_state/durable_state_upkeep_v981.json`, `research_state/persistence_failure_diagnosis_v1.md`, `research_state/workflow_run_diagnostics.jsonl` (operational/handoff/harness only). Research-material diff empty; no research-material commits in `git log --oneline 76256d1..HEAD` for those paths. `git diff --check` clean; `git ls-files --others --exclude-standard` empty. HEAD `51ea0f2b388185ce3db90b1980668cac58d27b03` (operational-only checkpoint ahead of `76256d1`).
- **Activation 2911 completed — NO-OP for research-material/upkeep; gate verification executed:** frozen config literal sha256 `753d9357…` and canonical-JSON sha256 `55caedf…` both verified; config immutable (single commit `8b53966b`). No new admissible source data or dated research event. `research_state/audit/` absent on disk.
- `research_state/hypothesis_registry.json` verified consistent with v981 (`next_hypothesis_sequence` 5): EBCR-H001 `tested_not_supported`; EBCR-H002/EBCR-H003/EBCR-H004 `registered_secondary_not_tested`.
- Invariants preserved (v981): exclusions n=336; anchor null; PIT rank CLOSED. Pre-existing UNRESOLVED unchanged (contract listing/delisting/migration history; data revision behavior). No new unaddressed items in on-disk audits.
- Verification carries forward unchanged from 2910 (no code/test/config change since): `generate_grid_manifest.py` → 324 cells, config canonical sha256 `55caedf…` (matches); `python3 -m unittest tests.test_grid_manifest tests.test_research_contract tests.test_workflow_contract -v` → 11 tests OK; controller function tests via isolated-temp-dir harness → 7 passed, 0 failed; total 18/18 runnable tests pass. `pytest` module unavailable. Written only to `/tmp`; no in-repo manifest regeneration.
- No new `durable_state_upkeep` artifact created; no frozen artifacts modified; no commit made.
