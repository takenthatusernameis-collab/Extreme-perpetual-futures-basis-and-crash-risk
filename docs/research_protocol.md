# Research protocol

## Hypothesis and scope
Primary: unusually rich positive perpetual-futures basis predicts greater underlying-asset crash incidence and downside-tail severity over the next 14 days. Seven- and 28-day horizons are prespecified secondary horizons. Cheap-negative and absolute-extreme basis are separate secondary hypotheses. Average returns are not the primary target.

## Signal
`basis_pct = 100 * (perpetual_mark / spot_index - 1)`. Build UTC daily medians from timestamp-aligned observations. Use rolling median features over 1/3/7 days. For formation day t, calculate thresholds from the preceding 90/180/365 valid daily observations, excluding the current feature. Rich-positive uses q; cheap-negative uses 1−q; absolute-extreme uses q of absolute basis. Require full history.

## Forward outcomes
For horizon h in {7,14,28} complete days:
`MAE_h = min(spot/index low[t+1..t+h]) / spot/index close[t] - 1`.
Crash indicators: MAE ≤ −10%, −15%, −20%. Vol-scaled indicators: MAE / (sigma_30 × sqrt(h)) ≤ −2, −3, −4, using only the 30 valid daily log returns ending t−1. Severity endpoints are mean MAE and worst-5% expected shortfall of MAE. Require complete labels. Perpetual price and close-to-close return outcomes are secondary.

## Exact grid
The JSON config is authoritative. Aggregation {1,3,7} × reference window {90,180,365} × orientation {rich_positive, cheap_negative, absolute_extreme} × quantile {0.90,0.95,0.975,0.99} × horizon {7,14,28} = 324 configurations. Fixed anchor: 1-day aggregate, 90-day reference, rich-positive, q95, 14 days. Each configuration reports 8 endpoints: 2,592 grid endpoint tests. Apply Holm across the entire development family. The anchor's co-primary endpoints are 15% crash incidence and worst-5% expected-shortfall severity; Holm-correct those two endpoints within each protected evaluation split.

## Chronology
Choose split boundaries from unique UTC dates and source coverage before calculating outcomes. Use chronological 60% development, 20% validation, 20% historical holdout. Enforce a 28-day embargo at boundaries. Grid is development-only; validation and historical holdout are anchor-only. After preregistration, start a forward block beyond the frozen latest-closed UTC cutoff and evaluate only the anchor after full horizons close. Do not use previously inspected dates as fresh independent evidence.

## Statistical inference
Use a consistent preregistered estimator. Report signal/non-signal rates, absolute risk difference, risk ratio, intervals, event counts, asset counts, effective time blocks, mean MAE, 5% expected shortfall, coverage and exclusions. Use asset and calendar-week effects where estimable, plus prior-only controls (past 7/30-day return, past 30-day volatility/drawdown, BTC/market returns and volatility, funding, turnover/liquidity and open interest when complete). Missing covariates remain missing.
Use a moving-block bootstrap with 56-calendar-day blocks sampled jointly across assets; sensitivity uses 28 and 84 days. The family must account for overlapping horizons and common market shocks. Thin data or unstable inference means inconclusive, never an excuse to relax gates.

## Expanding point-in-time universe
Discover new candidate assets in descending latest public market-cap rank with no fixed top-N cutoff. The rank frontier is for discovery only. Historical membership requires a defensible point-in-time cap/rank and asset/contract lifecycle at each formation date. Today's rank cannot be backfilled. Rank-unverified candidates remain visible as blockers or in a labelled coverage cohort. Preserve delisted, renamed and migrated contracts and every exclusion.

## Data gates
Require ≥95% valid daily coverage inside each analyzed feature/reference window, UTC timestamps, unique timestamps, positive plausible prices, documented spot/index/perpetual identity and contract lifecycle. Freeze source-specific cutoffs and raw hashes. No look-ahead interpolation, forward-filled prices/basis/funding/ranks or truncated outcomes.

## Cell status accounting
Every cell has one terminal status: `ok`, `blocked`, `failed`, `incomplete`, `invalid` or `not_run`. Every non-ok status needs a reason and evidence path. A manifest never proves execution. Report all null, adverse, contradictory, failed and not-run results; preserve confidence intervals and effect sizes regardless of significance.

## Reproducibility and continuity
Store code revision, config hash, data cutoff, raw/normalized hashes, source coverage, estimator/method version, commands, status, exclusions and output hashes. Writes must be atomic and resume idempotently. New code/data/design versions require new IDs. Every session updates handoff and next task. A blocked cell should not stop other candidate discovery, testing, source audit or red-team work. The scheduled loop is resumable, not guaranteed always-on.

## Falsification standard
Support requires materially increased 15% crash incidence and more severe tail-severity estimates at the fixed anchor in validation and historical holdout, with uncertainty and multiplicity reported and no evident leakage. Independent future blocks may strengthen or reverse a conclusion. If uncertainty is wide or effective counts sparse, conclude inconclusive. Repeated null/negative sealed results should remain a negative finding. Nothing here proves causality or tradability.
