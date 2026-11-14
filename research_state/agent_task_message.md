# Agent task message (EBCR-001) — activation 2942 (written at end of activation 2941)

## Read first (required)
- `research_state/agent_handoff.md` (activation 2941 completed — exclusion accounting evidence audit verified and recorded; deliverable committed in `b532bf6d`)
- `research_state/agent_task_message.md` (previous task message)
- `prompts/continuous_research_operating_contract_v1.md` and `prompts/continuous_research_operating_contract_v1_1_addendum.md`
- `docs/research_protocol.md`
- `configs/basis_crash_grid_v1.json` (frozen)
- `docs/sources.md` (free public source policy — verify actual coverage, never assume)

## What changed since the previous activation
- The activation-2941 deliverable `research_state/audit/exclusion_accounting_audit_v1.md` (exclusion accounting, option C extension) was independently re-verified this activation: all arithmetic identities hold (`5,346 = 5,010 + 336`; `5,318 = 5,010 + 308`; integrated exclusions exactly = 28 `basis_incomplete` ⊎ 308 `incomplete_forward_horizon`; row set == label `ok` set; 0 mae / 0 basis join mismatches; per-symbol table and no-forward-fill reproduced). It is recorded as a **presentational** finding only — the single `missing_label` reason conflates two exclusion causes; **no result impact**.
- No new source data, no new dated research event, no code/config/registry/audit change beyond the audit artifact.

## Objective (activation 2942)
Advance the highest-value genuinely unblocked work. Do not manufacture work. Expect at least one real, verifiable deliverable or an explicit, documented blocker. If no state change has occurred since activation 2941 and there is no new admissible source or dated event, classify as NO-OP per the v1.1 addendum and exit with the previous verified state intact — do not refresh timestamps or create empty artifacts.

## Required actions (activation 2942)
1. **State-change gate first** (cheap): verify frozen config literal sha256 `753d9357e1d535ef4229a901e25ef059a751e4c4d56188247f5f2e0ef1debd16` and canonical `55caedf84ac723289f70f49bbed4712c8195425feb4a95e737f3e8929479a0e0`; check `git status --short` clean and no new commits under `scripts/ tests/ configs/ data/ results/ docs/ prompts/ schemas/ research_state/hypothesis_registry.json research_state/universe_frontier.json research_state/audit/`. If nothing changed since activation 2941, NO-OP — skip steps 2–3.
2. **If state changed or an unblocked task exists, pick ONE (in priority order):**
   - **(1) Contract lifecycle / PIT rank audit (recommended first — resolves a long-standing blocker):** For the 11 traded symbols (ADA, BCH, BNB, DOGE, LINK, NEAR, SOL, TRX, XLM, XRP, ZEC), use only free public Binance data (`exchangeInfo` / `data.binance.vision` S3 archive / klines `_markPrice` and index streams) to record, per symbol: listing date, any delisting/migration, contract identity (mark vs index vs spot), and the UTC date from which continuous data exists. Compare against the `first`/`last` row dates already in `research_state/integrated_extended_v1.json` and the `candidate_perp_mapping_v1.json` mappings (`mapping_status = discovery_only_unverified`). Write findings to a new `research_state/audit/contract_lifecycle_audit_v1.md` (new path; do not edit frozen ledgers). If the public source is unreachable, record the blocker with the exact endpoint/error and cooldown — do not retry every activation.
   - **(2) Candidate frontier advance (point-in-time universe):** `research_state/universe_frontier.json` has 25 candidates, `candidates_rank_unverified = 25`, `rank_frontier_exhausted = false`, cursor source `coinpaprika`. Advance the descending market-cap discovery frontier (no fixed top-N cutoff) using a free public rank source (CoinPaprika `/v1/coins` or Coin Metrics community API), persisting each new candidate, cursor, retrieval timestamp and response checksum. Never project current rank backward as historical membership; mark PIT-unverified candidates explicitly. Write a new frontier artifact / cursor update (new ID), not an overwrite of frozen evidence.
   - **(3) EBCR-H002/H003:** still blocked — cannot preregister from inspected grid hits; requires a new experiment ID + independent preregistered rationale + a NEW anchor/config (see `research_state/h002_h003_feasibility_review_v1.json`). Do not proceed without that.
   - **(4) Registry follow-up (H004):** blocked — status change requires a separate preregistration decision; do not change `next_hypothesis_sequence` or statuses.
3. **Preserve invariants:** exclusions n=336; anchor null (`crash_incidence_15pct` adj p 0.24830545694889028; `expected_shortfall_5pct_forward_mae` adj p 0.9485); PIT rank CLOSED; EBCR-H001 `tested_not_supported`; EBCR-H002/H003/H004 `registered_secondary_not_tested`; `next_hypothesis_sequence` 5. No frozen artifact edits; no preregistration derived from grid hits; preserve null/contradictory/failed evidence (including V3's invalid claim as corrected evidence).
4. **Do not repeat already-completed work:** V4 controlled re-estimation (2938), V3→V4 inference audit (2939), and exclusion accounting audit (2941) are done; do not re-run unless an input changes.
5. **Report only verified findings.** Do not commit unless explicitly asked. Update this handoff and write the next task message.

## Verified baseline (activation 2941, 2026-11-14)
- State-change gate: config literal + canonical sha256 match frozen; manifest 324 cells; pytest 18 passed; `git diff --check` clean; working tree clean. Branch `main`, HEAD `014e9c32`.
- Exclusion audit verified and recorded: `research_state/audit/exclusion_accounting_audit_v1.md` (committed `b532bf6d`); 28 `basis_incomplete` + 308 `incomplete_forward_horizon` = 336; no result impact.
- V4 reproducibility (2938): `research_state/robustness_controlled_v4.json`; controlled cluster p 0.4931717622839955 (crash_incidence_15pct) and 0.4571603439994524 (expected_shortfall), both not Holm-significant.
- V3→V4 audit (2939): `research_state/audit/v3_v4_inference_correction_audit_v1.md` (sha256 `aaa473d0…`).
- Registry sha256 `d5b299bf…`; universe frontier sha256 `e8826caf…`.
- Venv: `.venv`, python 3.12.3, numpy 2.5.4, pandas 3.1.1, scipy 1.18.1, statsmodels 0.15.0, pytest 9.2.0 (rebuilt activation 2941; gitignored).
- No new `durable_state_upkeep` artifact (activation 2941 was bookkeeping/verification, not a material research change); no frozen artifact modified; no commit.

## Known blockers still open (do not re-probe every activation)
- Raw ingestion snapshots absent from the repo → re-ingestion not reproducible; only derived data.
- Contract listing/delisting/migration history: unresolved (`candidate_perp_mapping_v1.json` = discovery-only-unverified) — this is the target of option (1).
- Data revision behavior: unresolved.
- EBCR-H002/H003: not testable without new preregistration independent of grid hits and NEW anchor/config.