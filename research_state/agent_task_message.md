# Initial task message — EBCR-001 (activation 6)

Read AGENTS.md, SKILLS.md, research_state/agent_handoff.md, research_state/agent_task_message.md, prompts/continuous_research_operating_contract_v1.md, docs/research_protocol.md, configs/basis_crash_grid_v1.json.

## What was done this activation
- Required checks pass: grid manifest 324 cells, config_sha256=55caedf84ac723289f70f49bbed4712c8195425feb4a95e737f3e8929479a0e0 matches frozen config; 11 unittest tests pass; git diff --check clean.
- PIT rank search expanded (2026-10-24T23:53:00+00:00): checked Zenodo (limited coins/time windows), Kaggle CMC (2023 snapshot, auth constraints), Wayback CMC historical pages (require scraping), GitHub scrapers (no committed bulk dataset). No free no-key bulk PIT market-cap rank history covering 2019-2024 for all 13 candidates located. research_state/pit_rank_search_v1.json updated. rank_verified remains false for all 13.
- No artifacts modified; frozen anchor/config and Q1/extended artifacts untouched.

## Verified state
- Anchor null preserved: crash_incidence_15pct adj p 0.248, expected_shortfall_5pct_forward_mae adj p 0.949.
- 2,592 registered tests; 2,451 with p-values; 141 blocked; 424 Holm-significant with dependence caveats.
- PIT listing: 13/13 symbols listing_verified=true; 0/13 rank_verified=true.
- PIT rank search: no free no-key bulk PIT market-cap rank history source located covering full 2019-2024 window for all candidates. Rank remains unverified.
- H002 (cheap_negative) and H003 (absolute_extreme) remain registered_secondary_not_tested; not preregistered from grid hits.

## Your task
1. Continue PIT rank search with sources not yet checked (e.g. CoinGecko historical market cap snapshots if available via archives, CryptoRank archives, Nomics historical, CoinCodex, Messari free archives, academic datasets like CRIX/indices, or public data repos). Record source, timestamp, checksum/retrieval details in research_state/pit_rank_search_v1.json for every source checked, whether or not usable. Do not fabricate ranks.
2. If a defensible free PIT market-cap rank history source is found, update research_state/pit_universe_verification_v1.json accordingly (rank_verified only with full point-in-time evidence) and update handoff. Otherwise keep rank_verified=false and continue coverage-cohort approach. Do not project current ranks backward.
3. Do not preregister cheap-negative/absolute-extreme from grid hits. Any separate preregistration needs its own anchor/config, independent predeclared rationale, and new experiment ID. Do not modify frozen anchor/config or Q1/extended artifacts.
4. Run required checks after any change: python3 scripts/generate_grid_manifest.py --output /tmp/basis-grid-manifest.json ; python3 -m unittest discover -s tests ; git diff --check.
5. Update handoff and task message with verified findings only. A concrete next task must always remain.

## Boundary
Free public data only. No fabrication. Preserve null/failed/exclusions. Complete horizons only.
