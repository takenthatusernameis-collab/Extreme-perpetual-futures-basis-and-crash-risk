# Next task — EBCR-001

Read AGENTS.md, SKILLS.md, research_state/agent_handoff.md, prompts/continuous_research_operating_contract_v1.md, docs/research_protocol.md, configs/basis_crash_grid_v1.json.

## Immediate deliverables
1. Collect Q1 ingestion results for BTCUSDT+ETHUSDT (2024-01-01..2024-03-31). If present, summarize coverage/gaps; if still running, monitor and update when complete.
2. For remaining verified symbols (BNB,XRP,SOL,TRX,ZEC,DOGE,LINK,ADA,XLM,NEAR,BCH), audit concrete daily coverage (mark/index/funding/klines) over an overlapping window and update research_state/data_coverage_ledger.json with ok/total and gaps.
3. Implement/extend basis computation to all audited symbols with UTC medians, no forward-fill; write research_state/basis_computation_q1_partial.json with per-day basis_pct, component hashes, timestamps.
4. Update handoff and next task with concrete numbers.

## Boundary
Free public data only. No REST (Binance). No fabrication. Preserve null/failed/exclusions.

## Commands
python3 -m pytest -q tests 2>&1 | tail -5
python3 scripts/generate_grid_manifest.py --output /tmp/basis-grid-manifest.json
git diff --check
