# Durable state upkeep v38 — EBCR-001

## Required checks (re-run, all pass)
- Grid manifest regenerated: `python3 scripts/generate_grid_manifest.py --output /tmp/basis-grid-manifest.json` → 324 cells; config_sha256=55caedf84ac723289f70f49bbed4712c8195425feb4a95e737f3e8929479a0e0 (matches frozen canonical).
- `python3 -m pytest -q tests` → 11 passed (pytest was not on PATH; installed to local user bin via `pip3 install pytest` and re-run).
- `git diff --check` → clean.
- `git status --short` → clean (no tracked changes).

## Verifications
- Hypothesis registry consistency re-verified programmatically: H001 tested_not_supported (prior_status preregistered_not_tested) matches anchor EBCR-GRID-001-0005; evaluation_report_extended_v1.json anchor cell endpoints carry anchor_co_primary_adjusted_p_value 0.24830545694889028 / 0.9485 with anchor_co_primary_significant=false and holm_significant=false — identical to registry and to red_team_audit_extended_v1.json / leakage_audit_extended_v1.json. H002 and H003 registered_secondary_not_tested with null outcome_summary. next_hypothesis_sequence=4. No changes made.
- Red-team audit (extended v1), leakage audit (extended v1) and evaluation-ledger consistency audit (v1) re-reviewed — no new unaddressed gaps identified. Confounding and thin-tail caveats are pre-existing, preserved-by-design items, not new gaps.
- Prior upkeep v37 reviewed as reference; verdict no_gaps_found.

## Preservations
- Frozen anchor/config/Q1/extended artifacts untouched.
- Anchor null preserved (adj p 0.248/0.949); exclusions 336 preserved; 324 cells ok.
- H002/H003 remain registered_secondary_not_tested; PIT rank inquiry CLOSED (verified free Wayback-CMC); durable record research_state/pit_rank_verification_v1.json.

## Outcome
- Verdict: no_gaps_found. No registry/audit/frozen-artifact modifications. No preregistration from grid hits.

## Next concrete task
Continue durable-state upkeep — re-verify hypothesis registry consistency and re-review the three audits for any new unaddressed items; document only if gaps found, else record explicit "no_gaps_found" artifact (new version suffix v39). Update handoff and task message with verified findings only.