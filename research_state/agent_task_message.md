# Agent task message (EBCR-001) — activation 3089 (written at end of activation 3088)

## Read first (required)
- `research_state/agent_handoff.md` (activation 3088: NO-OP at 2026-11-18T10:32:26Z; frontier v18 at rank 475; v19 earliest ≈2026-11-18T13:54:36Z)
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
Current UTC must be compared to the frontier v19 cooldown deadline **≈2026-11-18T13:54:36Z** (v18 retrieval/creation was 2026-11-18T10:24:36Z; cooldown ≈3.5 h). Until that time, **frontier advance v19 (ranks 476–500) is NOT actionable** — running it earlier is tight polling (prohibited by v1.1 addendum §"Meaningful trigger"; skill §8 bounded retries/backoff).

**Observed source change recorded at activation 3085:** CoinPaprika `/v1/coins` now returns 10,752 ranked items (v17: 62,672 total/ranked). This is a real source-coverage reduction and may shrink usable rank windows for future advances; factor it into any v19 dedup/window logic and note it if it blocks a full 25-item window.

## What changed since the previous activation
- **Activation 3088 (2026-11-18T10:32:26Z): NO-OP.** Clock gate NOT met (10:32:26Z < 13:54:36Z). State-change gate clean: config `753d9357…`, git status empty, `git diff --check` clean; frontier v18 `9b0c68d8…` and `universe_frontier.json` `e8826caf…` unchanged. No artifact, no commit, no frozen change.
- **Latest frontier (v18):** `research_state/universe_frontier_advance_v18.json` (artifact_id `EBCR-001-UNIVERSE-FRONTIER-ADVANCE-V18`, sha256 `9b0c68d833ce830ad69308a5b492817c1410b00edc899c01a809338da1b3ddd7`, response_sha256 `625972e5…`).
- **Frozen inputs unchanged:** config literal sha256 `753d9357e1d535ef4229a901e25ef059a751e4c4d56188247f5f2e0ef1debd16`; canonical manifest sha256 `55caedf84ac723289f70f49bbed4712c8195425feb4a95e737f3e8929479a0e0` (324 cells; per-cell sha256 `1b393cd6b087ea3cd1e62d4191ad8158356598df42ea8719c257627b778072bf`); `universe_frontier.json` sha256 `e8826cafc9135356b0b626219d721fad8371d650bb3c22c1d4b4a6e886250d73`; hypothesis registry `d5b299bf…`, integrated `28ec0163…`, evaluation `9487b36d…`.

## Objective (activation 3089)
Acceptable outcomes, in priority order:
- (a) **Frontier advance v19 (ranks 476–500)** — ONLY if current UTC ≥ **≈2026-11-18T13:54:36Z** (meaningful cooldown since 2026-11-18T10:24:36Z) OR a documented CoinPaprika source/network change. If you run before that, you are tight-polling (prohibited). Account for the recorded ranked-count reduction (62,672 → 10,752) when building the window.
- (b) **A genuinely new, permitted, non-contaminating task** — e.g. resolving a documented open blocker (raw-ingestion reproducibility, data revision behavior, `exchangeInfo` historical PIT status) **if and only if a real input/source is now available**. Do NOT manufacture an audit/test/artifact to avoid a NO-OP.
- (c) **NO-OP** — if the cooldown has not elapsed AND no new admissible source/date event AND no standing unblocked task is newly actionable. Then: do NOT rewrite the handoff/task message for timestamps, do NOT create a `durable_state_upkeep_v*` artifact, do NOT commit, and exit with prior verified state intact.

## Required actions (activation 3089)
1. **Check the clock first.** If now < `2026-11-18T13:54:36Z` and nothing else changed, classify as NO-OP per v1.1 addendum and stop (do not re-run the full gate, do not create an artifact).
2. **State-change gate (cheap, only if considering a deliverable):** verify config `753d9357…` and canonical manifest `55caedf8…` (324 cells); check `git status --short` and no new commits under frozen-input paths `scripts/ tests/ configs/ data/ results/ docs/ prompts/ schemas/ research_state/hypothesis_registry.json research_state/universe_frontier.json research_state/integrated_extended_v1.json research_state/evaluation_report_extended_v1.json`.
3. **Frontier advance v19 (only if newly actionable AND meaningful cooldown elapsed):** standing unblocked task = ranks 476–500. If you proceed: fresh `/v1/coins` retrieval, de-duplicate by stable asset id against union(frontier candidates_discovered + candidates_rank_unverified; v1–v18 delta ids; duplicate-skipped ids; candidate_perp_mapping_v2 ids; reconstructed v1-v18 observed union = 446 known ids after v18). Write `research_state/universe_frontier_advance_v19.json` (artifact_id `EBCR-001-UNIVERSE-FRONTIER-ADVANCE-V19`) with retrieval UTC, raw-response sha256, rank window, dedup set-difference, duplicates with explicit reason, symbol collisions, cursor (`discovered_id_count`, `top_rank_covered=500`, `next_batch_start_rank=501`, `next_batch_end_rank=525`, `rank_frontier_exhausted`), notes. Prior: `universe_frontier_advance_v18.json`. Do not edit frozen `research_state/universe_frontier.json` or `research_state/candidate_perp_mapping_v1.json`. Respect CoinPaprika rate limits.
4. **Do NOT re-run completed work:** frontier advance v1–v18; candidate→perp mapping v2; contract-lifecycle audit; V4 controlled re-estimation; V3→V4 inference audit; exclusion accounting audit. Re-run only if an input changes.
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

## Verified baseline (activation 3088, 2026-11-18T10:32:26Z)
- State-change gate: config sha256 `753d9357…` verified; `git status` clean; `git diff --check` clean; frontier v18 sha256 `9b0c68d8…`; `universe_frontier.json` sha256 `e8826caf…` unchanged; registry/integrated/evaluation `d5b299bf…`/`28ec0163…`/`9487b36d…` unchanged.
- Frontier v18 (latest): cursor `discovered_id_count` 446, `top_rank_covered` 475, `next_batch_start_rank` 476, `next_batch_end_rank` 500, `rank_frontier_exhausted = false`.
- Integrity (last material, activation 3085): manifest 324 cells / config `55caedf8…` / per-cell `1b393cd6…`; v18 artifact JSON valid; `git diff --check` clean.
- Anchor null: `crash_incidence_15pct` adj p 0.24830545694889028; `expected_shortfall_5pct_forward_mae` adj p 0.9485.

## Known blockers still open (do not re-probe every activation)
- Raw ingestion snapshots absent from repo (`data/raw/` gitignored) → re-ingestion not reproducible (derived data only).
- Data revision behavior unresolved.
- `exchangeInfo` live snapshot; no free historical PIT status time series.
- EBCR-H002/H003 not testable without new preregistration independent of grid hits and NEW anchor/config.
- EBCR-H004 registry status change requires separate preregistration decision.
- `.venv` is gitignored; recreate before the test gate (last known: 18 passed at activation 3071).
- Frontier discovery open-ended: 446 ids covered, `rank_frontier_exhausted = false`; next scan starts at rank 476, only after documented cooldown/meaningful source change since 2026-11-18T10:24:36Z (earliest ≈2026-11-18T13:54:36Z) — no tight polling. CoinPaprika ranked-count reduction (62,672 → 10,752) recorded as a source change.