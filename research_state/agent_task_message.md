# Next task — EBCR-001 (updated)

Read `AGENTS.md`, `SKILLS.md`, `research_state/agent_handoff.md`, `prompts/continuous_research_operating_contract_v1.md`, `docs/research_protocol.md`, `configs/basis_crash_grid_v1.json`.

## Immediate deliverables
1. **Funding rate discovery:** List S3/archive contents under `data/futures/um/monthly/fundingRate/` for a sample symbol (e.g., BTCUSDT) to confirm actual files/formats. Check for daily funding paths. Record findings in `research_state/source_audit.md` and `research_state/data_coverage_ledger.json`.
2. **Coverage sampling:** Sample major symbols (start with BTCUSDT, ETHUSDT) for spot daily klines, UM futures klines, markPriceKlines, indexPriceKlines. For each, record earliest/latest UTC dates, file counts, schema (CSV columns), gaps. Update `research_state/data_coverage_ledger.json` with concrete windows.
3. **Ingestion design doc:** Create `research_state/ingestion_design.md` documenting UTC alignment, daily aggregation (median of valid timestamp-aligned samples), coverage gates (≥95%), exclusion rules, no lookahead/forward-fill, timestamp gates, basis calculation formula, and how to handle missing mark/index/spot.
4. **Universe scaffold:** Fetch top N from CoinPaprika `/v1/coins` (discovery only), write to `research_state/universe_frontier.json` as rank-unverified candidates with retrieval timestamp/hash. Never use for historical membership.
5. **State updates:** Update handoff with findings/blockers and write clear next task.

## Boundary
Free public data and open-source tools only. No paid services, keys/secrets, exchange credentials, live/paper trading/orders. Never fabricate coverage. Preserve negative/null/failed/not-run results. REST APIs blocked in env - use archives only.

## Commands to run/check
```bash
python3 -m unittest discover -s tests -v
python3 scripts/generate_grid_manifest.py --output /tmp/basis-grid-manifest.json
git diff --check
```
