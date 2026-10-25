# Durable-state upkeep v17 — EBCR-001 (activation 149)

## Checks (re-run)
- Grid manifest: `python3 scripts/generate_grid_manifest.py --output /tmp/basis-grid-manifest.json` → generated 324 cells; config_sha256_canonical 55caedf84ac723289f70f49bbed4712c8195425feb4a95e737f3e8929479a0e0 (matches frozen). OK.
- Tests: `python3 -m pytest -q tests` → 11 passed. OK.
- `git diff --check` clean. OK.
- `git status --short` clean of tracked changes. OK.

## Hypothesis registry consistency
- H001 (EBCR-H001): tested_not_supported; matches anchor EBCR-GRID-001-0005. Co-primary adj p: crash_incidence_15pct 0.24830545694889028, expected_shortfall_5pct_forward_mae 0.9485. OK.
- H002 (EBCR-H002): registered_secondary_not_tested. OK.
- H003 (EBCR-H003): registered_secondary_not_tested. OK.
- Verdict: no gaps found.

## Red-team audit review
- Reviewed: `research_state/red_team_audit_extended_v1.md`, `research_state/red_team_audit_extended_v1.json`.
- PIT verification reflected (rank_verified=true for all 13 via Wayback-CMC). Exclusions 336 (missing_label) preserved.
- Multiplicity/dependence caveats present; no new unaddressed items identified.
- Verdict: no unaddressed gaps found.

## Frozen artifacts / PIT / null
- Frozen config/anchor/Q1/extended: untouched.
- PIT rank inquiry: CLOSED (verified free Wayback-CMC). Extraction record preserved at `/tmp/pit_rank_evidence/`.
- Null preserved: anchor adj p [0.24830545694889028, 0.9485]; exclusions 336; 324 cells ok.

## Conclusion
Durable-state upkeep v17 complete. No gaps found; no modifications to hypothesis registry, red-team audit, or frozen artifacts. State remains clean and consistent.
