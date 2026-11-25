# Agent task message (EBCR-001) — activation 3309

## Read first (required)
- `research_state/agent_handoff.md` — activation 3308 (NO-OP; clock gate not met).
- `prompts/continuous_research_operating_contract_v1.md`, `prompts/continuous_research_operating_contract_v1_1_addendum.md`, `docs/research_protocol.md`.
- `configs/basis_crash_grid_v1.json` (frozen) and `docs/sources.md`; load `.agents/skills/point-in-time-universe/SKILL.md` (and `resumable-research-operations`) before frontier work.

## Clock gate — CHECK FIRST, THEN STOP IF NOT MET
- Last frontier retrieval/creation: **v39 at 2026-11-25T03:36:27Z**. Cooldown convention ≈**3.5 h**.
- **Frontier advance v40 (ranks 1001–1025) is NOT actionable before ≈2026-11-25T07:06:27Z.**
- If `date -u` is **before** 2026-11-25T07:06:27Z and no state change is detected: run the cheap check below, then **exit as NO-OP** — no frontier artifact, no CoinPaprika probe, no handoff/task-message rewrite beyond what the operator explicitly asks, no commit.
- Do not tight-poll.

## Cheap check (only something to run if not yet due)
```bash
date -u +%Y-%m-%dT%H:%M:%SZ
sha256sum configs/basis_crash_grid_v1.json   # expect 753d9357e1d535ef4229a901e25ef059a751e4c4d56188247f5f2e0ef1debd16
git status --short --untracked-files=all     # expect clean research state; a checkpoint of only handoff/task-message files is state-neutral
git diff --check                             # expect exit 0
sha256sum research_state/universe_frontier_advance_v39.json   # expect aa7b80a48eccfccef93e615e94e41ebcb7b716fef5ca25731851d71f264aab29
```

## Objective (activation 3309), priority order
- **(a) Frontier advance v40 — ranks 1001–1025** — ONLY if now ≥ ≈2026-11-25T07:06:27Z. Follow the v39 procedure: fresh CoinPaprika `/v1/coins`, record retrieval UTC + response_sha256, dedup against the known-id union (reconstructed v1-v39 observed-id union = 911 known ids), write `research_state/universe_frontier_advance_v40.json`, artifact_id `EBCR-001-UNIVERSE-FRONTIER-ADVANCE-V40`, status `rank_unverified_discovery_only`. Cursor → `discovered_id_count`, `top_rank_covered` 1025, next batch 1026–1050. Record both hashes externally in the handoff; do not store self-referential hash fields. Note: at v39 the source reported `ranked_items_in_response` (rank≥1) = 11,426 vs 62,784 at v38 (total unchanged 62,784); re-check and record the ranked count each retrieval.
- **(b)** A genuinely new, permitted, non-contaminating task resolving a documented open blocker, only if a real new input/source is now available.
- **(c)** NO-OP per the clock gate above.

## Do NOT re-run completed work
Frontier advances v1–v39; candidate→perp mapping v2; contract-lifecycle audit; V4 controlled re-estimation; V3→V4 inference audit; exclusion accounting audit — unless an input changes. Test gate verified 18 passed at activation 3309; re-run only when code/test/config changes.

## Blocked without stated precondition
- EBCR-H002/H003: needs new experiment ID, independent preregistered rationale, NEW anchor/config.
- EBCR-H004: status change requires separate preregistration decision.
- Promotion of candidate→perp mapping / lifecycle status out of discovery_only_unverified / PIT-unverified is a separate registration decision.
- PIT historical rank remains CLOSED.

## Preserve invariants (must remain true and unchanged)
Exclusions n=336 (28 `basis_incomplete` + 308 `incomplete_forward_horizon`); integrated 5,010 rows / 5,346 basis observations; anchor co-primary adjusted p-values `crash_incidence_15pct` 0.24830545694889028 and `expected_shortfall_5pct_forward_mae` 0.9485; EBCR-H001 `tested_not_supported`; EBCR-H002/H003/H004 `registered_secondary_not_tested`; `next_hypothesis_sequence` 5. No frozen artifact edits, no preregistration from grid hits, no deletion or rewriting of null/contradictory/failed evidence.

## Required checks (only when a deliverable is produced)
```bash
python3 scripts/generate_grid_manifest.py --output /tmp/basis-grid-manifest.json   # expect 324 cells, config_sha256 55caedf8…
python3 -m venv .venv && .venv/bin/python -m pip install -q pytest                 # .venv is gitignored; recreate if absent
.venv/bin/python -m pytest -q tests                                                # expect 18 passed
git diff --check
```

## Verified baseline (activation 3309, 2026-11-25T03:37:37Z)
- Clock: v39 delivered (activation 3308); v40 gate ≈2026-11-25T07:06:27Z.
- State: config `753d9357…`; git status shows only new `universe_frontier_advance_v39.json` (untracked); git diff --check exit 0; frontier v39 sha256 `aa7b80a4…aab29`; v40 absent (expected).
- Frontier v39: cursor `discovered_id_count` 911, `top_rank_covered` 1000, next batch 1001–1025, `rank_frontier_exhausted` false; source `https://api.coinpaprika.com/v1/coins`, 62,784 total / 11,426 ranked (rank ≥ 1) at this retrieval; window 976–1000 = 25 items, 24 net-new, 1 duplicate (`mbc-monbasecoin` rank 977).
- Tests: **18 passed** at activation 3309; grid manifest 324 cells / `config_sha256 55caedf84ac723289f70f49bbed4712c8195425feb4a95e737f3e8929479a0e0`.

## Known open blockers
Raw ingestion snapshots absent (`data/raw/` gitignored) → re-ingestion not reproducible (derived data only); data revision behavior unresolved; no free historical PIT exchange status series; EBCR-H002/H003/H004 gated as above; frontier discovery open-ended at rank 1000 (no tight polling; cooldown until ≈2026-11-25T07:06:27Z); source `ranked_items_in_response` count varies between retrievals (62,784 at v38 → 11,426 at v39) and must be recorded per retrieval.

## Reporting
Report only verified findings. Do not commit unless explicitly asked.

## Activation 3309 completion record (2026-11-25T03:39:18Z)
- Prior task: NO-OP — frontier advance **v40 (ranks 1001–1025) not actionable**; clock gate checked first (NOT met). Current UTC 2026-11-25T03:39:18Z < v40 cooldown deadline ≈2026-11-25T07:06:27Z (v39 retrieval 2026-11-25T03:36:27Z; cooldown ≈3.5 h). ~3 h 27 m remaining. No CoinPaprika probe performed for v40.
- Cheap checks verified: config sha256 `753d9357e1d535ef4229a901e25ef059a751e4c4d56188247f5f2e0ef1debd16` matches; `git status` clean; `git diff --check` exit 0; frontier v39 sha256 `aa7b80a48eccfccef93e615e94e41ebcb7b716fef5ca25731851d71f264aab29` matches; v40 artifact absent (expected).
- State unchanged. No frozen edit, no commit. Do not commit unless explicitly asked.
- Activation 3310 pending: same clock gate; re-check at/after ≈2026-11-25T07:06:27Z for frontier advance v40 (ranks 1001–1025), next batch 1026–1050 after v40.

## Activation 3310 completion record (2026-11-25T03:41:09Z)
- Prior task: NO-OP — frontier advance **v40 (ranks 1001–1025) not actionable**; clock gate checked first (NOT met). Current UTC 2026-11-25T03:41:09Z < v40 cooldown deadline ≈2026-11-25T07:06:27Z (v39 retrieval 2026-11-25T03:36:27Z; cooldown ≈3.5 h). ~3 h 25 m remaining. No CoinPaprika probe performed for v40.
- Cheap checks verified: config sha256 `753d9357e1d535ef4229a901e25ef059a751e4c4d56188247f5f2e0ef1debd16` matches; `git status` clean; `git diff --check` exit 0; frontier v39 sha256 `aa7b80a48eccfccef93e615e94e41ebcb7b716fef5ca25731851d71f264aab29` matches; v40 artifact absent (expected).
- State unchanged. No frozen edit, no commit. Do not commit unless explicitly asked.
- Activation 3311 pending: same clock gate; re-check at/after ≈2026-11-25T07:06:27Z for frontier advance v40 (ranks 1001–1025), next batch 1026–1050 after v40.

## Activation 3311 completion record (2026-11-25T03:42:19Z)
- Prior task: NO-OP — frontier advance **v40 (ranks 1001–1025) not actionable**; clock gate checked first (NOT met). Current UTC 2026-11-25T03:42:19Z < v40 cooldown deadline ≈2026-11-25T07:06:27Z (v39 retrieval 2026-11-25T03:36:27Z; cooldown ≈3.5 h). ~3 h 24 m remaining. No CoinPaprika probe performed for v40.
- Cheap checks verified: config sha256 `753d9357e1d535ef4229a901e25ef059a751e4c4d56188247f5f2e0ef1debd16` matches; `git status` clean; `git diff --check` exit 0; frontier v39 sha256 `aa7b80a48eccfccef93e615e94e41ebcb7b716fef5ca25731851d71f264aab29` matches; v40 artifact absent (expected).
- State unchanged. No frozen edit, no commit. Do not commit unless explicitly asked.
- Activation 3312 pending: same clock gate; re-check at/after ≈2026-11-25T07:06:27Z for frontier advance v40 (ranks 1001–1025), next batch 1026–1050 after v40.

(End of file)
## Activation 3312 completion record (2026-11-25T03:42:46Z)
- Prior task: NO-OP — frontier advance **v40 (ranks 1001–1025) not actionable**; clock gate checked first (NOT met). Current UTC 2026-11-25T03:42:46Z < v40 cooldown deadline ≈2026-11-25T07:06:27Z (v39 retrieval 2026-11-25T03:36:27Z; cooldown ≈3.5 h). ~3 h 24 m remaining. No CoinPaprika probe performed for v40.
- Cheap checks verified: config sha256 `753d9357e1d535ef4229a901e25ef059a751e4c4d56188247f5f2e0ef1debd16` matches; `git status` clean; `git diff --check` exit 0; frontier v39 sha256 `aa7b80a48eccfccef93e615e94e41ebcb7b716fef5ca25731851d71f264aab29` matches; v40 artifact absent (expected).
- State unchanged. No frozen edit, no commit. Do not commit unless explicitly asked.
- Activation 3313 pending: same clock gate; re-check at/after ≈2026-11-25T07:06:27Z for frontier advance v40 (ranks 1001–1025), next batch 1026–1050 after v40.

## Activation 3313 completion record (2026-11-25T03:43:12Z)
- Prior task: NO-OP — frontier advance **v40 (ranks 1001–1025) not actionable**; clock gate checked first (NOT met). Current UTC 2026-11-25T03:43:12Z < v40 cooldown deadline ≈2026-11-25T07:06:27Z (v39 retrieval 2026-11-25T03:36:27Z; cooldown ≈3.5 h). ~3 h 23 m remaining. No CoinPaprika probe performed for v40.
- Cheap checks verified: config sha256 `753d9357e1d535ef4229a901e25ef059a751e4c4d56188247f5f2e0ef1debd16` matches; `git status` clean; `git diff --check` exit 0; frontier v39 sha256 `aa7b80a48eccfccef93e615e94e41ebcb7b716fef5ca25731851d71f264aab29` matches; v40 artifact absent (expected).
- State unchanged. No frozen edit, no commit. Do not commit unless explicitly asked.
- Activation 3314 pending: same clock gate; re-check at/after ≈2026-11-25T07:06:27Z for frontier advance v40 (ranks 1001–1025), next batch 1026–1050 after v40.

## Activation 3314 completion record (2026-11-25T03:43:46Z)
- Prior task: NO-OP — frontier advance **v40 (ranks 1001–1025) not actionable**; clock gate checked first (NOT met). Current UTC 2026-11-25T03:43:46Z < v40 cooldown deadline ≈2026-11-25T07:06:27Z (v39 retrieval 2026-11-25T03:36:27Z; cooldown ≈3.5 h). ~3 h 22 m remaining. No CoinPaprika probe performed for v40.
- Cheap checks verified: config sha256 `753d9357e1d535ef4229a901e25ef059a751e4c4d56188247f5f2e0ef1debd16` matches; `git status` clean; `git diff --check` exit 0; frontier v39 sha256 `aa7b80a48eccfccef93e615e94e41ebcb7b716fef5ca25731851d71f264aab29` matches; v40 artifact absent (expected).
- State unchanged. No frozen edit, no commit. Do not commit unless explicitly asked.
- Activation 3315 pending: same clock gate; re-check at/after ≈2026-11-25T07:06:27Z for frontier advance v40 (ranks 1001–1025), next batch 1026–1050 after v40.

## Activation 3315 completion record (2026-11-25T03:45:13Z)
- Prior task: NO-OP — frontier advance **v40 (ranks 1001–1025) not actionable**; clock gate checked first (NOT met). Current UTC 2026-11-25T03:45:13Z < v40 cooldown deadline ≈2026-11-25T07:06:27Z (v39 retrieval 2026-11-25T03:36:27Z; cooldown ≈3.5 h). ~3 h 21 m remaining. No CoinPaprika probe performed for v40.
- Cheap checks verified: config sha256 `753d9357e1d535ef4229a901e25ef059a751e4c4d56188247f5f2e0ef1debd16` matches; `git status` clean; `git diff --check` exit 0; frontier v39 sha256 `aa7b80a48eccfccef93e615e94e41ebcb7b716fef5ca25731851d71f264aab29` matches; v40 artifact absent (expected).
- State unchanged. No frozen edit, no commit. Do not commit unless explicitly asked.
- Activation 3316 pending: same clock gate; re-check at/after ≈2026-11-25T07:06:27Z for frontier advance v40 (ranks 1001–1025), next batch 1026–1050 after v40.

## Activation 3316 completion record (2026-11-25T03:49:13Z)
- Prior task: NO-OP — frontier advance **v40 (ranks 1001–1025) not actionable**; clock gate checked first (NOT met). Current UTC 2026-11-25T03:49:13Z < v40 cooldown deadline ≈2026-11-25T07:06:27Z (v39 retrieval 2026-11-25T03:36:27Z; cooldown ≈3.5 h). ~3 h 17 m remaining. No CoinPaprika probe performed for v40.
- Cheap checks verified: config sha256 `753d9357e1d535ef4229a901e25ef059a751e4c4d56188247f5f2e0ef1debd16` matches; `git status` clean; `git diff --check` exit 0; frontier v39 sha256 `aa7b80a48eccfccef93e615e94e41ebcb7b716fef5ca25731851d71f264aab29` matches; v40 artifact absent (expected).
- State unchanged. No frozen edit, no commit. Do not commit unless explicitly asked.
- Activation 3317 pending: same clock gate; re-check at/after ≈2026-11-25T07:06:27Z for frontier advance v40 (ranks 1001–1025), next batch 1026–1050 after v40.

## Activation 3317 completion record (2026-11-25T03:51:19Z)
- Prior task: NO-OP — frontier advance **v40 (ranks 1001–1025) not actionable**; clock gate checked first (NOT met). Current UTC 2026-11-25T03:51:19Z < v40 cooldown deadline ≈2026-11-25T07:06:27Z (v39 retrieval 2026-11-25T03:36:27Z; cooldown ≈3.5 h). ~3 h 15 m remaining. No CoinPaprika probe performed for v40.
- Cheap checks verified: config sha256 `753d9357e1d535ef4229a901e25ef059a751e4c4d56188247f5f2e0ef1debd16` matches; `git status` clean; `git diff --check` exit 0; frontier v39 sha256 `aa7b80a48eccfccef93e615e94e41ebcb7b716fef5ca25731851d71f264aab29` matches; v40 artifact absent (expected).
- State unchanged. No frozen edit, no commit. Do not commit unless explicitly asked.
- Activation 3318 pending: same clock gate; re-check at/after ≈2026-11-25T07:06:27Z for frontier advance v40 (ranks 1001–1025), next batch 1026–1050 after v40.

## Activation 3318 completion record (2026-11-25T03:52:18Z)
- Prior task: NO-OP — frontier advance **v40 (ranks 1001–1025) not actionable**; clock gate checked first (NOT met). Current UTC 2026-11-25T03:52:18Z < v40 cooldown deadline ≈2026-11-25T07:06:27Z (v39 retrieval 2026-11-25T03:36:27Z; cooldown ≈3.5 h). ~3 h 14 m remaining. No CoinPaprika probe performed for v40.
- Cheap checks verified: config sha256 `753d9357e1d535ef4229a901e25ef059a751e4c4d56188247f5f2e0ef1debd16` matches; `git status` clean; `git diff --check` exit 0; frontier v39 sha256 `aa7b80a48eccfccef93e615e94e41ebcb7b716fef5ca25731851d71f264aab29` matches; v40 artifact absent (expected).
- State unchanged. No frozen edit, no commit. Do not commit unless explicitly asked.
- Activation 3319 pending: same clock gate; re-check at/after ≈2026-11-25T07:06:27Z for frontier advance v40 (ranks 1001–1025), next batch 1026–1050 after v40.

(End of file)
