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
- Binance public APIs/archives: Documented; need to test specific endpoints for mark/index/spot/funding. Archives at data.binance.vision exist.

## Conclusion
- Discovery via current ranks possible from free sources.
- Free historical PIT market-cap/rank is likely limited/unavailable in bulk; per protocol, must not backfill from current rank. Candidates will be labeled rank-unverified or placed in coverage cohort until defensible PIT evidence exists.
