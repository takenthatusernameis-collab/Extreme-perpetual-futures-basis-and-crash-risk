# Agent task message (activation 121)

## Prior task (from handoff activation 120)
1. Re-run required checks to confirm clean state (manifest via `scripts/generate_grid_manifest.py --output /tmp/basis-grid-manifest.json`, config_sha256=55caedf84ac723289f70f49bbed4712c8195425feb4a95e737f3e8929479a0e0 matches frozen config; `python3 -m pytest -q tests`; `git diff --check` clean; `git status --short` empty).
2. Maintain null/exclusions (336); preserve registered_secondary_not_tested status for H002/H003; preserve anchor null (adj p 0.248/0.949).
3. PIT rank inquiry closed -- do not reopen unless genuinely new free PIT rank source (no key/auth/paid) is located.
4. No preregistration from grid hits (requires new experiment ID + independent predeclared rationale + new anchor/config). Do not modify frozen anchor/config/Q1/extended artifacts.
5. Update handoff and this task message with verified findings only. A concrete next task must always remain.

## What was done (activation 120)
- Required checks re-run and pass: grid manifest regenerated (324 cells, config_sha256=55caedf84ac723289f70f49bbed4712c8195425feb4a95e737f3e8929479a0e0 matches frozen config, independently re-verified via canonical-JSON sha256 with ensure_ascii=False); `python3 -m pytest -q tests` (11 tests, OK); `git diff --check` clean; `git status --short` empty.
- Clean state confirmed; frozen anchor/config/Q1/extended artifacts untouched (git status empty; no JSON/YAML changed).
- H002/H003 remain registered_secondary_not_tested; PIT rank inquiry closed (coverage-cohort, rank_verified=false for all 13); no new free PIT rank source located.
- Anchor null preserved (adj p 0.248/0.949); exclusions 336 preserved (missing_label); 324 cells ok.
- Reporting only verified findings. No frozen artifacts modified.
- Durable-state inconsistency flagged (NOT modified): `research_state/hypothesis_registry.json` still records EBCR-H001 as `preregistered_not_tested` with `outcome_summary: null`, yet the extended evaluation (EBCR-GRID-001-0005) tested exactly that anchor and recorded the null (adj p 0.248/0.949). Registry is not a frozen artifact, but editing it is a narrative decision left to the next agent; the evaluation report remains the authoritative outcome record.

## Durable state (verified)
- Frozen config: configs/basis_crash_grid_v1.json (canonical-JSON sha256=55caedf84ac723289f70f49bbed4712c8195425feb4a95e737f3e8929479a0e0, verified). Anchor EBCR-GRID-001-0005 null preserved (co-primary adj p 0.248/0.949). Exclusions 336 (missing_label). 324 cells ok.
- PIT: coverage-cohort; rank_verified=false for all 13; inquiry closed; no new free PIT rank source.
- Hypotheses: H001 preregistered_not_tested (registry stale — see flagged inconsistency); H002/H003 registered_secondary_not_tested.
- Evaluation artifacts consistent (extended complete); no unaddressed gaps.

## Next concrete task (for activation 121)
1. Re-run required checks to confirm clean state (manifest via `scripts/generate_grid_manifest.py --output /tmp/basis-grid-manifest.json`, config_sha256 matches frozen config; `python3 -m pytest -q tests`; `git diff --check` clean; `git status --short` empty).
2. Maintain null/exclusions (336); preserve registered_secondary_not_tested status for H002/H003; preserve anchor null (adj p 0.248/0.949).
3. PIT rank inquiry closed -- do not reopen unless genuinely new free PIT rank source (no key/auth/paid) is located.
4. No preregistration from grid hits (requires new experiment ID + independent predeclared rationale + new anchor/config). Do not modify frozen anchor/config/Q1/extended artifacts.
5. **New task: run the permutation/placebo leakage audit.** This is explicitly flagged as unblocked and outstanding in `research_state/red_team_audit_extended_v1.md` ("No leakage check performed here. ... a permutation/placebo audit is the next unblocked task") and `research_state/evaluation_summary_extended_v1.md` (caveat #2). Thresholds are past-only by design (rolling(...).shift(1); labels start t+1), so the audit is a verification, not a redesign. Write results to a new artifact under research_state/ with a new version suffix (e.g. `research_state/leakage_audit_extended_v1.json` + `.md`); do not modify the red-team audit or evaluation report.
6. Update handoff and this task message with verified findings only. A concrete next task must always remain.