# Agent task message (EBCR-001) — activation 2943 (written at end of activation 2942)

## Read first (required)
- `research_state/agent_handoff.md` (activation 2942: NO-OP — state-change gate clean, no new admissible source/event; exclusion audit `b532bf6d` and V4/V3-audit baselines verified unchanged)
- `research_state/agent_task_message.md` (this message)
- `prompts/continuous_research_operating_contract_v1.md` and `prompts/continuous_research_operating_contract_v1_1_addendum.md`
- `docs/research_protocol.md`
- `configs/basis_crash_grid_v1.json` (frozen)
- `docs/sources.md` (free public source policy — verify actual coverage, never assume)

## What changed since the previous activation
- None (research-material). Activation 2942 ran the cheap state-change gate only: frozen config literal sha256 `753d9357e1d535ef4229a901e25ef059a751e4c4d56188247f5f2e0ef1debd16` and canonical `55caedf84ac723289f70f49bbed4712c8195425feb4a95e737f3e8929479a0e0` (324 cells) verified; `git status --short` clean; no research-material diffs/commits since `b532bf6d`. No new source data, no dated research event, no code/config/registry/audit/integrated/evaluation change.

## Objective (activation 2943)
Advance the highest-value genuinely unblocked work. Do not manufacture work. Expect at least one real, verifiable deliverable or an explicit, documented blocker. If no state change has occurred since activation 2942 and there is no new admissible source or dated event, classify as NO-OP per the v1.1 addendum and exit with the previous verified state intact — do not refresh timestamps or create empty artifacts.

## Required actions (activation 2943)
1. **State-change gate first (cheap):** verify frozen config literal sha256 `753d9357e1d535ef4229a901e25ef059a751e4c4d56188247f5f2e0ef1debd16` and canonical `55caedf84ac723289f70f49bbed4712c8195425feb4a95e737f3e8929479a0e0`; check `git status --short` clean and no new commits under `scripts/ tests/ configs/ data/ results/ docs/ prompts/ schemas/ research_state/hypothesis_registry.json research_state/universe_frontier.json research_state/audit/ research_state/integrated_extended_v1.json research_state/evaluation_report_extended_v1.json`. If nothing changed since activation 2942, NO-OP — skip steps 2–3.
2. **If state changed or an unblocked task is newly actionable, pick ONE (in priority order):**
   - **(1) Contract lifecycle / PIT rank audit (recommended — long-standing blocker):** For the 11 traded symbols (ADA, BCH, BNB, DOGE, LINK, NEAR, SOL, TRX, XLM, XRP, ZEC), use only free public Binance data (`exchangeInfo` / `data.binance.vision` archive / klines, mark-price, index streams as appropriate) to record per symbol: listing date, any delisting/migration, contract identity (mark vs index vs spot), and the UTC date from which continuous data exists. Compare against `first`/`last` dates in `research_state/integrated_extended_v1.json` and mappings in `research_state/candidate_perp_mapping_v1.json` (`mapping_status = discovery_only_unverified`). Write findings to a **new** `research_state/audit/contract_lifecycle_audit_v1.md` (do not edit frozen ledgers). If a source is unreachable, record the exact endpoint/error and respect a documented cooldown — do not retry every activation.
   - **(2) Candidate frontier advance (point-in-time universe):** `research_state/universe_frontier.json` has 25 candidates, `candidates_rank_unverified = 25`, `rank_frontier_exhausted = false` (cursor source `coinpaprika`). Advance descending market-cap discovery (no fixed top-N cutoff) using a free public rank source, persisting each new candidate, cursor, retrieval timestamp and response checksum in a **new** artifact/ID. Never project current rank backward as historical membership; mark PIT-unverified candidates explicitly.
   - **(3) EBCR-H002/H003:** blocked — cannot preregister from inspected grid hits; requires a **new** experiment ID + independent preregistered rationale + a **NEW** anchor/config (see `research_state/h002_h003_feasibility_review_v1.json`). Do not proceed without that.
   - **(4) Registry follow-up (H004):** blocked — status change requires a separate preregistration decision; do not change `next_hypothesis_sequence` or statuses.
3. **Preserve invariants:** exclusions n=336; anchor null (`crash_incidence_15pct` adj p 0.24830545694889028; `expected_shortfall_5pct_forward_mae` adj p 0.9485); PIT rank CLOSED; EBCR-H001 `tested_not_supported`; EBCR-H002/H003/H004 `registered_secondary_not_tested`; `next_hypothesis_sequence` 5. No frozen artifact edits; no preregistration derived from grid hits; preserve null/contradictory/failed evidence (including V3's invalid claim as corrected evidence).
4. **Do not repeat completed work:** V4 controlled re-estimation (2938), V3→V4 inference audit (2939), and exclusion accounting audit (2941, `b532bf6d`) are done; do not re-run unless an input changes.
5. **Report only verified findings.** Do not commit unless explicitly asked. Update handoff and write the next task message.

## Verified baseline (activation 2942, 2026-11-14)
- State-change gate: config literal + canonical sha256 match frozen; manifest 324 cells; `git diff --check` clean; working tree clean. Branch `main...origin/main`, HEAD `4fc9f699` (at gate time).
- Exclusion audit: `research_state/audit/exclusion_accounting_audit_v1.md` (committed `b532bf6d`); 28 `basis_incomplete` + 308 `incomplete_forward_horizon` = 336; no result impact.
- V4 reproducibility (2938): `research_state/robustness_controlled_v4.json`; controlled cluster p 0.4931717622839955 (crash_incidence_15pct) and 0.4571603439994524 (expected_shortfall), both not Holm-significant.
- V3→V4 audit (2939): `research_state/audit/v3_v4_inference_correction_audit_v1.md`.
- Venv: `.venv` present (gitignored).

## Known blockers still open (do not re-probe every activation)
- Raw ingestion snapshots absent from repo → re-ingestion not reproducible; only derived data.
- Contract listing/delisting/migration history unresolved (`candidate_perp_mapping_v1.json` = discovery-only-unverified) — target of option (1).
- Data revision behavior unresolved.
- EBCR-H002/H003 not testable without new preregistration independent of grid hits and NEW anchor/config.
