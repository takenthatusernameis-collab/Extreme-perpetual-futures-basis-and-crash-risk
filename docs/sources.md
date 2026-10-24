# Free public data sources and source policy

Availability, coverage, endpoint schemas and limits can change. On every refresh, test actual coverage and record endpoint, UTC query window, retrieval time, raw-response checksum and limitations. Do not claim a source is adequate until verified.

## Candidate discovery and market capitalization
- Coin Metrics Community API: https://docs.coinmetrics.io/api/v4/ and https://community-api.coinmetrics.io/v4/ . Verify supported asset metrics and actual historical market-cap/rank coverage; do not assume every asset exists.
- CoinPaprika public API: https://docs.coinpaprika.com/ and https://api.coinpaprika.com/v1/coins . Use a current market-cap ranking for candidate discovery only unless independently verifiable historical point-in-time rank history is available.
- Free public historical datasets may be used only after auditing licence, revisions, temporal coverage and survivorship. Pin exact revisions and hashes.

## Perpetual and spot/index history
- Binance USD-M Futures public market-data docs: https://developers.binance.com/docs/derivatives/usds-margined-futures/market-data/rest-api
- Binance COIN-M Futures public market-data docs: https://developers.binance.com/docs/derivatives/coin-margined-futures/market-data
- Binance Public Data Archive: https://data.binance.vision/
- Other venues' official public endpoints/archives may be added when free and documented. Keep each venue separately versioned; do not assume contracts are interchangeable.

## Evidence requirements
Current rankings discover candidates but do not reconstruct historical membership. Never infer missing historical rank, funding, index price or delisting date from today's values. Missing official histories remain explicit gaps. Cross-venue substitutions require a separate analysis arm. Respect rate limits, bounded retries and public terms; no subscription keys, paid endpoints, gated scraping or hidden trial access. Store provenance manifests and derived artefacts in Git; put bulky raw snapshots only in permitted free archives/artifacts with stable pointers and hashes.
