# Agent handoff — EBCR-001

## Status
- Research design initialized; no empirical finding verified.
- Frozen config: configs/basis_crash_grid_v1.json (config_sha256=55caedf84ac723289f70f49bbed4712c8195425feb4a95e737f3e8929479a0e0).
- Grid manifest generated: research_state/grid_manifest_v1.json (324 cells).
- Tests: 11 passed.
- Universe frontier: 25 discovery candidates (rank-unverified).
- Candidate-to-perp mapping: research_state/candidate_perp_mapping_v1.json (updated with archive verification).
- S3 XML listing implemented: scripts/s3_xml_listing.py; ETHUSDT index=2097 files (400 missing), mark=2464 files (33 missing).
- Multi-day ingestion sample created: research_state/ingestion_multi_day_sample.json (BTCUSDT, ETHUSDT 2024-01-01..10, coverage 100%, gate >=95% met).

## Completed this session
- Extended ingestion prototype to multi-day processing with >=95% coverage gate (scripts/ingestion_multi_day.py). Output saved.
- Verified remaining candidate mappings (ranks 11-25 non-blocked): DOGE/LINK/ADA/XLM/NEAR/BCH have zip files present in um klines daily archives (verified via S3 XML sample). Ranks 11,13,14,15,16,17,19,21,24 remain blocked per mapping rules.
- Began multi-symbol ingestion for BTCUSDT+ETHUSDT over overlapping complete-date window (2024-01-01..10) with full component coverage.

## Next action
1. Expand multi-symbol ingestion to a larger overlapping window (e.g., 2024-01-01..2024-03-31) and enforce >=95% coverage gate per symbol; log gaps.
2. For verified symbols (BTC,ETH,BNB,XRP,SOL,TRX,ZEC,DOGE,LINK,ADA,XLM,NEAR,BCH), audit mark/index/funding coverage completeness and record exclusions.
3. Build basis computation path over ingested days with UTC alignment and no forward-fill.
4. Update handoff/next task with concrete coverage numbers.

## Reporting rules
Separate completed, blocked, failed, incomplete and not-run. Preserve exclusions. A concrete next task must always remain.
