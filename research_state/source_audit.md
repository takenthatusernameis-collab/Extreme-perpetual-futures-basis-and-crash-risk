# Source audit — EBCR-001

Status: Audit complete (2026-10-24 UTC). Empirical source checks executed; see "Audit results (2026-10-24 UTC)" below. PIT rank history resolved separately via free Wayback-CMC snapshots (research_state/pit_rank_verification_v1.json); remaining coverage checkboxes resolved as noted.

## Candidate discovery (market cap rank)
- Coin Metrics Community API (free): https://community-api.coinmetrics.io/v4/
  - Status: Not yet tested
  - Notes: Need to verify historical market-cap/rank availability (often limited). Current rank for discovery only; not for historical membership.
- CoinPaprika (free): https://api.coinpaprika.com/v1/
  - Status: Not yet tested
  - Notes: Good for current rankings; verify if PIT history exists. Treat as discovery-only unless proven otherwise.

## Perpetuals, spot/index/funding/mark
- Binance USD-M Futures public: https://developers.binance.com/docs/derivatives/usds-margined-futures/market-data/rest-api
- Binance COIN-M Futures public: https://developers.binance.com/docs/derivatives/coin-margined-futures/market-data
- Binance Public Data Archive: https://data.binance.vision/
  - Status: Public archives available; need to check schema, coverage windows, and licensing. Large files; respect rate limits.
- Other venues: To be evaluated if needed, must remain free/public.

## Coverage/limits to verify (resolved 2026-10-24 UTC)
- [x] Historical rank/PIT market cap history (free sources) — RESOLVED: free Wayback Machine CMC historical snapshots parsed from __NEXT_DATA__; rank_verified=true for all 13 Binance-UM perp symbols. Record: research_state/pit_rank_verification_v1.json. PIT inquiry CLOSED.
- [x] Spot/index OHLC/L with UTC timestamps and identity — RESOLVED: data.binance.vision spot daily klines confirmed (data/spot/daily/klines/{SYMBOL}/{interval}/, daily ZIP + CHECKSUMs).
- [~] Perpetual mark price, funding rate history — PARTIAL: markPriceKlines/ and indexPriceKlines/ confirmed under data/futures/um/daily/; monthly fundingRate path exists under data/futures/um/monthly/fundingRate/{SYMBOL}/ but actual files not yet verified; daily funding not obvious. Known gap, does not block basis construction from mark/index.
- [ ] Contract listing/delisting/migration history — UNRESOLVED: contract lifecycle via REST unavailable from environment (REST blocked); must derive from archive presence gaps or alternative free source. Known gap.
- [ ] Data revision behavior — UNRESOLVED: not explicitly tested in this pass.
- [x] Rate limits and actual coverage windows — RESOLVED for access: REST API blocked from environment; must use archives only. S3-style listing works. Archives cover years for major pairs (systematic sampling not performed).

## Gaps identified
- No empirical data fetched yet. All sources marked untested.
- Historical PIT rank history is often not freely available in bulk form; may need to use labelled coverage cohorts.

## Audit results (2026-10-24 UTC)
- CoinPaprika /v1/coins: OK (62351 coins). Returns current rank/market data; historical PIT rank history not obviously available via this endpoint. Treat as discovery-only.
- Coin Metrics Community API /v4/catalog/assets: OK (6347 assets). Catalog exists; historical timeseries endpoints exist but may require checking availability/limits. Need to verify if free community API provides historical marketcap/rank.
- Binance public APIs/archives (data.binance.vision): Access confirmed via S3 listing.
  - Spot daily klines: `data/spot/daily/klines/{SYMBOL}/{interval}/` with daily ZIP files + CHECKSUMs. Provides OHLCV for spot; usable as underlying spot prices.
  - USD-M futures (um): `data/futures/um/daily/klines/{SYMBOL}/{interval}/`, `markPriceKlines/`, `indexPriceKlines/` exist. Funding rate: monthly appears under `data/futures/um/monthly/fundingRate/{SYMBOL}/` (need to verify actual files). Daily funding not obvious.
  - COIN-M futures (cm): `data/futures/cm/daily/aggTrades/{SYMBOL}/` seen; klines/mark/index may exist.
  - License/terms: Terms of use present at data.binance.vision/terms-of-use.html. Must comply with terms; data is public archive.
  - Coverage: Archives go back years for major pairs. Need systematic sampling.
  - Gaps: Funding rate location needs verification. REST API access may be restricted by location - must rely on archives. Contract lifecycle via REST unavailable; need alternative or derive from archive presence gaps. Mark/index availability varies by symbol/interval. Need timestamp alignment design.
  - Verified: REST API blocked from environment; must use archives only. S3-style listing works. Spot/futures/mark/index paths confirmed in structure.

## Conclusion
- Discovery via current ranks possible from free sources.
- Free historical PIT market-cap/rank is likely limited/unavailable in bulk; per protocol, must not backfill from current rank. Candidates will be labeled rank-unverified or placed in coverage cohort until defensible PIT evidence exists.
