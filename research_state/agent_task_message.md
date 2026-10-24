# Next task — EBCR-001

Read AGENTS.md, SKILLS.md, research_state/agent_handoff.md, prompts/continuous_research_operating_contract_v1.md, docs/research_protocol.md, configs/basis_crash_grid_v1.json.

## Context
- Extended evaluation complete: anchor null (adj p 0.248, 0.949), 424/2451 Holm-significant with dependence caveats.
- Red-team audit done; negative results report done.
- PIT verification: listing evidence collected via S3 XML; rank_verified=false for all (no free PIT rank history found). research_state/pit_universe_verification_v1.json.
- Prior-only controls (exploratory): null preserved.
- Exclusions 336 preserved; all 324 cells ok.

## Immediate deliverables
1. Continue PIT hardening: search free sources (archived rankings, snapshot datasets) for defensible PIT rank history. If found, record source/timestamp/checksum and update verification; else document explicit gaps and keep rank-unverified.
2. If investigating alternative orientation (cheap-negative/absolute-extreme), preregister separately with its own anchor/config (do not modify frozen anchor/config). Document rationale.
3. Update handoff/next task with verified findings only; preserve null/failed/exclusions.

## Boundary
Free public data only. No fabrication. Preserve null/failed/exclusions. Complete horizons only. Do not modify Q1 artifacts, evaluation reports, or the frozen anchor/config.

## Commands
python3 scripts/generate_grid_manifest.py --output /tmp/basis-grid-manifest.json
python3 -m unittest discover -s tests -q
git diff --check
