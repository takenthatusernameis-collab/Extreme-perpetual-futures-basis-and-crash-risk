# Agent handoff — EBCR-001

## Status
- Research design initialized; no empirical finding has yet been verified.
- Frozen config: `configs/basis_crash_grid_v1.json` (config_sha256=55caedf84ac723289f70f49bbed4712c8195425feb4a95e737f3e8929479a0e0).
- Grid manifest generated: `research_state/grid_manifest_v1.json` (324 cells, all unique IDs/hashes; primary anchor EBCR-GRID-001-0005 present).
- Tests: `python3 -m unittest discover -s tests -v` → 11 passed.
- Ledgers initialized/updated: `research_state/source_audit.md`, `research_state/data_coverage_ledger.json`, `research_state/cell_status_ledger.json`.
- Source audit updated (2026-10-24): CoinPaprika /v1/coins accessible (62351 coins, discovery-only). Coin Metrics Community API accessible. Binance data.binance.vision accessible via S3; REST APIs blocked from environment. Verified paths: spot daily klines, UM futures klines/markPriceKlines/indexPriceKlines, fundingRate monthly (BTCUSDT files exist 2020-01+), aggTrades. PIT historical market-cap/rank not confirmed free → discovery-only.
- Universe frontier updated with retrieval hashes/timestamps.
- Expected grid: 324 configurations × 8 endpoints = 2,592 exploratory cell-endpoint tests.
- Fixed anchor: 1-day feature, 90-day reference, rich-positive, q95, 14-day horizon.
- No source cutoff, coverage claim, completed grid or predictive result is established yet.

## Verified setup
- Deterministic manifest generator: `scripts/generate_grid_manifest.py`.
- Regression suite passes (11 tests).
- Historical research only; public free data and open-source tooling; no paid services, credentials, orders or live/paper trading.

## Completed this session
1. Confirmed baseline (tests pass, manifest present, anchor identified).
2. Audited Binance public archives via S3: REST blocked. Mapped spot klines, UM futures klines/markPriceKlines/indexPriceKlines, fundingRate monthly (confirmed BTCUSDT monthly funding files exist), aggTrades. Updated source audit and data coverage ledger.
3. Confirmed PIT rank constraints (discovery-only; no confirmed free bulk PIT history).

## Next action
1. **Coverage sampling:** Sample BTCUSDT and ETHUSDT for spot daily klines, UM klines/markPriceKlines/indexPriceKlines. Record earliest/latest UTC, file counts, schema, gaps in `research_state/data_coverage_ledger.json`.
2. **Funding rate inspection:** Download/read a sample fundingRate monthly ZIP (e.g., BTCUSDT-2023-01.zip) to confirm schema/columns/timestamps.
3. **Ingestion design:** Create `research_state/ingestion_design.md` documenting UTC alignment, daily aggregation (median of valid timestamp-aligned samples), coverage gates (≥95%), exclusion rules, no lookahead/forward-fill, timestamp gates, basis calc.
4. **Universe scaffold:** Fetch CoinPaprika `/v1/coins` (top ~200) as discovery-only candidates, write to `research_state/universe_frontier.json` marked rank-unverified.
5. **State updates:** Update handoff/next task with findings.

## Reporting rules
Separate completed, blocked, failed, incomplete and not-run tasks. Preserve every excluded candidate and adverse result. A concrete next task must always remain.
