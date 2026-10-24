# Data ingestion plan — EBCR-001

## Objective
Define a concrete, auditable plan to ingest spot/index, perpetual mark, and funding data from free public sources (primarily Binance public archives at data.binance.vision) for basis calculation and crash-risk analysis, without violating hard invariants.

## Sources (priority order)
1. **Binance Public Data Archive** (https://data.binance.vision/) - primary for historical OHLCV/klines, mark/index price klines, funding rates. REST APIs may be blocked by location; use archives.
2. **CoinPaprika** (https://api.coinpaprika.com/v1/) - candidate discovery only (current ranks). No confirmed free PIT history.
3. **Coin Metrics Community API** (https://community-api.coinmetrics.io/v4/) - catalog/metadata; verify historical timeseries availability case by case.

## Timestamp alignment (UTC)
- Normalize all timestamps to UTC.
- For daily aggregation, use UTC calendar days.
- Signal formation occurs only after UTC day `t` is fully complete.
- Forward outcomes use `t+1` onward; require full horizon completion.
- Compare spot and perpetual timestamps; record mismatches and exclude when alignment fails.
- Store raw timestamps and normalized UTC timestamps with evidence.

## Daily aggregation
- Build UTC daily basis as **median of valid timestamp-aligned samples** within each UTC day.
- Record matching tolerance (max allowed time difference between spot/index and perpetual observations), sample count, number of matched pairs, and coverage fraction per (symbol, day).
- Do **not** interpolate unmatched mark/index observations.
- Do **not** forward-fill or synthesize missing data.
- Rolling features: median over last 1/3/7 completed daily basis values (as per grid).

## Coverage gates (≥95%)
- Per analyzed window (feature/reference), require ≥95% valid daily coverage.
- For each window: count valid completed days / expected days in window; if < 0.95 → mark cell as `blocked` or `incomplete` with reason.
- For basis calculation on day t, require full rolling reference history of L valid completed days (90/180/365); never shorten window.
- Require ≥95% coverage for outcome days in horizon.
- Log coverage per asset/window in `data_coverage_ledger.json`.

## Exclusion rules (no lookahead/forward-fill)
- Exclude days with < required matched samples or > tolerance mismatch.
- Exclude assets/periods with missing contract identity/lifecycle (listing/delisting/migration unknown).
- Exclude if spot/index or mark price missing for any required timestamp in window.
- Do not backfill from current values. Do not project historical ranks.
- Do not truncate horizons to fit data - require complete horizons or mark cell status accordingly.
- Preserve all exclusions with reason, source, evidence path, UTC timestamp.

## Basis calculation details
- `basis_pct = 100 * (perpetual_mark_price / contemporaneous_underlying_spot_or_index_price - 1)`
- For formation day t, thresholds estimated from preceding L valid completed daily feature values, excluding current feature.
- Orientations: rich_positive (feature_t > q-quantile), cheap_negative (feature_t < (1-q)-quantile), absolute_extreme (|feature_t| > q-quantile of |feature|).
- Use underlying spot/index lows for primary MAE outcomes (not perpetual price as sole label).

## Data mapping
### Binance archives mapping
- **Spot prices**: `data/spot/daily/klines/{SYMBOL}/{interval}/` - use appropriate interval (1m or higher) to build daily medians; can aggregate from intraday. Need to confirm which quote currency/index is used as underlying.
- **Perpetual mark price**: `data/futures/um/daily/markPriceKlines/{SYMBOL}/{interval}/` (USD-M).
- **Index price**: `data/futures/um/daily/indexPriceKlines/{SYMBOL}/{interval}/` - may be used as underlying reference.
- **Funding**: `data/futures/um/monthly/fundingRate/{SYMBOL}/` and possibly daily; for controls when available.
- **Contract lifecycle**: Not directly in klines - need to infer from archive presence (first/last file dates), and be conservative. REST exchangeInfo blocked; must document gaps.

### Alignment strategy
1. For each candidate symbol, identify spot pair and corresponding perpetual contract(s).
2. Download/archive-scan daily files for required intervals covering date range.
3. Parse timestamps (UTC), extract prices (open/high/low/close/mark/index as appropriate).
4. For each UTC day, find timestamp-aligned samples between perpetual mark and spot/index within tolerance (e.g., ±60s or per exchange convention) - record matching policy.
5. Compute intraday basis samples, take median per day → daily basis series.
6. Build rolling features per grid spec.
7. Apply coverage gates.

## Implementation plan (phased)
### Phase 1: Scaffolding (current)
- [x] Audit sources (done)
- [x] Update ledgers
- [ ] Create ingestion utilities (parsers for Binance zip/CSV, timestamp normalization)
- [ ] Create universe discovery from CoinPaprika (candidates list, mark rank-unverified)

### Phase 2: Pilot
- [ ] Test on a small set of major symbols (e.g., BTCUSDT) with available data
- [ ] Verify daily aggregation, coverage calculation
- [ ] Verify basis calculation against known values if possible
- [ ] Validate gates work correctly

### Phase 3: Scale
- [ ] Systematic ingestion with checkpointing
- [ ] Full coverage audit per symbol
- [ ] Build formation dates only when gates pass

## Risks & mitigations
- **REST API blocked**: Use archives only; acceptable per sources.md.
- **Missing funding/mark/index for some symbols**: Mark as blocked/incomplete, don't synthesize.
- **Contract lifecycle unclear**: Conservative exclusions; document in ledger.
- **PIT rank history missing**: Candidates remain rank-unverified; discovery-only per protocol.
- **Large data volume**: Process symbol by symbol, daily files, store hashes/provenance.
- **Timezone/format issues**: Enforce UTC normalization, validate timestamps.

## Provenance requirements
- Record retrieval URL/path, fetch time (UTC), file hashes (SHA256), archive listing snapshot.
- Store in run manifests; keep raw artifacts with pointers.
- Every exclusion logged with evidence.
