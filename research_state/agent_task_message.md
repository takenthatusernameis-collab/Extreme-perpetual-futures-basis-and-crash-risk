# Next task — EBCR-001

Read AGENTS.md, SKILLS.md, research_state/agent_handoff.md, prompts/continuous_research_operating_contract_v1.md, docs/research_protocol.md, configs/basis_crash_grid_v1.json.

## Immediate deliverables
1. Apply Holm correction across all 2592 grid cell-endpoint tests (and anchor co-primary separately). Use integrated_extended_v1.json + cell_status_ledger_extended_v1.json.
2. Generate evaluation report with point estimates, intervals, event counts, exclusions, and stratified results; do not select by raw p-value.
3. Update handoff and this task with concrete eligible-row counts (5010 rows, 336 exclusions) and correction summary.

## Boundary
Free public data only. No fabrication. Preserve null/failed/exclusions. Complete horizons only. Do not modify Q1 artifacts.

## Commands
python3 scripts/generate_grid_manifest.py --output /tmp/basis-grid-manifest.json
python3 -m unittest discover -s tests -q
git diff --check
