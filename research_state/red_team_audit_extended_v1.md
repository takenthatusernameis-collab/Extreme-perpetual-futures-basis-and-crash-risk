# Red-team audit — EBCR-001-REDTEAM-EXTENDED-V1

- Report: `research_state/red_team_audit_extended_v1.json`
- Experiment: EBCR-001-BASELINE
- Window: 2023-01-01..2024-04-02
- Generated: 2026-10-24T21:52:41Z

## Leakage / permutation / placebo
- Thresholds use past-only (shift(1)): **True**
- Labels start at t+1: **True**
- Permutation/ES permutation implemented: **True**

## Overlapping horizons & dependence
- 7/14/28-day horizons overlap heavily (common forward windows).
- Caveat: Holm controls FWER across tests but does not eliminate dependence-induced correlation in effects.

## Survivorship / missingness / selection
- Exclusions preserved: **336**; reasons: {'missing_label': 336}

## Confounding vs prior-only controls
- Predeclared: past 7/30d returns, past 30d volatility/drawdown, BTC/market returns/vol, funding, liquidity/turnover, open interest (when reliable)
- Not exhaustively re-estimated in this pass; recommend stratified/regression with controls in follow-up.

## Multiplicity (full family)
- Registered: 2592, with p-value: 2451, blocked: 141
- Holm-significant (full family): **424/2451** (17.3%)

## Anchor co-primary
- crash_incidence_15pct: p_unadj=0.124, adj_anchor=0.248
- expected_shortfall_5pct_forward_mae: p_unadj=0.949, adj_anchor=0.949
- NOT SIGNIFICANT after correction (adj p 0.248, 0.949). Primary hypothesis not supported.

## Conclusion
- No evidence of support for the primary anchor after multiplicity correction. Many grid cells show unadjusted/adjusted significance but dependence and potential confounding preclude strong claims; interpret as suggestive only with heavy caveats. Null result is preserved.
