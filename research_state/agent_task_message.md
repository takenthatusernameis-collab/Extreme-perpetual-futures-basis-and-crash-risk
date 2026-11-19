# Agent task message (EBCR-001) — activation 3108 (written end of activation 3107)

## Read first (required)
- `research_state/agent_handoff.md` — activation 3107 (NO-OP, clock gate) and activation 3106 (frontier advance v21, cursor 514 / rank 550).
- `prompts/continuous_research_operating_contract_v1.md`, `prompts/continuous_research_operating_contract_v1_1_addendum.md`, `docs/research_protocol.md`.
- `configs/basis_crash_grid_v1.json` (frozen) and `docs/sources.md`; load `.agents/skills/point-in-time-universe/SKILL.md` (and `resumable-research-operations`) before frontier work.

## Clock gate — CHECK FIRST, THEN STOP IF NOT MET
- Last frontier retrieval/creation: **v21 at 2026-11-19T08:14:30Z** (artifact `created_at_utc` 2026-11-19T08:16:43Z). Cooldown convention ≈**3.5 h**.
- **Frontier advance v22 (ranks 551–575) is NOT actionable before ≈2026-11-19T11:50:45Z.**
- If `date -u` is **before** 2026-11-19T11:50:45Z and no state change is detected: run the cheap check below, then **exit as NO-OP** — no frontier artifact, no CoinPaprika probe, no handoff rewrite beyond a single short record if the operator explicitly asks, no commit.
- A wakeup is already scheduled for **2026-11-19T11:51:30Z** carrying the v22 trigger (id `wku_1f2e7fc82001LZ6q0nFu9L7c0u`). Do not add another and do not tight-poll.
- Note: the wakeup named in the previous task message (`wku_1f16f3490001NpLXwxPcdPkQJP`, 2026-11-19T04:24:30Z) already fired and did not carry over. Verify with `cancel_wakeup list` rather than trusting a stale id.
- Do not extend the deadline unless a documented source/network condition justifies a longer wait.

## Cheap check (only thing to run if not yet due)
```bash
date -u +%Y-%m-%dT%H:%M:%SZ
sha256sum configs/basis_crash_grid_v1.json   # expect 753d9357e1d535ef4229a901e25ef059a751e4c4d56188247f5f2e0ef1debd16
git status --short --untracked-files=all     # expect empty (or only expected new artifacts)
```

## Objective (activation 3108), priority order
- **(a) Frontier advance v22 — ranks 551–575** — ONLY if now ≥ ≈2026-11-19T11:50:45Z. Procedure:
  - Fresh public CoinPaprika `/v1/coins` retrieval; record retrieval UTC timestamp and `response_sha256`.
  - Record total items and ranked items (v21: 62,713 total / 11,015 ranked; always record the observed value; a ranked-count change is a documented source-coverage event).
  - Dedup the rank 551–575 window against the 514 known ids (reconstruct the v1–v21 observed-id union; skip current-rank duplicates and log symbol collisions separately).
  - Write `research_state/universe_frontier_advance_v22.json`, artifact_id `EBCR-001-UNIVERSE-FRONTIER-ADVANCE-V22`, status `rank_unverified_discovery_only`. Match the v21 artifact key layout: `artifact_id`, `schema_version`, `program_id`, `created_at_utc`, `task_activation`, `purpose`, `prior_artifact`, `source`, `frontier_state`, `discovery_method`, `candidates_discovered_delta`, `duplicates_skipped`, `symbol_collisions`, `cursor`, `notes`.
  - Cursor → `discovered_id_count`, `top_rank_covered` 575, next batch 576–600, `rank_frontier_exhausted` false unless the window is short.
  - No frozen edits. Record **both** hashes externally in the handoff (content sha256 = `json.dumps(d, sort_keys=False, separators=(",", ":"))`; raw-bytes sha256 = sha256 of the written file bytes). Do **not** store self-referential hash fields inside the artifact (matching v18–v21).
- **(b)** A genuinely new, permitted, non-contaminating task resolving a documented open blocker, only if a real new input/source is now available.
- **(c)** NO-OP per the clock gate above.

## Do NOT re-run completed work
Frontier advances v1–v21; candidate→perp mapping v2; contract-lifecycle audit; V4 controlled re-estimation; V3→V4 inference audit; exclusion accounting audit — unless an input changes.
The repository test gate is verified as of activation 3106 (18 passed at HEAD `0ce725ec`); re-run it only when code/test/config changes, not on every activation.

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

## Verified baseline (activation 3107, 2026-11-19T08:25:00Z)
- Clock: 08:23:43Z < 11:50:45Z → v22 NOT actionable (NO-OP).
- State: config `753d9357…`; `git status --short --untracked-files=all` → empty; `git diff --check` exit 0; frozen hashes `e8826caf…` (frontier) / `d5b299bf…` (registry) unchanged; v21 artifact content `c9daa696…` / raw-bytes `81aec400…` re-verified from disk.
- Frontier v21: `research_state/universe_frontier_advance_v21.json`; cursor `discovered_id_count` 514, `top_rank_covered` 550, next batch 551–575, `rank_frontier_exhausted = false`; source `https://api.coinpaprika.com/v1/coins`, `response_sha256` `54a96050bde72bd3fd834df114da120c3e5c8df306b41fca7a1de9780a06f183`, 62,713 total / 11,015 ranked.
- Wakeup: single pending `wku_1f2e7fc82001LZ6q0nFu9L7c0u` at 2026-11-19T11:51:30Z (v22 trigger).
- Tests: **18 passed** at activation 3106 (HEAD `0ce725ec`); grid manifest 324 cells / `config_sha256 55caedf8…`. Not re-run at 3107 (no code/test/config change).

## Known open blockers
Raw ingestion snapshots absent (`data/raw/` gitignored) → re-ingestion not reproducible (derived data only); data revision behavior unresolved; no free historical PIT exchange status series; EBCR-H002/H003/H004 gated as above; frontier discovery open-ended at rank 550 (no tight polling; cooldown until ≈11:50:45Z).

## Reporting
Report only verified findings. Do not commit unless explicitly asked.
