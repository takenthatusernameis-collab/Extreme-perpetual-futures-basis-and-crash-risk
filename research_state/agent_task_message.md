# Next task — EBCR-001

Read AGENTS.md, SKILLS.md, research_state/agent_handoff.md, prompts/continuous_research_operating_contract_v1.json (or .md), docs/research_protocol.md, configs/basis_crash_grid_v1.json.

## Immediate deliverables
1. Build integrated dataset (basis + crash labels) joining research_state/basis_computation_q1_all.json with research_state/crash_labels_q1.json on (symbol,date); write research_state/integrated_q1.json with schema, row counts, hashes, and any join exclusions (must be zero).
2. Prepare analysis scaffold for grid execution against preregistered endpoints (crash frequency/severity) for Q1 cohort; record mapping from grid cells to dataset slices without changing frozen config.
3. Run required checks and update handoff/next task with concrete numbers (rows, coverage, exclusions).

## Boundary
Free public data only. No REST (Binance). No fabrication. Preserve null/failed/exclusions. Complete horizons only. Do not inspect holdout/sealed splits. Apply correction across full family.

## Commands
python3 -m pytest -q tests 2>&1 | tail -5
python3 scripts/generate_grid_manifest.py --output /tmp/basis-grid-manifest.json
git diff --check
