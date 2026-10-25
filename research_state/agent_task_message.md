# Agent task message (activation 122)

## Prior task (from handoff activation 121)
1. Re-run required checks to confirm clean state (manifest via `scripts/generate_grid_manifest.py --output /tmp/basis-grid-manifest.json`, config_sha256=55caedf84ac723289f70f49bbed4712c8195425feb4a95e737f3e8929479a0e0 matches frozen config; `python3 -m pytest -q tests`; `git diff --check` clean; `git status --short` empty).
2. Maintain null/exclusions (336); preserve registered_secondary_not_tested status for H002/H003; preserve anchor null (adj p 0.248/0.949).
3. PIT rank inquiry closed -- do not reopen unless genuinely new free PIT rank source (no key/auth/paid) is located.
4. No preregistration from grid hits (requires new experiment ID + independent predeclared rationale + new anchor/config). Do not modify frozen anchor/config/Q1/extended artifacts.
5. Leakage audit complete: `research_state/leakage_audit_extended_v1.json` + `.md` (past-only True, forward-only True, permutation p=0.738/0.986 consistent with null, placebo negative = no leakage).
6. Update handoff and this task message with verified findings only. A concrete next task must always remain.

## What was done (activation 121)
- Required checks re-run and pass: grid manifest regenerated (324 cells, config_sha256=55caedf84ac723289f70f49bbed4712c8195425feb4a95e737f3e8929479a0e0 matches frozen config); `python3 -m pytest -q tests` (11 tests, OK); `git diff --check` clean; `git status --short` empty.
- Clean state confirmed; frozen anchor/config/Q1/extended artifacts untouched.
- Permutation/placebo leakage audit completed and written to `research_state/leakage_audit_extended_v1.json` + `.md` (EBCR-001-LEAKAGE-AUDIT-EXTENDED-V1).
  - Structural: past-only signal True (rolling quantile shift(1)); forward-only labels True (MAE_h uses t+1..t+h lows / close_t).
  - Permutation (2000 block permutations, 56-day blocks): empirical p risk_difference=0.738, es_difference=0.986 -> consistent with null (no look-ahead).
  - Temporal placebo (signal at t vs crashes at t-7/t-14/t-28): all negative (RD ≈ -0.10 to -0.14, p<1e-6), opposite direction of leakage; consistent with serial regime correlation, not look-ahead bias.
  - Verdict: no structural leakage detected; forward association not stronger than chance alignment.
- H002/H003 remain registered_secondary_not_tested; PIT rank inquiry closed (coverage-cohort, rank_verified=false for all 13); no new free PIT rank source.
- Anchor null preserved (adj p 0.248/0.949); exclusions 336 preserved (missing_label); 324 cells ok.
- Reporting only verified findings. No frozen artifacts modified. No preregistration from grid hits.
- Durable-state inconsistency still flagged (NOT modified): `research_state/hypothesis_registry.json` records EBCR-H001 as `preregistered_not_tested` with `outcome_summary: null` despite extended evaluation (EBCR-GRID-001-0005) testing that anchor and recording null (adj p 0.248/0.949).

## Durable state (verified)
- Frozen config: configs/basis_crash_grid_v1.json (canonical-JSON sha256=55caedf84ac723289f70f49bbed4712c8195425feb4a95e737f3e8929479a0e0, verified). Anchor EBCR-GRID-001-0005 null preserved (co-primary adj p 0.248/0.949). Exclusions 336 (missing_label). 324 cells ok.
- Leakage audit: EBCR-001-LEAKAGE-AUDIT-EXTENDED-V1 complete (no structural leakage; permutation consistent with null; placebo negative).
- PIT: coverage-cohort; rank_verified=false for all 13; inquiry closed; no new free PIT rank source.
- Hypotheses: H001 preregistered_not_tested (registry stale — see flagged inconsistency); H002/H003 registered_secondary_not_tested.
- Evaluation artifacts consistent (extended complete); no unaddressed gaps except registry inconsistency.

## Next concrete task (for activation 122)
1. Re-run required checks to confirm clean state (manifest via `scripts/generate_grid_manifest.py --output /tmp/basis-grid-manifest.json`, config_sha256 matches frozen config; `python3 -m pytest -q tests`; `git diff --check` clean; `git status --short` empty).
2. Maintain null/exclusions (336); preserve registered_secondary_not_tested status for H002/H003; preserve anchor null (adj p 0.248/0.949).
3. PIT rank inquiry closed -- do not reopen unless genuinely new free PIT rank source (no key/auth/paid) is located.
4. No preregistration from grid hits (requires new experiment ID + independent predeclared rationale + new anchor/config). Do not modify frozen anchor/config/Q1/extended artifacts.
5. **New task: reconcile `research_state/hypothesis_registry.json`**. EBCR-H001 still recorded as `preregistered_not_tested` with `outcome_summary: null`, yet the extended evaluation (EBCR-GRID-001-0005) tested exactly that anchor and recorded the null (adj p 0.248/0.949). Registry is not a frozen artifact. Update it to reflect the tested null outcome, preserving the prior value via a note/field rather than overwriting silently. The evaluation report remains the authoritative outcome record. Do not modify frozen artifacts.
6. Update handoff and this task message with verified findings only. A concrete next task must always remain.
