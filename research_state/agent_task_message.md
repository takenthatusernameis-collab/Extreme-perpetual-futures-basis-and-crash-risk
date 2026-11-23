# Agent task message (EBCR-001) — activation 3267

## Read first (required)
- `research_state/agent_handoff.md` — activation 3266 (NO-OP; v36 due ≈2026-11-23T15:49:10Z).
- `prompts/continuous_research_operating_contract_v1.md`, `prompts/continuous_research_operating_contract_v1_1_addendum.md`, `docs/research_protocol.md`.
- `configs/basis_crash_grid_v1.json` (frozen) and `docs/sources.md`; load `.agents/skills/point-in-time-universe/SKILL.md` (and `resumable-research-operations`) before frontier work.

## Clock gate — CHECK FIRST, THEN STOP IF NOT MET
- Last frontier retrieval/creation: **v35 at 2026-11-23T12:19:10Z**. Cooldown convention ≈**3.5 h**.
- **Frontier advance v36 (ranks 901–925) is NOT actionable before ≈2026-11-23T15:49:10Z.**
- If `date -u` is **before** 2026-11-23T15:49:10Z and no state change is detected: run the cheap check below, then **exit as NO-OP** — no frontier artifact, no CoinPaprika probe, no handoff/task-message rewrite beyond what the operator explicitly asks, no commit.
- Do not tight-poll.

## Cheap check (only thing to run if not yet due)
```bash
date -u +%Y-%m-%dT%H:%M:%SZ
sha256sum configs/basis_crash_grid_v1.json   # expect 753d9357e1d535ef4229a901e25ef059a751e4c4d56188247f5f2e0ef1debd16
git status --short --untracked-files=all     # expect clean research state; a checkpoint of only handoff/task-message files is state-neutral
git diff --check                             # expect exit 0
sha256sum research_state/universe_frontier_advance_v35.json   # expect 7c74352ac231c6aa006728aac82dd4e3124d473d5074294f6b9f28b56fd254d6
```

## Objective (activation 3267), priority order
- **(a) Frontier advance v36 — ranks 901–925** — ONLY if now ≥ ≈2026-11-23T15:49:10Z. Follow the v35 procedure: fresh CoinPaprika `/v1/coins`, record retrieval UTC + response_sha256, dedup against the 824 known ids (reconstructed v1-v35 observed-id union), write `research_state/universe_frontier_advance_v36.json`, artifact_id `EBCR-001-UNIVERSE-FRONTIER-ADVANCE-V36`, status `rank_unverified_discovery_only`. Cursor → `discovered_id_count`, `top_rank_covered` 925, next batch 926–950. Record both hashes externally in the handoff; do not store self-referential hash fields.
- **(b)** A genuinely new, permitted, non-contaminating task resolving a documented open blocker, only if a real new input/source is now available.
- **(c)** NO-OP per the clock gate above.

## Do NOT re-run completed work
Frontier advances v1–v35; candidate→perp mapping v2; contract-lifecycle audit; V4 controlled re-estimation; V3→V4 inference audit; exclusion accounting audit — unless an input changes. Test gate verified 18 passed at HEAD (activation 3233); re-run only when code/test/config changes.

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

## Verified baseline (activation 3266, 2026-11-23T12:31:39Z)
- Clock: v35 delivered (activation 3259); v36 gate ≈2026-11-23T15:49:10Z.
- State: config `753d9357…`; git status clean (frontier v35 tracked; HEAD state-neutral); git diff --check exit 0; frontier v35 sha256 `7c74352a…54d6`; v36 absent (expected).
- Frontier v35: cursor `discovered_id_count` 824, `top_rank_covered` 900, next batch 901–925, `rank_frontier_exhausted` false; source `https://api.coinpaprika.com/v1/coins`, 62,761 total / 11,270 ranked (rank ≥ 1).
- Tests: **18 passed** at activation 3233; grid manifest 324 cells / `config_sha256 55caedf84ac723289f70f49bbed4712c8195425feb4a95e737f3e8929479a0e0`.

## Known open blockers
Raw ingestion snapshots absent (`data/raw/` gitignored) → re-ingestion not reproducible (derived data only); data revision behavior unresolved; no free historical PIT exchange status series; EBCR-H002/H003/H004 gated as above; frontier discovery open-ended at rank 900 (no tight polling; cooldown until ≈2026-11-23T15:49:10Z).

## Reporting
Report only verified findings. Do not commit unless explicitly asked.