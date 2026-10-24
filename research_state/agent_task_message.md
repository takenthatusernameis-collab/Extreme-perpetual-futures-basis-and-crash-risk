# Next task — EBCR-001

Read AGENTS.md, SKILLS.md, research_state/agent_handoff.md, prompts/continuous_research_operating_contract_v1.md, docs/research_protocol.md, configs/basis_crash_grid_v1.json.

## Immediate deliverables
1. Implement ingestion parser prototype for one symbol/day (BTCUSDT): download sample ZIPs, parse CSV, compute spot/mark/index median + funding, write output to research_state/ with hash.
2. Audit per-day gaps: compare ETHUSDT index files vs mark files; record missing dates in data_coverage_ledger.json.
3. Investigate CoinPaprika pagination for next 25 candidates; record method or blocker.
4. State updates: update handoff and next task.

## Boundary
Free public data only. No REST (Binance). No fabrication. Preserve null/failed.

## Commands
python3 -m unittest discover -s tests -v
python3 scripts/generate_grid_manifest.py --output /tmp/basis-grid-manifest.json
git diff --check
EOF