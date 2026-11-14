# Agent task message (EBCR-001) — activation 2953 (written at end of activation 2952)

## Read first (required)
- `research_state/agent_handoff.md` (activation 2952: NO-OP — state-change gate clean, no new source/dated event)
- `research_state/agent_task_message.md` (this message)
- `prompts/continuous_research_operating_contract_v1.md` and `prompts/continuous_research_operating_contract_v1_1_addendum.md`
- `docs/research_protocol.md`
- `configs/basis_crash_grid_v1.json` (frozen)
- `docs/sources.md` (free public source policy — verify actual coverage, never assume)
- `.agents/skills/point-in-time-universe/SKILL.md` (discovery → PIT eligibility; never project current rank backward)

## What changed since the previous activation
- **No research-material change.** Activation 2952 ran the cheap state-change gate: config literal sha256 `753d9357e1d535ef4229a901e25ef059a751e4c4d56188247f5f2e0ef1debd16` and canonical manifest sha256 `55caedf84ac723289f70f49bbed4712c8195425feb4a95e737f3e8929479a0e0` both match frozen; `git status --short` clean; `git diff --check` clean; no new commits under frozen-input paths since activation 2949 checkpoint `d34780d2`. No new admissible source or dated event.
- **Candidate → perpetual-contract mapping v2 is DONE** (activation 2949, committed `d34780d2`). Maps all 75 discovered candidate ids against Binance USD-M `exchangeInfo`: 41 `mapped_discovery_only_unverified`, 25 `no_perp_expected`, 1 `no_trading_perp` (FTM SETTLING), 8 `not_listed_binance_um`, 0 `blocked_unknown`. All mappings are discovery-only; never PIT-verified.
- **Frontier state:** 75 distinct discovered ids; top 75 fully covered; `rank_frontier_exhausted` remains `false`; next scan starts at rank 76 and de-duplicates by stable asset id. All candidates `rank_unverified_discovery_only`.
- `.venv` absent (not recreated — no full gate required for NO-OP). Last known tests: **18 passed** (activation 2948).

## Objective (activation 2953)
Advance the highest-value genuinely unblocked work. Do not manufacture work. Expect at least one real, verifiable deliverable or an explicit, documented blocker. If the state-change gate is clean AND no new admissible source or dated event exists AND the remaining unblocked task is not newly actionable, classify as NO-OP per the v1.1 addendum and exit with the previous verified state intact — do not refresh timestamps or create empty artifacts.

## Required actions (activation 2953)
1. **State-change gate first (cheap):** verify frozen config literal sha256 `753d9357e1d535ef4229a901e25ef059a751e4c4d56188247f5f2e0ef1debd16` and canonical `55caedf84ac723289f70f49bbed4712c8195425feb4a95e737f3e8929479a0e0`; check `git status --short` (clean tree expected) and no new commits under frozen-input paths `scripts/ tests/ configs/ data/ results/ docs/ prompts/ schemas/ research_state/hypothesis_registry.json research_state/universe_frontier.json research_state/integrated_extended_v1.json research_state/evaluation_report_extended_v1.json`. If nothing changed and no task below is newly actionable, NO-OP.
2. **Environment:** `.venv` is absent. Recreate it (numpy 2.5.4, pandas 3.1.1, scipy 1.18.1, statsmodels 0.15.0, pytest 9.2.0) before the test gate can run; PyPI was reachable in prior activations. Do not reinstall unless it is missing and a test gate is required.
3. **Do NOT re-run completed work:** frontier advance v1/v2 (2947/2948), candidate→perp mapping v2 (2949), contract-lifecycle audit (2946), V4 controlled re-estimation (2938), V3→V4 inference audit (2939), exclusion accounting audit (2941). Re-run only if an input changes.
4. **Standing unblocked options (only if a source/date event makes them newly actionable):** advance the frontier to ranks 76–100 in a new artifact (de-duplicate by id). Do not edit frozen `research_state/candidate_perp_mapping_v1.json` — mapping promotion is a separate registration decision.
5. **Blocked (do not proceed without the stated precondition):**
   - **EBCR-H002/H003:** blocked — cannot preregister from inspected grid hits; requires a **new** experiment ID + independent preregistered rationale + a **NEW** anchor/config.
   - **EBCR-H004:** blocked — status change requires a separate preregistration decision; do not change `next_hypothesis_sequence` or statuses.
   - **Contract-lifecycle mapping promotion:** audit evidence exists for the 11 traded symbols, but promoting `candidate_perp_mapping_v1.json` out of `discovery_only_unverified` is a **separate registration decision**.
6. **Preserve invariants:** exclusions n=336 (28 `basis_incomplete` + 308 `incomplete_forward_horizon`); integrated 5,010 rows / 5,346 basis obs; anchor null (`crash_incidence_15pct` adj p 0.24830545694889028; `expected_shortfall_5pct_forward_mae` adj p 0.9485); PIT rank CLOSED; EBCR-H001 `tested_not_supported`; EBCR-H002/H003/H004 `registered_secondary_not_tested`; `next_hypothesis_sequence` 5. No frozen artifact edits; no preregistration derived from grid hits; preserve null/contradictory/failed evidence.
7. **Report only verified findings.** Do not commit unless explicitly asked. Update handoff and write the next task message.

## Required checks
```bash
python3 scripts/generate_grid_manifest.py --output /tmp/basis-grid-manifest.json   # expect 324 cells, canonical sha256 55caedf8…
# .venv must be recreated before: .venv/bin/python -m pytest -q tests  # expect 18 passed
git diff --check
# validate any changed JSON/JSONL/YAML and schemas
```

## Verified baseline (activation 2952, 2026-11-14)
- Mapping v2 artifact: `research_state/candidate_perp_mapping_v2.json`, sha256 `d2b442dd…`, committed `d34780d2`; frontier v2 sha256 `52070b3f…`; both tracked, frozen inputs unmodified.
- Tests: could not run (`.venv` absent); last known `.venv/bin/python -m pytest -q tests` → 18 passed (activation 2948).
- Manifest: 324 cells, canonical sha256 `55caedf8…`; config sha256 `753d9357…`.
- Frontier advance v2 (2948): 75 distinct discovered ids, top rank covered 75, `rank_frontier_exhausted = false`, next scan rank 76.
- Contract-lifecycle audit (2946): all 11 traded symbols `TRADING`/`PERPETUAL`/`USDT`, zero-gap window coverage; evidence JSON sha256 `4b419069…`.
- Exclusion audit (2941): 28 + 308 = 336; no result impact.
- V4 reproducibility (2938): controlled cluster p 0.4931717622839955 (crash_incidence_15pct), 0.4571603439994524 (expected_shortfall), not Holm-significant.
- Anchor null: `crash_incidence_15pct` adj p 0.24830545694889028; `expected_shortfall_5pct_forward_mae` adj p 0.9485.

## Known blockers still open (do not re-probe every activation)
- Raw ingestion snapshots absent from repo (`data/raw/` gitignored) → re-ingestion not reproducible; only derived data.
- Data revision behavior unresolved.
- `exchangeInfo` is a live snapshot; no free historical point-in-time status time series.
- EBCR-H002/H003 not testable without a new preregistration independent of grid hits and a NEW anchor/config.
- EBCR-H004 registry status change requires a separate preregistration decision.
- `.venv` absent; recreate before the test gate.
- Frontier discovery open-ended: 75 ids covered, `rank_frontier_exhausted = false`; next scan starts at rank 76.