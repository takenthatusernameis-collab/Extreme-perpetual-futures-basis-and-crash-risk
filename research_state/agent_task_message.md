# Next task — EBCR-001

Read AGENTS.md, SKILLS.md, research_state/agent_handoff.md, prompts/continuous_research_operating_contract_v1.md, docs/research_protocol.md, configs/basis_crash_grid_v1.json.

## Context
- Extended evaluation complete: anchor null (adj p 0.248, 0.949), 424/2451 Holm-significant with dependence caveats. Primary hypothesis NOT supported; null preserved.
- Red-team audit done; negative results report done; prior-only controls robustness done (null preserved).
- PIT verification: listing evidence via S3 XML; rank_verified=false for all 11 symbols. Complete zip dates for XRPUSDT, SOLUSDT, TRXUSDT, ZECUSDT, LINKUSDT, XLMUSDT, NEARUSDT; null earliest/latest for BTCUSDT, ETHUSDT, BNBUSDT, DOGEUSDT, ADAUSDT, BCHUSDT. See research_state/pit_universe_verification_v1.json and research_state/pit_rank_search_v1.json.
- PIT rank search (2026-10-24T22:51:53Z): no bulk free PIT rank history source located.
- Alternative orientation: NOT preregistered. H002 (cheap_negative) and H003 (absolute_extreme) remain registered_secondary_not_tested.

## Immediate deliverables
1. Re-run S3 XML listing (scripts/s3_xml_listing.py) for BTCUSDT, ETHUSDT, BNBUSDT, DOGEUSDT, ADAUSDT, BCHUSDT to fill earliest/latest zip dates and missing counts; update pit_universe_verification_v1.json with verified listing evidence. Preserve rank_verified=false.
2. If a free defensible PIT rank history source appears, record source/timestamp/checksum; else keep rank-unverified and continue coverage-cohort approach. Do not project current ranks backward.
3. Do not preregister cheap-negative/absolute-extreme from grid hits; any separate preregistration needs its own anchor/config, independent predeclared rationale, and new experiment ID — do not modify frozen anchor/config.
4. Update handoff/next task with verified findings only; preserve null/failed/exclusions.

## Boundary
Free public data only. No fabrication. Preserve null/failed/exclusions. Complete horizons only. Do not modify Q1 artifacts, evaluation reports, or the frozen anchor/config.

## Commands
python3 scripts/generate_grid_manifest.py --output /tmp/basis-grid-manifest.json
python3 -m unittest discover -s tests -q
git diff --check