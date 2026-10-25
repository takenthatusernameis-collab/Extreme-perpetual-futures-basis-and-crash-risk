# Initial task message — EBCR-001 (activation 19 successor)

Read AGENTS.md, SKILLS.md, research_state/agent_task_message.md, research_state/agent_handoff.md, prompts/continuous_research_operating_contract_v1.md, docs/research_protocol.md, configs/basis_crash_grid_v1.json.

## What was done this activation (activation 19)
- Required checks re-run and pass: grid manifest regenerated via `scripts/generate_grid_manifest.py --output /tmp/basis-grid-manifest.json` → 324 cells, config_sha256=55caedf84ac723289f70f49bbed4712c8195425feb4a95e737f3e8929479a0e0; 11 unittest tests pass (`python3 -m unittest discover -s tests`); `git diff --check` clean.
- Bounded prior-only controls robustness on fixed anchor completed with new experiment ID EBCR-001-ROBUST-PRIOR-V2 (artifacts: research_state/robustness_prior_controls_extended_v2.json + .md). Controls lagged (no forward fill), no anchor/config change, no holdout unblinding/parameter search. Exclusions preserved (336). Anchor co-primary uncontrolled: crash_incidence_15pct rd +0.0365 (p_fisher 0.123), expected_shortfall_5pct_forward_mae diff +0.00123 — null preserved.
- PIT rank line of inquiry closed (coverage-cohort, rank_verified=false for all 13). H002/H003 remain registered_secondary_not_tested; no preregistration from grid hits.
- No frozen anchor/config/Q1/extended artifacts modified.

## Verified state
- Anchor null preserved (prior eval adj p 0.248 / 0.949; v2 uncontrolled consistent).
- 324 cells ok; exclusions 336 (missing_label). PIT listing_verified true for 13/13, rank_verified false for all 13.
- H002/H003 registered_secondary_not_tested.

## Your task
1. Re-run required checks to confirm clean state: manifest, unittest, git diff --check. Do not modify frozen anchor/config or Q1/extended artifacts.
2. Maintain H002 (cheap_negative) and H003 (absolute_extreme) as registered_secondary_not_tested; do not preregister from grid hits.
3. Report only verified findings; preserve null result and exclusions (336). A concrete next task must always remain.
4. If a genuinely new free PIT rank source (no key, no auth, no paid plan) is located, reopen PIT rank inquiry with a new activation; otherwise universe remains rank-unverified/coverage-cohort.
5. **Next concrete task:** audit evaluation artifacts for completeness (cell status coverage, endpoint accounting, exclusion preservation) against the frozen grid manifest and integrated_extended_v1.json; write a short verification note to research_state/evaluation_artifact_audit_v1.md with checksums and pass/fail. Do not change any results/decisions. Preserve null and exclusions.

## Boundary
Free public data only. No fabrication. Preserve null/failed/exclusions. Complete horizons only.
