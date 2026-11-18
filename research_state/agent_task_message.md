# Agent task message (EBCR-001) — activation 3098 (written end of activation 3097)

## Read first (required)
- `research_state/agent_handoff.md` — activation 3097 (NO-OP, clock gate not met) and activation 3093 (frontier v19, cursor 469 / rank 500).
- `prompts/continuous_research_operating_contract_v1.md`, `prompts/continuous_research_operating_contract_v1_1_addendum.md`, `docs/research_protocol.md`.
- `configs/basis_crash_grid_v1.json` (frozen) and `docs/sources.md`; load `.agents/skills/point-in-time-universe/SKILL.md` (and `resumable-research-operations`) before frontier work.

## Clock gate — CHECK THIS FIRST
- Last frontier retrieval/creation: **v19 at 2026-11-18T18:56:30Z**. Cooldown convention ≈**3.5 h**.
- Therefore **frontier advance v20 (ranks 501–525) is NOT actionable before ≈2026-11-18T22:26:30Z.**
- Do not run v20 before that time (tight polling prohibited). Do not extend to 02:26:30Z unless a documented source/network condition justifies a longer wait.

## NO-OP discipline
If now < 2026-11-18T22:26:30Z and nothing below has changed, classify the activation **NO-OP** and exit with prior verified state intact. On a NO-OP do NOT:
- re-run the state-change gate, regenerate the grid manifest, re-probe CoinPaprika, or rerun pytest;
- create a `durable_state_upkeep_v*` artifact;
- rewrite the handoff/task message for timestamps only (a substantive NO-OP record at operator request is acceptable, as at activation 3097);
- create a checkpoint commit.

## State-change gate (only if considering a deliverable)
1. `sha256sum configs/basis_crash_grid_v1.json` → expect `753d9357e1d535ef4229a901e25ef059a751e4c4d56188247f5f2e0ef1debd16`.
2. `git status --short --untracked-files=all` → expect empty; `git diff --check` → exit 0.
3. Frozen identities: `universe_frontier.json` `e8826caf…`, registry `d5b299bf…`, integrated `28ec0163…`, evaluation `9487b36d…`.
4. Material-change check. If none, NO-OP.

## Objective (activation 3098), priority order
- **(a) Frontier advance v20 — ranks 501–525** — ONLY if now ≥ ≈2026-11-18T22:26:30Z (or a documented CoinPaprika source/network change). Procedure per prior message: fresh public retrieval, dedup against 469 known ids, write `research_state/universe_frontier_advance_v20.json`, artifact_id `EBCR-001-UNIVERSE-FRONTIER-ADVANCE-V20`, status `rank_unverified_discovery_only`, no frozen edits, record both compact-content and raw-bytes sha256, handle ranked-count shortfall.
- **(b)** A genuinely new, permitted, non-contaminating task resolving a documented open blocker, only if a real new input/source is now available.
- **(c)** **NO-OP** if the cooldown has not elapsed and nothing changed.

## Do NOT re-run completed work
Frontier advances v1–v19; candidate→perp mapping v2; contract-lifecycle audit; V4 controlled re-estimation; V3→V4 inference audit; exclusion accounting audit — unless an input changes.

## Blocked without stated precondition
- EBCR-H002/H003: needs new experiment ID, independent preregistered rationale, NEW anchor/config.
- EBCR-H004: status change requires separate preregistration decision.
- Promotion of candidate→perp mapping / lifecycle status out of `discovery_only_unverified` / PIT-unverified is a separate registration decision.
- PIT historical rank remains CLOSED.

## Preserve invariants (must remain true and unchanged)
Exclusions n=336 (28 `basis_incomplete` + 308 `incomplete_forward_horizon`); integrated 5,010 rows / 5,346 basis observations; anchor co-primary adjusted p-values `crash_incidence_15pct` 0.24830545694889028 and `expected_shortfall_5pct_forward_mae` 0.9485; EBCR-H001 `tested_not_supported`; EBCR-H002/H003/H004 `registered_secondary_not_tested`; `next_hypothesis_sequence` 5. No frozen artifact edits, no preregistration from grid hits, no deletion or rewriting of null/contradictory/failed evidence.

## Required checks (only when a relevant input changed / a deliverable is produced)
```bash
python3 scripts/generate_grid_manifest.py --output /tmp/basis-grid-manifest.json   # expect 324 cells, config_sha256 55caedf84ac723289f70f49bbed4712c8195425feb4a95e737f3e8929479a0e0
# recreate .venv if absent (gitignored), then: .venv/bin/python -m pytest -q tests   # expect 18 passed
git diff --check
# validate any changed JSON/JSONL/YAML and its schema
```

## Verified baseline (activation 3097, 2026-11-18T19:02:07Z)
- Clock: 19:02:07Z < 22:26:30Z → v20 not actionable; ~3.41 h remaining.
- State: config `753d9357…`; git tree clean; `git diff --check` exit 0; frozen hashes `e8826caf…` / `d5b299bf…` / `28ec0163…` / `9487b36d…` unchanged.
- Frontier v19: `research_state/universe_frontier_advance_v19.json`; content sha256 `12f3a08a…` (compact) / raw-bytes `92d99c4e…`; cursor `discovered_id_count` 469, `top_rank_covered` 500, next batch 501–525, `rank_frontier_exhausted = false`.

## Known open blockers
Raw ingestion snapshots absent (`data/raw/` gitignored) → re-ingestion not reproducible (derived data only); data revision behavior unresolved; no free historical PIT exchange status series; EBCR-H002/H003/H004 gated as above; `.venv` gitignored (recreate before pytest); frontier discovery open-ended at rank 500 (no tight polling).

## Reporting
Report only verified findings. Do not commit unless explicitly asked.