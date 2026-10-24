# Next task — EBCR-001

Read `AGENTS.md`, `SKILLS.md`, this file, `research_state/agent_handoff.md`, the operating contract, grid config, source guide and relevant skills.

## Immediate deliverables
1. **Baseline confirmed:** Tests pass (11/11). Grid manifest generated (324 cells). Source discovery tested (CoinPaprika/CoinMetrics accessible). PIT rank history not confirmed free → discovery-only.
2. **Binance audit:** Check Binance USD-M/COIN-M public market data endpoints and data.binance.vision for available historical data (spot/index, mark price, funding). Record coverage windows, formats, rate limits, licensing notes. Update `research_state/source_audit.md` and `research_state/data_coverage_ledger.json`.
3. **Ingestion design:** Document timestamp alignment (UTC), daily aggregation (median of valid timestamp-aligned samples), coverage gates (≥95%), exclusion rules, no lookahead/forward-fill. Create plan before fetching large data.
4. **Universe handling:** Implement discovery list from CoinPaprika tickers (top by rank) as candidates; mark all as rank-unverified pending PIT evidence. Never infer historical membership from current rank.
5. **State updates:** Update handoff and next task with concrete findings/blockers.

## Boundary
Use only free public data and open-source tools. No paid services, keys/secrets, exchange credentials, live/paper trading or orders. Never fabricate coverage or metrics. Preserve negative, null, failed and not-run results. Finish with an updated handoff and next measurable task.
