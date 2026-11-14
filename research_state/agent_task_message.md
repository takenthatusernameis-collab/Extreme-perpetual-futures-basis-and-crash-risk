# Agent task message (EBCR-001) — activation 2949 (written at end of activation 2948)

## Read first (required)
- `research_state/agent_handoff.md` (activation 2948: CANDIDATE FRONTIER ADVANCE COMPLETED / VERIFIED — v1 verified, duplicate defect corrected in `research_state/universe_frontier_advance_v2.json`)
- `research_state/agent_task_message.md` (this message)
- `prompts/continuous_research_operating_contract_v1.md` and `prompts/continuous_research_operating_contract_v1_1_addendum.md`
- `docs/research_protocol.md`
- `configs/basis_crash_grid_v1.json` (frozen)
- `docs/sources.md` (free public source policy — verify actual coverage, never assume)
- `.agents/skills/point-in-time-universe/SKILL.md` (discovery → PIT eligibility; never project current rank backward)

## What changed since the previous activation
- **Candidate frontier advance (option 2) is DONE through the current top 75.** Activation 2947 produced `research_state/universe_frontier_advance_v1.json` (committed `e21caaf8`). Activation 2948 verified it, found a duplicate defect (2 of 25 batch entries were already in the frontier), and corrected/extended it in the new artifact `research_state/universe_frontier_advance_v2.json` (sha256 `52070b3f7a110c078e5d606234c01c6dae4f5b87bbd163e8f797a16f0f640bf8`).
- **Frontier state now:** 75 distinct discovered asset ids; top 75 fully covered; `rank_frontier_exhausted` remains `false`; next scan should start at rank 76 and **de-duplicate by stable asset id** (not by rank window). All candidates are `rank_unverified_discovery_only` — current rank is **not** historical PIT membership.
- **New symbol-collision flag:** `WETH` maps to two CoinPaprika ids (`weth-weth` and `eth-ethereum-token` / Binance-Peg Ethereum Token). Any future mapping must key on stable asset id, not symbol.
- `research_state/universe_frontier_advance_v2.json` is **untracked** at the time of writing. No frozen artifact/config/registry/ledger was modified.

## Objective (activation 2949)
Advance the highest-value genuinely unblocked work. Do not manufacture work. Expect at least one real, verifiable deliverable or an explicit, documented blocker. If the state-change gate is clean AND no new admissible source or dated event exists AND the remaining unblocked task is not newly actionable, classify as NO-OP per the v1.1 addendum and exit with the previous verified state intact — do not refresh timestamps or create empty artifacts.

## Required actions (activation 2949)
1. **State-change gate first (cheap):** verify frozen config literal sha256 `753d9357e1d535ef4229a901e25ef059a751e4c4d56188247f5f2e0ef1debd16` and canonical `55caedf84ac723289f70f49bbed4712c8195425feb4a95e737f3e8929479a0e0`; check `git status --short` (expect a clean tree if the end-of-run checkpoint committed `research_state/universe_frontier_advance_v2.json`, otherwise that file untracked) and no new commits under the frozen-input paths `scripts/ tests/ configs/ data/ results/ docs/ prompts/ schemas/ research_state/hypothesis_registry.json research_state/universe_frontier.json research_state/integrated_extended_v1.json research_state/evaluation_report_extended_v1.json`. If nothing changed and the task below is not newly actionable, NO-OP.
2. **Recommended next deliverable — candidate → perpetual-contract mapping for the top-75 discovery frontier (new artifact/ID):** create `research_state/candidate_perp_mapping_v2.json` (artifact `EBCR-001-CANDIDATE-PERP-MAPPING-V2`). Using free public Binance USDT-M `exchangeInfo` (and the `data.binance.vision` archive only for listing dates if needed), map each of the 75 discovered asset ids to a `binance_um_symbol` where a perpetual exists. Record an explicit status per candidate: `mapped_discovery_only_unverified`, `no_perp_expected` (stablecoin / wrapped / non-tradable), or `blocked_unknown`, with the matched contract's `contractType`/`status`/`quoteAsset`. Never treat the result as PIT-verified; never edit frozen `research_state/candidate_perp_mapping_v1.json`. If mapping produces no new information, fall back to continuing the frontier advance to ranks 76–100 in a new artifact (de-duplicate by id).
3. **Do NOT re-run completed work:** frontier advance v1/v2 (2947/2948), contract-lifecycle audit (2946), V4 controlled re-estimation (2938), V3→V4 inference audit (2939), exclusion accounting audit (2941). Re-run only if an input changes.
4. **Blocked (do not proceed without the stated precondition):**
   - **EBCR-H002/H003:** blocked — cannot preregister from inspected grid hits; requires a **new** experiment ID + independent preregistered rationale + a **NEW** anchor/config (see `research_state/h002_h003_feasibility_review_v1.json`).
   - **EBCR-H004:** blocked — status change requires a separate preregistration decision; do not change `next_hypothesis_sequence` or statuses.
   - **Contract-lifecycle mapping promotion:** audit evidence exists for the 11 traded symbols, but promoting `candidate_perp_mapping_v1.json` out of `discovery_only_unverified` is a **separate registration decision** — do not edit that frozen file as part of routine work.
5. **Preserve invariants:** exclusions n=336 (28 `basis_incomplete` + 308 `incomplete_forward_horizon`); integrated 5,010 rows / 5,346 basis obs; anchor null (`crash_incidence_15pct` adj p 0.24830545694889028; `expected_shortfall_5pct_forward_mae` adj p 0.9485); PIT rank CLOSED; EBCR-H001 `tested_not_supported`; EBCR-H002/H003/H004 `registered_secondary_not_tested`; `next_hypothesis_sequence` 5. No frozen artifact edits; no preregistration derived from grid hits; preserve null/contradictory/failed evidence (including V3's invalid claim as corrected evidence).
6. **Report only verified findings.** Do not commit unless explicitly asked. Update handoff and write the next task message.

## Required checks
```bash
python3 scripts/generate_grid_manifest.py --output /tmp/basis-grid-manifest.json   # expect 324 cells, canonical sha256 55caedf8…
.venv/bin/python -m pytest -q tests                                              # expect 18 passed
git diff --check
# validate any changed JSON/JSONL/YAML and schemas
```
Note: `.venv` was absent at the start of activation 2948 and was recreated (gitignored) with numpy 2.5.4, pandas 3.1.1, scipy 1.18.1, statsmodels 0.15.0, pytest 9.2.0. Reuse it; recreate only if it disappears.

## Verified baseline (activation 2948, 2026-11-14)
- State-change gate: config literal + canonical sha256 match frozen; manifest 324 cells; `git diff --check` clean.
- Tests: `.venv/bin/python -m pytest -q tests` → 18 passed.
- Frontier advance v1 (2947) verified: 25 entries, ranks 26–50; 2 duplicates (BCH, RAIN) → net 23 new; v1 sha256 `847a3f2a…`.
- Frontier advance v2 (2948): 27 new + 48 duplicates skipped; 75 distinct discovered ids; response sha256 `e4eda12a…`; artifact sha256 `52070b3f…`.
- Contract-lifecycle audit (2946): all 11 traded symbols `TRADING`/`PERPETUAL`/`USDT`, no delisting/migration, zero-gap window coverage; evidence JSON sha256 `4b419069…`.
- Exclusion audit (2941): `research_state/audit/exclusion_accounting_audit_v1.md`; 28 + 308 = 336; no result impact.
- V4 reproducibility (2938): controlled cluster p 0.4931717622839955 (crash_incidence_15pct), 0.4571603439994524 (expected_shortfall), not Holm-significant.
- V3→V4 audit (2939): `research_state/audit/v3_v4_inference_correction_audit_v1.md`.

## Known blockers still open (do not re-probe every activation)
- Raw ingestion snapshots absent from repo (`data/raw/` gitignored) → re-ingestion not reproducible; only derived data.
- Data revision behavior unresolved.
- `exchangeInfo` is a live snapshot; no free historical point-in-time status time series (archive continuity is the PIT proxy for the 11 traded symbols).
- EBCR-H002/H003 not testable without a new preregistration independent of grid hits and a NEW anchor/config.
- EBCR-H004 registry status change requires a separate preregistration decision.
- Frontier discovery is open-ended: 75 ids covered, `rank_frontier_exhausted = false`; next scan starts at rank 76.