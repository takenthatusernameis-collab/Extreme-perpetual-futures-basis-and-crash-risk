# Agent handoff — EBCR-001

## Status
- Research design initialized; no empirical finding has yet been verified.
- Frozen config: `configs/basis_crash_grid_v1.json` (config_sha256=55caedf84ac723289f70f49bbed4712c8195425feb4a95e737f3e8929479a0e0).
- Grid manifest generated: `research_state/grid_manifest_v1.json` (324 cells, all unique IDs/hashes; primary anchor EBCR-GRID-001-0005 present).
- Tests: 11 passed.
- Ledgers initialized/updated.
- Source audit updated (2026-10-24): CoinPaprika accessible (62351 coins, discovery-only). Coin Metrics accessible. Binance archives accessible via S3; REST blocked. Funding rate monthly confirmed BTCUSDT 2020-01+ (schema: calc_time ms, funding_interval_hours, last_funding_rate). Universe frontier populated with 25 discovery candidates (rank-unverified).
- Ingestion design documented: `research_state/ingestion_design.md`.

## Verified setup
- Deterministic manifest generator.
- Regression suite passes (11 tests).
- Historical research only; public free data.

## Completed this session
1. Confirmed baseline.
2. Audited Binance archives; funding schema confirmed.
3. Confirmed PIT rank constraints.
4. Created ingestion design doc.
5. Populated universe frontier (25 candidates, discovery-only).

## Next action
1. Coverage sampling: spot daily klines + UM klines/mark/index for BTCUSDT/ETHUSDT; record windows/gaps.
2. Universe expansion: fetch next pages of CoinPaprika tickers (batch 25) with hashes.
3. Implement ingestion parser prototype for one symbol/day.
4. State updates.

## Reporting rules
Separate completed, blocked, failed, incomplete and not-run tasks. Preserve exclusions. A concrete next task must always remain.
