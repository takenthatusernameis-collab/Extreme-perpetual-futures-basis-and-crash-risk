# Next task — EBCR-001

Read AGENTS.md, SKILLS.md, research_state/agent_handoff.md, prompts/continuous_research_operating_contract_v1.md, docs/research_protocol.md, configs/basis_crash_grid_v1.json.

## Immediate deliverables
1. Coverage sampling: Sample BTCUSDT and ETHUSDT for spot daily klines, UM klines, markPriceKlines, indexPriceKlines. Record earliest/latest UTC dates, file counts, schema, gaps in data_coverage_ledger.json.
2. Universe expansion: Fetch next 25 CoinPaprika tickers (offset), append to universe_frontier.json with hash/timestamp.
3. Ingestion prototype: Build minimal parser for one symbol/day producing spot/mark/index median + funding; write to research_state/ingestion_prototype_notes.md.
4. State updates: update handoff and next task.

## Boundary
Free public data only. No REST. No fabrication. Preserve null/failed.

## Commands
python3 -m unittest discover -s tests -v
python3 scripts/generate_grid_manifest.py --output /tmp/basis-grid-manifest.json
git diff --check
