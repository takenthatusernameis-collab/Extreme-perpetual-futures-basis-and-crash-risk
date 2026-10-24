# Ingestion design — EBCR-001

## Sources
- Binance public data archive (data.binance.vision) only. REST APIs blocked in environment.
- Spot daily klines, UM futures klines, markPriceKlines, indexPriceKlines, fundingRate monthly ZIPs.
- CoinPaprika/Coin Metrics for candidate discovery only (no PIT membership).

## UTC alignment
- All timestamps interpreted as UTC. Kline open times converted from ms to UTC dates.
- Daily aggregation uses completed UTC days only; no partial-day bars.
- Funding calc_time (ms UTC) assigned to its UTC date.

## Daily aggregation
- For each symbol/day, compute median of valid timestamp-aligned samples for spot close, mark close, index close.
- Coverage gate: >=95% of expected minutes present per day; otherwise day excluded with reason.
- No forward-fill, no interpolation, no synthesis of missing observations.

## Basis calculation
- basis = (mark_price - index_price) / index_price (rich-positive orientation) per declared grid.
- Also variants: cheap-negative (index-mark)/index, absolute abs(mark-index)/index.
- Signal timestamp = close of feature day (causal; no lookahead into outcome window).

## Exclusion rules
- Missing mark or index for a day -> day excluded (record reason, source, UTC time).
- Contract not listed for full window -> excluded from PIT analysis (not silently dropped).
- Coverage <95% -> day excluded.

## Timestamp gates
- Feature computed only from completed observations strictly before outcome window.
- Forward horizon 7-28 days fully closed (UTC) before scoring.
- No use of future data in feature.

## Funding
- Monthly ZIPs: calc_time (ms), funding_interval_hours, last_funding_rate.
- Aggregate to daily by taking last funding rate of completed UTC day; if multiple, median.

## Universe
- Discovery-only candidates from CoinPaprika; rank-unverified. No historical membership claims without PIT evidence.
