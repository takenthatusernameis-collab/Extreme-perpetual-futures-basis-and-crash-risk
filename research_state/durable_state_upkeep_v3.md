# Durable state upkeep v3 (activation 135)

## Checks
- Grid manifest regenerated: 324 cells, config_sha256 55caedf84ac723289f70f49bbed4712c8195425feb4a95e737f3e8929479a0e0 (matches frozen; independently re-verified via canonical-JSON sha256 with ensure_ascii=False).
- Tests: `python3 -m pytest -q tests` -> 11 passed.
- `git diff --check`: clean (0).
- `git status --short`: clean (0) before this activation's artifacts.

## Hypothesis registry consistency
- EBCR-H001: tested_not_supported (prior_status preregistered_not_tested preserved). Anchor EBCR-GRID-001-0005 outcomes match (adj p 0.248305/0.9485). Evaluation report remains authoritative.
- EBCR-H002/H003: registered_secondary_not_tested (unchanged).
- Registry remains accurate post-reconciliation (activation 122). No registry modifications needed.

## Red-team audit review
- research_state/red_team_audit_extended_v1.json reviewed: all sections addressed. PIT verification reflected; leakage audit complete; confounding lists predeclared follow-up only; thin-tail and overlapping-horizon caveats recorded. No unaddressed gaps found. No new items since upkeep v2.

## State
- Frozen artifacts untouched. PIT rank inquiry CLOSED (verified free Wayback-CMC). Anchor null preserved; exclusions 336 preserved. No preregistration from grid hits.
- Verdict: no_gaps_found.
