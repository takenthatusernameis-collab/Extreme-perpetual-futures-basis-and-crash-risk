# PIT ranks vs anchor interpretation — EBCR-001

Date: 2026-10-25T13:48:11Z
Source artifacts:
- research_state/evaluation_summary_extended_v1.md (anchor null: adj p 0.248/0.949)
- research_state/pit_rank_verification_v1.json (rank_verified=true for all 13; ranks are conservative upper bounds at snapshots >= formation)
- research_state/red_team_audit_extended_v1.md (updated for PIT verification; no finding depended on rank-unverified)

## Finding
PIT market-cap ranks are now verified via free Wayback-CMC snapshots for all 13 symbols in the coverage cohort (BTC=1, ETH=2, BNB up to 11, XRP up to 8, SOL ranges 5-120, TRX 10-32, LINK 6-21, ADA/XLM/DOGE/ZEC/NEAR as in verification). Ranks are snapshot-based at/after formation dates, so they are conservative upper bounds (rank can fall after listing, not rise before).

The anchor test (rich-positive, 90-day ref, q95, 1-day agg, 14-day forward; crash_incidence_15pct and ES_5% MAE) remains null after Holm correction (adj p 0.248, 0.949). The red-team audit was re-run after PIT verification and found no prior finding depended on the rank-unverified assumption; survivorship/selection notes were updated accordingly.

**Conclusion:** Verified PIT ranks do not change the interpretation of the null anchor result for the coverage cohort. No non-null implication arises. Exclusions (336, missing_label) and cell status (324 ok) remain unchanged.

## Constraints preserved
- No preregistration from grid hits.
- Frozen artifacts untouched (config_sha256 55caedf84ac723289f70f49bbed4712c8195425feb4a95e737f3e8929479a0e0).
- H002/H003 remain registered_secondary_not_tested.
- PIT inquiry closed; do not reopen without genuinely new free PIT source.
- /tmp/pit_rank_evidence/ extraction record preserved.
