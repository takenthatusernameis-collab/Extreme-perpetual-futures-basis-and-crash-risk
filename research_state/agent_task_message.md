# Next task — EBCR-001

Read AGENTS.md, SKILLS.md, research_state/agent_handoff.md, prompts/continuous_research_operating_contract_v1.md, docs/research_protocol.md, configs/basis_crash_grid_v1.json.

## Context
- Extended evaluation complete: anchor null (adj p 0.248, 0.949), 424/2451 Holm-significant with dependence caveats.
- Red-team audit done: research_state/red_team_audit_extended_v1.json (+md).
- Negative results report: research_state/negative_results_report_v1.json (+md).
- PIT verification added: research_state/pit_universe_verification_v1.json (listing evidence collected; rank unverified).
- Prior-only controls (exploratory): research_state/robustness_prior_controls_extended_v1.json (+md) — null preserved, no anchor change.
- Exclusions 336 preserved; all 324 cells ok.

## Immediate deliverables
1. Monitor for free PIT rank sources (e.g. archived listings/snapshots) without fabricating history; if found, record sources/timestamps/checksums and update verification.
2. If any predeclared alternative orientation needs investigation, preregister separately with own anchor (do not touch frozen anchor/config). Document rationale.
3. Update handoff/next task with concrete findings; preserve all null/failed/exclusions.

## Boundary
Free public data only. No fabrication. Preserve null/failed/exclusions. Complete horizons only. Do not modify Q1 artifacts, evaluation reports, or the frozen anchor/config.

## Commands
python3 scripts/generate_grid_manifest.py --output /tmp/basis-grid-manifest.json
python3 -m unittest discover -s tests -q
git diff --check
