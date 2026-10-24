# Ingestion prototype notes — EBCR-001

## Scope
Minimal parser design for one symbol/day (BTCUSDT) producing spot/mark/index median + funding. No full download executed yet.

## Steps
1. Download one daily ZIP per series: spot 1d, UM klines 1d, markPriceKlines 1d, indexPriceKlines 1d, and the relevant monthly funding ZIP.
2. Read CSV (no header for klines): open_time_ms, open, high, low, close, volume, close_time_ms, quote_asset_volume, num_trades, taker_buy_base, taker_buy_quote, ignore.
3. Convert open_time_ms to UTC date; require fully completed UTC day (close_time >= day end).
4. Median of close prices per UTC day across all valid bars (daily file = one bar, so close used; for 1m files median of minute closes).
5. Coverage gate: >=95% of expected minutes present per day else exclude with reason.
6. basis_pct = 100*(mark_median/index_median - 1).
7. Funding: from monthly ZIP (calc_time ms, funding_interval_hours, last_funding_rate); take last funding rate of completed UTC day; if multiple, median.

## Exclusions
- Missing mark or index for a day -> day excluded (record reason, source, UTC time).
- Coverage <95% -> day excluded.
- No forward-fill/interpolation.

## Status
Design documented; parser code not yet implemented. Next: implement parser for one symbol/day and verify schema against downloaded sample.
EOF