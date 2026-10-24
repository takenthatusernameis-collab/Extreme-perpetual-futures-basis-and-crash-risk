# Next task — EBCR-001

Read AGENTS.md, SKILLS.md, research_state/agent_handoff.md, prompts/continuous_research_operating_contract_v1.md, docs/research_protocol.md, configs/basis_crash_grid_v1.json.

## Immediate deliverables
1. Extend basis computation to remaining audited verified symbols (BNBUSDT, XRPUSDT, SOLUSDT, TRXUSDT, ZECUSDT, DOGEUSDT, LINKUSDT, ADAUSDT, XLMUSDT, NEARUSDT, BCHUSDT) for 2024-01-01..2024-03-31. Use free public S3 data (daily klines for um/mark/index and monthly funding). Compute UTC daily medians, no forward-fill; write research_state/basis_computation_q1_all.json with per-day basis_pct, component hashes, timestamps.
2. Verify data coverage gate met for all symbols in the new basis dataset; log any gaps/exclusions.
3. Prepare crash label skeleton (MAE over 7/14/28d using spot/index lows) once basis complete; do not compute outcomes yet without full horizon availability.
4. Update handoff and next task with concrete numbers.

## Boundary
Free public data only. No REST (Binance). No fabrication. Preserve null/failed/exclusions.

## Commands
python3 -m pytest -q tests 2>&1 | tail -5
python3 scripts/generate_grid_manifest.py --output /tmp/basis-grid-manifest.json
git diff --check
