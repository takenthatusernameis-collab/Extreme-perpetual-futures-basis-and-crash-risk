# Agent task message (EBCR-001) — activation 2973 (written at end of activation 2972)

## Read first (required)
- `research_state/agent_handoff.md` (activation 2972: NO-OP, state-change gate clean; frontier v6 at rank 175, next batch start 176; no meaningful cooldown for v7 yet)
- `research_state/agent_task_message.md` (this message)
- `prompts/continuous_research_operating_contract_v1.md` and `prompts/continuous_research_operating_contract_v1_1_addendum.md`
- `docs/research_protocol.md`
- `configs/basis_crash_grid_v1.json` (frozen)
- `docs/sources.md` (free public source policy — verify actual coverage, never assume)
- `.agents/skills/point-in-time-universe/SKILL.md` (discovery → PIT eligibility; never project current rank backward)

## What changed since the previous activation
- **Activation 2972 (2026-11-15T00:16:42Z): NO-OP.** State-change gate verified clean: config literal sha256 `753d9357e1d535ef4229a901e25ef059a751e4c4d56188247f5f2e0ef1debd16`; canonical manifest sha256 `55caedf84ac723289f70f49bbed4712c8195425feb4a95e737f3e8929479a0e0` (324 cells); `git status` clean; `git diff --check` clean; no commits under frozen-input paths since `d34780d2`.
- **Frontier advance v6 (activation 2964, 2026-11-15T00:01:17Z):** fresh CoinPaprika `/v1/coins` retrieval, `response_sha256 = f01dd377e331b6915d56ff5cd67af5654e6b2629bd45b72dcd9961ddbfe78b2d` (62,635 items). Rank window scanned **151–175**. Dedup against union(frontier + v1–v5 = 148 known ids): **24 net-new candidates, 1 duplicate (XTZ rank 151 `xtz-tezos`, ranking drift), 0 symbol collisions**. Artifact: `research_state/universe_frontier_advance_v6.json` (tracked, commit `21aae78d`), artifact_id `EBCR-001-UNIVERSE-FRONTIER-ADVANCE-V6`, sha256 `2f116b29fb1299361c093b5e319a4fbeb6f66f42c2225faa0baf950246870585`. Cursor: discovered-after 172, top rank covered 175, `rank_frontier_exhausted = false`, next batch start rank 176.
- **Frontier advance v7 (ranks 176–200) is NOT newly actionable yet:** last CoinPaprika retrieval was 2026-11-15T00:01:17Z; activation 2972 was ~15 minutes later (~3.3 hours short of the ~3.5-hour cooldown that made v6 actionable). Re-probing shortly after the last retrieval is tight polling and is prohibited by the v1.1 addendum. Wait for a documented cooldown/meaningful source change.
- **Frozen inputs unchanged:** config literal sha256 `753d9357…`; canonical manifest sha256 `55caedf8…` (324 cells). `git diff --check` clean; no commits under frozen-input paths since `d34780d2`.
- `.venv` absent (not recreated — no test gate required for NO-OP). Last known tests: **18 passed** (activation 2948).

## Objective (activation 2973)
Advance the highest-value genuinely unblocked work, or document a blocker. Do NOT manufacture work and do NOT tight-poll any external source. Acceptable outcomes: (a) a real verifiable deliverable (e.g. frontier advance v7 to ranks 176–200 after a meaningful cooldown, an evidence audit, a blocker-resolution attempt), (b) a documented blocker, or (c) a NO-OP if the state-change gate is clean AND no new admissible source/date event exists AND no standing unblocked task is newly actionable.

## Required actions (activation 2973)
1. **State-change gate first (cheap):** verify config literal sha256 `753d9357e1d535ef4229a901e25ef059a751e4c4d56188247f5f2e0ef1debd16` and canonical `55caedf84ac723289f70f49bbed4712c8195425feb4a95e737f3e8929479a0e0`; check `git status --short` and no new commits under frozen-input paths `scripts/ tests/ configs/ data/ results/ docs/ prompts/ schemas/ research_state/hypothesis_registry.json research_state/universe_frontier.json research_state/integrated_extended_v1.json research_state/evaluation_report_extended_v1.json`. If nothing changed and no task below is newly actionable, classify as NO-OP per the v1.1 addendum.
2. **Frontier advance v7 (only if newly actionable AND a meaningful cooldown has elapsed):** the only genuinely unblocked standing task is frontier advance v7 to ranks 176–200. It is newly actionable ONLY after a meaningful cooldown since the last retrieval (2026-11-15T00:01:17Z) or a documented source/network change — re-probing CoinPaprika shortly after the last retrieval is tight polling and is prohibited. If you proceed: fresh `/v1/coins` retrieval, de-duplicate by stable asset id against the union of frontier candidates_discovered + candidates_rank_unverified, v1 delta, v2 delta, v3 delta, v4 delta, v5 delta, v6 delta = 172 known ids. Write `research_state/universe_frontier_advance_v7.json` (artifact_id `EBCR-001-UNIVERSE-FRONTIER-ADVANCE-V7`) using the same schema: retrieval UTC, raw-response sha256, rank window, dedup set-difference, duplicates with explicit reason, symbol collisions, cursor (`discovered_id_count`, `top_rank_covered`, `next_batch_start_rank=201`, `next_batch_end_rank=225`, `rank_frontier_exhausted`), notes. Prior artifact: `universe_frontier_advance_v6.json` sha256 `2f116b29fb1299361c093b5e319a4fbeb6f66f42c2225faa0baf950246870585`. Do not edit frozen `research_state/universe_frontier.json` or `research_state/candidate_perp_mapping_v1.json`. Respect CoinPaprika rate limits; do not tight-poll.
3. **Do NOT re-run completed work:** frontier advance v1–v6; candidate→perp mapping v2; contract-lifecycle audit; V4 controlled re-estimation; V3→V4 inference audit; exclusion accounting audit. Re-run only if an input changes.
4. **Blocked (do not proceed without the stated precondition):**
   - **EBCR-H002/H003:** blocked — cannot preregister from inspected grid hits; requires a new experiment ID + independent preregistered rationale + a NEW anchor/config.
   - **EBCR-H004:** blocked — status change requires a separate preregistration decision; do not change `next_hypothesis_sequence` or statuses.
   - **Contract-lifecycle mapping promotion:** promoting `candidate_perp_mapping_v1.json` out of `discovery_only_unverified` is a separate registration decision.
   - **Candidate→perp mapping:** promoting any v4/v5/v6 candidate to PIT-verified or mapping it to a perpetual contract is a separate registration decision.
5. **Preserve invariants:** exclusions n=336 (28 `basis_incomplete` + 308 `incomplete_forward_horizon`); integrated 5,010 rows / 5,346 basis obs; anchor null (`crash_incidence_15pct` adj p 0.24830545694889028; `expected_shortfall_5pct_forward_mae` adj p 0.9485); PIT rank CLOSED; EBCR-H001 `tested_not_supported`; EBCR-H002/H003/H004 `registered_secondary_not_tested`; `next_hypothesis_sequence` 5. No frozen artifact edits; no preregistration derived from grid hits; preserve null/contradictory/failed evidence.
6. **Report only verified findings.** Do not commit unless explicitly asked. Update handoff and write the next task message.

## Required checks (run only when a relevant input changed)
```bash
python3 scripts/generate_grid_manifest.py --output /tmp/basis-grid-manifest.json   # expect 324 cells, canonical sha256 55caedf8…
# recreate .venv before any test gate: .venv/bin/python -m pytest -q tests  # expect 18 passed
git diff --check
# validate any changed JSON/JSONL/YAML and schemas
```

## Verified baseline (activation 2972, 2026-11-15)
- State-change gate: config sha256 `753d9357…` verified; canonical manifest sha256 `55caedf8…` verified (324 cells); `git status --short` clean; `git diff --check` clean.
- Frontier advance v6: `research_state/universe_frontier_advance_v6.json` (tracked, commit `21aae78d`), sha256 `2f116b29fb1299361c093b5e319a4fbeb6f66f42c2225faa0baf950246870585`; 24 net-new at ranks 151–175; 1 duplicate (XTZ rank 151 `xtz-tezos`, ranking drift); 0 symbol collisions; discovered-after 172; top rank covered 175; `rank_frontier_exhausted = false`; next batch start 176.
- Frontier advance v5: `research_state/universe_frontier_advance_v5.json` (tracked, commit `d7f31dc5`), sha256 `f5205cd5…`; v4 sha256 `d32f5c87…`; v3 sha256 `99b0daab…`; v2 sha256 `52070b3f…`; mapping v2 `d34780d2` sha256 `d2b442dd…`.
- Tests: not run (`.venv` absent, no code/test change); last known 18 passed (activation 2948).
- Anchor null: `crash_incidence_15pct` adj p 0.24830545694889028; `expected_shortfall_5pct_forward_mae` adj p 0.9485.

## Known blockers still open (do not re-probe every activation)
- Raw ingestion snapshots absent from repo (`data/raw/` gitignored) → re-ingestion not reproducible; only derived data.
- Data revision behavior unresolved.
- `exchangeInfo` is a live snapshot; no free historical point-in-time status time series.
- EBCR-H002/H003 not testable without a new preregistration independent of grid hits and a NEW anchor/config.
- EBCR-H004 registry status change requires a separate preregistration decision.
- `.venv` absent; recreate before the test gate.
- Frontier discovery open-ended: 172 ids covered (frontier + v1–v6), `rank_frontier_exhausted = false`; next scan starts at rank 176, but only after a documented cooldown/meaningful source change (no tight polling).