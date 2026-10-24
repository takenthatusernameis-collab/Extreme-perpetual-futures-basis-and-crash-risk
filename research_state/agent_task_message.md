# Next task — EBCR-001

Read AGENTS.md, SKILLS.md, research_state/agent_handoff.md, prompts/continuous_research_operating_contract_v1.md, docs/research_protocol.md, configs/basis_crash_grid_v1.json.

## Immediate deliverables
1. Build grid execution scaffold mapping research_state/integrated_q1.json rows to preregistered cells (crash frequency/severity) per frozen config; write research_state/grid_execution_scaffold_v1.json with cell-to-slice mapping, counts, hashes. Do not change frozen config.
2. Execute grid cells for Q1 cohort against preregistered endpoints; record terminal status (ok/blocked/failed/incomplete/invalid/not_run) with reason and artifact path for every cell; apply correction across full 324-cell family.
3. Run required checks and update handoff/next task with concrete numbers.

## Boundary
Free public data only. No REST (Binance). No fabrication. Preserve null/failed/exclusions. Complete horizons only. Do not inspect holdout/sealed splits. Apply correction across full family. Never select by raw p-value.

## Commands
python3 scripts/generate_grid_manifest.py --output /tmp/basis-grid-manifest.json
python3 -m unittest discover -s tests -q
git diff --check