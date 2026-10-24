# Next task — EBCR-001

Read AGENTS.md, SKILLS.md, research_state/agent_handoff.md, prompts/continuous_research_operating_contract_v1.md, docs/research_protocol.md, configs/basis_crash_grid_v1.json.

## Immediate deliverables
1. Complete ingestion: python3 scripts/ingest_extended_window.py (monitor; verify research_state/ingestion_extended_v1.json). Do not modify Q1 artifacts.
2. Run python3 scripts/compute_basis_extended.py, compute_crash_labels_extended.py, integrate_extended.py; then execute grid successor and record terminal statuses for all 324 cells.
3. Run required checks and update handoff/next task with concrete eligible-row counts.

## Boundary
Free public data only. No REST (Binance). No fabrication. Preserve null/failed/exclusions. Complete horizons only.

## Commands
python3 scripts/generate_grid_manifest.py --output /tmp/basis-grid-manifest.json
python3 -m unittest discover -s tests -q
git diff --check
