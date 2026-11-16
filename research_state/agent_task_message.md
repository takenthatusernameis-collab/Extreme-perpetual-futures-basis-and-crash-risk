# Agent task message (EBCR-001) — activation 3023 (written at end of activation 3022)

## Read first (required)
- `research_state/agent_handoff.md` (activation 3022: NO-OP — state-change gate clean, frontier v11 at rank 300, ~3.25 min since v11, cooldown not elapsed for v12; `research_state/universe_frontier_advance_v11.json` untracked, NOT committed)
- `research_state/agent_task_message.md` (this message)
- `prompts/continuous_research_operating_contract_v1.md` and `prompts/continuous_research_operating_contract_v1_1_addendum.md`
- `docs/research_protocol.md`
- `configs/basis_crash_grid_v1.json` (frozen)
- `docs/sources.md` and `.agents/skills/point-in-time-universe/SKILL.md` for source/frontier work

## What changed since the previous activation
- **Activation 3022 (2026-11-16T03:08:48Z): NO-OP.** State-change gate clean (config sha256 `753d9357…`, canonical manifest sha256 `55caedf8…`, 324 cells; git status only v11 untracked; no frozen-path commits since `d34780d2`). Frontier v11 retrieval at 2026-11-16T03:05:33Z — only ~3.25 minutes elapsed, far short of the ~3.5-hour cooldown (earliest actionable ≈2026-11-16T06:35:33Z). No other unblocked task newly actionable.
- **Frozen inputs unchanged:** config literal sha256 `753d9357e1d535ef4229a901e25ef059a751e4c4d56188247f5f2e0ef1debd16`; canonical manifest sha256 `55caedf84ac723289f70f49bbed4712c8195425feb4a95e737f3e8929479a0e0` (324 cells). `.venv` absent; last known **18 passed** (activation 2948).

## Objective (activation 3023)
Advance the highest-value genuinely unblocked work, or document a blocker. Do NOT manufacture work and do NOT tight-poll. Acceptable outcomes: (a) verifiable deliverable (e.g. frontier advance v12 to ranks 301–325 only after meaningful cooldown since 2026-11-16T03:05:33Z or a documented source/network change, evidence audit, or blocker-resolution attempt), (b) documented blocker, or (c) NO-OP if state-change gate clean AND no new admissible source/date event AND no standing unblocked task newly actionable.

## Required actions (activation 3023)
1. **State-change gate first (cheap):** verify config `753d9357…` and canonical manifest `55caedf8…` (324 cells); check `git status --short` and no new commits under frozen-input paths `scripts/ tests/ configs/ data/ results/ docs/ prompts/ schemas/ research_state/hypothesis_registry.json research_state/universe_frontier.json research_state/integrated_extended_v1.json research_state/evaluation_report_extended_v1.json`. If nothing changed and no task below is newly actionable, classify as NO-OP per v1.1 addendum. Do NOT re-run the gate on a minutes-apart cadence (activations 3011–3022 include back-to-back NO-OPs until v11; v12 cooldown not yet elapsed).
2. **Frontier advance v12 (only if newly actionable AND meaningful cooldown elapsed):** standing unblocked task = ranks 301–325. Newly actionable ONLY after meaningful cooldown since last retrieval (2026-11-16T03:05:33Z; ≈2026-11-16T06:35:33Z at ~3.5h) or a documented source/network change — do not tight-poll. If you proceed: fresh `/v1/coins` retrieval, de-duplicate by stable asset id against union(frontier candidates_discovered + candidates_rank_unverified, v1–v11 delta = 270 known ids per v11 cursor; note recorded delta union is 247 unique ids). Write `research_state/universe_frontier_advance_v12.json` (artifact_id `EBCR-001-UNIVERSE-FRONTIER-ADVANCE-V12`) with retrieval UTC, raw-response sha256, rank window, dedup set-difference, duplicates with explicit reason, symbol collisions, cursor (`discovered_id_count`, `top_rank_covered=325`, `next_batch_start_rank=326`, `next_batch_end_rank=350`, `rank_frontier_exhausted`), notes. Prior: `universe_frontier_advance_v11.json`. Do not edit frozen `research_state/universe_frontier.json` or `research_state/candidate_perp_mapping_v1.json`. Respect CoinPaprika rate limits.
3. **Do NOT re-run completed work:** frontier advance v1–v11; candidate→perp mapping v2; contract-lifecycle audit; V4 controlled re-estimation; V3→V4 inference audit; exclusion accounting audit. Re-run only if an input changes.
4. **Blocked (do not proceed without stated precondition):** EBCR-H002/H003 — cannot preregister from inspected grid hits; requires new experiment ID + independent preregistered rationale + NEW anchor/config. EBCR-H004 — status change requires separate preregistration decision. Candidate→perp mapping/contract-lifecycle promotion out of `discovery_only_unverified`/PIT-unverified is a separate registration decision.
5. **Preserve invariants:** exclusions n=336 (28 `basis_incomplete` + 308 `incomplete_forward_horizon`); integrated 5,010 rows / 5,346 basis obs; anchor null (`crash_incidence_15pct` adj p 0.24830545694889028; `expected_shortfall_5pct_forward_mae` adj p 0.9485); PIT rank CLOSED; EBCR-H001 `tested_not_supported`; EBCR-H002/H003/H004 `registered_secondary_not_tested`; `next_hypothesis_sequence` 5. No frozen artifact edits; no preregistration from grid hits; preserve null/contradictory/failed evidence.
6. **Report only verified findings.** Do not commit unless explicitly asked. Update handoff and write the next task message.

## Required checks (run only when a relevant input changed)
```bash
python3 scripts/generate_grid_manifest.py --output /tmp/basis-grid-manifest.json   # expect 324 cells, canonical sha256 55caedf8…
# recreate .venv before any test gate: .venv/bin/python -m pytest -q tests  # expect 18 passed
git diff --check
# validate any changed JSON/JSONL/YAML and schemas
```

## Verified baseline (activation 3022, 2026-11-16T03:08:48Z)
- State-change gate: config sha256 `753d9357…` verified; canonical manifest sha256 `55caedf8…` verified (324 cells); `git status --short` clean at gate except v11 untracked artifact; `git diff --check` clean at gate; no frozen-path commits since `d34780d2`.
- Frontier v11: `research_state/universe_frontier_advance_v11.json` (created 2026-11-16T03:05:33Z, response_sha256 `36995e20…`, 62,635 items); 23 net-new ranks 278–300, 2 duplicates (GUSD@276, QTUM@277), 0 collisions, discovered-after 270, top rank 300, next start 301. Tests not run (`.venv` absent); last known 18 passed (activation 2948).
- Anchor null: `crash_incidence_15pct` adj p 0.24830545694889028; `expected_shortfall_5pct_forward_mae` adj p 0.9485.

## Known blockers still open (do not re-probe every activation)
- Raw ingestion snapshots absent from repo (`data/raw/` gitignored) → re-ingestion not reproducible (derived data only).
- Data revision behavior unresolved.
- `exchangeInfo` live snapshot; no free historical PIT status time series.
- EBCR-H002/H003 not testable without new preregistration independent of grid hits and NEW anchor/config.
- EBCR-H004 registry status change requires separate preregistration decision.
- `.venv` absent; recreate before test gate.
- Frontier discovery open-ended: 270 ids covered, `rank_frontier_exhausted = false`; next scan starts at rank 301, only after documented cooldown/meaningful source change since 2026-11-16T03:05:33Z — no tight polling.