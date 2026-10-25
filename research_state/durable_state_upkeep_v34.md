# Durable state upkeep v34 (activation 166)

## Required checks
- Grid manifest regenerated via scripts/generate_grid_manifest.py --output /tmp/basis-grid-manifest.json: 324 cells, config_sha256 55caedf84ac723289f70f49bbed4712c8195425feb4a95e737f3e8929479a0e0 (matches frozen canonical)
- python3 -m pytest -q tests: 11 passed
- git diff --check: clean
- git status --short: only intended research_state changes

## Verifications
- Hypothesis registry: H001 tested_not_supported (matches anchor EBCR-GRID-001-0005 adj p 0.24830545694889028/0.9485; matches evaluation_report_extended_v1.json, leakage_audit_extended_v1.json, red_team_audit_extended_v1.json). H002/H003 registered_secondary_not_tested. No changes.
- Audits reviewed (red_team_audit_extended_v1, leakage_audit_extended_v1, evaluation_ledger_consistency_audit_v1): no new unaddressed gaps.
- Prior upkeep v33 reviewed as reference (verdict no_gaps_found).

## Preservations
- Frozen anchor/config/Q1/extended artifacts untouched
- Anchor null preserved (adj p 0.248305/0.9485)
- Exclusions 336 preserved
- H002/H003 registered_secondary_not_tested preserved
- PIT rank inquiry CLOSED (durable: research_state/pit_rank_verification_v1.json)

## Outcome
- Verdict: no_gaps_found (no new gaps). No preregistration from grid hits. No registry/audit/frozen-artifact modifications.
