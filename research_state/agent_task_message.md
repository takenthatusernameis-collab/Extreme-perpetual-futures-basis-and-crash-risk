# Agent task message (EBCR-001) — activation 3035 (written at end of activation 3034)

## Read first (required)
- `research_state/agent_handoff.md` (activation 3034: NO-OP, cooldown not elapsed; v12 now committed at rank 325; v13 earliest ≈2026-11-16T14:12:24Z)
- `research_state/agent_task_message.md` (this message)
- `prompts/continuous_research_operating_contract_v1.md` and `prompts/continuous_research_operating_contract_v1_1_addendum.md`
- `docs/research_protocol.md`
- `configs/basis_crash_grid_v1.json` (frozen)
- `docs/sources.md` and `.agents/skills/point-in-time-universe/SKILL.md` for source/frontier work

## Loop note — READ THIS FIRST
Activations 3011–3034 are **all back-to-back NO-OPs minutes apart**, driven by a tight activation cadence. Per the v1.1 addendum (§"Activation gate", §"Meaningful trigger", §"Work while blocked") and AGENTS.md (§"Activation cadence — state-change driven"), **do NOT** re-run the state-change gate, regenerate the manifest, re-probe CoinPaprika, create an upkeep artifact, or rewrite the handoff just to refresh timestamps while nothing has changed. A NO-OP must end with the prior verified state intact and no new artifact/commit. If you arrive before the cooldown below and no new admissible source/dated event exists, exit immediately.

## Clock gate (check this FIRST)
Current UTC must be compared to the frontier v12 cooldown deadline **≈2026-11-16T14:12:24Z** (v12 retrieval/creation was 2026-11-16T10:42:24Z). Until that time, **frontier advance v13 is NOT actionable** — running it earlier is tight polling (prohibited).

## What changed since the previous activation
- **Activation 3034 (2026-11-16T11:06:57Z): NO-OP.** State-change gate clean: config literal sha256 `753d9357…`, canonical manifest sha256 `55caedf8…` (324 cells), `git status` empty, `git diff --check` clean, no frozen-path commits since `d34780d2`. Current UTC (11:06:57Z) < v13 cooldown deadline (≈14:12:24Z). No new admissible source/event. No standing unblocked task newly actionable.
- **Only delta:** v12 artifact `research_state/universe_frontier_advance_v12.json` is now **tracked/committed** (content sha256 `61268ed8…`, unchanged). No frozen-input content changed.
- **Frozen inputs unchanged:** config literal sha256 `753d9357e1d535ef4229a901e25ef059a751e4c4d56188247f5f2e0ef1debd16`; canonical manifest sha256 `55caedf84ac723289f70f49bbed4712c8195425feb4a95e737f3e8929479a0e0` (324 cells). `.venv` absent; last known **18 passed** (activation 2948).

## Objective (activation 3035)
Acceptable outcomes, in priority order:
- (a) **Frontier advance v13 (ranks 326–350)** — ONLY if current UTC ≥ **≈2026-11-16T14:12:24Z** (meaningful cooldown since 2026-11-16T10:42:24Z) OR a documented CoinPaprika source/network change. If you run before that, you are tight-polling (prohibited).
- (b) **A genuinely new, permitted, non-contaminating task** — e.g. resolving a documented open blocker (raw-ingestion reproducibility, data revision behavior, `exchangeInfo` historical PIT status) **if and only if a real input/source is now available**. Do NOT manufacture an audit/test/artifact to avoid a NO-OP.
- (c) **NO-OP** — if the cooldown has not elapsed AND no new admissible source/date event AND no standing unblocked task is newly actionable. Then: do NOT rewrite the handoff/task message for timestamps, do NOT create a `durable_state_upkeep_v*` artifact, do NOT commit, and exit with prior verified state intact.

## Required actions (activation 3035)
1. **Check the clock first.** If now < `2026-11-16T14:12:24Z` and nothing else changed, classify as NO-OP per v1.1 addendum and stop (do not re-run the full gate, do not create an artifact).
2. **State-change gate (cheap, only if considering a deliverable):** verify config `753d9357…` and canonical manifest `55caedf8…` (324 cells); check `git status --short` and no new commits under frozen-input paths `scripts/ tests/ configs/ data/ results/ docs/ prompts/ schemas/ research_state/hypothesis_registry.json research_state/universe_frontier.json research_state/integrated_extended_v1.json research_state/evaluation_report_extended_v1.json`.
3. **Frontier advance v13 (only if newly actionable AND meaningful cooldown elapsed):** standing unblocked task = ranks 326–350. If you proceed: fresh `/v1/coins` retrieval, de-duplicate by stable asset id against union(frontier candidates_discovered + candidates_rank_unverified; v12 cursor discovered-after = 292 known ids — note recorded delta union may differ due to inheritance gap). Write `research_state/universe_frontier_advance_v13.json` (artifact_id `EBCR-001-UNIVERSE-FRONTIER-ADVANCE-V13`) with retrieval UTC, raw-response sha256, rank window, dedup set-difference, duplicates with explicit reason, symbol collisions, cursor (`discovered_id_count`, `top_rank_covered=350`, `next_batch_start_rank=351`, `next_batch_end_rank=375`, `rank_frontier_exhausted`), notes. Prior: `universe_frontier_advance_v12.json`. Do not edit frozen `research_state/universe_frontier.json` or `research_state/candidate_perp_mapping_v1.json`. Respect CoinPaprika rate limits.
4. **Do NOT re-run completed work:** frontier advance v1–v12; candidate→perp mapping v2; contract-lifecycle audit; V4 controlled re-estimation; V3→V4 inference audit; exclusion accounting audit. Re-run only if an input changes.
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

## Verified baseline (activation 3034, 2026-11-16T11:06:57Z)
- State-change gate: config sha256 `753d9357…` verified; canonical manifest sha256 `55caedf8…` verified (324 cells); `git status --short` empty; `git diff --check` clean; no frozen-path commits since `d34780d2`.
- Frontier v12: `research_state/universe_frontier_advance_v12.json` (created 2026-11-16T10:42:24Z, response_sha256 `902986da…`, 62,654 items; content sha256 `61268ed8…`, now committed); 22 net-new ranks 303–325, 3 duplicates (SAVAX, ORDI, TAG — v11 ranks 298–300), 0 collisions, discovered-after 270→292, top rank 325, next start 326. Tests not run (`.venv` absent); last known 18 passed (activation 2948).
- Anchor null: `crash_incidence_15pct` adj p 0.24830545694889028; `expected_shortfall_5pct_forward_mae` adj p 0.9485.

## Known blockers still open (do not re-probe every activation)
- Raw ingestion snapshots absent from repo (`data/raw/` gitignored) → re-ingestion not reproducible (derived data only).
- Data revision behavior unresolved.
- `exchangeInfo` live snapshot; no free historical PIT status time series.
- EBCR-H002/H003 not testable without new preregistration independent of grid hits and NEW anchor/config.
- EBCR-H004 registry status change requires separate preregistration decision.
- `.venv` absent; recreate before test gate.
- Frontier discovery open-ended: 292 ids covered, `rank_frontier_exhausted = false`; next scan starts at rank 326, only after documented cooldown/meaningful source change since 2026-11-16T10:42:24Z (earliest ≈2026-11-16T14:12:24Z) — no tight polling.