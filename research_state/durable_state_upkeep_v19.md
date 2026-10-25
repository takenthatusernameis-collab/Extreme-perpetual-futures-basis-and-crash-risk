# Durable-state upkeep v19 (activation 151)

## Checks
- Grid manifest: `python3 scripts/generate_grid_manifest.py --output /tmp/basis-grid-manifest.json` → 324 cells, config_sha256_canonical 55caedf8... OK.
- Tests: `python3 -m pytest -q tests` → 11 passed OK.
- Git: `git diff --check` clean; `git status --short` clean of tracked changes OK.

## Hypothesis registry consistency
- EBCR-H001: tested_not_supported; matches anchor EBCR-GRID-001-0005 (co-primary adj p 0.248305/0.9485). OK.
- EBCR-H002/H003: registered_secondary_not_tested. OK.
- Gaps found: false.

## Red-team audit review
- Reviewed research_state/red_team_audit_extended_v1.md/json.
- PIT verification reflected (rank_verified=true for all 13). Exclusions 336 preserved. Multiplicity/dependence caveats present.
- Unaddressed gaps found: false.

## State preservation
- Frozen artifacts untouched (configs/basis_crash_grid_v1.json canonical 55caedf8..., anchor/Q1/extended unmodified).
- PIT CLOSED; /tmp/pit_rank_evidence/ preserved.
- Null preserved (adj p 0.248/0.949), exclusions 336, 324 cells ok.

## Verdict
no_gaps_found
