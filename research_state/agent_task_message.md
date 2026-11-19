# Agent task message (EBCR-001) — activation 3106 (written end of activation 3105)

## Read first (required)
- `research_state/agent_handoff.md` — activation 3105 (NO-OP, clock gate not met) and activation 3100 (frontier advance v20, cursor 490 / rank 525).
- `prompts/continuous_research_operating_contract_v1.md`, `prompts/continuous_research_operating_contract_v1_1_addendum.md`, `docs/research_protocol.md`.
- `configs/basis_crash_grid_v1.json` (frozen) and `docs/sources.md`; load `.agents/skills/point-in-time-universe/SKILL.md` (and `resumable-research-operations`) before frontier work.

## Clock gate — CHECK FIRST, THEN STOP IF NOT MET
- Last frontier retrieval/creation: **v20 at 2026-11-19T00:54:10Z**. Cooldown convention ≈**3.5 h**.
- **Frontier advance v21 (ranks 526–550) is NOT actionable before ≈2026-11-19T04:24:10Z.**
- If `date -u` is **before** 2026-11-19T04:24:10Z and no state change is detected: run the cheap check below, then **exit as NO-OP** — no frontier artifact, no CoinPaprika probe, no handoff rewrite beyond a single short record if the operator explicitly asks, no commit.
- A wakeup is already scheduled for 2026-11-19T04:24:30Z carrying the v21 trigger. Do not add another and do not tight-poll.
- Do not extend the deadline unless a documented source/network condition justifies a longer wait.

## Cheap check (only thing to run if not yet due)
```bash
date -u +%Y-%m-%dT%H:%M:%SZ
sha256sum configs/basis_crash_grid_v1.json   # expect 753d9357e1d535ef4229a901e25ef059a751e4c4d56188247f5f2e0ef1debd16
git status --short --untracked-files=all     # expect empty (or only expected new artifacts)
```

## Objective (activation 3106), priority order
- **(a) Frontier advance v21 — ranks 526–550** — ONLY if now ≥ ≈2026-11-19T04:24:10Z. Procedure:
  - Fresh public CoinPaprika `/v1/coins` retrieval; record retrieval UTC timestamp and `response_sha256`.
  - Record total items and ranked items (v20: 62,712 / 62,712; always record the observed value; a ranked-count change is a documented source-coverage event).
  - Dedup the rank 526–550 window against the 490 known ids (reconstruct the v1–v20 observed-id union; skip current-rank duplicates and log symbol collisions separately).
  - Write `research_state/universe_frontier_advance_v21.json`, artifact_id `EBCR-001-UNIVERSE-FRONTIER-ADVANCE-V21`, status `rank_unverified_discovery_only`.
  - Cursor → `discovered_id_count`, `top_rank_covered` 550, next batch 551–575, `rank_frontier_exhausted` false unless the window is short.
  - No frozen edits. Record **both** hashes externally in the handoff (content sha256 = `json.dumps(d, sort_keys=False, separators=(",", ":"))`; raw-bytes sha256 = sha256 of the written file bytes). Do **not** store self-referential hash fields inside the artifact (matching v18/v19/v20).
- **(b)** A genuinely new, permitted, non-contaminating task resolving a documented open blocker, only if a real new input/source is now available.
- **(c)** NO-OP per the clock gate above.

## Do NOT re-run completed work
Frontier advances v1–v21; candidate→perp mapping v2; contract-lifecycle audit; V4 controlled re-estimation; V3→V4 inference audit; exclusion accounting audit — unless an input changes.
The repository test gate is verified as of activation 3103 (18 passed at HEAD `7f703279`); re-run it only when code/test/config changes, not on every activation.

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

## Verified baseline (activation 3105, 2026-11-19T01:39:32Z)
- Clock: 01:39:32Z < 04:24:10Z → v21 not actionable (~2.75 h remaining at that time).
- State: config `753d9357…`; `git status --short --untracked-files=all` empty; `git diff --check` exit 0; frozen hashes `e8826caf…` (frontier) / `d5b299bf…` (registry) / `28ec0163…` (integrated) / `9487b36d…` (evaluation) unchanged.
- Frontier v20: `research_state/universe_frontier_advance_v20.json`; content sha256 `b0c91e4069e6b5de14ec4cd516f5d5d02129c1fc7f110bffa9bd17fac1f0e0b1`, raw-bytes sha256 `cce2193421b050e6654473cdcbaf7538fec9606c5ed0b038e5fd553819a028b2` (both re-verified from disk at activation 3103); cursor `discovered_id_count` 490, `top_rank_covered` 525, next batch 526–550, `rank_frontier_exhausted = false`.
- Tests: **18 passed** (`.venv`, pytest 0.14s) at HEAD `7f703279`; grid manifest 324 cells / `config_sha256 55caedf8…`.

## Known open blockers
Raw ingestion snapshots absent (`data/raw/` gitignored) → re-ingestion not reproducible (derived data only); data revision behavior unresolved; no free historical PIT exchange status series; EBCR-H002/H003/H004 gated as above; frontier discovery open-ended at rank 525 (no tight polling; single scheduled trigger at ≈04:24:30Z).

## Reporting
Report only verified findings. Do not commit unless explicitly asked.
