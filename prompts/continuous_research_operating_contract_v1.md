# Continuous Research Operating Contract v1

**Program:** EBCR-001 — Extreme Perpetual-Futures Basis and Crash Risk  
**Status:** Active continuous research; no empirical result is verified yet  
**Scope:** Free public data, open-source tools, historical research only

## Iterative improvement record

This operative prompt is the result of three explicit refinement passes, completed before empirical execution.

### Pass 1 — Make the hypothesis testable
Clarified that the target is forward crash incidence and downside-tail severity, not necessarily negative mean returns. Fixed signal definition, direction, 7/14/28-day horizons, primary anchor, parameter grid and outcomes.

### Pass 2 — Red-team the identification
Added time-causal feature construction, point-in-time ranks and contract lifecycles, survivorship controls, complete-horizon requirements, embargoes, missingness rules, overlap-aware uncertainty, placebos, full-family multiplicity correction and an anchor-only holdout.

### Pass 3 — Make execution auditable and resumable
Added stable IDs and hashes, machine-readable preregistration, six terminal statuses, free-source rules, persistent candidate frontier, bounded checkpointing, regression tests, failure recovery, handoffs and explicit limits on uptime claims.

Improve this prompt further when a material ambiguity is discovered, but never change this frozen configuration after outcomes are visible. Any material design change requires a new version/experiment ID and a documented reason.

## Mission

Test whether extreme perpetual-futures basis conditions predict more frequent and more severe underlying-asset crashes over the next 1–4 weeks.

**Primary conjecture:** a very rich positive perpetual basis can indicate crowded-long exposure and elevated forward downside tail risk. **Secondary hypotheses:** extremely cheap negative basis and extreme absolute basis magnitude may also predict crashes. These directions must remain separate; never merge them after seeing results.

This is a predictive-risk study, not a claim of causation, not a trading or shorting instruction and not a profitability backtest. Average returns may be flat or positive while crash probability or severity rises. Do not require negative average returns or optimize average returns.

## Immediate execution sequence

1. Read `AGENTS.md`, `SKILLS.md`, the handoff and task files, this contract, the grid config, sources documentation and relevant skills.
2. Run tests and regenerate the deterministic manifest. Confirm exactly 324 unique configuration IDs/hashes and presence of the frozen anchor.
3. Audit free data sources, actual historical coverage, revision behavior, rate limits, point-in-time market-cap/rank availability and contract identity/lifecycle records. Record evidence before computing outcome variables.
4. Persist raw response/file hashes, retrieval times, source-specific last-complete UTC timestamps, gap/exclusion ledgers and exact code/config revisions.
5. Determine chronological boundaries from dates and coverage only, before calculating forward outcomes. Split unique UTC formation dates chronologically 60% development / 20% validation / 20% historical holdout, with a 28-day embargo at every boundary.
6. Execute the full grid only on development. On validation and historical holdout, evaluate the fixed anchor only. A new genuinely forward block is also anchor-only and cannot be evaluated until complete horizons close.
7. Checkpoint bounded batches, record all cell statuses and update frontier, registry, run manifest, handoff and next task. If one source or cell blocks, continue with other unblocked work.

## Frozen basis definition

`basis_pct = 100 * (perpetual_mark_price / contemporaneous_underlying_spot_or_index_price - 1)`.

Normalize all timestamps to UTC. Produce each UTC daily basis as the median of valid timestamp-aligned samples. Record matching tolerance, sample count and coverage; do not interpolate unmatched mark/index observations. The grid then forms a rolling median feature for the last 1, 3 or 7 completed daily basis values.

For formation day `t`, estimate thresholds only from the preceding `L` valid completed daily feature values, excluding the current feature from the reference distribution. `L` is 90, 180 or 365 days, and every cell requires the full valid history. Do not shorten a window or substitute another estimator to rescue a cell.

- `rich_positive`: feature at t exceeds historical q quantile.
- `cheap_negative`: feature at t falls below historical (1−q) quantile.
- `absolute_extreme`: absolute feature at t exceeds historical q quantile of absolute feature.
- q ∈ {0.90, 0.95, 0.975, 0.99}.

## Exact registered parameter grid

The authoritative source is `configs/basis_crash_grid_v1.json`.

| Axis | Values |
|---|---|
| Basis feature aggregation | 1, 3, 7 days |
| Trailing reference window | 90, 180, 365 valid completed days |
| Orientation | rich positive, cheap negative, absolute extreme |
| Tail quantile | 0.90, 0.95, 0.975, 0.99 |
| Forward horizon | 7, 14, 28 completed UTC days |

Total grid = 3 × 3 × 3 × 4 × 3 = **324 configurations**. Never silently add axes or change the grid under the same ID. Every configuration emits all eight registered endpoints, for a grid-wide family of **2,592 cell-endpoint tests**.

**Frozen primary anchor:** 1-day feature × 90-day reference × rich-positive × q=0.95 × 14-day horizon. Do not select or replace it based on the grid. Cheap-negative and absolute-extreme tests are separate registered secondary hypotheses.

## Outcomes and causal time alignment

Signal formation happens only after UTC day `t` is fully complete. For horizon h, define the forward maximum adverse excursion (MAE):

`MAE_h = min(spot_or_index_low[t+1 ... t+h]) / spot_or_index_close[t] - 1`.

Use underlying spot/index lows for primary endpoints so a perpetual mark/price series is not both the predictor and the sole crash label. Perpetual price outcomes are secondary. Require every day and the entire horizon; never truncate a horizon or allow windows to cross split boundaries.

The eight registered endpoints are:
1. crash incidence at MAE ≤ −10%;
2. crash incidence at MAE ≤ −15%;
3. crash incidence at MAE ≤ −20%;
4. volatility-scaled crash at MAE / (σ₃₀√h) ≤ −2;
5. same at ≤ −3;
6. same at ≤ −4;
7. mean forward MAE;
8. expected shortfall of MAE in the worst 5% of observations.

For volatility scaling, σ₃₀ is the standard deviation of the 30 valid daily log returns ending at `t−1`. More negative MAE or expected-shortfall means more severe downside tail risk. Forward close-to-close returns are secondary diagnostics only.

## Inference and multiplicity

- Report exposed/control event rates, absolute risk difference, risk ratio, confidence intervals, severity estimates, unique asset/event counts, effective calendar-block counts, coverage and exclusions.
- The primary anchor has two co-primary endpoints: 15% crash incidence and worst-5% expected-shortfall severity. Holm-adjust across these two endpoints separately for validation, historical holdout and each truly sealed forward block.
- The exploratory development family is all 324 configurations × 8 endpoints = 2,592 tests. Apply Holm across the **entire** family, not per asset, per horizon or per parameter group.
- Use a predeclared moving-block bootstrap over 56-day calendar blocks sampled jointly across assets, with 28- and 84-day block-length sensitivity. Preserve the serial dependence caused by overlapping horizons and common market shocks.
- Use asset and calendar-week effects where estimable. Pre-registered prior-only controls are past 7/30-day returns, past 30-day volatility and drawdown, BTC/market returns and volatility, funding, liquidity/turnover, and open interest when reliable. Covariates must be known at formation time; do not forward-fill.
- Unadjusted estimates are descriptive; do not choose whichever model gives the smallest p-value. Use cluster-preserving permutations and a placebo in which future basis is tested against already-realized past crashes.
- If event counts, effective blocks or coverage are too small, report inconclusive/blocked status and the exact reason. Never loosen a gate after observing outcomes.

## Point-in-time expanding universe

Candidate discovery must continually advance through descending latest publicly available market-cap rank, with no fixed top-N cutoff. A batch size is a checkpoint size, never a final universe limit. Persist each source response, timestamp, rank, cursor, ID and checksum. When a page or source is exhausted, try the next documented page/source; declare exhaustion only after recording the actual limits and alternatives tried.

Candidate ranking is not historical membership. At each formation date, historical universe eligibility requires defensible point-in-time market-cap/rank evidence and valid listing, delisting, migration, spot, index and perpetual contract mappings. Current rank must never be projected backward. If PIT rank history is unavailable, preserve the asset as rank-unverified or a clearly separate coverage cohort; do not silently exclude it or treat it as eligible. Keep delisted contracts, ticker reuse, redenominations and migrations in the audit.

Process the next candidate if one is blocked. No paid APIs, paid data, trials, subscriptions, paid compute, secret credentials or gated scraping. Prefer official public endpoint/history sources listed in `docs/sources.md`, but verify current access and data coverage rather than assuming.

## Complete accounting of cells and evidence

Each cell has exactly one terminal status:
- `ok`
- `blocked`
- `failed`
- `incomplete`
- `invalid`
- `not_run`

Every non-`ok` status requires a reason, evidence path and next step where appropriate. A manifest does not mean a grid ran. Store experiment/config IDs, canonical hashes, source and data cutoffs, input hashes, method/code revision, full command, start/end status, outputs, missingness and exclusions. Never overwrite previous outputs; new data, code or rules require new identifiers and paths. Preserve all unfavorable, null, contradictory, failed and not-run states.

## Autonomous continuation

Research remains active until explicitly stopped by the repository owner. Within this repository and historical-only boundary, do not wait for another manual experiment ID. Generate a unique ID from the local registry, preregister before outcome calculation, and continue the highest-value unblocked task. A data source failure does not stop tests, source discovery, candidate mapping, integrity checks, red-team work or a new separately registered hypothesis.

At every activation:
1. verify the current branch, workflow status, tasks, state, cutoff, pending cells and diagnostics;
2. pick a measurable task and save a checkpoint;
3. run the relevant tests and inspect the diff;
4. update state/handoff and write the next task;
5. report only verified work, with exact blockers and commands.

The scheduled workflow is resumable, not a promise of literal uninterrupted uptime. A successful job or test is not evidence of a predictive effect. Do not conclude causality or tradability from this study alone.
