# Extreme Perpetual-Futures Basis and Crash Risk

**Research status:** initialized; hypothesis untested; no empirical result has yet been verified.

This repository tests whether extreme perpetual-futures basis conditions predict a higher frequency and severity of underlying-asset crashes over the next **7, 14 and 28 calendar days**. The primary directional hypothesis is that unusually rich positive perpetual basis can signal crowded-long exposure. Cheap-negative and absolute-basis extremes are separately registered secondary hypotheses.

This is a **tail-risk forecasting study**, not an assumption that average returns must be negative, not a causal claim, and not a trading or profitability backtest.

## Non-negotiable boundaries

- Free public data and open-source tools only; no paid APIs, subscriptions, trials, paid compute, private data, exchange credentials or secrets.
- Historical research only; never place orders or deploy live or paper trading.
- Candidate discovery continuously expands in descending public market-cap rank with no fixed top-N cutoff. Current ranking is for discovery, not historical point-in-time universe membership.
- Preserve delisted assets, data gaps, adverse/null results, failed tests, invalid cells, and blockers. Do not silently omit candidates.
- Freeze each experiment before calculating outcomes. No look-ahead, survival backfill, forward-filled prices/basis/funding, or outcome-informed grid edits.
- A successful workflow run proves automation health, not a predictive effect. Scheduled recovery is resumable, not guaranteed to run without interruption.

## First steps

1. Read `AGENTS.md`, `SKILLS.md`, `research_state/agent_task_message.md` and the operating contract.
2. Validate the grid: `python3 scripts/generate_grid_manifest.py --output research_state/grid_manifest_v1.json`.
3. Run tests: `python3 -m pytest -q tests`.
4. Before evaluating outcomes, freeze source-specific cutoffs, data hashes, coverage, chronological boundaries and the run manifest.

## Grid at a glance

The immutable configuration is `configs/basis_crash_grid_v1.json`: 324 cells formed by 1/3/7-day feature aggregation, 90/180/365-day historical thresholds, three distinct basis orientations, 90/95/97.5/99th percentiles, and 7/14/28-day horizons. Eight endpoints give 2,592 registered grid endpoint tests, Holm-corrected as one family. The fixed primary anchor is 1-day / 90-day / rich-positive / q95 / 14-day.

## Repository map

- `AGENTS.md`: always-on behavior and invariants.
- `SKILLS.md` + `.agents/skills/`: progressive-disclosure agent procedures.
- `prompts/continuous_research_operating_contract_v1.md`: full research and continuation mandate.
- `configs/`, `schemas/`, `scripts/`, `tests/`: preregistration, deterministic manifests, and checks.
- `research_state/`: frontier, hypothesis registry, run manifest, handoff and next task.
- `docs/`: architecture, research protocol, sources and frozen-decision record.
- `.github/workflows/main.yml`: complete scheduled resumable controller and worker script.

The first research activation must establish real source coverage before any empirical conclusion.
