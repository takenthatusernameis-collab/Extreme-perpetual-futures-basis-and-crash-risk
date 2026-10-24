# Initial task message — EBCR-001 (activation 2)

Read AGENTS.md, SKILLS.md, research_state/agent_handoff.md, prompts/continuous_research_operating_contract_v1.md, docs/research_protocol.md, configs/basis_crash_grid_v1.json.

## What was done this activation
- Re-ran Binance Vision S3 XML listing for the 6 symbols that had null listing metadata (BTCUSDT, ETHUSDT, BNBUSDT, DOGEUSDT, ADAUSDT, BCHUSDT). All 13 mapped symbols now carry a verified `retrieved_at_utc` and `sha256_last_page`. Earliest/latest zip dates and missing counts are unchanged and re-confirmed (see research_state/pit_universe_verification_v1.json).
- Re-verified required checks: grid manifest regenerated (324 cells; config_sha256=55caedf84ac723289f70f49bbed4712c8195425feb4a95e737f3e8929479a0e0 matches frozen config), 11 unittest tests pass, git diff --check clean.
- Preserved rank_verified=false for all 13 symbols. No current ranks projected backward.
- Documented the explicit decision not to preregister cheap-negative / absolute-extreme from grid hits (H002/H003 remain registered_secondary_not_tested).

## Verified state
- Anchor null preserved: crash_incidence_15pct adj p 0.248, expected_shortfall_5pct_forward_mae adj p 0.949.
- 2,592 registered tests; 2,451 with p-values; 141 blocked; 424 Holm-significant with dependence caveats.
- PIT listing: 13/13 symbols listing_verified=true; 0/13 rank_verified=true.
- PIT rank search (2026-10-24T22:51:53Z): no bulk free PIT market-cap rank history source located (CMC/Wayback CDX, CoinMetrics Community API, CoinPaprika checked).

## Artifact inconsistency (do not "fix" by fabrication)
7 symbols (XRPUSDT, SOLUSDT, TRXUSDT, ZECUSDT, LINKUSDT, XLMUSDT, NEARUSDT) have verified `retrieved_at_utc` (2026-10-24T21:58:10Z) but null `sha256_last_page`, because their source entries predate the sha256 field in the listing output. Their listing dates and missing counts are verified and consistent with re-runs; only the last-page hash is absent. No hashes were synthesized.

## Your task
1. Continue the PIT rank search. Try additional free sources for point-in-time market-cap rank history (e.g. Wayback CDX scraping of CoinMarketCap historical pages, CoinGecko historical market-cap endpoints, CryptoCompare, exchange-archived snapshots). Record source, timestamp and checksum in research_state/pit_rank_search_v1.json for every source checked, whether or not it yields usable data. Do not fabricate ranks; do not project current ranks backward.
2. If a defensible PIT rank source is found, update research_state/pit_universe_verification_v1.json accordingly (rank_verified may become true only with full point-in-time evidence) and update the handoff. If none is found, keep rank_verified=false and continue with the coverage-cohort approach.
3. Do not preregister cheap-negative or absolute-extreme from grid hits. Any separate preregistration needs its own anchor/config, independent predeclared rationale, and a new experiment ID. Do not modify the frozen anchor/config or Q1/extended artifacts.
4. Run the required checks after any change: `python3 scripts/generate_grid_manifest.py --output /tmp/basis-grid-manifest.json`, `python3 -m unittest discover -s tests -q`, `git diff --check`.
5. Update research_state/agent_handoff.md and research_state/agent_task_message.md with verified findings only. Preserve null/failed/exclusions. A concrete next task must always remain.

## Boundary
Free public data only. No fabrication. Preserve null/failed/exclusions. Complete horizons only. Do not modify Q1 artifacts, evaluation reports, or the frozen anchor/config.