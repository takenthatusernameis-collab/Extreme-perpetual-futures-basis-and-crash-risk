# Agent handoff — EBCR-001

## Status
- Research design initialized; no empirical finding verified.
- Frozen config: configs/basis_crash_grid_v1.json (config_sha256=55caedf84ac723289f70f49bbed4712c8195425feb4a95e737f3e8929479a0e0).
- Grid manifest generated: research_state/grid_manifest_v1.json (324 cells).
- Tests: 11 passed (unittest).
- Universe frontier: 25 discovery candidates (rank-unverified).
- Candidate-to-perp mapping: research_state/candidate_perp_mapping_v1.json (updated with archive verification).
- S3 XML listing implemented: scripts/s3_xml_listing.py; verified coverage via s3_xml_listing.
- Q1 2024 ingestion (BTCUSDT+ETHUSDT): research_state/ingestion_btc_eth_q1_2024.json (ok, coverage 1.0 for both, 91 days each).
- Data coverage ledger: research_state/data_coverage_ledger.json (all verified symbols audited for Q1 2024).
- Basis computation (BTC+ETH): research_state/basis_computation_q1_partial.json (182 obs).
- Basis computation (all 13 verified symbols): research_state/basis_computation_q1_all.json (1001 obs, coverage 1.0 all symbols, 91 days each, 2024-01-01..2024-03-31).
- Crash label skeleton: research_state/crash_labels_skeleton_q1.json (horizons 7/14/28, not computed).

## Completed this session
- Extended basis computation to 11 remaining verified symbols (BNB,XRP,SOL,TRX,ZEC,DOGE,LINK,ADA,XLM,NEAR,BCH) for Q1 2024 via S3 daily klines + monthly funding; 91 days each, coverage 1.0.
- Wrote research_state/basis_computation_q1_all.json (1001 observations) with per-day basis_pct, component medians and hashes.
- Created crash label skeleton placeholder (MAE 7/14/28) pending full horizon availability.

## Next action
1. Obtain spot/index data beyond 2024-03-31 to complete forward horizons (7/14/28d) for crash labels; compute MAE over 7/14/28 using spot/index lows.
2. Compute crash labels and append to basis dataset; verify complete horizons only.
3. Update handoff/next task with concrete numbers.

## Reporting rules
Separate completed, blocked, failed, incomplete and not-run. Preserve exclusions. A concrete next task must always remain.
