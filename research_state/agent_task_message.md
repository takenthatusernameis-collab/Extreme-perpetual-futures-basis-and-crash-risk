# Agent task message (EBCR-001) — activation 3107 (written end of activation 3106)

## Read first (required)
- `research_state/agent_handoff.md` — activation 3106 (frontier advance v21, cursor 514 / rank 550) and activation 3100 (frontier advance v20, cursor 490 / rank 525).
- `prompts/continuous_research_operating_contract_v1.md`, `prompts/continuous_research_operating_contract_v1_1_addendum.md`, `docs/research_protocol.md`.
- `configs/basis_crash_grid_v1.json` (frozen) and `docs/sources.md`; load `.agents/skills/point-in-time-universe/SKILL.md` (and `resumable-research-operations`) before frontier work.

## Clock gate — CHECK FIRST, THEN STOP IF NOT MET
- Last frontier retrieval/creation: **v21 at 2026-11-19T08:14:30Z**. Cooldown convention ≈**3.5 h**.
- **Frontier advance v22 (ranks 551–575) is NOT actionable before ≈2026-11-19T11:50:45Z.**
- If `date -u` is **before** 2026-11-19T11:50:45Z and no state change is detected: run the cheap check below, then **exit as NO-OP** — no frontier artifact, no CoinPaprika probe, no handoff rewrite beyond a single short record if the operator explicitly asks, no commit.
- A wakeup is already scheduled for 2026-11-19T04:24:30Z carrying the v21 trigger (id `wku_1f16f3490001NpLXwxPcdPkQJP`). Do not add another and do not tight-poll.
- Do not extend the deadline unless a documented source/network condition justifies a longer wait.

## Cheap check (only thing to run if not yet due)
```bash
date -u +%Y-%m-%dT%H:%M:%SZ
sha256sum configs/basis_crash_grid_v1.json   # expect 753d9357e1d535ef4229a901e25ef059a751e4c4d56188247f5f2e0ef1debd16
git status --short --untracked-files=all     # expect empty (or only expected new artifacts)
```

## Objective (activation 3107), priority order
- **(a) Frontier advance v22 — ranks 551–575** — ONLY if now ≥ ≈2026-11-19T11:50:45Z. Procedure:
  - Fresh public CoinPaprika `/v1/coins` retrieval; record retrieval UTC timestamp and `response_sha256`.
  - Record total items and ranked items (v21: 62,713 / 11,015; always record the observed value; a ranked-count change is a documented source-coverage event).
  - Dedup the rank 551–575 window against the 514 known ids (reconstruct the v1–v21 observed-id union; skip current-rank duplicates and log symbol collisions separately).
  - Write `research_state/universe_frontier_advance_v22.json`, artifact_id `EBCR-001-UNIVERSE-FRONTIER-ADVANCE-V22`, status `rank_unverified_discovery_only`.
  - Cursor → `discovered_id_count`, `top_rank_covered` 575, next batch 576–600, `rank_frontier_exhausted` false unless the window is short.
  - No frozen edits. Record **both** hashes externally in the handoff (content sha256 = `json.dumps(d, sort_keys=False, separators=(",", ":"))`; raw-bytes sha256 = sha256 of the written file bytes). Do **not** store self-referential hash fields inside the artifact (matching v18/v19/v20/v21).
- **(b)** A genuinely new, permitted, non-contaminating task resolving a documented open blocker, only if a real new input/source is now available.
- **(c)** NO-OP per the clock gate above.

## Do NOT re-run completed work
Frontier advances v1–v22; candidate→perp mapping v2; contract-lifecycle audit; V4 controlled re-estimation; V3→V4 inference audit; exclusion accounting audit — unless an input changes.
The repository test gate is verified as of activation 3106 (18 passed at HEAD); re-run it only when code/test/config changes, not on every activation.

## Blocked without stated precondition
- EBCR-H002/H003: needs new experiment ID, independent preregistered rationale, NEW anchor/config.
- EBCR-H004: status change requires separate preregistration decision.
- Promotion of candidate→perp mapping / lifecycle status out of `discovery_only_unverified` / PIT-unverified is a separate registration decision.
- PIT historical rank remains CLOSED.

## Preserve invariants (must remain true and unchanged)
Exclusions n=336 (28 `basis_incomplete` + 308 `incomplete_forward_horizon`); integrated 5,010 rows / 5,346 basis observations; anchor co-primary adjusted p-values `crash_incidence_15pct` 0.24830545694889028 and `expected_shortfall_5pct_forward_mae` 0.9485; EBCR-H001 `tested_not_supported`; EBCR-H002/H003/H004 `registered_secondary_not_tested`; `next_hypothesis_sequence` 5. No frozen artifact edits, no preregistration from grid hits, no deletion or rewriting of null/contradictory/failed evidence.

## Required checks (only when a deliverable is produced)
```bash
python3 scripts/generate_grid_manifest.py --output /tmp/basis-grid-manifest.json   # expect 324 cells, config_sha256 55caedf84ac723289f70f49bbed4712c8195425feb4a95e737f3e8929479a0e0
python3 -m venv .venv && .venv/bin/python -m pip install -q pytest                 # .venv is gitignored; recreate if absent
.venv/bin/python -m pytest -q tests                                                # expect 18 passed
git diff --check
# validate any changed JSON/JSONL/YAML and its schema
```

## Verified baseline (activation 3106, 2026-11-19T08:16:45Z)
- Clock: 08:14:25Z ≥ 04:24:10Z → v21 actionable. v21 retrieval 08:14:30Z.
- State: config `753d9357…`; `git status --short --untracked-files=all` → only `research_state/universe_frontier_advance_v21.json`; `git diff --check` exit 0; frozen hashes `e8826caf…` (frontier) / `d5b299bf…` (registry) / `28ec0163…` (integrated) / `9487b36d…` (evaluation) unchanged.
- Frontier v21: `research_state/universe_frontier_advance_v21.json`; content sha256 `c9daa696e2b1a5763343501c8fa914a00397275e9760182c4c50e20cddc6c634`, raw-bytes sha256 `81aec400750abb5c5683b42034c96f6f6040e7a52700a4e75d43235108eed68e`; cursor `discovered_id_count` 514, `top_rank_covered` 550, next batch 551–575, `rank_frontier_exhausted = false`.
- Tests: **18 passed** (`.venv`, pytest 0.25s) at HEAD; grid manifest 324 cells / `config_sha256 55caedf8…`.
- Source coverage change: CoinPaprika ranked count 11,015 (v20: 62,712; v19: 62,712) — documented.

## Known open blockers
Raw ingestion snapshots absent (`data/raw/` gitignored) → re-ingestion not reproducible (derived data only); data revision behavior unresolved; no free historical PIT exchange status series; EBCR-H002/H003/H004 gated as above; frontier discovery open-ended at rank 550 (no tight polling; cooldown until ≈11:50:45Z).

## Reporting
Report only verified findings. Do not commit unless explicitly asked.

(End of file - total 65 lines)