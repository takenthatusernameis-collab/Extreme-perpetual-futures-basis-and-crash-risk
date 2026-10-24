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
6. Coverage sampling: BTCUSDT/ETHUSDT spot/UM/mark/index daily klines + funding monthly; recorded windows/gaps in data_coverage_ledger.json.
7. Attempted universe expansion via CoinPaprika offset=25; endpoint returned same first 25 (no pagination exposed) — recorded; frontier remains 25.
8. Wrote ingestion prototype notes.
9. Implemented ingestion parser prototype (scripts/ingestion_prototype.py); verified schema on BTCUSDT 2024-01-01 sample; output research_state/ingestion_prototype_sample.json.
10. CoinPaprika pagination: /v1/coins returns all 62351 rows sorted by rank; no cursor/next page; next 25 obtainable by client-side slice of full list.
11. ETHUSDT index gap audit: blocked on S3 directory listing; recorded as incomplete.

## Next action
1. Implement S3 directory listing parser for ETHUSDT mark/index to enumerate missing dates.
2. Extend ingestion prototype to multi-day and coverage gating.
3. Map first 25 candidates to Binance perpetual symbols.
4. State updates.

## Reporting rules
Separate completed, blocked, failed, incomplete and not-run tasks. Preserve exclusions. A concrete next task must always remain.
