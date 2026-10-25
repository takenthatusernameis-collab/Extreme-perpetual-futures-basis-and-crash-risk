# Red-team audit — EBCR-001-REDTEAM-EXTENDED-V1

- Report: `research_state/red_team_audit_extended_v1.json`
- Experiment: EBCR-001-BASELINE
- Window: 2023-01-01..2024-04-02
- Generated: 2026-10-25T13:46:33Z

## Leakage / permutation / placebo
- Thresholds use past-only (shift(1)): **True**
- Labels start at t+1: **True**
- Permutation/ES permutation implemented: **True**

## Overlapping horizons & dependence
- 7/14/28-day horizons overlap heavily (common forward windows).
- Caveat: Holm controls FWER across tests but does not eliminate dependence-induced correlation in effects.

## Survivorship / missingness / selection
- Exclusions preserved: **336** (reasons: None)
- Exclusions preserved: **336**
- Exclusions recorded and preserved (missing_label=336).
- PIT rank verification completed via Wayback Machine CMC historical snapshots (__NEXT_DATA__ parsed); rank_verified=true for all 13 Binance-UM perp symbols in the coverage cohort (see research_state/pit_rank_verification_v1.json).
- PIT ranks now verified for the coverage cohort (13 symbols) via free Wayback-CMC snapshots; selection risk from missing rank history is reduced for this cohort. Residual missingness (exclusions=336, missing_label) remains recorded and preserved.

## Confounding vs prior-only controls
- Predeclared: past 7/30d returns, past 30d volatility/drawdown, BTC/market returns/vol, funding, liquidity/turnover, open interest (when reliable)
- Not exhaustively re-estimated in this pass; recommend stratified/regression with controls in follow-up.

## Multiplicity (full family)
- Registered: 2592, with p-value: 2451, blocked: 141
- Holm-significant (full family): **424/2451** (17.3%)

## Anchor co-primary
- NOT SIGNIFICANT after correction (adj p 0.248, 0.949). Primary hypothesis not supported.
- Adj p: crash_incidence_15pct=0.248, expected_shortfall_5pct_forward_mae=0.949

## Conclusion
- No evidence of support for the primary anchor after multiplicity correction. Many grid cells show unadjusted/adjusted significance but dependence and potential confounding preclude strong claims; interpret as suggestive only with heavy caveats. Null result is preserved.
