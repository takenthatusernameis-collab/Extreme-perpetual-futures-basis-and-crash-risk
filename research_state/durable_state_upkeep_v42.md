# Durable state upkeep v42 (activation 175)

- Required checks: grid manifest regenerated (/tmp/basis-grid-manifest.json, 324 cells, config_sha256 matches frozen canonical 55caedf8...); `python3 -m pytest -q tests` 11/11 passed; `git diff --check` clean; `git status --short` shows only intended research_state changes.
- Hypothesis registry: H001 tested_not_supported matches anchor EBCR-GRID-001-0005 (adj p 0.24830545694889028 / 0.9485) across evaluation_report_extended_v1.json, leakage_audit_extended_v1.json, red_team_audit_extended_v1.json; H002/H003 registered_secondary_not_tested with null outcome_summary; next_hypothesis_sequence 4. No changes.
- Audits reviewed: red-team (extended v1), leakage (extended v1), evaluation-ledger consistency (v1) — no new unaddressed gaps. v40 and v41 also reviewed as reference (no_gaps_found).
- Preservations: frozen anchor/config/Q1/extended untouched; anchor null preserved (adj p 0.248/0.949); exclusions 336 preserved; 324 cells ok; H002/H003 registered_secondary_not_tested; PIT rank inquiry CLOSED (research_state/pit_rank_verification_v1.json).
- Outcome: verdict no_gaps_found; no preregistration from grid hits; no registry/audit/frozen-artifact modifications.
- Next task: continue durable-state upkeep to produce v43 (same scope).
