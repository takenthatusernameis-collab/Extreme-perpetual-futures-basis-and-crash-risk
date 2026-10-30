# Agent task message — EBCR-001 (activation 1103)

## Objective
Continue durable-state upkeep for EBCR-001. Do not reopen testing of H001 (tested_not_supported; null preserved). Keep secondary hypotheses untested. Preserve frozen artifacts and invariants.

## Required checks (must pass)
- `python3 scripts/generate_grid_manifest.py --output /tmp/basis-grid-manifest.json` (expect 324 cells, 324 unique hashes, config_sha256 matches frozen 55caedf84ac723289f70f49bbed4712c8195425feb4a95e737f3e8929479a0e0)
- `python3 -m unittest discover -s tests -q` (expect OK, 11 tests)
- `python3 -m pytest -q tests` (if available; otherwise record unavailable)
- `git diff --check` (clean)
- `git status --short` (clean)

## Invariants to preserve
- Anchor null: crash_incidence_15pct adj p 0.24830545694889028; expected_shortfall_5pct adj p 0.9485
- Exclusions: 336
- Hypothesis registry: H001 tested_not_supported; H002/H003/H004 registered_secondary_not_tested (next_seq 5)
- PIT rank: CLOSED (research_state/pit_rank_verification_v1.json). Do not reopen without genuinely new free PIT rank source.
- No preregistration from grid hits; do not modify frozen anchor/config/Q1/extended artifacts.

## Audits
Review on-disk audits for any new unaddressed items. Pre-existing UNRESOLVED preserved: Contract listing/delisting/migration history; Data revision behavior.

## Deliverables
1. Run required checks and record exact commands/results.
2. Re-verify hypothesis registry consistency.
3. If no gaps found, create `research_state/durable_state_upkeep_v970.json` with verdict `no_gaps_found` following the schema of prior upkeep artifacts (see research_state/durable_state_upkeep_v969.json). If gaps found, document explicitly with artifact paths and concrete next steps.
4. Update `research_state/agent_handoff.md` with activation 1103 summary and concrete Next action (activation 1104).
5. Report only verified findings; do not commit changes unless explicitly asked.
