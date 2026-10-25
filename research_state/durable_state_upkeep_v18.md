# Durable-state upkeep v18 (activation 150)

## Checks
- Grid manifest regenerated: 324 cells; config_sha256_canonical 55caedf84ac723289f70f49bbed4712c8195425feb4a95e737f3e8929479a0e0 (matches frozen).
- Tests: `python3 -m pytest -q tests` → 11 passed.
- git diff --check clean; git status --short clean of tracked changes.

## Hypothesis registry consistency
- EBCR-H001: tested_not_supported; matches anchor EBCR-GRID-001-0005 (adj p 0.24830545694889028 / 0.9485). OK.
- EBCR-H002/H003: registered_secondary_not_tested (preserved). OK.
- Gaps found: no.

## Red-team audit review
- Reviewed research_state/red_team_audit_extended_v1.json + .md. All sections addressed; PIT verification reflected. No unaddressed gaps found.

## Frozen artifacts / PIT / null
- configs/basis_crash_grid_v1.json and anchor/Q1/extended artifacts untouched.
- PIT CLOSED (Wayback-CMC), rank_verified_all_13 true; /tmp/pit_rank_evidence/ preserved.
- Anchor null preserved (adj p 0.248/0.949), exclusions 336, 324 cells ok.

## Verdict
no_gaps_found. No modifications to registry/red-team/frozen artifacts.
