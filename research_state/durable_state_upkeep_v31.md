# Durable state upkeep v31 (activation 163)

## Required checks (re-run)
- `python3 scripts/generate_grid_manifest.py --output /tmp/basis-grid-manifest.json` → generated 324 cells, config_sha256 55caedf84ac723289f70f49bbed4712c8195425feb4a95e737f3e8929479a0e0 (matches frozen)
- `python3 -m pytest -q tests` → 11 passed
- `git diff --check` → clean (0)
- `git status --short` → clean of tracked changes (0)

## Hypothesis registry consistency
- H001: tested_not_supported, anchor EBCR-GRID-001-0005 adj p 0.248305/0.9485, matches evaluation_report_extended_v1.json, leakage_audit_extended_v1.json, red_team_audit_extended_v1.json. ✓
- H002: registered_secondary_not_tested ✓
- H003: registered_secondary_not_tested ✓

## Audits reviewed
- Red-team audit extended v1: reviewed, no unaddressed gaps.
- Leakage audit extended v1: reviewed, no unaddressed gaps (leakage design verified; permutation consistent with null; placebos negative/opposite of leakage).
- Evaluation-ledger consistency audit v1: reviewed, counts match (324×8=2592, 2451 with p-value, 141 blocked), all cells ok. No unaddressed gaps.

## State invariants
- Anchor null preserved (adj p 0.248/0.949)
- Exclusions 336 preserved (missing_label)
- 324 cells ok, 0 terminal issues
- PIT rank inquiry CLOSED (durable record research_state/pit_rank_verification_v1.json, rank_verified all)
- Frozen artifacts unchanged (config/Q1/extended)

## Verdict
no_gaps_found

## Next concrete action
Continue durable-state upkeep (v32): re-verify hypothesis registry consistency and re-review red-team/leakage/ledger consistency audits for any new unaddressed items; document findings only if gaps found else record "no_gaps_found". Maintain null/exclusions/H002-H003/PIT CLOSED. No preregistration from grid hits. Do not modify frozen artifacts.
