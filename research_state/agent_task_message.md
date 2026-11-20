# Agent task message (EBCR-001) — activation 3134 (written end of activation 3133)

## Read first (required)
- `research_state/agent_handoff.md` — activation 3133 (NO-OP; clock gate not met) and activation 3132 (NO-OP); last research state-change was activation 3123 (frontier advance v24, ranks 601–625, cursor 557→578, top_rank_covered 625).
- `prompts/continuous_research_operating_contract_v1.md`, `prompts/continuous_research_operating_contract_v1_1_addendum.md`, `docs/research_protocol.md`.
- `configs/basis_crash_grid_v1.json` (frozen) and `docs/sources.md`; load `.agents/skills/point-in-time-universe/SKILL.md` (and `resumable-research-operations`) before frontier work.

## Clock gate — CHECK FIRST, THEN STOP IF NOT MET
- Last frontier retrieval/creation: **v24 at 2026-11-20T04:17:40Z**. Cooldown convention ≈**3.5 h**.
- **Frontier advance v25 (ranks 626–650) is NOT actionable before ≈2026-11-20T07:47:40Z.**
- If `date -u` is **before** 2026-11-20T07:47:40Z and no state change is detected: run the cheap check below, then **exit as NO-OP** — no frontier artifact, no CoinPaprika probe, no handoff rewrite beyond a single short record if the operator explicitly asks, no commit.
- A wakeup fires at **2026-11-20T07:50:00Z** carrying the v25 trigger (id `wku_1f73c67dc001Bpx2387dzGQtb4`). Do not add another and do not tight-poll.
- Verify with `cancel_wakeup list` rather than trusting a stale id.

## Cheap check (only thing to run if not yet due)
```bash
date -u +%Y-%m-%dT%H:%M:%SZ
sha256sum configs/basis_crash_grid_v1.json   # expect 753d9357e1d535ef4229a901e25ef059a751e4c4d56188247f5f2e0ef1debd16
git status --short --untracked-files=all     # expect empty (or only expected new artifacts)
git diff --check                             # expect exit 0
```

## Objective (activation 3134), priority order
- **(a) Frontier advance v25 — ranks 626–650** — ONLY if now ≥ ≈2026-11-20T07:47:40Z. Procedure:
  - Fresh public CoinPaprika `/v1/coins` retrieval; record retrieval UTC timestamp and `response_sha256`.
  - Record total items and ranked items (v24: 62,730 total / 11,087 ranked (rank ≥ 1); always record the observed value; a ranked-count change is a documented source-coverage event).
  - Dedup the rank 626–650 window against the 578 known ids (reconstruct the v1–v24 observed-id union; skip current-rank duplicates and log symbol collisions separately).
  - Write `research_state/universe_frontier_advance_v25.json`, artifact_id `EBCR-001-UNIVERSE-FRONTIER-ADVANCE-V25`, status `rank_unverified_discovery_only`. Match the v24 artifact key layout: `artifact_id`, `schema_version`, `program_id`, `created_at_utc`, `task_activation`, `purpose`, `prior_artifact`, `source`, `frontier_state`, `discovery_method`, `candidates_discovered_delta`, `duplicates_skipped`, `symbol_collisions`, `cursor`.
  - Cursor → `discovered_id_count`, `top_rank_covered` 650, next batch 651–675, `rank_frontier_exhausted` false unless the window is short.
  - No frozen edits. Record **both** hashes externally in the handoff (content sha256 = `json.dumps(d, sort_keys=False, separators=(",", ":"))`; raw-bytes sha256 = sha256 of the written file bytes). Do **not** store self-referential hash fields inside the artifact (matching v18–v24).
- **(b)** A genuinely new, permitted, non-contaminating task resolving a documented open blocker, only if a real new input/source is now available.
- **(c)** NO-OP per the clock gate above.

## Do NOT re-run completed work
Frontier advances v1–v24; candidate→perp mapping v2; contract-lifecycle audit; V4 controlled re-estimation; V3→V4 inference audit; exclusion accounting audit — unless an input changes.
The repository test gate is verified as of activation 3123 (18 passed at HEAD); re-run it only when code/test/config changes, not on every activation.

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

## Verified baseline (activation 3133, 2026-11-20T04:36:52Z)
- Clock: 04:36:52Z < 07:47:40Z → v25 gate NOT met (NO-OP).
- State: config `753d9357…`; `git status --short --untracked-files=all` → empty; `git diff --check` exit 0; frozen hashes unchanged (frontier `e8826caf…` / registry `d5b299bf…` / v24 `33af01f2…`).
- Frontier v24: `research_state/universe_frontier_advance_v24.json`; cursor `discovered_id_count` 578, `top_rank_covered` 625, next batch 626–650, `rank_frontier_exhausted = false`; source `https://api.coinpaprika.com/v1/coins`, `response_sha256` `fa1b19546e1a683942252ea6e2175a1407e375f3a81d998087badf8f0d4c7038`, 62,730 total / 11,087 ranked (rank ≥ 1).
- Tests: **18 passed** at activation 3123 (HEAD); grid manifest 324 cells / `config_sha256 55caedf8…`.
- Wakeup: scheduled for 2026-11-20T07:50:00Z carrying the v25 trigger (id `wku_1f73c67dc001Bpx2387dzGQtb4`).

## Known open blockers
Raw ingestion snapshots absent (`data/raw/` gitignored) → re-ingestion not reproducible (derived data only); data revision behavior unresolved; no free historical PIT exchange status series; EBCR-H002/H003/H004 gated as above; frontier discovery open-ended at rank 625 (no tight polling; cooldown until ≈2026-11-20T07:47:40Z).

## Reporting
Report only verified findings. Do not commit unless explicitly asked.