# Agent task message (EBCR-001) — activation 2939 (written at end of activation 2938)

## Read first (required)
- `research_state/agent_handoff.md` (activation 2938 completed — TASK (A) COMPLETED: EBCR-H004 controlled re-estimation with corrected inference; artifacts `research_state/h004_controlled_rereg_v2.json`, `research_state/robustness_controlled_v4.json/.md`, new script `scripts/robustness_controlled_v4.py`)
- `research_state/agent_task_message.md` (previous task message)
- `prompts/continuous_research_operating_contract_v1.md` and `prompts/continuous_research_operating_contract_v1_1_addendum.md`
- `docs/research_protocol.md`
- `configs/basis_crash_grid_v1.json` (frozen)

## What changed since the previous activation
1. **Task (A) completed.** EBCR-H004 controlled re-estimation ran as experiment `EBCR-001-ROBUST-CTRL-V4` (preregistered first in `research_state/h004_controlled_rereg_v2.json`). Result: `crash_incidence_15pct` controlled cluster p 0.4932 and `expected_shortfall_5pct_forward_mae` controlled cluster p 0.4572 — both Holm-not-significant; null preserved, consistent with anchor co-primary (adj p 0.2483 / 0.9485). Outputs at new paths only; V3 outputs preserved untouched.
2. **V3 inference bug identified and corrected.** V3's hand-rolled cluster-robust SE used bread `(X'X)^-1` for Logit (misspecified), producing a false Holm-significant claim (p=5.65e-08 vs correct p 0.4932; correct SE ~0.266 vs V3's ~0.034). V4 uses statsmodels `cov_type='cluster'` (symbol-month). Bug documented in `robustness_controlled_v4.json` (`correction_vs_v3`) and in the handoff; V3 files left intact as preserved evidence.
3. **Environment:** `.venv` exists (gitignored, not committed) with python 3.12.3, numpy 2.5.4, pandas 3.1.1, scipy 1.18.1, statsmodels 0.15.0, pytest 9.2.0. PyPI reachable if reinstall needed. Use `.venv/bin/python`.
4. **Gates pass:** manifest 324 cells / canonical sha256 `55caedf…`; `pytest -q tests` 18 passed; `git diff --check` clean; config literal sha256 `753d9357…` matches frozen value.

## Objective (activation 2939)
Advance the highest-value genuinely unblocked work. Do not manufacture work, do not re-run the frozen evaluation or the V4 controlled estimation (both done; inputs unchanged), and do not touch frozen artifacts or V3 outputs. Expect at least one real, verifiable deliverable or an explicit, documented blocker.

## Required actions (activation 2939)
1. **State-change gate first** (cheap): compare code/test/config/grid/source/registry/frontier/audit identities against `research_state/durable_state_upkeep_v981.json` / commit `76256d1`; verify frozen config literal sha256 `753d9357e1d535ef4229a901e25ef059a751e4c4d56188247f5f2e0ef1debd16` and canonical `55caedf84ac723289f70f49bbed4712c8195425feb4a95e737f3e8929479a0e0`. Note activation 2938's new untracked files in the gate summary. Do not rerun the full gate if nothing changed.
2. **Pick ONE unblocked task and preregister it before computing outcomes:**
   - **(B) EBCR-H002 / EBCR-H003.** Require a NEW experiment ID + independent preregistered rationale + a NEW anchor/config, because the fixed grid already covers cheap-negative and absolute-extreme orientations on the inspected window (double-dipping risk). See `research_state/h002_h003_feasibility_v1.md` / `h002_h003_feasibility_review_v1.*`. Do not re-use the H001/H004 anchor.
   - **(C) Evidence audit.** Audit the derived artifacts (`integrated_extended_v1.json`, `basis_computation_extended_v1.json`, `crash_labels_extended_v1.json`) for undocumented assumptions, coverage/missingness and exclusion accounting (exclusions n=336), and record findings in `research_state/audit/` (directory currently absent). Does not contaminate frozen evidence. A natural first audit item: confirm `robustness_controlled_v4.json` panel/reproduce V4 from preregistration, and document the V3→V4 inference correction as a red-team finding.
   - **(A) follow-up (registry decision only, no computation):** EBCR-H004 is now supported ("robust to predeclared prior-only controls, null preserved") but registry status remains `registered_secondary_not_tested`. Any status change needs a separate preregistration decision — do not change `next_hypothesis_sequence` or statuses without one.
3. **Preserve invariants:** exclusions n=336; anchor null (crash_incidence_15pct adj p 0.24830545694889028; expected_shortfall_5pct_forward_mae adj p 0.9485); PIT rank CLOSED; EBCR-H001 `tested_not_supported`; EBCR-H002/H003/H004 `registered_secondary_not_tested`; `next_hypothesis_sequence` 5. No preregistration derived from inspected grid hits; no frozen artifact edits; apply Holm across the complete registered family; preserve null/contradictory/failed evidence (including V3's invalid claim as corrected evidence, not deleted).
4. **Do not repeat already-completed work:** frozen extended evaluation reproduction (activation 2937) and H004 controlled re-estimation V4 (activation 2938) are done; do not re-run unless an input changes.
5. **Report only verified findings.** Do not commit unless explicitly asked. Update this handoff and write the next task message.

## Verified baseline (activation 2938, 2026-11-13)
- State-change gate: config literal sha256 and canonical sha256 match frozen; manifest 324 cells; git diff --check clean.
- V4: `research_state/robustness_controlled_v4.json` — 4014 obs, 11 symbols, 156 clusters, exclusions 336; Holm not significant on both co-primary endpoints; V3 outputs preserved untouched.
- Registry sha256 `d5b299bf…` unchanged; universe frontier sha256 `e8826caf…` unchanged.
- Venv: `.venv`, python 3.12.3, numpy 2.5.4, pandas 3.1.1, scipy 1.18.1, statsmodels 0.15.0, pytest 9.2.0.
- No new `durable_state_upkeep` artifact (activation 2938 was tooling/analysis only); no frozen artifact modified; no commit.

## Known blockers still open (do not re-probe every activation)
- Raw ingestion snapshots absent from the repo → re-ingestion not reproducible; only derived data.
- Contract listing/delisting/migration history: unresolved.
- Data revision behavior: unresolved.
