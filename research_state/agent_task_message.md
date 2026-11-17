# Agent task message (EBCR-001) — activation 3056 (written at end of activation 3055)

## Read first (required)
- `research_state/agent_handoff.md` (activation 3055: NO-OP at 2026-11-17T03:27:47Z; frontier v14 at rank 375 cursor; v15 earliest ≈2026-11-17T06:41:51Z; systemic upkeep-artifact churn flagged)
- `research_state/agent_task_message.md` (this message)
- `prompts/continuous_research_operating_contract_v1.md` and `prompts/continuous_research_operating_contract_v1_1_addendum.md`
- `docs/research_protocol.md`
- `configs/basis_crash_grid_v1.json` (frozen)
- `docs/sources.md` and `.agents/skills/point-in-time-universe/SKILL.md` for source/frontier work

## Loop note — READ THIS FIRST (NO-OP discipline)
Per the v1.1 addendum (§"Activation gate", §"Meaningful trigger") and AGENTS.md (§"Activation cadence — state-change driven"): when the clock gate below is not met and nothing has changed, classify the activation as **NO-OP** and exit with prior verified state intact. On a NO-OP do NOT:
- re-run the state-change gate, regenerate the manifest, re-probe CoinPaprika, or rerun the test suite;
- create the next numbered `durable_state_upkeep_v*.json` artifact;
- rewrite the handoff or this task message solely to refresh timestamps;
- create a checkpoint commit.

`research_state/` already contains **976** `durable_state_upkeep_v*.json` artifacts (v1…v981) plus a long run of sub-5-minute NO-OP activations — that is exactly the housekeeping churn the addendum removes. Do not add to it while waiting. If you arrive before the cooldown and no new admissible source/dated event exists, exit immediately.

## Clock gate (check this FIRST)
Current UTC must be compared to the frontier v14 cooldown deadline **≈2026-11-17T06:41:51Z** (v14 retrieval/creation was 2026-11-17T03:11:51Z). Until that time, **frontier advance v15 (ranks 376–400) is NOT actionable** — running it earlier is tight polling (prohibited).

## What changed since the previous activation
- **Activation 3055 (2026-11-17T03:27:47Z): NO-OP.** Cheap gate clean: clock 03:27:47Z < cooldown ≈06:41:51Z; git tree clean; config sha256 `753d9357…` matches; no frozen-path commits since `d34780d2`; v14 artifact unchanged (`e4bdb9f3…`). No new admissible source/date event and no newly actionable standing task. No artifact created (deliberately skipped `durable_state_upkeep_v982`). Handoff/task message advanced to activation 3056.
- **Prior deliverable (activation 3044, 2026-11-17T03:12:45Z): FRONTIER ADVANCE V14.** `research_state/universe_frontier_advance_v14.json` (artifact_id `EBCR-001-UNIVERSE-FRONTIER-ADVANCE-V14`, untracked): 24 net-new candidates (ranks 352–375), 1 duplicate skipped (ANVL@351, drift from v13 rank 344), 0 collisions, cursor `discovered_id_count` 360, `top_rank_covered` 375, `next_batch_start_rank` 376, `next_batch_end_rank` 400, `rank_frontier_exhausted = false`, response_sha256 `c04a40a5…`.
- **Frozen inputs unchanged:** config literal sha256 `753d9357e1d535ef4229a901e25ef059a751e4c4d56188247f5f2e0ef1debd16`; canonical manifest sha256 `55caedf84ac723289f70f49bbed4712c8195425feb4a95e737f3e8929479a0e0` (324 cells; per-cell file sha256 `1b393cd6b087ea3cd1e62d4191ad8158356598df42ea8719c257627b778072bf`).

## Objective (activation 3056)
Acceptable outcomes, in priority order:
- (a) **Frontier advance v15 (ranks 376–400)** — ONLY if current UTC ≥ **≈2026-11-17T06:41:51Z** (meaningful cooldown since 2026-11-17T03:11:51Z) OR a documented CoinPaprika source/network change. If you run before that, you are tight-polling (prohibited).
- (b) **A genuinely new, permitted, non-contaminating task** — e.g. resolving a documented open blocker (raw-ingestion reproducibility, data revision behavior, `exchangeInfo` historical PIT status) **if and only if a real input/source is now available**. Do NOT manufacture an audit/test/artifact to avoid a NO-OP.
- (c) **NO-OP** — if the cooldown has not elapsed AND no new admissible source/date event AND no standing unblocked task is newly actionable. Then: do NOT rewrite the handoff/task message for timestamps, do NOT create a `durable_state_upkeep_v*` artifact, do NOT commit, and exit with prior verified state intact.

## Required actions (activation 3056)
1. **Check the clock first.** If now < `2026-11-17T06:41:51Z` and nothing else changed, classify as NO-OP per v1.1 addendum and stop (do not re-run the full gate, do not create an artifact).
2. **State-change gate (cheap, only if considering a deliverable):** verify config `753d9357…` and canonical manifest `55caedf8…` (324 cells); check `git status --short` and no new commits under frozen-input paths `scripts/ tests/ configs/ data/ results/ docs/ prompts/ schemas/ research_state/hypothesis_registry.json research_state/universe_frontier.json research_state/integrated_extended_v1.json research_state/evaluation_report_extended_v1.json`.
3. **Frontier advance v15 (only if newly actionable AND meaningful cooldown elapsed):** standing unblocked task = ranks 376–400. If you proceed: fresh `/v1/coins` retrieval, de-duplicate by stable asset id against union(frontier candidates_discovered + candidates_rank_unverified; v14 cursor discovered-after = 360 known ids, reconstructed v1–v14 observed union). Write `research_state/universe_frontier_advance_v15.json` (artifact_id `EBCR-001-UNIVERSE-FRONTIER-ADVANCE-V15`) with retrieval UTC, raw-response sha256, rank window, dedup set-difference, duplicates with explicit reason, symbol collisions, cursor (`discovered_id_count`, `top_rank_covered=400`, `next_batch_start_rank=401`, `next_batch_end_rank=425`, `rank_frontier_exhausted`), notes. Prior: `universe_frontier_advance_v14.json`. Do not edit frozen `research_state/universe_frontier.json` or `research_state/candidate_perp_mapping_v1.json`. Respect CoinPaprika rate limits.
4. **Do NOT re-run completed work:** frontier advance v1–v14; candidate→perp mapping v2; contract-lifecycle audit; V4 controlled re-estimation; V3→V4 inference audit; exclusion accounting audit. Re-run only if an input changes.
5. **Blocked (do not proceed without stated precondition):** EBCR-H002/H003 — cannot preregister from inspected grid hits; requires new experiment ID + independent preregistered rationale + NEW anchor/config. EBCR-H004 — status change requires separate preregistration decision. Candidate→perp mapping/contract-lifecycle promotion out of `discovery_only_unverified`/PIT-unverified is a separate registration decision.
6. **Preserve invariants:** exclusions n=336 (28 `basis_incomplete` + 308 `incomplete_forward_horizon`); integrated 5,010 rows / 5,346 basis obs; anchor null (`crash_incidence_15pct` adj p 0.24830545694889028; `expected_shortfall_5pct_forward_mae` adj p 0.9485); PIT rank CLOSED; EBCR-H001 `tested_not_supported`; EBCR-H002/H003/H004 `registered_secondary_not_tested`; `next_hypothesis_sequence` 5. No frozen artifact edits; no preregistration from grid hits; preserve null/contradictory/failed evidence.
7. **Report only verified findings.** Do not commit unless explicitly asked. If this is a genuine NO-OP, leave the handoff unchanged and do not create an artifact.

## Required checks (run only when a relevant input changed)
```bash
python3 scripts/generate_grid_manifest.py --output /tmp/basis-grid-manifest.json   # expect 324 cells, canonical sha256 55caedf8…
# recreate .venv before any test gate: .venv/bin/python -m pytest -q tests  # expect 18 passed
git diff --check
# validate any changed JSON/JSONL/YAML and schemas
```

## Verified baseline (activation 3055, 2026-11-17T03:27:47Z)
- State-change gate: config sha256 `753d9357…` verified; git tree clean; no frozen-path commits since `d34780d2`; v14 artifact sha256 `e4bdb9f3…` unchanged. (Manifest not regenerated — NO-OP, no relevant input changed.)
- Frontier v14 (latest): `research_state/universe_frontier_advance_v14.json` (created 2026-11-17T03:11:51Z, response_sha256 `c04a40a5…`, 62,665 items; 24 net-new ranks 352–375, 1 duplicate (ANVL@351, v13 rank 344 drift), 0 collisions, discovered-after 336→360, top rank 375, next start 376).
- Frontier v13 (prior): `research_state/universe_frontier_advance_v13.json` (created 2026-11-16T20:43:03Z, 21 net-new ranks 328–350, 4 duplicates, discovered_id_count 313, top rank 350).
- Anchor null: `crash_incidence_15pct` adj p 0.24830545694889028; `expected_shortfall_5pct_forward_mae` adj p 0.9485.

## Known blockers still open (do not re-probe every activation)
- Raw ingestion snapshots absent from repo (`data/raw/` gitignored) → re-ingestion not reproducible (derived data only).
- Data revision behavior unresolved.
- `exchangeInfo` live snapshot; no free historical PIT status time series.
- EBCR-H002/H003 not testable without new preregistration independent of grid hits and NEW anchor/config.
- EBCR-H004 registry status change requires separate preregistration decision.
- `.venv` absent; recreate before test gate.
- Frontier discovery open-ended: 360 ids covered, `rank_frontier_exhausted = false`; next scan starts at rank 376, only after documented cooldown/meaningful source change since 2026-11-17T03:11:51Z (earliest ≈2026-11-17T06:41:51Z) — no tight polling.