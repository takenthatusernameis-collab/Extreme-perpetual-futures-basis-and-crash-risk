# Evaluation artifact audit — EBCR-001

Date (UTC): 2026-10-25T01:53:21Z
Experiment: EBCR-001 (extended window EBCR-001-EXTENDED-V1)

## Scope
Audit evaluation artifacts against the frozen grid manifest and integrated extended dataset. No results/decisions changed.

## Checks
- Frozen config sha256: 55caedf84ac723289f70f49bbed4712c8195425feb4a95e737f3e8929479a0e0 (matches configs/basis_crash_grid_v1.json).
- Grid manifest: 324 cells.
- evaluation_report_extended_v1.json: n_cells=324; all 324 cells present; all 324 cells have exactly 8 endpoints; cell IDs match manifest order; n_endpoints_per_cell=8; endpoints=8.
- Recorded exclusions: 336, reason missing_label (preserved).
- Anchor cell: EBCR-GRID-001-0005; co-primary endpoints crash_incidence_15pct, expected_shortfall_5pct_forward_mae; anchor null preserved (adj p 0.248 / 0.949).
- H002/H003 remain registered_secondary_not_tested; no preregistration from grid hits.
- PIT: listing_verified true for 13/13, rank_verified false for all 13 (coverage-cohort).

## Checksums (sha256)
- evaluation_report_extended_v1.json: 9487b36d08cad6eeb5b1af2a4748f959e6d0e47bd629024d4b29dbde60926cd4
- negative_results_report_v1.json: bbf8c0fd2e52d199b9718bed324588a297650c4065e3c685652c61e644b8f368
- red_team_audit_extended_v1.json: 9e2374dbbe9d9a09c1403559faf3a0afd9c8effbd840489aa37cd3ad5cfc83cc
- integrated_extended_v1.json: 28ec0163a95c857073c35c6d908fa2b62f9e1117d2e84b686150de02cce0fabf

## Result
PASS. No unaddressed data gaps; no silent data changes; null result and exclusions preserved.
