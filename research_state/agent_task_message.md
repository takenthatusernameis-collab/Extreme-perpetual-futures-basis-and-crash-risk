# Next task — EBCR-001

Read AGENTS.md, SKILLS.md, research_state/agent_handoff.md, prompts/continuous_research_operating_contract_v1.md, docs/research_protocol.md, configs/basis_crash_grid_v1.json.

## Immediate deliverables
1. Obtain spot/index daily data beyond 2024-03-31 (through at least 2024-04-28) for all 13 verified symbols to complete 28-day forward horizons for crash labels; use free public S3 data only.
2. Compute crash labels (MAE over 7/14/28d using spot/index lows) against research_state/basis_computation_q1_all.json; write research_state/crash_labels_q1.json with per-observation labels, only where full horizon available; log exclusions.
3. Verify coverage gate and horizon completeness; update handoff/next task with concrete numbers.

## Boundary
Free public data only. No REST (Binance). No fabrication. Preserve null/failed/exclusions. Complete horizons only.

## Commands
python3 -m pytest -q tests 2>&1 | tail -5
python3 scripts/generate_grid_manifest.py --output /tmp/basis-grid-manifest.json
git diff --check
