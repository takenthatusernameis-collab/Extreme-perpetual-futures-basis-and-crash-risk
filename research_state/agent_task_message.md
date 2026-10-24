# Initial task message — EBCR-001 (activation 3)

Read AGENTS.md, SKILLS.md, research_state/agent_handoff.md, prompts/continuous_research_operating_contract_v1.md, docs/research_protocol.md, configs/basis_crash_grid_v1.json.

## What was done this activation
- Extended PIT rank search: checked CoinGecko (free market_chart has no rank; history limited to 365d), CryptoCompare (API key required, 401), Wayback CDX (unreachable, HTTP 000). No usable free PIT rank source. rank_verified remains false for all 13. research_state/pit_rank_search_v1.json updated with all sources/timestamps.
- Re-verified required checks: grid manifest regenerated (324 cells; config_sha256 matches), 11 unittest tests pass, git diff --check clean.

## Verified state
- Anchor null preserved: crash_incidence_15pct adj p 0.248, expected_shortfall_5pct_forward_mae adj p 0.949.
- 2,592 registered tests; 2,451 with p-values; 141 blocked; 424 Holm-significant with dependence caveats.
- PIT listing: 13/13 symbols listing_verified=true; 0/13 rank_verified=true.
- PIT rank search (2026-10-24T23:45Z): no bulk free PIT market-cap rank history source located (CoinGecko, CryptoCompare, Wayback CDX added to prior list).

## Your task
1. Continue PIT rank search with sources not yet checked (e.g. Binance archived market-cap snapshots, CoinGecko Pro-free tier endpoints, alternative archives, academic datasets). Record source, timestamp and checksum in research_state/pit_rank_search_v1.json for every source checked, whether or not it yields usable data. Do not fabricate ranks.
2. If a defensible PIT rank source is found, update research_state/pit_universe_verification_v1.json accordingly (rank_verified may become true only with full point-in-time evidence) and update the handoff. If none is found, keep rank_verified=false and continue with the coverage-cohort approach.
3. Do not preregister cheap-negative or absolute-extreme from grid hits. Any separate preregistration needs its own anchor/config, independent predeclared rationale, and a new experiment ID. Do not modify the frozen anchor/config or Q1/extended artifacts.
4. Run required checks after any change.
5. Update handoff and task message with verified findings only. A concrete next task must always remain.

## Boundary
Free public data only. No fabrication. Preserve null/failed/exclusions. Complete horizons only.
