# Durable-state upkeep — v32 (activation 164)

## Required checks (re-run, all pass)
- Grid manifest regenerated: 324 cells; config_sha256=55caedf84ac723289f70f49bbed4712c8195425feb4a95e737f3e8929479a0e0 (matches frozen canonical hash).
- `python3 -m pytest -q tests`: 11 passed.
- `git diff --check`: clean (0 issues).
- `git status --short`: clean of tracked changes.

## Hypothesis registry consistency (re-verified)
- H001 `tested_not_supported` matches anchor EBCR-GRID-001-0005 (adj p 0.24830545694889028 / 0.9485) and cross-matches evaluation_report_extended_v1.json, leakage_audit_extended_v1.json and red_team_audit_extended_v1.json.
- H002/H003 remain `registered_secondary_not_tested`.

## Audits re-reviewed (no new unaddressed gaps)
- red_team_audit_extended_v1: reviewed; no unaddressed gaps.
- leakage_audit_extended_v1: reviewed; no unaddressed gaps.
- evaluation_ledger_consistency_audit_v1: reviewed; counts match (324 cells x 8 endpoints = 2,592 tests; 2,451 with p; 141 blocked); no unaddressed gaps.

## Invariants preserved
- Null preserved (anchor adj p 0.248/0.949). Exclusions 336 preserved. 324 cells ok / 324 total.
- PIT CLOSED (verified free Wayback-CMC; durable record research_state/pit_rank_verification_v1.json).
- Frozen artifacts untouched (config raw sha256 753d9357..., canonical 55caedf8...).

## Verdict
no_gaps_found. No registry/red-team/frozen-artifact modifications. Artifact: research_state/durable_state_upkeep_v32.json + .md.

## Next action (activation 165)
Continue durable-state upkeep (v33): re-verify hypothesis registry consistency and re-review the three audits for new unaddressed items; record explicit "no gaps found" artifact if none. Maintain null/exclusions/H002-H003/PIT CLOSED. No preregistration from grid hits. Do not modify frozen artifacts.

(End of file)