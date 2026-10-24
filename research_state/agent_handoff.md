# Agent handoff — EBCR-001

## Status
- Research design initialized; no empirical finding has yet been verified.
- Frozen config: `configs/basis_crash_grid_v1.json`.
- Expected grid: 324 configurations × 8 endpoints = 2,592 exploratory cell-endpoint tests.
- Fixed anchor: 1-day feature, 90-day reference, rich-positive, q95, 14-day horizon.
- No source cutoff, coverage claim, completed grid or predictive result is established yet.

## Verified setup
- Deterministic manifest generator: `scripts/generate_grid_manifest.py`.
- Regression suite: `python3 -m pytest -q tests`.
- Historical research only; public free data and open-source tooling; no paid services, credentials, orders or live/paper trading.

## Next action
1. Run the tests and generate `research_state/grid_manifest_v1.json`; persist the config hash.
2. Audit actual free-source coverage, point-in-time market-cap/rank history, and public spot/index/mark/funding histories.
3. Freeze source-specific UTC cutoffs and chronological split boundaries before calculating forward outcomes.
4. Implement timestamp/coverage gates and a terminal-status ledger. Do not claim results until a reproducible run completes.

## Reporting rules
Separate completed, blocked, failed, incomplete and not-run tasks. Preserve every excluded candidate and adverse result. A concrete next task must always remain.
