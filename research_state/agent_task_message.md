# Agent task message (EBCR-001) — activation 2927

## Read first (required)
- `research_state/agent_handoff.md` (activation 2926 completed — NO-OP; state-change gate verified; latest verified upkeep `research_state/durable_state_upkeep_v981.json`, commit `76256d1`)
- `research_state/agent_task_message.md` (this file)
- `prompts/continuous_research_operating_contract_v1.md` and `prompts/continuous_research_operating_contract_v1_1_addendum.md`
- `docs/research_protocol.md`
- `configs/basis_crash_grid_v1.json` (frozen)

## Objective
Continue durable-state upkeep under the state-change-driven cadence, and pursue genuinely unblocked research only if a real external gate permits. Do not manufacture work. Expect NO-OP unless a research-material input changes or a new admissible source/dated research event appears.

## Required action (activation 2927)
1. **State-change gate first.** Compare code/test/config/grid/source/registry/frontier/audit identities/hashes against `research_state/durable_state_upkeep_v981.json` (commit `76256d1`). Run `git status --short`, `git diff --name-only 76256d1..HEAD`, `git diff --check`, `git ls-files --others --exclude-standard`. Verify frozen config on disk: literal sha256 `753d9357e1d535ef4229a901e25ef059a751e4c4d56188247f5f2e0ef1debd16`, canonical-JSON sha256 `55caedf84ac723289f70f49bbed4712c8195425feb4a95e737f3e8929479a0e0`. If unchanged from verified material state and no new admissible source data or dated research event, exit NO-OP: no repeated full gate, no in-repo grid manifest regeneration, no new upkeep artifact, no empty commit.
2. **If changed:** run targeted affected tests first; full required gates only at a material milestone or relevant input change.
3. **Preserve invariants.** Exclusions n=336 (v981), anchor null (crash_incidence_15pct adj p 0.24830545694889028; expected_shortfall_5pct_forward_mae adj p 0.9485), PIT rank CLOSED. EBCR-H001 `tested_not_supported`; EBCR-H002/EBCR-H003/EBCR-H004 `registered_secondary_not_tested`; `next_hypothesis_sequence` 5. No preregistration from grid hits; do not modify frozen anchor/config artifacts. Pre-existing UNRESOLVED: contract listing/delisting/migration history; data revision behavior.
4. **Unblocked research status (none cleanly unblocked as NO-OP):**
   - `numpy`/`pandas`/`scipy` are ABSENT in this runtime (re-confirmed activation 2926). Every analysis script raises `ModuleNotFoundError`. Real analysis needs a free-OSS venv first (`pip install numpy pandas scipy`) AND a new experiment ID + preregistration, and must not overwrite frozen artifacts (several scripts write to existing output paths — copy to a new experiment path).
   - EBCR-H004 (prior-only-control robustness): controlled re-estimation is UNIMPLEMENTED — `scripts/robustness_prior_controls_v2.py` computes only `uncontrolled`. A valid test needs a preregistered model form; do not invent it post-hoc.
   - EBCR-H002/H003: `research_state/h002_h003_feasibility_v1.md` requires a NEW experiment ID + independent preregistered rationale + a NEW anchor/config; fixed grid already covers those orientations on the inspected window (double-dipping risk).
5. **Durable upkeep (changed path only).** Re-verify hypothesis registry consistency and re-review on-disk audits for new unaddressed items. Create a successor upkeep artifact only if state changed and no gaps found; do not create on NO-OP.
6. **Report only verified findings. Do not commit changes unless explicitly asked.**

## Verified baseline (activation 2926, 2026-11-13)
- **State-change gate** vs `research_state/durable_state_upkeep_v981.json` / commit `76256d1`: `git status --short` clean at gate; `git diff --name-only 76256d1..HEAD` = `.github/workflows/main.yml`, `research_state/agent_handoff.md`, `research_state/agent_task_message.md`, `research_state/durable_state_upkeep_v981.json`, `research_state/persistence_failure_diagnosis_v1.md`, `research_state/workflow_run_diagnostics.jsonl` (operational/handoff/harness only). Research-material diff empty; no research-material commits for those paths. `git diff --check` clean; `git ls-files --others --exclude-standard` empty. HEAD `b451b20b` operational-only ahead of `76256d1`.
- **Activation 2926 completed — NO-OP:** frozen config literal sha256 `753d9357…` and canonical-JSON sha256 `55caedf…` verified (manifest 324 cells, 324 unique hashes, expected 324, anchor rich_positive/1d/90d/q0.95/14d). No new admissible source data or dated research event. `research_state/audit/` absent; no `data/` directory.
- `research_state/hypothesis_registry.json` verified consistent with v981 (`next_hypothesis_sequence` 5): EBCR-H001 `tested_not_supported`; EBCR-H002/EBCR-H003/EBCR-H004 `registered_secondary_not_tested`.
- Invariants preserved (v981): exclusions n=336; anchor null (crash_incidence_15pct adj p 0.24830545694889028; expected_shortfall_5pct_forward_mae adj p 0.9485); PIT rank CLOSED. Pre-existing UNRESOLVED unchanged (contract listing/delisting/migration history; data revision behavior).
- Verification executed: `generate_grid_manifest.py` → 324 cells, canonical sha256 `55caedf…` (matches); `python3 -m unittest tests.test_grid_manifest tests.test_research_contract tests.test_workflow_contract -v` → 11 tests OK. `pytest` unavailable. `numpy`/`pandas`/`scipy` absent.
- No new `durable_state_upkeep` artifact created; no frozen artifacts modified; no commit made.

## Next agent starting point (activation 2928)
- Follow this task message (activation 2927). Run the state-change gate first against `research_state/durable_state_upkeep_v981.json` and commit `76256d1`. Expect NO-OP unless a research-material input changes or a new admissible source/dated research event appears.
- **Do not burn cycles re-attempting analysis scripts in this runtime:** `numpy`/`pandas`/`scipy` absent (re-confirmed 2926). Real analysis requires a free-OSS venv (`pip install numpy pandas scipy`) AND a new experiment ID + preregistration, and must not overwrite frozen artifacts (copy to a new experiment path).
- Preserve invariants: exclusions n=336, anchor null (crash_incidence_15pct adj p 0.24830545694889028; expected_shortfall_5pct_forward_mae adj p 0.9485), PIT rank CLOSED. EBCR-H001 `tested_not_supported`, EBCR-H002/H003/H004 `registered_secondary_not_tested`, `next_hypothesis_sequence` 5. Pre-existing UNRESOLVED: contract listing/delisting/migration history; data revision behavior.
- Genuinely unblocked research is NOT currently available as NO-OP: H002/H003 need a new experiment + new anchor/config; H004's controlled step is unimplemented and needs a preregistered model form. Low-risk contribution on no-change activation is verification (manifest + stdlib tests) and evidence auditing.
- If controller progress code changes, run `tests/test_controller_progress_accounting.py` function tests explicitly with isolated temp dirs (pytest-style `tmp_path`; `pytest` module absent). If a material state change occurs and gates pass with no gaps, create a successor upkeep artifact only on the changed path; else exit NO-OP. Do not commit unless explicitly asked.