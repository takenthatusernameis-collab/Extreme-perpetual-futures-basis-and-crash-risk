# Agent task message (EBCR-001) — activation 3145 (written end of activation 3144)

## Read first (required)
- `research_state/agent_handoff.md` — activation 3144 (NO-OP, clock gate not met; v26 due ≈2026-11-20T16:34:15Z).
- `prompts/continuous_research_operating_contract_v1.md`, `prompts/continuous_research_operating_contract_v1_1_addendum.md`, `docs/research_protocol.md`.
- `configs/basis_crash_grid_v1.json` (frozen) and `docs/sources.md`; load `.agents/skills/point-in-time-universe/SKILL.md` (and `resumable-research-operations`) before frontier work.

## Clock gate — CHECK FIRST, THEN STOP IF NOT MET
- Last frontier retrieval/creation: **v25 at 2026-11-20T13:04:15Z**. Cooldown convention ≈**3.5 h**.
- **Frontier advance v26 (ranks 651–675) is NOT actionable before ≈2026-11-20T16:34:15Z.**
- If `date -u` is **before** 2026-11-20T16:34:15Z and no state change is detected: run the cheap check below, then **exit as NO-OP** — no frontier artifact, no CoinPaprika probe, no handoff rewrite beyond a single short record if the operator explicitly asks, no commit.
- Do not tight-poll.

## Cheap check (only thing to run if not yet due)
```bash
date -u +%Y-%m-%dT%H:%M:%SZ
sha256sum configs/basis_crash_grid_v1.json   # expect 753d9357e1d535ef4229a901e25ef059a751e4c4d56188247f5f2e0ef1debd16
git status --short --untracked-files=all     # expect empty (or only expected new artifacts)
git diff --check                             # expect exit 0
```

## Objective (activation 3145), priority order
- **(a) Frontier advance v26 — ranks 651–675** — ONLY if now ≥ ≈2026-11-20T16:34:15Z. Follow the v25 procedure: fresh CoinPaprika `/v1/coins`, record retrieval UTC + response_sha256, dedup against 600 known ids, write `research_state/universe_frontier_advance_v26.json`, artifact_id `EBCR-001-UNIVERSE-FRONTIER-ADVANCE-V26`, status `rank_unverified_discovery_only`. Cursor → discovered_id_count, top_rank_covered 675, next batch 676–700. Record both hashes externally in handoff; do not store self-referential hash fields.
- **(b)** A genuinely new, permitted, non-contaminating task resolving a documented open blocker, only if a real new input/source is now available.
- **(c)** NO-OP per the clock gate above.

## Do NOT re-run completed work
Frontier advances v1–v25; candidate→perp mapping v2; contract-lifecycle audit; V4 controlled re-estimation; V3→V4 inference audit; exclusion accounting audit — unless an input changes. Test gate verified 18 passed at HEAD; re-run only when code/test/config changes.

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

## Verified baseline (activation 3144, 2026-11-20T13:18:34Z)
- Clock: v25 delivered; v26 gate ≈2026-11-20T16:34:15Z.
- State: config `753d9357…`; git status clean; git diff --check exit 0; frozen hashes unchanged (frontier `e8826caf…` / registry `d5b299bf…` / v25 `89fe8c82…`).
- Frontier v25: `research_state/universe_frontier_advance_v25.json`; cursor `discovered_id_count` 600, `top_rank_covered` 650, next batch 651–675, `rank_frontier_exhausted = false`; source `https://api.coinpaprika.com/v1/coins`, 62,736 total / 11,408 ranked (rank ≥ 1).
- Tests: **18 passed** at HEAD; grid manifest 324 cells / `config_sha256 55caedf8…`.

## Known open blockers
Raw ingestion snapshots absent (`data/raw/` gitignored) → re-ingestion not reproducible (derived data only); data revision behavior unresolved; no free historical PIT exchange status series; EBCR-H002/H003/H004 gated as above; frontier discovery open-ended at rank 650 (no tight polling; cooldown until ≈2026-11-20T16:34:15Z).

## Reporting
Report only verified findings. Do not commit unless explicitly asked.