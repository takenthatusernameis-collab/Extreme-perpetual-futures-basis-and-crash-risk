# Agent task message (EBCR-001) — activation 3100 (written end of activation 3099)

## Read first (required)
- `research_state/agent_handoff.md` — activation 3099 (NO-OP, clock gate not met, loop-churn note) and activation 3093 (frontier v19, cursor 469 / rank 500).
- `prompts/continuous_research_operating_contract_v1.md`, `prompts/continuous_research_operating_contract_v1_1_addendum.md`, `docs/research_protocol.md`.
- `configs/basis_crash_grid_v1.json` (frozen) and `docs/sources.md`; load `.agents/skills/point-in-time-universe/SKILL.md` (and `resumable-research-operations`) before frontier work.

## Clock gate — CHECK THIS FIRST, THEN STOP IF NOT MET
- Last frontier retrieval/creation: **v19 at 2026-11-18T18:56:30Z**. Cooldown convention ≈**3.5 h**.
- **Frontier advance v20 (ranks 501–525) is NOT actionable before ≈2026-11-18T22:26:30Z.**
- A self-scheduled wakeup for ≈2026-11-18T22:26:40Z already carries the v20 trigger (set at activation 3099). Verify with `cancel_wakeup list` / `cron_list` before scheduling anything; do not stack duplicate timers.
- If `date -u` is **before** 2026-11-18T22:26:30Z and no state change is detected: run the single cheap check below, then **exit as NO-OP without rewriting this file or the handoff**. Do not create a new NO-OP handoff record, do not re-schedule, do not commit — activations 3094–3099 already produced six such entries inside a 6-minute window and that churn is now the main defect to avoid. Anti-churn rule for the remainder of this cooldown: **one `date -u` check and a silent exit, or nothing at all.**
- Do not extend the deadline to 2026-11-19T02:26:30Z unless a documented source/network condition justifies a longer wait (the +7.5 h figure in the activation-3093 message was an arithmetic slip, corrected at activation 3094).

## Cheap check (only thing to run if not yet due)
```bash
date -u +%Y-%m-%dT%H:%M:%SZ
sha256sum configs/basis_crash_grid_v1.json   # expect 753d9357e1d535ef4229a901e25ef059a751e4c4d56188247f5f2e0ef1debd16
git status --short --untracked-files=all     # expect empty
```

## Objective (activation 3100), priority order
- **(a) Frontier advance v20 — ranks 501–525** — ONLY if now ≥ ≈2026-11-18T22:26:30Z. Procedure: fresh public CoinPaprika `/v1/coins` retrieval; record retrieval UTC timestamp and `response_sha256`; record total items and ranked items (v19 had 62,712 / 62,712; ranked-count coverage has already flipped twice, so always record the observed value); dedup the rank 501–525 window against the 469 known ids; write `research_state/universe_frontier_advance_v20.json`, artifact_id `EBCR-001-UNIVERSE-FRONTIER-ADVANCE-V20`, status `rank_unverified_discovery_only`; cursor → `discovered_id_count`, `top_rank_covered` 525, next batch 526–550, `rank_frontier_exhausted` false unless the window is short; no frozen edits; record **both** the compact-content sha256 (`json.dumps(d, sort_keys=False, separators=(",", ":"))`) and the raw-file-bytes sha256 — v18 recorded raw-bytes, v19 recorded compact, and mixing them caused a false tamper scare at activation 3094.
- **(b)** A genuinely new, permitted, non-contaminating task resolving a documented open blocker, only if a real new input/source is now available.
- **(c)** NO-OP as described above.

## Do NOT re-run completed work
Frontier advances v1–v19; candidate→perp mapping v2; contract-lifecycle audit; V4 controlled re-estimation; V3→V4 inference audit; exclusion accounting audit — unless an input changes.

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
# recreate .venv if absent (gitignored), then: .venv/bin/python -m pytest -q tests   # expect 18 passed
git diff --check
# validate any changed JSON/JSONL/YAML and its schema
```

## Verified baseline (activation 3099, 2026-11-18T19:05:35Z)
- Clock: 19:05:35Z < 22:26:30Z → v20 not actionable; ~3.35 h remaining.
- State: config `753d9357…`; git tree clean; `git diff --check` exit 0; frozen hashes `e8826caf…` (frontier) / `d5b299bf…` (registry) / `28ec0163…` (integrated) / `9487b36d…` (evaluation) unchanged.
- Frontier v19: `research_state/universe_frontier_advance_v19.json`; raw-bytes `92d99c4e…`, compact content `12f3a08a…`; cursor `discovered_id_count` 469, `top_rank_covered` 500, next batch 501–525, `rank_frontier_exhausted = false`.

## Known open blockers
Raw ingestion snapshots absent (`data/raw/` gitignored) → re-ingestion not reproducible (derived data only); data revision behavior unresolved; no free historical PIT exchange status series; EBCR-H002/H003/H004 gated as above; `.venv` gitignored (recreate before pytest); frontier discovery open-ended at rank 500 (no tight polling; single scheduled trigger only).

## Reporting
Report only verified findings. Do not commit unless explicitly asked.
