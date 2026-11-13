# Agent task message (EBCR-001) — activation 2938 (written at end of activation 2937)

## Read first (required)
- `research_state/agent_handoff.md` (activation 2937 completed — BLOCKER RESOLVED + REPRODUCTION VERIFIED; artifacts `research_state/repro_verification_v982.json`, `research_state/evaluation_report_repro_v982.json`, commit still `76256d1` + operational checkpoints)
- `research_state/agent_task_message.md` (previous task message)
- `prompts/continuous_research_operating_contract_v1.md` and `prompts/continuous_research_operating_contract_v1_1_addendum.md`
- `docs/research_protocol.md`
- `configs/basis_crash_grid_v1.json` (frozen)

## What changed since the previous activation
1. **The runtime analysis stack is now available.** A free-OSS venv exists at `.venv` (gitignored) with python 3.12.3, numpy 2.5.4, pandas 3.1.1, scipy 1.18.1, pytest 9.2.0. PyPI is reachable. Use `.venv/bin/python` as the analysis interpreter; do not reinstall unless it is gone.
2. **The frozen extended evaluation was reproduced exactly.** `scripts/evaluate_grid_extended.py` re-run on `research_state/integrated_extended_v1.json` into a NEW path produced a report whose 324 cells are identical to `research_state/evaluation_report_extended_v1.json` (identical canonical sha256 excluding `generated_at_utc` = `abc3dfe418fdc09a5483f0c56d3f7579b20f94ab20d61b6eebfd5a2b9d817aac`). Anchor co-primary adj p: crash_incidence_15pct 0.24830545694889028; expected_shortfall_5pct_forward_mae 0.9485. Full required gates pass: manifest 324 cells/canonical `55caedf…`, `pytest -q tests` 18 passed.
3. **New constraint:** raw per-timestamp ingestion snapshots are not in-repo (`data/raw/` gitignored), so re-ingestion is NOT reproducible. Only the derived `integrated_extended_v1.json` (5010 rows, 336 exclusions) is reproducible.

## Objective (activation 2938)
Advance the highest-value genuinely unblocked work now that the stack works. Do not manufacture work, do not re-run the already-reproduced frozen evaluation for a third time, and do not touch frozen artifacts. Expect at least one real, verifiable deliverable or an explicit, documented blocker.

## Required actions (activation 2938)
1. **State-change gate first** (cheap): compare code/test/config/grid/source/registry/frontier/audit identities against `research_state/durable_state_upkeep_v981.json` / commit `76256d1`, and note that the environment change (venv + repro artifacts) is already recorded in `repro_verification_v982.json`. Verify frozen config literal sha256 `753d9357e1d535ef4229a901e25ef059a751e4c4d56188247f5f2e0ef1debd16` and canonical `55caedf84ac723289f70f49bbed4712c8195425feb4a95e737f3e8929479a0e0`. Do not rerun the full gate if nothing changed.
2. **Pick ONE unblocked task and preregister it before computing outcomes:**
   - **(A) EBCR-H004 controlled re-estimation (highest value).** The control set is already preregistered in `research_state/hypothesis_registry.json` (`control_specification`: past 7/30-day returns, 30-day volatility/drawdown, BTC/market return+vol, funding, liquidity/turnover, open interest when reliable; covariates must be known at formation t, no forward fill). What is missing is implementation: `scripts/robustness_prior_controls_v2.py` computes only `uncontrolled`. **Write the model form down in a new preregistration artifact BEFORE running it** (e.g. a new experiment ID `EBCR-001-ROBUST-CTRL-V3` with explicit estimator, covariate list, missing-data handling, inference/cluster approach and co-primary Holm handling). Then implement in a NEW script or a new output path; never overwrite `research_state/robustness_prior_controls_extended_v2.json` or the frozen evaluation.
   - **(B) EBCR-H002 / EBCR-H003.** Still require a NEW experiment ID + independent preregistered rationale + a NEW anchor/config, because the fixed grid already covers those orientations on the inspected window (double-dipping risk). See `research_state/h002_h003_feasibility_v1.md`. Do not re-use the anchor.
   - **(C) Evidence audit.** Audit the derived artifacts (`integrated_extended_v1.json`, `basis_computation_extended_v1.json`, `crash_labels_extended_v1.json`) for undocumented assumptions, coverage/missingness and exclusion accounting, and record findings in `research_state/audit/` (directory currently absent). This does not contaminate frozen evidence.
3. **Preserve invariants:** exclusions n=336; anchor null (crash_incidence_15pct adj p 0.24830545694889028; expected_shortfall_5pct_forward_mae adj p 0.9485); PIT rank CLOSED; EBCR-H001 `tested_not_supported`; EBCR-H002/H003/H004 `registered_secondary_not_tested`; `next_hypothesis_sequence` 5. No preregistration derived from inspected grid hits; no frozen artifact edits; apply Holm across the complete registered family; preserve null/contradictory/failed evidence.
4. **Do not repeat already-completed work:** the extended evaluation reproduction (activation 2937) is done; do not re-run it unless an input changes.
5. **Report only verified findings.** Do not commit unless explicitly asked. Update this handoff and write the next task message.

## Verified baseline (activation 2937, 2026-11-13)
- State-change gate: research-material diff vs `76256d1` empty; no research-material commits; `git diff --check` clean; untracked = only the two new `research_state/` repro files.
- Frozen config hashes match; manifest 324 cells; anchor rich_positive/1d/90d/q0.95/14d; config immutable (`8b53966b`).
- Venv: `.venv`, python 3.12.3, numpy 2.5.4, pandas 3.1.1, scipy 1.18.1, pytest 9.2.0.
- Repro: `.venv/bin/python scripts/evaluate_grid_extended.py --report-out research_state/evaluation_report_repro_v982.json` → cells=324, tests=2592, with_p=2451, blocked_no_p=141, family Holm significant=424; cells identical to frozen report.
- Gates: manifest canonical `55caedf…` matches; `pytest -q tests` → 18 passed.
- Registry: `research_state/hypothesis_registry.json` sha256 `d5b299bf…` unchanged; universe frontier `research_state/universe_frontier.json` sha256 `e8826caf…` unchanged.
- No new `durable_state_upkeep` artifact (environment/tooling-only change); no frozen artifact modified; no commit.

## Known blockers still open (do not re-probe every activation)
- Raw ingestion snapshots absent from the repo → re-ingestion not reproducible; only derived data.
- Contract listing/delisting/migration history: unresolved.
- Data revision behavior: unresolved.
- `scripts/robustness_prior_controls_v2.py` controlled step unimplemented (now actionable under task A).