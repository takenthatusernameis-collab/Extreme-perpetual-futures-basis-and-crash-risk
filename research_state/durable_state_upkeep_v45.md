# Durable state upkeep v45 — EBCR-001 (activation 178)

## Required checks
- Grid manifest regenerated: 324 cells; config_sha256 matches frozen canonical 55caedf8...; `/tmp/basis-grid-manifest.json`.
- `python3 -m pytest -q tests`: 11 passed.
- `git diff --check`: clean.
- `git status --short`: only intended research_state changes (v45 artifacts).

## Verifications
- Hypothesis registry consistency re-verified (programmatic cross-check of hypothesis_registry.json vs evaluation_report_extended_v1.json): H001 tested_not_supported, anchor EBCR-GRID-001-0005, adj p crash_incidence_15pct=0.24830545694889028 / expected_shortfall_5pct_forward_mae=0.9485 — exact match with evaluation report inference.anchor_co_primary_adjusted_p_values and with red_team_audit_extended_v1 / leakage_audit_extended_v1. H002/H003 registered_secondary_not_tested with null outcome_summary. next_hypothesis_sequence=4. No changes made.
- Cell status ledger (cell_status_ledger_extended_v1.json) re-verified: 324 cells, all status `ok`, summary {ok:324, blocked:0, failed:0, incomplete:0, invalid:0, not_run:0}; matches evaluation report n_cells=324, n_registered_grid_tests=2592 (324×8), n_recorded_exclusions=336, family_tests_with_p_value=2451, family_tests_blocked_no_p=141.
- PIT rank verification (pit_rank_verification_v1.json) re-verified: 13 symbols, rank_verified=true for all.
- Red-team audit extended v1, leakage audit extended v1, evaluation-ledger consistency audit v1, evaluation_artifact_audit_v1, leakage_audit_verification_v1, robustness_prior_controls_extended_v2, h002_h003_feasibility_review_v1 and prior upkeep v44 re-reviewed: no new unaddressed gaps.

## Preservations
Anchor null preserved (adj p 0.248/0.949); exclusions 336 (missing_label); 324 cells ok; H002/H003 registered_secondary_not_tested; PIT CLOSED with durable record research_state/pit_rank_verification_v1.json; frozen anchor/config/Q1/extended artifacts untouched; candidate_perp_mapping_v1.json discovery state preserved (unverified mappings + explicit blockers).

## Outcome
Verdict: no_gaps_found. No preregistration from grid hits. No registry/audit/frozen-artifact modifications.

## Next concrete task
Continue durable-state upkeep — re-verify hypothesis registry consistency and re-review audits; document findings only if gaps found, else record explicit "no_gaps_found" artifact (v46). Update handoff and task message with verified findings only. A concrete next task must always remain.
