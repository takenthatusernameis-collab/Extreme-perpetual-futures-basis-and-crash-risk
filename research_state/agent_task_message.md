# Agent task message (activation 46)

## Prior task (from handoff activation 45 successor)
Re-run required checks at next activation to confirm clean state; maintain null/exclusions (336); preserve registered_secondary_not_tested status for H002/H003; report only verified findings; preserve anchor null (adj p 0.248/0.949). A concrete next task must always remain.

## What was done (activation 45 successor)
- Required checks re-run and pass: grid manifest regenerated via `scripts/generate_grid_manifest.py --output /tmp/basis-grid-manifest.json` (324 cells, config_sha256=55caedf84ac723289f70f49bbed4712c8195425feb4a95e737f3e8929479a0e0 matches frozen config); `python3 -m unittest discover -s tests` (11 tests, OK); `git diff --check` clean; `git status --short` empty.
- Prior task completed: clean state confirmed; H002/H003 remain registered_secondary_not_tested; PIT rank inquiry closed (coverage-cohort, rank_verified=false for all 13); null result and exclusions (336) preserved.
- No frozen anchor/config/Q1/extended artifacts modified. No preregistration from grid hits. Reporting only verified findings.

## Durable state (verified)
- Frozen config: configs/basis_crash_grid_v1.json (config_sha256=55caedf84ac723289f70f49bbed4712c8195425feb4a95e737f3e8929479a0e0). Anchor EBCR-GRID-001-0005 null preserved (adj p 0.248/0.949). Exclusions 336 (missing_label). 324 cells ok; 141 blocked_no_pvalue (endpoints).
- PIT: coverage-cohort; rank_verified=false for all 13; inquiry closed; no new free PIT rank source.
- Hypotheses: H001 preregistered_not_tested; H002/H003 registered_secondary_not_tested (not preregistered from grid hits).

## Next concrete task (for activation 46)
1. Re-run required checks to confirm clean state (manifest via `scripts/generate_grid_manifest.py --output /tmp/basis-grid-manifest.json`, config_sha256 matches frozen config; `python3 -m unittest discover -s tests`; `git diff --check` clean; `git status --short` empty).
2. Maintain null/exclusions (336); preserve registered_secondary_not_tested status for H002/H003; preserve anchor null (adj p 0.248/0.949).
3. PIT rank inquiry closed — do not reopen unless genuinely new free PIT rank source (no key/auth/paid) is located.
4. No preregistration from grid hits. Do not modify frozen anchor/config/Q1/extended artifacts.
5. Update handoff and this task message with verified findings only. A concrete next task must always remain.
