# Agent task message (EBCR-001) — activation 2947 (written at end of activation 2946)

## Read first (required)
- `research_state/agent_handoff.md` (activation 2946: CONTRACT LIFECYCLE / PIT AUDIT COMPLETED — new audit `research_state/audit/contract_lifecycle_audit_v1.md` + `contract_lifecycle_evidence_v1.json`)
- `research_state/agent_task_message.md` (this message)
- `prompts/continuous_research_operating_contract_v1.md` and `prompts/continuous_research_operating_contract_v1_1_addendum.md`
- `docs/research_protocol.md`
- `configs/basis_crash_grid_v1.json` (frozen)
- `docs/sources.md` (free public source policy — verify actual coverage, never assume)

## What changed since the previous activation
- **Contract lifecycle / PIT rank audit (option 1) is now DONE for the 11 traded symbols.** Activation 2946 produced `research_state/audit/contract_lifecycle_audit_v1.md` (artifact `EBCR-001-AUDIT-CONTRACT-LIFECYCLE-V1`) and `research_state/audit/contract_lifecycle_evidence_v1.json` (sha256 `4b419069b34e6fe622669b3c690cf1500a609610c8a3435d23523cfc26bfddfd`). Verified: all 11 (ADA, BCH, BNB, DOGE, LINK, NEAR, SOL, TRX, XLM, XRP, ZEC) are live `TRADING` `PERPETUAL` `USDT` contracts with **no delisting/migration**, clean distinct mark/index/funding/kline identity, and **full zero-gap coverage of the test window 2023-01-01→2024-04-30** (only Dec-2020 maintenance gaps, outside window). Mapping still `discovery_only_unverified` on disk (no frozen edit).
- These two new audit files are **untracked** at the time of writing. No frozen artifact/config/registry/ledger was modified.

## Objective (activation 2947)
Advance the highest-value genuinely unblocked work. Do not manufacture work. Expect at least one real, verifiable deliverable or an explicit, documented blocker. If the state-change gate is clean AND no new admissible source or dated event exists AND the remaining unblocked task is not newly actionable, classify as NO-OP per the v1.1 addendum and exit with the previous verified state intact — do not refresh timestamps or create empty artifacts.

## Required actions (activation 2947)
1. **State-change gate first (cheap):** verify frozen config literal sha256 `753d9357e1d535ef4229a901e25ef059a751e4c4d56188247f5f2e0ef1debd16` and canonical `55caedf84ac723289f70f49bbed4712c8195425feb4a95e737f3e8929479a0e0`; check `git status --short` (expect the two new audit files untracked, otherwise clean) and no new commits under the frozen-input paths `scripts/ tests/ configs/ data/ results/ docs/ prompts/ schemas/ research_state/hypothesis_registry.json research_state/universe_frontier.json research_state/integrated_extended_v1.json research_state/evaluation_report_extended_v1.json`. If nothing changed and the next task below is not newly actionable, NO-OP.
2. **Recommended next deliverable — Candidate frontier advance (option 2, point-in-time universe):** `research_state/universe_frontier.json` has 25 candidates, `candidates_rank_unverified = 25`, `rank_frontier_exhausted = false` (cursor source `coinpaprika`). Advance descending market-cap discovery (no fixed top-N cutoff) using a free public rank source, persisting each new candidate, cursor, retrieval timestamp and response checksum in a **new** artifact/ID. **Never project current rank backward as historical membership**; mark PIT-unverified candidates explicitly. Do not edit frozen `universe_frontier.json` in place — use a new artifact/experiment ID and record the delta.
3. **Do NOT re-run completed work:** contract-lifecycle audit (2946), V4 controlled re-estimation (2938), V3→V4 inference audit (2939), exclusion accounting audit (2941) — all done. Re-run only if an input changes.
4. **Blocked (do not proceed without the stated precondition):**
   - **EBCR-H002/H003:** blocked — cannot preregister from inspected grid hits; requires a **new** experiment ID + independent preregistered rationale + a **NEW** anchor/config (see `research_state/h002_h003_feasibility_review_v1.json`).
   - **EBCR-H004:** blocked — status change requires a separate preregistration decision; do not change `next_hypothesis_sequence` or statuses.
   - **Contract-lifecycle mapping promotion:** audit evidence now exists for the 11, but promoting `candidate_perp_mapping_v1.json` out of `discovery_only_unverified` is a **separate registration decision** — do not edit that frozen file as part of routine work.
5. **Preserve invariants:** exclusions n=336 (28 `basis_incomplete` + 308 `incomplete_forward_horizon`); integrated 5,010 rows / 5,346 basis obs; anchor null (`crash_incidence_15pct` adj p 0.24830545694889028; `expected_shortfall_5pct_forward_mae` adj p 0.9485); PIT rank CLOSED; EBCR-H001 `tested_not_supported`; EBCR-H002/H003/H004 `registered_secondary_not_tested`; `next_hypothesis_sequence` 5. No frozen artifact edits; no preregistration derived from grid hits; preserve null/contradictory/failed evidence (including V3's invalid claim as corrected evidence).
6. **Report only verified findings.** Do not commit unless explicitly asked. Update handoff and write the next task message.

## Required checks
```bash
python3 scripts/generate_grid_manifest.py --output /tmp/basis-grid-manifest.json   # expect 324 cells, canonical sha256 55caedf8…
.venv/bin/python -m pytest -q tests                                              # expect 18 passed
git diff --check
# validate any changed JSON/JSONL/YAML and schemas
```

## Verified baseline (activation 2946, 2026-11-14)
- State-change gate: config literal + canonical sha256 match frozen; manifest 324 cells; `git diff --check` clean.
- Tests: `.venv/bin/python -m pytest -q tests` → 18 passed.
- Contract-lifecycle audit complete (2946): all 11 traded symbols `TRADING`/`PERPETUAL`/`USDT`, no delisting/migration, zero-gap window coverage; evidence JSON sha256 `4b419069b34e6fe622669b3c690cf1500a609610c8a3435d23523cfc26bfddfd`.
- Exclusion audit (2941): `research_state/audit/exclusion_accounting_audit_v1.md`; 28 + 308 = 336; no result impact.
- V4 reproducibility (2938): controlled cluster p 0.4931717622839955 (crash_incidence_15pct), 0.4571603439994524 (expected_shortfall), not Holm-significant.
- V3→V4 audit (2939): `research_state/audit/v3_v4_inference_correction_audit_v1.md`.
- Venv: `.venv` present (gitignored), python 3.12.3.

## Known blockers still open (do not re-probe every activation)
- Raw ingestion snapshots absent from repo (`data/raw/` gitignored) → re-ingestion not reproducible; only derived data.
- Data revision behavior unresolved.
- `exchangeInfo` is a live snapshot; no free historical point-in-time status time series (archive continuity is the PIT proxy — sufficient for the 11 traded symbols).
- EBCR-H002/H003 not testable without new preregistration independent of grid hits and NEW anchor/config.
- EBCR-H004 registry status change requires separate preregistration decision.
- Candidate frontier advance (option 2) still open — 25 candidates, `rank_frontier_exhausted = false`.