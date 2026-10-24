# Source audit — EBCR-001

Status: Initial audit in progress (design phase). No empirical fetches executed yet.

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

## Coverage/limits to verify
- [ ] Historical rank/PIT market cap history (free sources)
- [ ] Spot/index OHLC/L with UTC timestamps and identity
- [ ] Perpetual mark price, funding rate history
- [ ] Contract listing/delisting/migration history
- [ ] Data revision behavior
- [ ] Rate limits and actual coverage windows

## Gaps identified
- No empirical data fetched yet. All sources marked untested.
- Historical PIT rank history is often not freely available in bulk form; may need to use labelled coverage cohorts.

## Audit results (2026-10-24 UTC)
- CoinPaprika /v1/coins: OK (62351 coins). Returns current rank/market data; historical PIT rank history not obviously available via this endpoint. Treat as discovery-only.
- Coin Metrics Community API /v4/catalog/assets: OK (6347 assets). Catalog exists; historical timeseries endpoints exist but may require checking availability/limits. Need to verify if free community API provides historical marketcap/rank.
- Binance public APIs/archives (data.binance.vision): Access confirmed via S3 listing.
  - Spot daily klines: `data/spot/daily/klines/{SYMBOL}/{interval}/` with daily ZIP files + CHECKSUMs. Provides OHLCV for spot; usable as underlying spot prices.
  - USD-M futures (um): `data/futures/um/daily/klines/{SYMBOL}/{interval}/` exists. `markPriceKlines/` and `indexPriceKlines/` exist under daily for some symbols/intervals. Funding rate appears under monthly/daily in different paths - `data/futures/um/monthly/fundingRate/` and possibly daily; need to inspect exact locations. Contract info may come from exchangeInfo (REST) but REST blocked from this location; need alternative for contract lifecycle/listings.
  - COIN-M futures (cm): Similar structure exists (`data/futures/cm/daily/...` has aggTrades).
  - License/terms: Terms of use present at data.binance.vision/terms-of-use.html. Must comply with terms; data is public archive.
  - Coverage: Archives go back years for major pairs (BTCUSDT klines seen from 2023+). Need systematic sampling.
  - Gaps: Funding rate location needs verification (monthly/daily). REST API access may be restricted by location (Binance REST APIs blocked here) - so we must rely on archives and public non-REST sources where possible. Contract lifecycle (listings/delists) via REST may be unavailable; need alternative sources or derive from archive presence gaps. Mark/index availability varies by symbol/interval - must check coverage gates. For basis calculation we need perpetual mark price and underlying spot/index price with UTC alignment. Need to design ingestion to pull matching timestamps.

## Conclusion
- Discovery via current ranks possible from free sources.
- Free historical PIT market-cap/rank is likely limited/unavailable in bulk; per protocol, must not backfill from current rank. Candidates will be labeled rank-unverified or placed in coverage cohort until defensible PIT evidence exists.
