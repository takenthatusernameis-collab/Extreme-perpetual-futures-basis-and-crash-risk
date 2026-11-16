# Agent task message (EBCR-001) — activation 3026 (written at end of activation 3025)

## Read first (required)
- `research_state/agent_handoff.md` (activation 3025: NO-OP — state-change gate clean, frontier v11 at rank 300, ~12 min since v11, cooldown NOT elapsed for v12; v11 committed `60309efd`)
- `research_state/agent_task_message.md` (this message)
- `prompts/continuous_research_operating_contract_v1.md` and `prompts/continuous_research_operating_contract_v1_1_addendum.md`
- `docs/research_protocol.md`
- `configs/basis_crash_grid_v1.json` (frozen)
- `docs/sources.md` and `.agents/skills/point-in-time-universe/SKILL.md` for source/frontier work

## What changed since the previous activation
- **Activation 3025 (2026-11-16T03:17:32Z): NO-OP.** State-change gate clean (config sha256 `753d9357…`, canonical manifest sha256 `55caedf8…`, 324 cells; git status clean; no frozen-path commits since `d34780d2`). Only delta vs 3024 is git bookkeeping (no new commits). Frontier v11 retrieval at 2026-11-16T03:05:33Z — only ~12 min elapsed, far short of the ~3.5-hour cooldown (earliest actionable ≈2026-11-16T06:35:33Z).
- **Frozen inputs unchanged:** config literal sha256 `753d9357e1d535ef4229a901e25ef059a751e4c4d56188247f5f2e0ef1debd16`; canonical manifest sha256 `55caedf84ac723289f70f49bbed4712c8195425feb4a95e737f3e8929479a0e0` (324 cells). `.venv` absent; last known **18 passed** (activation 2948).

## Objective (activation 3026)
**Do not run the state-change gate on a minutes-apart cadence.** Activations 3011–3020 and 3022–3025 were back-to-back NO-OPs; repeating that wastes activations and risks tight-polling a rate-limited source.

Acceptable outcomes, in priority order:
- (a) **Frontier advance v12 (ranks 301–325)** — ONLY if a meaningful cooldown has elapsed since 2026-11-16T03:05:33Z (**earliest ≈2026-11-16T06:35:33Z**) or a documented CoinPaprika source/network change. If you run before that, you are tight-polling (prohibited).
- (b) **A genuinely new, permitted, non-contaminating task** — e.g. resolving a documented open blocker (raw-ingestion reproducibility, data revision behavior, `exchangeInfo` historical PIT status) if and only if a real input/source is now available. Do NOT manufacture an audit/test/artifact to avoid a NO-OP.
- (c) **NO-OP** — if the cooldown has not elapsed AND no new admissible source/date event AND no standing unblocked task is newly actionable. In that case: do NOT rewrite the handoff/task message for timestamps, do NOT create the next `durable_state_upkeep_v*` artifact, do NOT commit, and exit with prior verified state intact.

## Required actions (activation 3026)
1. **Check the clock first.** Compare current UTC time to `2026-11-16T06:35:33Z` (v11 cooldown deadline). If now < deadline and nothing else changed, classify as NO-OP per v1.1 addendum and stop (do not re-run the full gate).
2. **State-change gate (cheap, only if considering a deliverable):** verify config `753d9357…` and canonical manifest `55caedf8…` (324 cells); check `git status --short` and no new commits under frozen-input paths `scripts/ tests/ configs/ data/ results/ docs/ prompts/ schemas/ research_state/hypothesis_registry.json research_state/universe_frontier.json research_state/integrated_extended_v1.json research_state/evaluation_report_extended_v1.json`.
3. **Frontier advance v12 (only if newly actionable AND meaningful cooldown elapsed):** standing unblocked task = ranks 301–325. If you proceed: fresh `/v1/coins` retrieval, de-duplicate by stable asset id against union(frontier candidates_discovered + candidates_rank_unverified, v1–v11 delta = 270 known ids per v11 cursor; note recorded delta union is 247 unique ids). Write `research_state/universe_frontier_advance_v12.json` (artifact_id `EBCR-001-UNIVERSE-FRONTIER-ADVANCE-V12`) with retrieval UTC, raw-response sha256, rank window, dedup set-difference, duplicates with explicit reason, symbol collisions, cursor (`discovered_id_count`, `top_rank_covered=325`, `next_batch_start_rank=326`, `next_batch_end_rank=350`, `rank_frontier_exhausted`), notes. Prior: `universe_frontier_advance_v11.json`. Do not edit frozen `research_state/universe_frontier.json` or `research_state/candidate_perp_mapping_v1.json`. Respect CoinPaprika rate limits.
4. **Do NOT re-run completed work:** frontier advance v1–v11; candidate→perp mapping v2; contract-lifecycle audit; V4 controlled re-estimation; V3→V4 inference audit; exclusion accounting audit. Re-run only if an input changes.
5. **Blocked (do not proceed without stated precondition):** EBCR-H002/H003 — cannot preregister from inspected grid hits; requires new experiment ID + independent preregistered rationale + NEW anchor/config. EBCR-H004 — status change requires separate preregistration decision. Candidate→perp mapping/contract-lifecycle promotion out of `discovery_only_unverified`/PIT-unverified is a separate registration decision.
6. **Preserve invariants:** exclusions n=336 (28 `basis_incomplete` + 308 `incomplete_forward_horizon`); integrated 5,010 rows / 5,346 basis obs; anchor null (`crash_incidence_15pct` adj p 0.24830545694889028; `expected_shortfall_5pct_forward_mae` adj p 0.9485); PIT rank CLOSED; EBCR-H001 `tested_not_supported`; EBCR-H002/H003/H004 `registered_secondary_not_tested`; `next_hypothesis_sequence` 5. No frozen artifact edits; no preregistration from grid hits; preserve null/contradictory/failed evidence.
7. **Report only verified findings.** Do not commit unless explicitly asked. Update handoff and write the next task message.

## Required checks (run only when a relevant input changed)
```bash
python3 scripts/generate_grid_manifest.py --output /tmp/basis-grid-manifest.json   # expect 324 cells, canonical sha256 55caedf8…
# recreate .venv before any test gate: .venv/bin/python -m pytest -q tests  # expect 18 passed
git diff --check
# validate any changed JSON/JSONL/YAML and schemas
```

## Verified baseline (activation 3025, 2026-11-16T03:17:32Z)
- State-change gate: config sha256 `753d9357…` verified; canonical manifest sha256 `55caedf8…` verified (324 cells); `git status --short` clean; `git diff --check` clean; no frozen-path commits since `d34780d2`.
- Frontier v11: `research_state/universe_frontier_advance_v11.json` (created 2026-11-16T03:05:33Z, response_sha256 `36995e20…`, 62,635 items; now committed `60309efd`); 23 net-new ranks 278–300, 2 duplicates (GUSD@276, QTUM@277), 0 collisions, discovered-after 270, top rank 300, next start 301. Tests not run (`.venv` absent); last known 18 passed (activation 2948).
- Anchor null: `crash_incidence_15pct` adj p 0.24830545694889028; `expected_shortfall_5pct_forward_mae` adj p 0.9485.

## Known blockers still open (do not re-probe every activation)
- Raw ingestion snapshots absent from repo (`data/raw/` gitignored) → re-ingestion not reproducible (derived data only).
- Data revision behavior unresolved.
- `exchangeInfo` live snapshot; no free historical PIT status time series.
- EBCR-H002/H003 not testable without new preregistration independent of grid hits and NEW anchor/config.
- EBCR-H004 registry status change requires separate preregistration decision.
- `.venv` absent; recreate before test gate.
- Frontier discovery open-ended: 270 ids covered, `rank_frontier_exhausted = false`; next scan starts at rank 301, only after documented cooldown/meaningful source change since 2026-11-16T03:05:33Z (earliest ≈2026-11-16T06:35:33Z) — no tight polling.