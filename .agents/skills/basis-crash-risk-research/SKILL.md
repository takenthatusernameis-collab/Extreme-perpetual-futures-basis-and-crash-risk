---
name: basis-crash-risk-research
description: Preregister and test whether extreme perpetual-futures basis predicts future crash frequency and downside-tail severity over 7–28 days. Use for experiment design, grid execution, outcome analysis, or interpretation; not for trading.
---

# Basis-to-crash research

1. Read the operating contract and immutable JSON grid. Confirm experiment ID, config hash, UTC cutoff, input manifest and split boundaries are recorded before outcomes are computed.
2. Confirm the fixed anchor: 1-day basis aggregation, 90-day trailing reference, rich-positive, q95, 14-day horizon.
3. Basis (%) = 100 × (perpetual mark / contemporaneous underlying spot/index − 1). Build daily UTC medians from timestamp-aligned observations; preserve sample count and coverage.
4. For each formation day t, calculate 1/3/7-day rolling median features. Estimate threshold only from the preceding 90/180/365 valid daily features; exclude t from the reference history.
5. Rich-positive uses q, cheap-negative uses 1−q, and absolute-extreme uses q of absolute basis. Never merge orientations after inspecting results.
6. Primary risk outcome uses underlying spot/index lows: forward MAE = minimum low over t+1 through t+h divided by spot/index close at t, minus one. Require complete horizons and respect a 28-day split embargo.
7. Run exactly the 324 frozen configs and all eight endpoints. Holm-correct the full 2,592 cell-endpoint family. For the fixed anchor, Holm-correct the 15% crash-incidence and worst-5% MAE expected-shortfall co-primary endpoints within each protected split.
8. Use a 56-day moving-block bootstrap sampled jointly across assets; test 28- and 84-day block lengths as robustness. Report effects, intervals, event counts, effective blocks, coverage and adjusted p-values.
9. Treat missing histories, thin tails, unstable estimates and incomplete horizons as blocked/invalid/inconclusive—not as a reason to improvise replacement parameters.
10. Preserve all adverse findings. Predictive association is not causality or profitability.
