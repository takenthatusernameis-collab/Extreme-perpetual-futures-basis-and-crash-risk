# Agent task message (EBCR-001) — activation 2941 (written at end of activation 2940)

## Read first (required)
- `research_state/agent_handoff.md` (activation 2940 completed — NO-OP; no research-material change since activation 2939)
- `research_state/agent_task_message.md` (previous task message)
- `prompts/continuous_research_operating_contract_v1.md` and `prompts/continuous_research_operating_contract_v1_1_addendum.md`
- `docs/research_protocol.md`
- `configs/basis_crash_grid_v1.json` (frozen)

## What changed since the previous activation
Nothing. Activation 2940 was a NO-OP: state-change gate passed (config literal sha256 `753d9357…` and canonical `55caedf…` verified; manifest 324 cells; pytest 18 passed; `git diff --check` clean; working tree clean, no untracked files), and there was no new source data, no dated research event, and no code/config/registry/audit change since activation 2939.

## Objective (activation 2941)
Advance the highest-value genuinely unblocked work. Do not manufacture work. Expect at least one real, verifiable deliverable or an explicit, documented blocker. If no state change has occurred since activation 2940 and there is no new admissible source or dated event, classify as NO-OP per the v1.1 addendum and exit with the previous verified state intact — do not refresh timestamps or create empty artifacts.

## Required actions (activation 2941)
1. **State-change gate first** (cheap): compare code/test/config/grid/source/registry/frontier/audit identities against `research_state/durable_state_upkeep_v981.json` / commit `76256d1`; verify frozen config literal sha256 `753d9357e1d535ef4229a901e25ef059a751e4c4d56188247f5f2e0ef1debd16` and canonical `55caedf84ac723289f70f49bbed4712c8195425feb4a95e737f3e8929479a0e0`. If nothing changed since activation 2940, NO-OP — skip steps 2–3.
2. **If state changed or an unblocked task exists, pick ONE:**
    - **Continue evidence audit (option C extension):** audit exclusion accounting (exclusions n=336) against `integrated_extended_v1.json` row counts; record findings in `research_state/audit/`. Other unresolved items: contract listing/delisting/migration history; data revision behavior.
    - **(B) EBCR-H002/H003:** still blocked — cannot preregister from inspected grid hits; requires new experiment ID + independent preregistered rationale + NEW anchor/config.
    - **(A) registry follow-up:** blocked — H004 status change requires a separate preregistration decision.
3. **Preserve invariants:** exclusions n=336; anchor null (crash_incidence_15pct adj p 0.24830545694889028; expected_shortfall_5pct_forward_mae adj p 0.9485); PIT rank CLOSED; EBCR-H001 `tested_not_supported`; EBCR-H002/H003/H004 `registered_secondary_not_tested`; `next_hypothesis_sequence` 5. No frozen artifact edits; no preregistration from grid hits; preserve null/contradictory/failed evidence (including V3's invalid claim as corrected evidence).
4. **Do not repeat already-completed work:** V4 controlled re-estimation (activation 2938) and V3→V4 evidence audit (activation 2939) are done; do not re-run unless an input changes.
5. **Report only verified findings.** Do not commit unless explicitly asked. Update this handoff and write the next task message.

## Verified baseline (activation 2940, 2026-11-13)
- State-change gate: config literal sha256 and canonical sha256 match frozen; manifest 324 cells; git diff --check clean; 18 pytest passed.
- V4 reproducibility confirmed: `robustness_controlled_v4.json` regenerates identically from `scripts/robustness_controlled_v4.py`; preregistration `h004_controlled_rereg_v2.json` sha256 `ef53d9f8…`.
- Audit artifact: `research_state/audit/v3_v4_inference_correction_audit_v1.md` — first in `research_state/audit/`; documents V3→V4 correction as red-team finding.
- Registry sha256 `d5b299bf…` unchanged; universe frontier sha256 `e8826caf…` unchanged.
- Venv: `.venv`, python 3.12.3, numpy 2.5.4, pandas 3.1.1, scipy 1.18.1, statsmodels 0.15.0, pytest 9.2.0.
- No new `durable_state_upkeep` artifact (activation 2940 was NO-OP); no frozen artifact modified; no commit.

## Known blockers still open (do not re-probe every activation)
- Raw ingestion snapshots absent from the repo → re-ingestion not reproducible; only derived data.
- Contract listing/delisting/migration history: unresolved.
- Data revision behavior: unresolved.
- EBCR-H002/H003: not testable without new preregistration independent of grid hits and NEW anchor/config.
