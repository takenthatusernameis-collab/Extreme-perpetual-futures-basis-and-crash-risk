# Agent task message (EBCR-001) — activation 3093 (written at end of activation 3093)

## Read first (required)
- `research_state/agent_handoff.md` (activation 3093: frontier advance v19 at 2026-11-18T18:56:30Z; cursor 469, top_rank_covered 500; v20 earliest ≈2026-11-19T02:26:30Z)
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

`research_state/` holds ~**1032** `durable_state_upkeep*` entries (highest version v981) — housekeeping churn the addendum removes. **Do not add to it while waiting.** If you arrive before the cooldown and no new admissible source/dated event exists, exit immediately rather than re-firing.

## Clock gate (check this FIRST)
Current UTC must be compared to the frontier v20 cooldown deadline **≈2026-11-19T02:26:30Z** (v19 retrieval/creation was 2026-11-18T18:56:30Z; cooldown ≈3.5 h). Until that time, **frontier advance v20 (ranks 501–525) is NOT actionable** — running it earlier is tight polling (prohibited by v1.1 addendum §"Meaningful trigger"; skill §8 bounded retries/backoff).

**Observed source change recorded at activation 3085:** CoinPaprika `/v1/coins` now returns 10,752 ranked items (v17: 62,672 total/ranked). This is a real source-coverage reduction and may shrink usable rank windows for future advances; factor it into any v20 dedup/window logic and note it if it blocks a full 25-item window. **At activation 3093, ranked-count recovered to 62,712** — the reduction appears intermittent; treat as a source change to monitor.

## What changed since the previous activation
- **Activation 3093 (2026-11-18T18:56:30Z): FRONTIER ADVANCE v19.** Clock gate met (18:55:18Z ≥ 13:54:36Z). State-change gate clean: config `753d9357…`, git status shows only new `universe_frontier_advance_v19.json`, `git diff --check` clean. Delivered 23 net-new candidates (ranks 476–500), 2 duplicates skipped, 1 symbol collision (SENT). Cursor: `discovered_id_count` 469, `top_rank_covered` 500, `next_batch_start_rank` 501, `next_batch_end_rank` 525, `rank_frontier_exhausted = false`. Integrity gate green (manifest 324 cells, config sha256 `55caedf8…`, `git diff --check` clean).
- **Latest frontier (v19):** `research_state/universe_frontier_advance_v19.json` (artifact_id `EBCR-001-UNIVERSE-FRONTIER-ADVANCE-V19`, sha256 `12f3a08a62c1d00ee7ac32555cf59a5440118f61008b52d6036aab30ef0c4a4e`, response_sha256 `f2739bb105b324aec183a3a7887aedd70b84eb8d8825a0efad528b65a78cbeff`).
- **Frozen inputs unchanged:** config literal sha256 `753d9357e1d535ef4229a901e25ef059a751e4c4d56188247f5f2e0ef1debd16`; canonical manifest sha256 `55caedf84ac723289f70f49bbed4712c8195425feb4a95e737f3e8929479a0e0` (324 cells; per-cell sha256 `1b393cd6b087ea3cd1e62d4191ad8158356598df42ea8719c257627b778072bf`); `universe_frontier.json` sha256 `e8826cafc9135356b0b626219d721fad8371d650bb3c22c1d4b4a6e886250d73`; hypothesis registry `d5b299bf…`, integrated `28ec0163…`, evaluation `9487b36d…`.

## Objective (activation 3094)
Acceptable outcomes, in priority order:
- (a) **Frontier advance v20 (ranks 501–525)** — ONLY if current UTC ≥ **≈2026-11-19T02:26:30Z** (meaningful cooldown since 2026-11-18T18:56:30Z) OR a documented CoinPaprika source/network change. If you run before that, you are tight-polling (prohibited). Account for the observed ranked-count fluctuation (62,672 → 10,752 → 62,712) when building the window.
- (b) **A genuinely new, permitted, non-contaminating task** — e.g. resolving a documented open blocker (raw-ingestion reproducibility, data revision behavior, `exchangeInfo` historical PIT status) **if and only if a real input/source is now available**. Do NOT manufacture an audit/test/artifact to avoid a NO-OP.
- (c) **NO-OP** — if the cooldown has not elapsed AND no new admissible source/date event AND no standing unblocked task is newly actionable. Then: do NOT rewrite the handoff/task message for timestamps, do NOT create a `durable_state_upkeep_v*` artifact, do NOT commit, and exit with prior verified state intact.

## Required actions (activation 3094)
1. **Check the clock first.** If now < `2026-11-19T02:26:30Z` and nothing else changed, classify as NO-OP per v1.1 addendum and stop (do not re-run the full gate, do not create an artifact).
2. **State-change gate (cheap, only if considering a deliverable):** verify config `753d9357…` and canonical manifest `55caedf8…` (324 cells); check `git status --short` and no new commits under frozen-input paths `scripts/ tests/ configs/ data/ results/ docs/ prompts/ schemas/ research_state/hypothesis_registry.json research_state/universe_frontier.json research_state/integrated_extended_v1.json research_state/evaluation_report_extended_v1.json`.
3. **Frontier advance v20 (only if newly actionable AND meaningful cooldown elapsed):** standing unblocked task = ranks 501–525. If you proceed: fresh `/v1/coins` retrieval, de-duplicate by stable asset id against union(frontier candidates_discovered + candidates_rank_unverified; v1–v19 delta ids; duplicate-skipped ids; candidate_perp_mapping_v2 ids; reconstructed v1-v19 observed union = 469 known ids after v19). Write `research_state/universe_frontier_advance_v20.json` (artifact_id `EBCR-001-UNIVERSE-FRONTIER-ADVANCE-V20`) with retrieval UTC, raw-response sha256, rank window, dedup set-difference, duplicates with explicit reason, symbol collisions, cursor (`discovered_id_count`, `top_rank_covered=525`, `next_batch_start_rank=526`, `next_batch_end_rank=550`, `rank_frontier_exhausted`), notes. Prior: `universe_frontier_advance_v19.json`. Do not edit frozen `research_state/universe_frontier.json` or `research_state/candidate_perp_mapping_v1.json`. Respect CoinPaprika rate limits.
4. **Do NOT re-run completed work:** frontier advance v1–v19; candidate→perp mapping v2; contract-lifecycle audit; V4 controlled re-estimation; V3→V4 inference audit; exclusion accounting audit. Re-run only if an input changes.
5. **Blocked (do not proceed without stated precondition):** EBCR-H002/H003 — cannot preregister from inspected grid hits; requires new experiment ID + independent preregistered rationale + NEW anchor/config. EBCR-H004 — status change requires separate preregistration decision. Candidate→perp mapping/contract-lifecycle promotion out of `discovery_only_unverified`/PIT-unverified is a separate registration decision.
6. **Preserve invariants:** exclusions n=336 (28 `basis_incomplete` + 308 `incomplete_forward_horizon`); integrated 5,010 rows / 5,346 basis obs; anchor null (`crash_incidence_15pct` adj p 0.24830545694889028; `expected_shortfall_5pct_forward_mae` adj p 0.9485); PIT rank CLOSED; EBCR-H001 `tested_not_supported`; EBCR-H002/H003/H004 `registered_secondary_not_tested`; `next_hypothesis_sequence` 5. No frozen artifact edits; no preregistration from grid hits; preserve null/contradictory/failed evidence.
7. **Report only verified findings.** Do not commit unless explicitly asked. If this is a genuine NO-OP, leave the handoff unchanged and do not create an artifact.

## Required checks (run only when a relevant input changed)
```bash
python3 scripts/generate_grid_manifest.py --output /tmp/basis-grid-manifest.json   # expect 324 cells, canonical sha256 55caedf8…
# test gate: recreate .venv if absent, then: .venv/bin/python -m pytest -q tests   # expect 18 passed
git diff --check
# validate any changed JSON/JSONL/YAML and schemas
```

## Verified baseline (activation 3093, 2026-11-18T18:56:30Z)
- State-change gate: config sha256 `753d9357…` verified; `git status` shows only new `universe_frontier_advance_v19.json`; `git diff --check` clean; frontier v19 sha256 `f2739bb1…`; `universe_frontier.json` sha256 `e8826caf…` unchanged; registry/integrated/evaluation `d5b299bf…`/`28ec0163…`/`9487b36d…` unchanged.
- Frontier v19 (latest): cursor `discovered_id_count` 469, `top_rank_covered` 500, `next_batch_start_rank` 501, `next_batch_end_rank` 525, `rank_frontier_exhausted = false`.
- Integrity (last material, activation 3093): manifest 324 cells / config `55caedf8…` / per-cell `1b393cd6…`; v19 artifact JSON valid; `git diff --check` clean.
- Anchor null: `crash_incidence_15pct` adj p 0.24830545694889028; `expected_shortfall_5pct_forward_mae` adj p 0.9485.

## Known blockers still open (do not re-probe every activation)
- Raw ingestion snapshots absent from repo (`data/raw/` gitignored) → re-ingestion not reproducible (derived data only).
- Data revision behavior unresolved.
- `exchangeInfo` live snapshot; no free historical PIT status time series.
- EBCR-H002/H003 not testable without new preregistration independent of grid hits and NEW anchor/config.
- EBCR-H004 registry status change requires separate preregistration decision.
- `.venv` is gitignored; recreate before the test gate (last known: 18 passed at activation 3071).
- Frontier discovery open-ended: 469 ids covered, `rank_frontier_exhausted = false`; next scan starts at rank 501, only after documented cooldown/meaningful source change since 2026-11-18T18:56:30Z (earliest ≈2026-11-19T02:26:30Z) — no tight polling. CoinPaprika ranked-count fluctuation (62,672 → 10,752 → 62,712) recorded as a source change.