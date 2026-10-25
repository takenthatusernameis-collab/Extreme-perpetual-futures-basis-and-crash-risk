# Durable-state upkeep (EBCR-001-DURABLE-STATE-UPKEEP-V1) — activation 133

- Generated: 2026-10-25T14:20:20Z
- Frozen config: configs/basis_crash_grid_v1.json (sha256 55caedf84ac723289f70f49bbed4712c8195425feb4a95e737f3e8929479a0e0) — matches frozen config; not modified.

## Required checks (all pass)
- Grid manifest regenerated: 324 cells, /tmp/basis-grid-manifest.json, config_sha256 matches frozen config.
- `python3 -m pytest -q tests`: 11 passed.
- `git diff --check`: clean. `git status --short`: empty (no changes before this activation's artifacts).

## Hypothesis registry consistency (verified post-reconciliation)
Registry file: research_state/hypothesis_registry.json. Authoritative outcome record: research_state/evaluation_report_extended_v1.json. No discrepancies found.

- EBCR-H001: status `tested_not_supported`; prior_status `preregistered_not_tested` preserved; anchor_cell_id EBCR-GRID-001-0005; experiment_id EBCR-001-EXTENDED-V1; grid_id EBCR-GRID-001; verdict `null_preserved_not_significant`; co-primaries crash_incidence_15pct adj p 0.24830545694889028 (not significant), expected_shortfall_5pct_forward_mae adj p 0.9485 (not significant). Reconciliation block present (activation 122). Registry matches evaluation report. No gaps.
- EBCR-H002: status `registered_secondary_not_tested`; outcome_summary null; not preregistered from grid hits. No gaps.
- EBCR-H003: status `registered_secondary_not_tested`; outcome_summary null; not preregistered from grid hits. No gaps.

## Red-team audit review (no unaddressed gaps)
File: research_state/red_team_audit_extended_v1.json + .md. Sections reviewed: leakage/permutation/placebo; overlapping horizons & dependence; survivorship/missingness/selection; confounding vs prior-only controls; multiplicity (full family); anchor co-primary.

- Leakage/permutation/placebo: all structural checks true; no structural leakage detected.
- Overlapping horizons: caveat noted (Holm controls FWER but not dependence-induced correlation).
- Survivorship/missingness: exclusions 336 preserved (missing_label); PIT ranks verified=true for all 13 coverage-cohort symbols via free Wayback-CMC snapshots; residual missingness recorded and preserved.
- Confounding: predeclared controls listed; follow-up recommendation (stratified/regression with controls) noted, not a gap requiring modification.
- Multiplicity: 2592 registered; 2451 with p-values; 141 blocked; Holm-significant 424/2451.
- Anchor co-primary: not significant after correction (adj p 0.248/0.949). Null preserved.

Verdict: no gaps found. No modifications to registry, red-team audit, or frozen artifacts.

## Preserved state
- Exclusions: 336 (missing_label); preserved.
- Cells ok: 324.
- Anchor null preserved (adj p 0.248/0.949).
- PIT rank inquiry: CLOSED (verified free Wayback-CMC source, no key/auth/paid); extraction record preserved at /tmp/pit_rank_evidence/.
- H002/H003: registered_secondary_not_tested.
- No preregistration from grid hits; no frozen anchor/config/Q1/extended artifacts modified.
