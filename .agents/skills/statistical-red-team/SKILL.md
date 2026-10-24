---
name: statistical-red-team
description: Audit leakage, survivorship, overlapping horizons, sparse crash tails, confounding, multiplicity and regime dependence. Use before accepting an effect or changing a hypothesis; never use a sealed holdout for parameter search.
---

# Red-team checklist

- Reconstruct each signal timestamp and prove all inputs were available at formation close.
- Verify thresholds use prior observations only, forward labels start at t+1 and complete horizons stay inside chronological splits with a 28-day embargo.
- Audit point-in-time ranks, listing/delisting history, migrations, renamed tickers, missing index constituents, and whether missingness selects survivors.
- Quantify overlapping windows, event counts, effective time blocks and common shocks; use block uncertainty.
- Report base/signal event rates, risk differences, risk ratios, confidence intervals, MAE severity, worst-5% ES, asset counts and all exclusions.
- Apply Holm across all 2,592 exploratory grid endpoint tests. Apply Holm to the two anchor co-primary endpoints inside each validation, historical holdout and sealed forward block.
- Check placebo signals against already-realized crashes, cluster-preserving permutations, and that thresholds exclude current/future observations.
- Compare the registered model to predeclared prior-only controls; never choose the model with the best p-value.
- Test 28/56/84-day bootstrap blocks, regimes, liquidity cohorts and other free venues as robustness, clearly labelled exploratory unless preregistered.
- If effective samples or history are too small, conclude inconclusive. Do not relax the gate after seeing outcomes.
- Predictive association is not causality and is not evidence that a trade or short position is profitable.
