# Agent task message (EBCR-001) — activation 3117 (written end of activation 3116)

## Read first (required)
- `research_state/agent_handoff.md` — activation 3116 (frontier advance v23, cursor 557 / rank 600) and activation 3115 (NO-OP).
- `prompts/continuous_research_operating_contract_v1.md`, `prompts/continuous_research_operating_contract_v1_1_addendum.md`, `docs/research_protocol.md`.
- `configs/basis_crash_grid_v1.json` (frozen) and `docs/sources.md`; load `.agents/skills/point-in-time-universe/SKILL.md` (and `resumable-research-operations`) before frontier work.

## Clock gate — CHECK FIRST, THEN STOP IF NOT MET
- Last frontier retrieval/creation: **v23 at 2026-11-19T23:40:50Z** (artifact `created_at_utc`). Cooldown convention ≈**3.5 h**.
- **Frontier advance v24 (ranks 601–625) is NOT actionable before ≈2026-11-20T03:10:50Z.**
- If `date -u` is **before** 2026-11-20T03:10:50Z and no state change is detected: run the cheap check below, then **exit as NO-OP** — no frontier artifact, no CoinPaprika probe, no handoff rewrite beyond a single short record if the operator explicitly asks, no commit.
- A wakeup will fire at **≈2026-11-20T03:10:33Z** carrying the v24 trigger (id `wku_1f6314be90019d6JJOeHrI2y03`). Do not add another and do not tight-poll.
- Verify with `cancel_wakeup list` rather than trusting a stale id.

## Cheap check (only thing to run if not yet due)
```bash
date -u +%Y-%m-%dT%H:%M:%SZ
sha256sum configs/basis_crash_grid_v1.json   # expect 753d9357e1d535ef4229a901e25ef059a751e4c4d56188247f5f2e0ef1debd16
git status --short --untracked-files=all     # expect empty (or only expected new artifacts)
```

## Objective (activation 3117), priority order
- **(a) Frontier advance v24 — ranks 601–625** — ONLY if now ≥ ≈2026-11-20T03:10:50Z. Procedure:
  - Fresh public CoinPaprika `/v1/coins` retrieval; record retrieval UTC timestamp and `response_sha256`.
  - Record total items and ranked items (v23: 62,730 total / 10,958 ranked (rank ≥ 1); always record the observed value; a ranked-count change is a documented source-coverage event).
  - Dedup the rank 601–625 window against the 557 known ids (reconstruct the v1–v23 observed-id union; skip current-rank duplicates and log symbol collisions separately).
  - Write `research_state/universe_frontier_advance_v24.json`, artifact_id `EBCR-001-UNIVERSE-FRONTIER-ADVANCE-V24`, status `rank_unverified_discovery_only`. Match the v23 artifact key layout: `artifact_id`, `schema_version`, `program_id`, `created_at_utc`, `task_activation`, `purpose`, `prior_artifact`, `source`, `frontier_state`, `discovery_method`, `candidates_discovered_delta`, `duplicates_skipped`, `symbol_collisions`, `cursor`, `notes`.
  - Cursor → `discovered_id_count`, `top_rank_covered` 625, next batch 626–650, `rank_frontier_exhausted` false unless the window is short.
  - No frozen edits. Record **both** hashes externally in the handoff (content sha256 = `json.dumps(d, sort_keys=False, separators=(",", ":"))`; raw-bytes sha256 = sha256 of the written file bytes). Do **not** store self-referential hash fields inside the artifact (matching v18–v23).
- **(b)** A genuinely new, permitted, non-contaminating task resolving a documented open blocker, only if a real new input/source is now available.
- **(c)** NO-OP per the clock gate above.

## Do NOT re-run completed work
Frontier advances v1–v23; candidate→perp mapping v2; contract-lifecycle audit; V4 controlled re-estimation; V3→V4 inference audit; exclusion accounting audit — unless an input changes.
The repository test gate is verified as of activation 3116 (18 passed at HEAD); re-run it only when code/test/config changes, not on every activation.

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

## Verified baseline (activation 3116, 2026-11-19T23:41:00Z)
- Clock: 23:40:04Z ≥ 20:53:45Z → v23 actionable (frontier advanced v22→v23).
- State: config `753d9357…`; `git status --short --untracked-files=all` → only `research_state/universe_frontier_advance_v23.json`; `git diff --check` exit 0; frozen hashes unchanged (frontier `e8826caf…` / registry `d5b299bf…`); v23 artifact content `62a5878e…` / raw-bytes `62a5878e…` verified.
- Frontier v23: `research_state/universe_frontier_advance_v23.json`; cursor `discovered_id_count` 557, `top_rank_covered` 600, next batch 601–625, `rank_frontier_exhausted = false`; source `https://api.coinpaprika.com/v1/coins`, `response_sha256` `ea2997abccbd8fc8741637dea810275ba96caff587512ece7e64731d5f3e72f2`, 62,730 total / 10,958 ranked (rank ≥ 1).
- Tests: **18 passed** at activation 3116 (HEAD); grid manifest 324 cells / `config_sha256 55caedf8…`.
- Wakeup: scheduled for ≈2026-11-20T03:10:33Z carrying the v24 trigger (id `wku_1f6314be90019d6JJOeHrI2y03`).

## Known open blockers
Raw ingestion snapshots absent (`data/raw/` gitignored) → re-ingestion not reproducible (derived data only); data revision behavior unresolved; no free historical PIT exchange status series; EBCR-H002/H003/H004 gated as above; frontier discovery open-ended at rank 600 (no tight polling; cooldown until ≈2026-11-20T03:10:50Z).

## Reporting
Report only verified findings. Do not commit unless explicitly asked.
(End of file)
