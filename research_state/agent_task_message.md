# Next task — EBCR-001

Read AGENTS.md, SKILLS.md, research_state/agent_handoff.md, prompts/continuous_research_operating_contract_v1.md, docs/research_protocol.md, configs/basis_crash_grid_v1.json.

## Immediate deliverables
1. Extend ingestion prototype to multi-day processing with >=95% coverage gate; output research_state/ingestion_multi_day_sample.json.
2. Verify remaining candidate mappings (ranks 11-25 non-blocked) against Binance archive file existence; record blocked statuses.
3. Begin multi-symbol ingestion for BTCUSDT+ETHUSDT over overlapping complete-date window.
4. State updates: update handoff and next task.

## Boundary
Free public data only. No REST (Binance). No fabrication. Preserve null/failed.

## Commands
python3 -m unittest discover -s tests -v
python3 scripts/generate_grid_manifest.py --output /tmp/basis-grid-manifest.json
git diff --check
