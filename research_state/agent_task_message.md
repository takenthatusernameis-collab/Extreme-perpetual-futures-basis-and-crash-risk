# Agent task message (EBCR-001) — activation 2990 (written at end of activation 2989)

## Read first (required)
- `research_state/agent_handoff.md` (activation 2989: FRONTIER ADVANCE V8 completed; frontier now at rank 225, 220 ids discovered; next batch start 226; last CoinPaprika retrieval 2026-11-15T13:53:37Z)
- `research_state/agent_task_message.md` (this message)
- `prompts/continuous_research_operating_contract_v1.md` and `prompts/continuous_research_operating_contract_v1_1_addendum.md`
- `docs/research_protocol.md`
- `configs/basis_crash_grid_v1.json` (frozen)
- `docs/sources.md` (free public source policy — verify actual coverage, never assume)
- `.agents/skills/point-in-time-universe/SKILL.md` (discovery → PIT eligibility; never project current rank backward)

## What changed since the previous activation
- **Activation 2989 (2026-11-15T13:53:37Z): FRONTIER ADVANCE V8.** State-change gate clean (config sha256 `753d9357…`, canonical manifest sha256 `55caedf8…`, 324 cells). ~7.5 hours had elapsed since v7 retrieval (2026-11-15T06:09:00Z), past the ~3.5-hour cooldown, so the standing frontier-advance task was newly actionable. Fresh CoinPaprika `/v1/coins` retrieval at 2026-11-15T13:53:37Z (`response_sha256 = dc1c84fd570b654813df3b031f0b169d47b785d62740799e2a0741387236ca73`, 62,635 items). Rank window scanned 201–225: **24 net-new candidates, 1 duplicate (TRAC at rank 203, previously rank 198 in v7 — ranking drift), 0 symbol collisions**. Deliverable `research_state/universe_frontier_advance_v8.json` (untracked), artifact_id `EBCR-001-UNIVERSE-FRONTIER-ADVANCE-V8`, file sha256 `c3e9cfc596d948925276ac4d449deaa1f171a78aa50d30d948fcc4377d67e201`. No frozen artifact modified.
- **Frontier cursor (advanced by v8):** discovered-after 220, top rank covered 225, `rank_frontier_exhausted = false`, next batch start rank 226, next batch end rank 250. Dedup by stable asset id against union(frontier candidates_discovered + candidates_rank_unverified, v1–v8 delta = 220 known ids).
- **Frozen inputs unchanged:** config literal sha256 `753d9357e1d535ef4229a901e25ef059a751e4c4d56188247f5f2e0ef1debd16`; canonical manifest sha256 `55caedf84ac723289f70f49bbed4712c8195425feb4a95e737f3e8929479a0e0` (324 cells). `.venv` absent (no test gate for source-coverage delta); last known **18 passed** (activation 2948).

## Objective (activation 2990)
Advance the highest-value genuinely unblocked work, or document a blocker. Do NOT manufacture work and do NOT tight-poll any external source. Acceptable outcomes: (a) a real verifiable deliverable (e.g. frontier advance v9 to ranks 226–250 after a meaningful cooldown, an evidence audit, a blocker-resolution attempt), (b) a documented blocker, or (c) a NO-OP if the state-change gate is clean AND no new admissible source/date event exists AND no standing unblocked task is newly actionable.

## Required actions (activation 2990)
1. **State-change gate first (cheap):** verify config literal sha256 `753d9357e1d535ef4229a901e25ef059a751e4c4d56188247f5f2e0ef1debd16` and canonical `55caedf84ac723289f70f49bbed4712c8195425feb4a95e737f3e8929479a0e0`; check `git status --short` and no new commits under frozen-input paths `scripts/ tests/ configs/ data/ results/ docs/ prompts/ schemas/ research_state/hypothesis_registry.json research_state/universe_frontier.json research_state/integrated_extended_v1.json research_state/evaluation_report_extended_v1.json`. If nothing changed and no task below is newly actionable, classify as NO-OP per the v1.1 addendum.
2. **Frontier advance v9 (only if newly actionable AND a meaningful cooldown has elapsed):** standing unblocked task = ranks 226–250. Newly actionable ONLY after a meaningful cooldown since last retrieval (2026-11-15T13:53:37Z) or a documented source/network change — re-probing CoinPaprika shortly after last retrieval is tight polling and prohibited. If you proceed: fresh `/v1/coins` retrieval, de-duplicate by stable asset id against union(frontier candidates_discovered + candidates_rank_unverified, v1–v8 delta = 220 known ids). Write `research_state/universe_frontier_advance_v9.json` (artifact_id `EBCR-001-UNIVERSE-FRONTIER-ADVANCE-V9`) with retrieval UTC, raw-response sha256, rank window, dedup set-difference, duplicates with explicit reason, symbol collisions, cursor (`discovered_id_count`, `top_rank_covered=250`, `next_batch_start_rank=251`, `next_batch_end_rank=275`, `rank_frontier_exhausted`), notes. Prior: `universe_frontier_advance_v8.json` sha256 `c3e9cfc596d948925276ac4d449deaa1f171a78aa50d30d948fcc4377d67e201`. Do not edit frozen `research_state/universe_frontier.json` or `research_state/candidate_perp_mapping_v1.json`. Respect CoinPaprika rate limits; do not tight-poll.
3. **Do NOT re-run completed work:** frontier advance v1–v8; candidate→perp mapping v2; contract-lifecycle audit; V4 controlled re-estimation; V3→V4 inference audit; exclusion accounting audit. Re-run only if an input changes.
4. **Blocked (do not proceed without the stated precondition):**
    - **EBCR-H002/H003:** blocked — cannot preregister from inspected grid hits; requires a new experiment ID + independent preregistered rationale + a NEW anchor/config.
    - **EBCR-H004:** blocked — status change requires a separate preregistration decision; do not change `next_hypothesis_sequence` or statuses.
    - **Contract-lifecycle/candidate→perp mapping promotion:** promoting `candidate_perp_mapping_v1.json` or any v4/v5/v6/v7/v8 candidate out of `discovery_only_unverified`/PIT-unverified is a separate registration decision.
5. **Preserve invariants:** exclusions n=336 (28 `basis_incomplete` + 308 `incomplete_forward_horizon`); integrated 5,010 rows / 5,346 basis obs; anchor null (`crash_incidence_15pct` adj p 0.24830545694889028; `expected_shortfall_5pct_forward_mae` adj p 0.9485); PIT rank CLOSED; EBCR-H001 `tested_not_supported`; EBCR-H002/H003/H004 `registered_secondary_not_tested`; `next_hypothesis_sequence` 5. No frozen artifact edits; no preregistration derived from grid hits; preserve null/contradictory/failed evidence.
6. **Report only verified findings.** Do not commit unless explicitly asked. Update handoff and write the next task message.

## Required checks (run only when a relevant input changed)
```bash
python3 scripts/generate_grid_manifest.py --output /tmp/basis-grid-manifest.json   # expect 324 cells, canonical sha256 55caedf8…
# recreate .venv before any test gate: .venv/bin/python -m pytest -q tests  # expect 18 passed
git diff --check
# validate any changed JSON/JSONL/YAML and schemas
```

## Verified baseline (activation 2990, 2026-11-15)
- State-change gate: config sha256 `753d9357…` verified; canonical manifest sha256 `55caedf8…` verified (324 cells); `git status --short` clean; `git diff --check` clean.
- Frontier v8: `research_state/universe_frontier_advance_v8.json` (untracked), sha256 `c3e9cfc596d948925276ac4d449deaa1f171a78aa50d30d948fcc4377d67e201`; 24 net-new ranks 201–225; 1 duplicate (TRAC rank 203, ranking drift from rank 198 in v7); discovered-after 220; top rank covered 225; next batch start 226. v7 `e20adf7f…`; v6 `2f116b29…`; v5 `f5205cd5…`; v4 `d32f5c87…`; v3 `99b0daab…`; v2 `52070b3f…`; mapping v2 `d34780d2` sha256 `d2b442dd…`.
- Tests: not run (`.venv` absent, no code/test change); last known 18 passed (activation 2948).
- Anchor null: `crash_incidence_15pct` adj p 0.24830545694889028; `expected_shortfall_5pct_forward_mae` adj p 0.9485.

## Known blockers still open (do not re-probe every activation)
- Raw ingestion snapshots absent from repo (`data/raw/` gitignored) → re-ingestion not reproducible; only derived data.
- Data revision behavior unresolved.
- `exchangeInfo` is a live snapshot; no free historical point-in-time status time series.
- EBCR-H002/H003 not testable without a new preregistration independent of grid hits and a NEW anchor/config.
- EBCR-H004 registry status change requires a separate preregistration decision.
- `.venv` absent; recreate before the test gate.
- Frontier discovery open-ended: 220 ids covered (frontier + v1–v8), `rank_frontier_exhausted = false`; next scan starts at rank 226, but only after a documented cooldown/meaningful source change since last retrieval (2026-11-15T13:53:37Z) — no tight polling.
