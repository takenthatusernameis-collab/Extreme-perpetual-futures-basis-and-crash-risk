# Next task — EBCR-001

Read AGENTS.md, SKILLS.md, research_state/agent_handoff.md, prompts/continuous_research_operating_contract_v1.md, docs/research_protocol.md, configs/basis_crash_grid_v1.json.

## Immediate deliverables
1. Acquire pre-window daily basis history (free public source only) for the 11 integrated symbols covering at least 365 days before 2024-01-01, plus forward extension through at least 2024-04-28; update ingestion + data coverage ledger under a new experiment ID/path without modifying Q1 artifacts.
2. Recompute basis and crash labels on the extended window and rebuild the integrated dataset; rerun scripts/execute_grid_q1.py (or successor) and record terminal statuses for all 324 cells.
3. Run required checks and update handoff/next task with concrete eligible-row counts.

## Boundary
Free public data only. No REST (Binance). No fabrication. Preserve null/failed/exclusions. Complete horizons only. Do not inspect holdout/sealed splits. Apply correction across full family. Never select by raw p-value.

## Commands
python3 scripts/generate_grid_manifest.py --output /tmp/basis-grid-manifest.json
python3 -m unittest discover -s tests -q
git diff --check
"""