# Contract lifecycle & PIT rank audit v1 — 11 traded UM perpetual symbols

- **Artifact ID:** `EBCR-001-AUDIT-CONTRACT-LIFECYCLE-V1`
- **Program:** EBCR-001 (perpetual-futures basis → crash frequency / downside tail)
- **Retrieved at:** 2026-11-14 (UTC)
- **Status of this audit:** `ok` — evidence gathered from free public sources only; **no frozen ledger edited**. Companion machine-readable evidence: `research_state/audit/contract_lifecycle_evidence_v1.json` (sha256 `4b419069b34e6fe622669b3c690cf1500a609610c8a3435d23523cfc26bfddfd`).
- **Scope:** the 11 symbols present in `research_state/integrated_extended_v1.json` (window 2023-01-01 → 2024-04-30): ADAUSDT, BCHUSDT, BNBUSDT, DOGEUSDT, LINKUSDT, NEARUSDT, SOLUSDT, TRXUSDT, XLMUSDT, XRPUSDT, ZECUSDT.

## Question
`research_state/candidate_perp_mapping_v1.json` carries `mapping_status = discovery_only_unverified`, with a note that "contract lifecycle / mark-index / funding coverage still needs per-symbol audit before use." This audit resolves, per symbol, (a) listing date, (b) any delisting/migration, (c) contract identity (mark vs index vs spot), and (d) the UTC date from which continuous data exists — then compares that against the integrated file's `first`/`last` dates and the candidate mapping.

## Sources (free public only; no credentials, no paid access)
1. **Binance USDT-M futures `exchangeInfo`** — `https://www.binance.com/fapi/v1/exchangeInfo` → HTTP 200. Provides `status`, `contractType`, `onboardDate`, `deliveryDate`, `baseAsset`/`quoteAsset`.
   - **Endpoint note:** the canonical `fapi.binance.com` and `api.binance.com` hosts returned **HTTP 451 (geo-blocked)** at retrieval. `www.binance.com/fapi/v1/exchangeInfo` was reachable and used. No credential, no order, no trading endpoint was touched.
2. **Binance public data S3 archive (XML bucket listing)** — `https://s3-ap-northeast-1.amazonaws.com/data.binance.vision` → HTTP 200. Fully paginated (marker paging past the 500/1000-key page cap) for:
   - `data/futures/um/daily/klines/<SYM>/1d/` (all 11),
   - `data/futures/um/daily/{markPriceKlines,indexPriceKlines}/<SYM>/1d/` (all 11),
   - `data/futures/um/monthly/fundingRate/<SYM>/` (all 11).

No other endpoints were required. Retries were bounded to one pagination pass per prefix; the mark/index full re-pagination pass was aborted on wall-time after the first-seen dates had already been captured in the earlier successful pass (the deliverable does not depend on mark/index end dates, only first-seen continuity vs listing).

## Per-symbol lifecycle table

All dates UTC. "first kline" = earliest `YYYY-MM-DD` daily kline zip in the S3 archive. "mark first" / "index first" = earliest daily mark-price / index-price kline zip.

| Symbol | exchangeInfo status | contractType | onboardDate | first kline | last kline | mark first | index first | funding first month | gaps in full span |
|---|---|---|---|---|---|---|---|---|---|
| ADAUSDT | TRADING | PERPETUAL | 2020-01-31 | 2020-01-31 | 2026-11-12 | 2020-01-19 | 2020-01-19 | 2020-01 | 0 |
| BCHUSDT | TRADING | PERPETUAL | 2019-12-19 | 2019-12-31 | 2026-11-12 | 2019-12-23 | 2019-12-23 | 2020-01 | 0 |
| BNBUSDT | TRADING | PERPETUAL | 2020-02-10 | 2020-02-10 | 2026-11-12 | 2019-12-31 | 2020-01-01 | 2020-02 | 0 |
| DOGEUSDT | TRADING | PERPETUAL | 2020-07-10 | 2020-07-10 | 2026-11-12 | 2020-07-10 | 2020-07-21 | 2020-07 | 0 |
| LINKUSDT | TRADING | PERPETUAL | 2020-01-17 | 2020-01-17 | 2026-11-12 | 2020-01-17 | 2020-01-15 | 2020-01 | 0 |
| NEARUSDT | TRADING | PERPETUAL | 2020-10-15 | 2020-10-15 | 2026-11-12 | 2020-10-14 | 2021-01-01 | 2020-10 | 0 |
| SOLUSDT | TRADING | PERPETUAL | 2020-09-14 | 2020-09-14 | 2026-11-12 | 2020-09-13 | 2021-01-01 | 2020-09 | 0 |
| TRXUSDT | TRADING | PERPETUAL | 2020-01-15 | 2020-01-15 | 2026-11-12 | 2020-01-15 | 2020-01-19 | 2020-01 | 0 |
| XLMUSDT | TRADING | PERPETUAL | 2020-01-20 | 2020-01-20 | 2026-11-12 | 2020-01-19 | 2020-01-19 | 2020-01 | 5 |
| XRPUSDT | TRADING | PERPETUAL | 2020-01-06 | 2020-01-06 | 2026-11-12 | 2020-01-06 | 2020-01-19 | 2020-01 | 4 |
| ZECUSDT | TRADING | PERPETUAL | 2020-02-05 | 2020-02-05 | 2026-11-12 | 2020-02-04 | 2020-02-04 | 2020-02 | 1 |

### Gap detail (all outside the test window)
The only missing daily-kline dates across the full multi-year span are in a single late-2020 window, none inside 2023-01-01 → 2024-04-30:
- **XLMUSDT** (5): 2020-11-30 … 2020-12-04.
- **XRPUSDT** (4): 2020-11-30, 2020-12-02, 2020-12-03, 2020-12-04.
- **ZECUSDT** (1): 2020-12-02.
These correspond to the well-known Dec-2020 exchange-maintenance gap and do not touch the research window.

## Findings (verified)

1. **No delisting or migration among the 11 traded symbols.** Every symbol is `status = TRADING`, `contractType = PERPETUAL`, `quoteAsset = USDT`, with `deliveryDate = 2100-12-31` (perpetual, no expiry). Each has a single unbroken daily kline series from listing through 2026-11-12. No symbol required a contract-identity migration (no mark↔index↔spot substitution, no symbol rollover) during or after the test window. The exchange `onboardDate` and the archive first kline agree to the day for 8/11 symbols; BCHUSDT and BNBUSDT show the archive series starting a few days *before* the recorded `onboardDate` (archive backfill includes pre-announcement bars), and LINKUSDT/NEARUSDT/SOLUSDT show the mark/index stream beginning slightly before the `onboardDate`. These are benign backfill/coverage offsets, not lifecycle events.

2. **Contract identity is clean and distinct.** For every symbol the kline (trade) series, mark-price series, index-price series, and funding-rate series are separately archived and separately addressable. This is the identity the basis computation relies on (`basis = mark / index − 1`, with spot close fallback). There is no evidence of the mark series silently being a copy of the index series or of a spot price standing in for a perp series.

3. **Continuous data exists from well before the window for all 11 symbols.** The latest listing among the 11 is NEARUSDT (2020-10-15); every symbol has ≥ 27 months of continuous daily klines before 2023-01-01. Within the test window (2023-01-01 → 2024-04-30) **all 11 symbols have zero missing days and full coverage** (`first kline ≤ window start` and `last kline ≥ window end`). This is consistent with the integrated file's observed per-symbol counts and with the 308 `incomplete_forward_horizon` exclusions (a label-horizon truncation at the window's right edge, not a data gap).

4. **Mapping status can be upgraded for these 11 (evidence-based).** All 11 `binance_um_symbol` values in `candidate_perp_mapping_v1.json` are now confirmed against live `exchangeInfo` (`baseAsset` matches the asset symbol; `quoteAsset = USDT`) and against a fully paginated S3 archive with per-symbol daily/mark/index/funding coverage. The 5 symbols previously marked `candidate_mapping_unverified` (BNB, XRP, SOL, TRX, ZEC) are confirmed. **This audit does not edit the frozen mapping file** (that is a separate registration decision); it records the evidence needed to do so.

## Comparison to `integrated_extended_v1.json`
- Integrated `window` = 2023-01-01 → 2024-04-30; per-symbol observed `first`/`last` row dates all fall inside that window (earliest row 2023-01-01, latest 2024-04-02 for every symbol, per the row-level date min/max). The archive confirms continuous upstream data for the entire window, so the 2024-04-02 row-date end is a forward-horizon label truncation, not a missing-data boundary.
- No symbol's integrated coverage is contradicted by the archive. No survivorship issue is introduced by this audit: all 11 symbols were listed years before the window and remain live today.

## Invariants preserved
- No frozen config, anchor, integrated file, evaluation report, hypothesis registry, universe frontier, or prior audit was modified. This is a **new** artifact (`contract_lifecycle_evidence_v1.json` + this `.md`).
- No preregistration was derived from any grid hit; no holdout was inspected; no p-value was selected.
- Anchor remains null (`crash_incidence_15pct` adj p `0.24830545694889028`; `expected_shortfall_5pct_forward_mae` adj p `0.9485`); PIT rank remains CLOSED; EBCR-H001 `tested_not_supported`; EBCR-H002/H003/H004 `registered_secondary_not_tested`; `next_hypothesis_sequence` = 5.
- Unfavorable/null evidence preserved: the mapping file remains `discovery_only_unverified` on disk; this audit records *candidate-verification evidence* only and does not promote it.

## Residual / not resolved here
- **`exchangeInfo` is a live snapshot, not a historical point-in-time record.** It gives current `status`/`onboardDate`; it does not by itself prove there was no temporary halt or re-listing in, e.g., 2021. The archive's *unbroken daily series* is the stronger PIT evidence and shows no such gap for these 11. A definitive historical status ledger would require a dated `exchangeInfo` time series, which Binance does not publish free.
- **Dec-2020 archive gaps** for XLM/XRP/ZEC are documented; they are outside the window and do not affect any estimate.
- **Data revision behavior** (whether Binance restates historical klines) remains unresolved; this audit does not address it.
- **Raw ingestion snapshots** remain absent from the repo (`data/raw/` gitignored), so the derived-to-raw provenance is still not reproducible from the repository alone.

## Reproducibility
- Commands: `curl`/S3 XML listings via `urllib` (paginated); `exchangeInfo` via `https://www.binance.com/fapi/v1/exchangeInfo`; canonical/literal config hashes via `sha256sum` + `scripts/generate_grid_manifest.py`.
- Evidence JSON sha256: `4b419069b34e6fe622669b3c690cf1500a609610c8a3435d23523cfc26bfddfd`.
- Grid manifest regenerated to `/tmp/basis-grid-manifest-2946.json`: **324 cells**, `config_sha256 = 55caedf84ac723289f70f49bbed4712c8195425feb4a95e737f3e8929479a0e0`; config literal sha256 `753d9357e1d535ef4229a901e25ef059a751e4c4d56188247f5f2e0ef1debd16`.