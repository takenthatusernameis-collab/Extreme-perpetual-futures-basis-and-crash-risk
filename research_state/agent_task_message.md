# Next task — EBCR-001

Read AGENTS.md, SKILLS.md, research_state/agent_handoff.md, prompts/continuous_research_operating_contract_v1.md, docs/research_protocol.md, configs/basis_crash_grid_v1.json.

## Immediate deliverables
1. Expand ingestion to larger overlapping window for BTCUSDT+ETHUSDT (suggest 2024-01-01 to 2024-03-31). Enforce >=95% coverage gate; write research_state/ingestion_btc_eth_q1_2024.json with per-day component status and basis_pct where computable.
2. Audit mark/index/funding coverage for verified symbols (BTC,ETH,BNB,XRP,SOL,TRX,ZEC,DOGE,LINK,ADA,XLM,NEAR,BCH) using S3 XML listings; record gaps/exclusions in data_coverage_ledger.json (update if exists, else create).
3. Implement basis computation with UTC medians, no forward-fill; store hashes and timestamps.
4. State updates: update handoff and next task with concrete numbers.

## Boundary
Free public data only. No REST (Binance). No fabrication. Preserve null/failed/exclusions.

## Commands
python3 -m pytest -q tests
python3 scripts/generate_grid_manifest.py --output /tmp/basis-grid-manifest.json
git diff --check
