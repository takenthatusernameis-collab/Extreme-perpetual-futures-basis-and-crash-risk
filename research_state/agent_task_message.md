# Agent task message (activation 390)

## Prior task (from handoff activation 389)
1. Re-run required checks to confirm clean state: `python3 scripts/generate_grid_manifest.py --output /tmp/basis-grid-manifest.json`; `python3 -m unittest discover -s tests -q`; `git diff --check`; `git status --short`.
2. Maintain null/exclusions (336); preserve registered_secondary_not_tested status for H002/H003; preserve anchor null (adj p 0.248/0.949).
3. PIT rank inquiry CLOSED. Do not reopen unless genuinely new free PIT rank source.
4. No preregistration from grid hits. Do not modify frozen anchor/config/Q1/extended artifacts.
5. Continue durable-state upkeep — re-verify hypothesis registry consistency and re-review the on-disk audits for any new unaddressed items; document findings only if gaps found, else record explicit "no_gaps_found" artifact (new version suffix v256) at research_state/durable_state_upkeep_v256.json.
6. PIT rank evidence: durable record is research_state/pit_rank_verification_v1.json (the /tmp extraction dir is not persistent across hosts).
7. Report only verified findings; do not commit changes unless explicitly asked.

## What was done (activation 389)
- Required checks re-run and pass: grid manifest regenerated to /tmp/basis-grid-manifest.json (324 cells, config_sha256 matches frozen canonical 55caedf8...); 11 unittest tests OK; git diff --check clean; git status clean.
- Durable-state claims re-verified programmatically (hypothesis registry: H001 tested_not_supported, H002/H003 registered_secondary_not_tested, next_hypothesis_sequence 4; anchor null preserved; exclusions 336 preserved).
- Audits reviewed: evaluation_artifact_audit_v1.md, evaluation_ledger_consistency_audit_v1.md, leakage_audit_extended_v1.md, red_team_audit_extended_v1.md — no gaps found.
- Durable-state upkeep v256 created (verdict: no_gaps_found). Artifact: research_state/durable_state_upkeep_v256.json.
- No frozen artifacts modified. No preregistration from grid hits. PIT remains CLOSED.

## Durable state (verified after activation 389)
- Frozen config canonical sha256 55caedf8... (grid manifest) / 753d9357... (ledger/eval/config file). Anchor null preserved (adj p 0.24830545694889028 / 0.9485). Exclusions 336 (reason: missing_label). 324 cells ok (0 non-ok).
- PIT: CLOSED (13 rank_verified of 13). Durable record: research_state/pit_rank_verification_v1.json.
- Hypotheses: H001 tested_not_supported; H002/H003 registered_secondary_not_tested. next_hypothesis_sequence=4.
- Latest durable-state upkeep: research_state/durable_state_upkeep_v256.json (verdict: no_gaps_found).

## Next concrete task (for activation 390)
1. Re-run required checks to confirm clean state: `python3 scripts/generate_grid_manifest.py --output /tmp/basis-grid-manifest.json`; `python3 -m unittest discover -s tests -q`; `git diff --check`; `git status --short`.
2. Maintain null/exclusions (336); preserve registered_secondary_not_tested status for H002/H003; preserve anchor null (adj p 0.248/0.949).
3. PIT rank inquiry CLOSED. Do not reopen unless genuinely new free PIT rank source.
4. No preregistration from grid hits. Do not modify frozen anchor/config/Q1/extended artifacts.
5. Continue durable-state upkeep — re-verify hypothesis registry consistency and re-review the on-disk audits for any new unaddressed items; document findings only if gaps found, else record explicit "no_gaps_found" artifact (new version suffix v257) at research_state/durable_state_upkeep_v257.json.
6. PIT rank evidence: durable record is research_state/pit_rank_verification_v1.json (the /tmp extraction dir is not persistent across hosts).
7. Report only verified findings; do not commit changes unless explicitly asked.

(End of file)
