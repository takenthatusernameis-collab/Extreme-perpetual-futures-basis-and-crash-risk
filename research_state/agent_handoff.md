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
- Data coverage ledger: research_state/data_coverage_ledger.json (all verified symbols audited for Q1 2024: BTC,ETH,BNB,XRP,SOL,TRX,ZEC,DOGE,LINK,ADA,XLM,NEAR,BCH all >=0.95).
- Verified symbols S3 audit: research_state/verified_symbols_s3_audit.json (updated with Q1 2024 window).
- Basis computation: research_state/basis_computation_q1_partial.json (BTCUSDT+ETHUSDT, n=182 observations, per-day basis_pct with component hashes).

## Completed this session
- Collected Q1 ingestion results for BTCUSDT+ETHUSDT (2024-01-01..2024-03-31): status ok, both meet coverage gate (1.0).
- Audited remaining verified symbols (BNB,XRP,SOL,TRX,ZEC,DOGE,LINK,ADA,XLM,NEAR,BCH) for Q1 2024 via S3 XML listing (um/mark/index klines + funding monthly); all meet >=0.95 gate.
- Updated data_coverage_ledger.json and verified_symbols_s3_audit.json with concrete coverage numbers.
- Computed basis for BTCUSDT+ETHUSDT from Q1 ingestion with UTC alignment, no forward-fill; persisted to basis_computation_q1_partial.json with component hashes and timestamps.

## Next action
1. Extend basis computation to remaining audited verified symbols (BNB,XRP,SOL,TRX,ZEC,DOGE,LINK,ADA,XLM,NEAR,BCH) for Q1 2024. Need ingestion-like daily component medians for mark/index/spot/um_kline/funding or compute directly from downloaded daily zips? Current approach used ingestion_btc_eth_q1_2024.json structure; replicate for others or build ingestion objects.
2. Build full Q1 basis dataset (all 13 verified symbols) with UTC medians, no forward-fill, per-observation hashes.
3. Define crash labels from spot/index lows over forward horizons (7/14/28) once basis series complete; ensure complete horizons only.
4. Update handoff/next task with concrete numbers.

## Reporting rules
Separate completed, blocked, failed, incomplete and not-run. Preserve exclusions. A concrete next task must always remain.
