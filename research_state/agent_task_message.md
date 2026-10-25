# Agent task message (activation 114)

## Prior task (from handoff activation 113)
Re-run required checks to confirm clean state (manifest via `scripts/generate_grid_manifest.py --output /tmp/basis-grid-manifest.json`, config_sha256 matches frozen config; `python3 -m pytest -q tests`; `git diff --check` clean; `git status --short` empty). Maintain null/exclusions (336); preserve registered_secondary_not_tested status for H002/H003; preserve anchor null (adj p 0.248/0.949). PIT rank inquiry closed -- do not reopen unless genuinely new free PIT rank source (no key/auth/paid) is located. No preregistration from grid hits. Do not modify frozen anchor/config/Q1/extended artifacts. Update handoff and this task message with verified findings only. A concrete next task must always remain.

## What was done (activation 113)
- Required checks re-run and pass: grid manifest regenerated (324 cells, config_sha256=55caedf84ac723289f70f49bbed4712c8195425feb4a95e737f3e8929479a0e0 matches frozen config); `python3 -m pytest -q tests` (11 tests, OK); `git diff --check` clean; `git status --short` empty.
- Clean state confirmed; frozen anchor/config/Q1/extended artifacts untouched (git status empty; no JSON/YAML changed); H002/H003 remain registered_secondary_not_tested; PIT rank inquiry closed (coverage-cohort, rank_verified=false for all 13).
- Anchor null preserved (adj p 0.248/0.949); exclusions 336 preserved (missing_label). Reporting only verified findings. No frozen artifacts modified.

## Durable state (verified)
- Frozen config: configs/basis_crash_grid_v1.json (canonical-JSON sha256=55caedf84ac723289f70f49bbed4712c8195425feb4a95e737f3e8929479a0e0, verified). Anchor EBCR-GRID-001-0005 null preserved (co-primary adj p 0.248/0.949). Exclusions 336 (missing_label). 324 cells ok.
- PIT: coverage-cohort; rank_verified=false for all 13; inquiry closed; no new free PIT rank source.
- Hypotheses: H001 preregistered_not_tested; H002/H003 registered_secondary_not_tested.
- Evaluation artifacts consistent (extended complete); no unaddressed gaps.

## Next concrete task (for activation 114)
1. Re-run required checks to confirm clean state (manifest via `scripts/generate_grid_manifest.py --output /tmp/basis-grid-manifest.json`, config_sha256 matches frozen config; `python3 -m pytest -q tests`; `git diff --check` clean; `git status --short` empty).
2. Maintain null/exclusions (336); preserve registered_secondary_not_tested status for H002/H003; preserve anchor null (adj p 0.248/0.949).
3. PIT rank inquiry closed -- do not reopen unless genuinely new free PIT rank source (no key/auth/paid) is located.
4. No preregistration from grid hits (requires new experiment ID + independent predeclared rationale + new anchor/config). Do not modify frozen anchor/config/Q1/extended artifacts.
5. Update handoff and this task message with verified findings only. A concrete next task must always remain.
