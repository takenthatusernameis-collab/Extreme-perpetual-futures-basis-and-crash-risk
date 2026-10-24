# Next task — EBCR-001

Read AGENTS.md, SKILLS.md, research_state/agent_handoff.md, prompts/continuous_research_operating_contract_v1.md, docs/research_protocol.md, configs/basis_crash_grid_v1.json.

## Context
- Extended evaluation complete: anchor null (adj p 0.248, 0.949), 424/2451 Holm-significant with dependence caveats.
- Red-team audit done: research_state/red_team_audit_extended_v1.json (+md).
- Negative results report: research_state/negative_results_report_v1.json (+md).
- Exclusions 336 preserved; all 324 cells ok.

## Immediate deliverables
1. PIT universe hardening: use `point-in-time-universe` skill to improve rank/listing evidence for mapped symbols (ADAUSDT,BCHUSDT,BNBUSDT,DOGEUSDT,LINKUSDT,NEARUSDT,SOLUSDT,TRXUSDT,XLMUSDT,XRPUSDT,ZECUSDT). Record sources/timestamps/checksums; mark rank-verified vs rank-unverified. Do not infer history from current ranks.
2. Prior-only controls robustness (exploratory, documented): test anchor with predeclared controls (past returns/vol/drawdown, BTC, funding) where available; report controlled estimates/p-values without changing anchor or unblinding selection. Preserve all outputs.
3. Update handoff/next task with results; if controls meaningfully change interpretation, document caveats without softening the null.

## Boundary
Free public data only. No fabrication. Preserve null/failed/exclusions. Complete horizons only. Do not modify Q1 artifacts, evaluation reports, or the frozen anchor/config.

## Commands
python3 scripts/generate_grid_manifest.py --output /tmp/basis-grid-manifest.json
python3 -m unittest discover -s tests -q
git diff --check
