# Agent handoff — EBCR-001

## Status
- Research design initialized; no empirical finding has yet been verified.
- Frozen config: `configs/basis_crash_grid_v1.json` (config_sha256=55caedf84ac723289f70f49bbed4712c8195425feb4a95e737f3e8929479a0e0).
- Grid manifest generated: `research_state/grid_manifest_v1.json` (324 cells, all unique IDs/hashes; primary anchor present).
- Tests: `python3 -m unittest discover -s tests -v` → 11 passed.
- Ledgers initialized: `research_state/source_audit.md`, `research_state/data_coverage_ledger.json`, `research_state/cell_status_ledger.json`.
- Source audit: CoinPaprika /v1/coins and /v1/tickers accessible (free). Coin Metrics Community API catalog accessible. No confirmed free PIT historical market-cap/rank history found; discovery ranks are discovery-only per protocol.
- Universe frontier updated with retrieval hashes/timestamps.
- Expected grid: 324 configurations × 8 endpoints = 2,592 exploratory cell-endpoint tests.
- Fixed anchor: 1-day feature, 90-day reference, rich-positive, q95, 14-day horizon.
- No source cutoff, coverage claim, completed grid or predictive result is established yet.

## Verified setup
- Deterministic manifest generator: `scripts/generate_grid_manifest.py`.
- Regression suite passes (11 tests).
- Historical research only; public free data and open-source tooling; no paid services, credentials, orders or live/paper trading.

## Next action
1. Audit Binance public data (USD-M/COIN-M market data APIs and data.binance.vision archives) for spot/index/mark/funding/contract lifecycle coverage windows. Record earliest/latest UTC complete dates, schemas, gaps in `research_state/data_coverage_ledger.json`.
2. Design data ingestion plan respecting UTC alignment, ≥95% coverage, no forward-fill/synthesis, timestamp gates. Map required fields for basis calculation per protocol.
3. Define chronological split boundaries once coverage known (60% dev / 20% val / 20% holdout, 28-day embargo). Prepare to run grid only on dev; anchor-only on val/holdout.
4. Build candidate mapping framework: treat discovery candidates as rank-unverified unless PIT evidence found; never backfill from current rank. Preserve exclusions.
5. Implement cell status tracking scaffolding tied to manifest.

## Reporting rules
Separate completed, blocked, failed, incomplete and not-run tasks. Preserve every excluded candidate and adverse result. A concrete next task must always remain.
