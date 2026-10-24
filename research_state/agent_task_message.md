# Initial task message — EBCR-001 (activation 5)

Read AGENTS.md, SKILLS.md, research_state/agent_handoff.md, research_state/agent_task_message.md, prompts/continuous_research_operating_contract_v1.md, docs/research_protocol.md, configs/basis_crash_grid_v1.json.

## What was done this activation
- Required checks pass: grid manifest 324 cells, config_sha256=55caedf84ac723289f70f49bbed4712c8195425feb4a95e737f3e8929479a0e0 matches frozen config; 11 unittest tests pass; git diff --check clean.
- PIT rank search extended: checked CoinMarketCap listings/historical (API key required), Coinranking rank-history (paid), Kaggle daily tracker (2026 only), Zenodo single-date snapshot. No usable free no-key bulk PIT rank source. rank_verified remains false for all 13.
- research_state/pit_rank_search_v1.json updated with 5 new sources/timestamps. No artifacts modified otherwise; frozen anchor/config and Q1/extended artifacts untouched.

## Verified state
- Anchor null preserved: crash_incidence_15pct adj p 0.248, expected_shortfall_5pct_forward_mae adj p 0.949.
- 2,592 registered tests; 2,451 with p-values; 141 blocked; 424 Holm-significant with dependence caveats.
- PIT listing: 13/13 symbols listing_verified=true; 0/13 rank_verified=true.
- PIT rank search: no free no-key bulk PIT market-cap rank history source located. Rank remains unverified for all candidates.
- H002 (cheap_negative) and H003 (absolute_extreme) remain registered_secondary_not_tested; not preregistered from grid hits.

## Your task
1. Continue PIT rank search with sources not yet checked (e.g. Binance archived market-cap snapshots, alternative archives, academic datasets, public mirrors of CMC historical listings). Record source, timestamp and checksum in research_state/pit_rank_search_v1.json for every source checked, whether or not it yields usable data. Do not fabricate ranks.
2. If a defensible free PIT market-cap rank history source is found, update research_state/pit_universe_verification_v1.json accordingly (rank_verified may become true only with full point-in-time evidence) and update the handoff. If none is found, keep rank_verified=false and continue with the coverage-cohort approach. Do not project current ranks backward.
3. Do not preregister cheap-negative or absolute-extreme from grid hits. Any separate preregistration needs its own anchor/config, independent predeclared rationale, and a new experiment ID. Do not modify the frozen anchor/config or Q1/extended artifacts.
4. Run required checks after any change: python3 scripts/generate_grid_manifest.py --output /tmp/basis-grid-manifest.json ; python3 -m unittest discover -s tests ; git diff --check.
5. Update handoff and task message with verified findings only. A concrete next task must always remain.

## Boundary
Free public data only. No fabrication. Preserve null/failed/exclusions. Complete horizons only.