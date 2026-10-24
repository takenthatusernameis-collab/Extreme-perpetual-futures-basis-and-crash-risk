# Next task — EBCR-001

Read AGENTS.md, SKILLS.md, research_state/agent_handoff.md, prompts/continuous_research_operating_contract_v1.md, docs/research_protocol.md, configs/basis_crash_grid_v1.json.

## Immediate deliverables
1. Implement S3 directory listing parser for ETHUSDT mark/index to enumerate missing dates; update data_coverage_ledger.json.
2. Extend ingestion prototype to multi-day processing with >=95% coverage gate.
3. Map first 25 candidates to Binance perpetual symbols; record mapping/blocked status.
4. State updates: update handoff and next task.

## Boundary
Free public data only. No REST (Binance). No fabrication. Preserve null/failed.

## Commands
python3 -m unittest discover -s tests -v
python3 scripts/generate_grid_manifest.py --output /tmp/basis-grid-manifest.json
git diff --check
EOF