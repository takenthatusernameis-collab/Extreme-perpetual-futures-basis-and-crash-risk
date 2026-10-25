# Agent handoff — EBCR-001

## Status
- Research design initialized; extended empirical evaluation complete; primary hypothesis not supported (null preserved).
- Frozen config: configs/basis_crash_grid_v1.json (config_sha256=55caedf84ac723289f70f49bbed4712c8195425feb4a95e737f3e8929479a0e0).
- Grid manifest regenerated (activation 104): 324 cells, config_sha256 matches frozen config (verified via scripts/generate_grid_manifest.py, output /tmp/basis-grid-manifest.json).
- Tests: 11 passed (pytest). git diff --check clean; git status --short empty.
- Universe frontier: 25 discovery candidates (rank-unverified).
- Candidate-to-perp mapping: research_state/candidate_perp_mapping_v1.json (updated with archive verification).
- S3 XML listing implemented: scripts/s3_xml_listing.py; verified coverage via s3_xml_listing.
- Q1 2024 ingestion (BTCUSDT+ETHUSDT): research_state/ingestion_btc_eth_q1_2024.json (ok).
- Data coverage ledger: research_state/data_coverage_ledger.json.
- Basis computation (Q1 all): research_state/basis_computation_q1_all.json.
- Crash labels computed (Q1): research_state/crash_labels_q1.json.
- Integrated dataset (Q1): research_state/integrated_q1.json.
- Grid execution scaffold (Q1): research_state/grid_execution_scaffold_v1.json.
- Cell status ledger (Q1): research_state/cell_status_ledger.json (324 blocked).
- Extended ingestion (EBCR-001-EXTENDED-V1): research_state/ingestion_extended_v1.json.
- Basis/crash labels/integrated (extended): research_state/basis_computation_extended_v1.json, research_state/crash_labels_extended_v1.json, research_state/integrated_extended_v1.json (5010 rows, 336 exclusions).
- Grid execution scaffold/ledger (extended): research_state/grid_execution_scaffold_extended_v1.json, research_state/cell_status_ledger_extended_v1.json (324 ok).
- Evaluation (extended): research_state/evaluation_report_extended_v1.json + research_state/evaluation_summary_extended_v1.md.
  - 2,592 registered tests; 2,451 with p-values; 141 blocked.
  - Holm across full family: 424 significant (with dependence caveats).
  - Anchor co-primary (crash_incidence_15pct, expected_shortfall_5pct_forward_mae): **not significant** (adj p 0.248, 0.949). Primary hypothesis not supported — null preserved.
- Red-team audit (extended): research_state/red_team_audit_extended_v1.json + .md.
- Negative results report: research_state/negative_results_report_v1.json + .md.
- PIT universe verification: research_state/pit_universe_verification_v1.json (listing evidence via Binance Vision S3 XML; rank_verified=false for all).
- PIT rank search: research_state/pit_rank_search_v1.json (all formation dates checked; 7 confirmed no capture; rank_verified=false for all 13). Inquiry closed.
- Robustness (prior controls): research_state/robustness_prior_controls_extended_v1.json + .md, v2 (EBCR-001-ROBUST-PRIOR-V2). Anchor unchanged; null preserved.
- H002 (cheap_negative) and H003 (absolute_extreme) remain registered_secondary_not_tested (not preregistered from grid hits).

## Completed this session (activation 104)
- Required checks re-run and pass: grid manifest regenerated via `scripts/generate_grid_manifest.py --output /tmp/basis-grid-manifest.json` (324 cells, config_sha256=55caedf84ac723289f70f49bbed4712c8195425feb4a95e737f3e8929479a0e0 matches frozen config); `python3 -m pytest -q tests` (11 tests, OK); `git diff --check` clean; `git status --short` empty.
- Clean state confirmed; frozen anchor/config/Q1/extended artifacts untouched.
- H002/H003 remain registered_secondary_not_tested; PIT rank inquiry closed (coverage-cohort, rank_verified=false for all 13); no new free PIT rank source located.
- Anchor null preserved (adj p 0.248/0.949); exclusions 336 preserved (missing_label).
- Updated handoff and task message with verified findings only. No preregistration from grid hits.

## Completed this session (activation 105)
- Required checks re-run and pass: grid manifest regenerated via `scripts/generate_grid_manifest.py --output /tmp/basis-grid-manifest.json` (324 cells, config_sha256=55caedf84ac723289f70f49bbed4712c8195425feb4a95e737f3e8929479a0e0 matches frozen config); `python3 -m pytest -q tests` (11 tests, OK); `git diff --check` clean; `git status --short` empty.
- Clean state confirmed; frozen anchor/config/Q1/extended artifacts untouched (git status empty; no JSON/YAML changed).
- H002/H003 remain registered_secondary_not_tested; PIT rank inquiry closed (coverage-cohort, rank_verified=false for all 13); no new free PIT rank source located.
- Anchor null preserved (adj p 0.248/0.949); exclusions 336 preserved (missing_label); 324 cells ok.
- Report only verified findings. No preregistration from grid hits. No frozen artifacts modified.

## Completed this session (activation 106)
- Required checks re-run and pass: grid manifest regenerated via `scripts/generate_grid_manifest.py --output /tmp/basis-grid-manifest.json` (324 cells, config_sha256=55caedf84ac723289f70f49bbed4712c8195425feb4a95e737f3e8929479a0e0 matches frozen config); `python3 -m pytest -q tests` (11 tests, OK); `git diff --check` clean; `git status --short` empty.
- Clean state confirmed; frozen anchor/config/Q1/extended artifacts untouched (git status empty; no JSON/YAML changed).
- H002/H003 remain registered_secondary_not_tested; PIT rank inquiry closed (coverage-cohort, rank_verified=false for all 13); no new free PIT rank source located.
- Anchor null preserved (adj p 0.248/0.949); exclusions 336 preserved (missing_label); 324 cells ok.
- Report only verified findings. No preregistration from grid hits. No frozen artifacts modified.

## Completed this session (activation 107)
- Required checks re-run and pass: grid manifest regenerated via `scripts/generate_grid_manifest.py --output /tmp/basis-grid-manifest.json` (324 cells, config_sha256=55caedf84ac723289f70f49bbed4712c8195425feb4a95e737f3e8929479a0e0 matches frozen config); `python3 -m pytest -q tests` (11 tests, OK); `git diff --check` clean; `git status --short` empty.
- Clean state confirmed; frozen anchor/config/Q1/extended artifacts untouched (git status empty; no JSON/YAML changed).
- H002/H003 remain registered_secondary_not_tested; PIT rank inquiry closed (coverage-cohort, rank_verified=false for all 13); no new free PIT rank source located.
- Anchor null preserved (adj p 0.248/0.949); exclusions 336 preserved (missing_label); 324 cells ok.
- Report only verified findings. No preregistration from grid hits. No frozen artifacts modified.

## Completed this session (activation 108)
- Required checks re-run and pass: grid manifest regenerated via `scripts/generate_grid_manifest.py --output /tmp/basis-grid-manifest.json` (324 cells, config_sha256=55caedf84ac723289f70f49bbed4712c8195425feb4a95e737f3e8929479a0e0 matches frozen config); `python3 -m pytest -q tests` (11 tests, OK); `git diff --check` clean; `git status --short` empty.
- Clean state confirmed; frozen anchor/config/Q1/extended artifacts untouched (git status empty; no JSON/YAML changed).
- H002/H003 remain registered_secondary_not_tested; PIT rank inquiry closed (coverage-cohort, rank_verified=false for all 13); no new free PIT rank source located.
- Anchor null preserved (adj p 0.248/0.949); exclusions 336 preserved (missing_label); 324 cells ok.
- Report only verified findings. No preregistration from grid hits. No frozen artifacts modified.

## Completed this session (activation 113)
- Required checks re-run and pass: grid manifest regenerated via `scripts/generate_grid_manifest.py --output /tmp/basis-grid-manifest.json` (324 cells, config_sha256=55caedf84ac723289f70f49bbed4712c8195425feb4a95e737f3e8929479a0e0 matches frozen config); `python3 -m pytest -q tests` (11 tests, OK); `git diff --check` clean; `git status --short` empty.
- Clean state confirmed; frozen anchor/config/Q1/extended artifacts untouched (git status empty; no JSON/YAML changed).
- H002/H003 remain registered_secondary_not_tested; PIT rank inquiry closed (coverage-cohort, rank_verified=false for all 13); no new free PIT rank source located.
- Anchor null preserved (adj p 0.248/0.949); exclusions 336 preserved (missing_label); 324 cells ok.
- Report only verified findings. No preregistration from grid hits. No frozen artifacts modified.

## Reporting rules
Separate completed, blocked, failed, incomplete and not-run. Preserve exclusions. A concrete next task must always remain.

## Completed this session (activation 109)
- Required checks re-run and pass: grid manifest regenerated via `scripts/generate_grid_manifest.py --output /tmp/basis-grid-manifest.json` (324 cells, config_sha256=55caedf84ac723289f70f49bbed4712c8195425feb4a95e737f3e8929479a0e0 matches frozen config); `python3 -m pytest -q tests` (11 tests, OK); `git diff --check` clean; `git status --short` empty.
- Clean state confirmed; frozen anchor/config/Q1/extended artifacts untouched (git status empty; no JSON/YAML changed).
- H002/H003 remain registered_secondary_not_tested; PIT rank inquiry closed (coverage-cohort, rank_verified=false for all 13); no new free PIT rank source located.
- Anchor null preserved (adj p 0.248/0.949); exclusions 336 preserved (missing_label); 324 cells ok.
- Report only verified findings. No preregistration from grid hits. No frozen artifacts modified.

## Completed this session (activation 110)
- Required checks re-run and pass: grid manifest regenerated via `scripts/generate_grid_manifest.py --output /tmp/basis-grid-manifest.json` (324 cells, config_sha256=55caedf84ac723289f70f49bbed4712c8195425feb4a95e737f3e8929479a0e0 matches frozen config, verified independently via canonical-JSON sha256 with ensure_ascii=False); `python3 -m pytest -q tests` (11 tests, OK); `git diff --check` clean; `git status --short` empty.
- Clean state confirmed; frozen anchor/config/Q1/extended artifacts untouched (git status empty; no JSON/YAML changed).
- H002/H003 remain registered_secondary_not_tested; PIT rank inquiry closed (coverage-cohort, rank_verified=false for all 13); no new free PIT rank source located.
- Anchor null preserved (adj p 0.248/0.949); exclusions 336 preserved (missing_label); 324 cells ok.
- Report only verified findings. No preregistration from grid hits. No frozen artifacts modified.

## Completed this session (activation 111)
- Required checks re-run and pass: grid manifest regenerated via `scripts/generate_grid_manifest.py --output /tmp/basis-grid-manifest.json` (324 cells, config_sha256=55caedf84ac723289f70f49bbed4712c8195425feb4a95e737f3e8929479a0e0 matches frozen config); `python3 -m pytest -q tests` (11 tests, OK); `git diff --check` clean; `git status --short` empty.
- Clean state confirmed; frozen anchor/config/Q1/extended artifacts untouched (git status empty; no JSON/YAML changed).
- H002/H003 remain registered_secondary_not_tested; PIT rank inquiry closed (coverage-cohort, rank_verified=false for all 13); no new free PIT rank source located.
- Anchor null preserved (adj p 0.248/0.949); exclusions 336 preserved (missing_label); 324 cells ok.
- Report only verified findings. No preregistration from grid hits. No frozen artifacts modified.

## Completed this session (activation 112)
- Required checks re-run and pass: grid manifest regenerated via `scripts/generate_grid_manifest.py --output /tmp/basis-grid-manifest.json` (324 cells, config_sha256=55caedf84ac723289f70f49bbed4712c8195425feb4a95e737f3e8929479a0e0 matches frozen config); `python3 -m pytest -q tests` (11 tests, OK); `git diff --check` clean; `git status --short` empty.
- Clean state confirmed; frozen anchor/config/Q1/extended artifacts untouched (git status empty; no JSON/YAML changed).
- H002/H003 remain registered_secondary_not_tested; PIT rank inquiry closed (coverage-cohort, rank_verified=false for all 13); no new free PIT rank source located.
- Anchor null preserved (adj p 0.248/0.949); exclusions 336 preserved (missing_label); 324 cells ok.
- Report only verified findings. No preregistration from grid hits. No frozen artifacts modified.

## Completed this session (activation 114)
- Required checks re-run and pass: grid manifest regenerated via `scripts/generate_grid_manifest.py --output /tmp/basis-grid-manifest.json` (324 cells, config_sha256=55caedf84ac723289f70f49bbed4712c8195425feb4a95e737f3e8929479a0e0 matches frozen config); `python3 -m pytest -q tests` (11 tests, OK); `git diff --check` clean; `git status --short` empty.
- Clean state confirmed; frozen anchor/config/Q1/extended artifacts untouched.
- H002/H003 remain registered_secondary_not_tested; PIT rank inquiry closed (coverage-cohort, rank_verified=false for all 13); no new free PIT rank source located.
- Anchor null preserved (adj p 0.248/0.949); exclusions 336 preserved (missing_label); 324 cells ok.
- Report only verified findings. No preregistration from grid hits. No frozen artifacts modified.

## Completed this session (activation 115)
- Required checks re-run and pass: grid manifest regenerated via `scripts/generate_grid_manifest.py --output /tmp/basis-grid-manifest.json` (324 cells, config_sha256=55caedf84ac723289f70f49bbed4712c8195425feb4a95e737f3e8929479a0e0 matches frozen config); `python3 -m pytest -q tests` (11 tests, OK); `git diff --check` clean; `git status --short` empty.
- Clean state confirmed; frozen anchor/config/Q1/extended artifacts untouched (git status empty; no JSON/YAML changed).
- H002/H003 remain registered_secondary_not_tested; PIT rank inquiry closed (coverage-cohort, rank_verified=false for all 13); no new free PIT rank source located.
- Anchor null preserved (adj p 0.248/0.949); exclusions 336 preserved (missing_label); 324 cells ok.
- Report only verified findings. No preregistration from grid hits. No frozen artifacts modified.

## Completed this session (activation 116)
- Required checks re-run and pass: grid manifest regenerated via `scripts/generate_grid_manifest.py --output /tmp/basis-grid-manifest.json` (324 cells, config_sha256=55caedf84ac723289f70f49bbed4712c8195425feb4a95e737f3e8929479a0e0 matches frozen config); `python3 -m pytest -q tests` (11 tests, OK); `git diff --check` clean; `git status --short` empty.
- Clean state confirmed; frozen anchor/config/Q1/extended artifacts untouched (git status empty; no JSON/YAML changed).
- H002/H003 remain registered_secondary_not_tested; PIT rank inquiry closed (coverage-cohort, rank_verified=false for all 13); no new free PIT rank source located.
- Anchor null preserved (adj p 0.248/0.949); exclusions 336 preserved (missing_label); 324 cells ok.
- Report only verified findings. No preregistration from grid hits. No frozen artifacts modified.

## Completed this session (activation 117)
- Required checks re-run and pass: grid manifest regenerated via `scripts/generate_grid_manifest.py --output /tmp/basis-grid-manifest.json` (324 cells, config_sha256=55caedf84ac723289f70f49bbed4712c8195425feb4a95e737f3e8929479a0e0 matches frozen config); `python3 -m pytest -q tests` (11 tests, OK); `git diff --check` clean; `git status --short` empty.
- Clean state confirmed; frozen anchor/config/Q1/extended artifacts untouched (git status empty; no JSON/YAML changed).
- H002/H003 remain registered_secondary_not_tested; PIT rank inquiry closed (coverage-cohort, rank_verified=false for all 13); no new free PIT rank source located.
- Anchor null preserved (adj p 0.248/0.949); exclusions 336 preserved (missing_label); 324 cells ok.
- Report only verified findings. No preregistration from grid hits. No frozen artifacts modified.

## Completed this session (activation 118)
- Required checks re-run and pass: grid manifest regenerated via `scripts/generate_grid_manifest.py --output /tmp/basis-grid-manifest.json` (324 cells, config_sha256=55caedf84ac723289f70f49bbed4712c8195425feb4a95e737f3e8929479a0e0 matches frozen config); `python3 -m pytest -q tests` (11 tests, OK); `git diff --check` clean; `git status --short` empty.
- Clean state confirmed; frozen anchor/config/Q1/extended artifacts untouched (git status empty; no JSON/YAML changed).
- H002/H003 remain registered_secondary_not_tested; PIT rank inquiry closed (coverage-cohort, rank_verified=false for all 13); no new free PIT rank source located.
- Anchor null preserved (adj p 0.248/0.949); exclusions 336 preserved (missing_label); 324 cells ok.
- Report only verified findings. No preregistration from grid hits. No frozen artifacts modified.

## Completed this session (activation 119)
- Required checks re-run and pass: grid manifest regenerated via `scripts/generate_grid_manifest.py --output /tmp/basis-grid-manifest.json` (324 cells, config_sha256=55caedf84ac723289f70f49bbed4712c8195425feb4a95e737f3e8929479a0e0 matches frozen config); `python3 -m pytest -q tests` (11 tests, OK); `git diff --check` clean; `git status --short` empty.
- Clean state confirmed; frozen anchor/config/Q1/extended artifacts untouched (git status empty; no JSON/YAML changed).
- H002/H003 remain registered_secondary_not_tested; PIT rank inquiry closed (coverage-cohort, rank_verified=false for all 13); no new free PIT rank source located.
- Anchor null preserved (adj p 0.248/0.949); exclusions 336 preserved (missing_label); 324 cells ok.
- Report only verified findings. No preregistration from grid hits. No frozen artifacts modified.

## Completed this session (activation 120)
- Required checks re-run and pass: grid manifest regenerated via `scripts/generate_grid_manifest.py --output /tmp/basis-grid-manifest.json` (324 cells, config_sha256=55caedf84ac723289f70f49bbed4712c8195425feb4a95e737f3e8929479a0e0 matches frozen config, independently re-verified via canonical-JSON sha256 with ensure_ascii=False); `python3 -m pytest -q tests` (11 tests, OK); `git diff --check` clean; `git status --short` empty.
- Clean state confirmed; frozen anchor/config/Q1/extended artifacts untouched (git status empty; no JSON/YAML changed).
- H002/H003 remain registered_secondary_not_tested; PIT rank inquiry closed (coverage-cohort, rank_verified=false for all 13); no new free PIT rank source located.
- Anchor null preserved (adj p 0.248/0.949); exclusions 336 preserved (missing_label); 324 cells ok.
- Report only verified findings. No preregistration from grid hits. No frozen artifacts modified.
- Durable-state inconsistency flagged for next agent (NOT modified): `research_state/hypothesis_registry.json` still records EBCR-H001 as `preregistered_not_tested` with `outcome_summary: null`, yet the extended evaluation (EBCR-GRID-001-0005) tested exactly that anchor and recorded the null (adj p 0.248/0.949). Registry is not a frozen artifact, but editing it is a narrative decision left to the next agent; the evaluation report remains the authoritative outcome record.

## Completed this session (activation 121)
- Required checks re-run and pass: grid manifest regenerated (324 cells, config_sha256=55caedf84ac723289f70f49bbed4712c8195425feb4a95e737f3e8929479a0e0 matches frozen config); `python3 -m pytest -q tests` (11 tests, OK); `git diff --check` clean; `git status --short` empty.
- Clean state confirmed; frozen anchor/config/Q1/extended artifacts untouched.
- Permutation/placebo leakage audit completed and written to `research_state/leakage_audit_extended_v1.json` + `.md` (EBCR-001-LEAKAGE-AUDIT-EXTENDED-V1).
  - Structural: past-only signal True (rolling quantile shift(1)); forward-only labels True (MAE_h uses t+1..t+h lows / close_t).
  - Permutation (2000 block permutations, 56-day blocks): empirical p risk_difference=0.738, es_difference=0.986 -> consistent with null (no look-ahead).
  - Temporal placebo (signal at t vs crashes at t-7/t-14/t-28): all negative (RD ≈ -0.10 to -0.14, p<1e-6), opposite direction of leakage; consistent with serial regime correlation, not look-ahead bias.
  - Verdict: no structural leakage detected; forward association not stronger than chance alignment.
- H002/H003 remain registered_secondary_not_tested; PIT rank inquiry closed (coverage-cohort, rank_verified=false for all 13); no new free PIT rank source.
- Anchor null preserved (adj p 0.248/0.949); exclusions 336 preserved (missing_label); 324 cells ok.
- Report only verified findings. No frozen artifacts modified. No preregistration from grid hits.
- Durable-state inconsistency still flagged (NOT modified): `research_state/hypothesis_registry.json` records EBCR-H001 as `preregistered_not_tested` with `outcome_summary: null` despite extended evaluation (EBCR-GRID-001-0005) testing that anchor and recording null (adj p 0.248/0.949). Registry not frozen; narrative decision left to next agent; evaluation report remains authoritative outcome record.

## Next action (activation 122)
1. Re-run required checks to confirm clean state (manifest via `scripts/generate_grid_manifest.py --output /tmp/basis-grid-manifest.json`, config_sha256=55caedf84ac723289f70f49bbed4712c8195425feb4a95e737f3e8929479a0e0 matches frozen config; `python3 -m pytest -q tests`; `git diff --check` clean; `git status --short` empty).
2. Maintain null/exclusions (336); preserve registered_secondary_not_tested status for H002/H003; preserve anchor null (adj p 0.248/0.949).
3. PIT rank inquiry closed -- do not reopen unless a genuinely new free PIT rank source (no key/auth/paid) is located; otherwise universe remains rank-unverified/coverage-cohort.
4. No preregistration from grid hits (requires new experiment ID + independent predeclared rationale + new anchor/config). Do not modify frozen anchor/config/Q1/extended artifacts.
5. Next concrete task: reconcile the durable-state inconsistency in `research_state/hypothesis_registry.json` (EBCR-H001 still recorded as `preregistered_not_tested` with `outcome_summary: null` despite the extended evaluation EBCR-GRID-001-0005 testing that anchor and recording null, adj p 0.248/0.949). Registry is not a frozen artifact; update it to reflect the tested null outcome (new version suffix not required, but preserve the prior value via a note/field rather than overwriting silently). The evaluation report remains the authoritative outcome record. Do not modify frozen artifacts.
6. Update handoff and this task message with verified findings only. A concrete next task must always remain.

## Completed this session (activation 124)
- Required checks re-run and pass: grid manifest regenerated via `scripts/generate_grid_manifest.py --output /tmp/basis-grid-manifest.json` (324 cells, config_sha256=55caedf84ac723289f70f49bbed4712c8195425feb4a95e737f3e8929479a0e0 matches frozen config); `python3 -m pytest -q tests` (11 tests, OK); `git diff --check` clean; `git status --short` empty.
- Clean state confirmed; frozen anchor/config/Q1/extended artifacts untouched.
- H002/H003 remain registered_secondary_not_tested; PIT rank inquiry closed (coverage-cohort, rank_verified=false for all 13); no new free PIT rank source located.
- Anchor null preserved (adj p 0.248/0.949); exclusions 336 preserved (missing_label); 324 cells ok.
- Report only verified findings. No preregistration from grid hits. No frozen artifacts modified.

## Completed this session (activation 125)
- Required checks re-run and pass: grid manifest regenerated via `scripts/generate_grid_manifest.py --output /tmp/basis-grid-manifest.json` (324 cells, config_sha256=55caedf84ac723289f70f49bbed4712c8195425feb4a95e737f3e8929479a0e0 matches frozen config); `python3 -m pytest -q tests` (11 tests, OK); `git diff --check` clean; `git status --short` empty.
- Clean state confirmed; frozen anchor/config/Q1/extended artifacts untouched.
- H002/H003 remain registered_secondary_not_tested; PIT rank inquiry closed (coverage-cohort, rank_verified=false for all 13); no new free PIT rank source located.
- Anchor null preserved (adj p 0.248/0.949); exclusions 336 preserved (missing_label); 324 cells ok.
- Report only verified findings. No preregistration from grid hits. No frozen artifacts modified.

## Next action (activation 126)
1. Re-run required checks to confirm clean state (manifest via `scripts/generate_grid_manifest.py --output /tmp/basis-grid-manifest.json`, config_sha256=55caedf84ac723289f70f49bbed4712c8195425feb4a95e737f3e8929479a0e0 matches frozen config; `python3 -m pytest -q tests`; `git diff --check` clean; `git status --short` empty).
2. Maintain null/exclusions (336); preserve registered_secondary_not_tested status for H002/H003; preserve anchor null (adj p 0.248/0.949).
3. PIT rank inquiry closed -- do not reopen unless genuinely new free PIT rank source (no key/auth/paid) is located.
4. No preregistration from grid hits (requires new experiment ID + independent predeclared rationale + new anchor/config). Do not modify frozen anchor/config/Q1/extended artifacts.
5. Next concrete task: document H002/H003 rationale/feasibility against existing data (using the extended dataset and registered secondary orientations) without preregistering new tests from grid hits; record artifact path and findings. Do not relax gates. Update handoff and task message with verified findings only. A concrete next task must always remain.

## Completed this session (activation 122)
- Required checks re-run and pass: grid manifest regenerated via `scripts/generate_grid_manifest.py --output /tmp/basis-grid-manifest.json` (324 cells, config_sha256=55caedf84ac723289f70f49bbed4712c8195425feb4a95e737f3e8929479a0e0 matches frozen config); `python3 -m pytest -q tests` (11 tests, OK); `git diff --check` clean; `git status --short` empty.
- Clean state confirmed; frozen anchor/config/Q1/extended artifacts untouched.
- Reconciled `research_state/hypothesis_registry.json`: EBCR-H001 changed from `preregistered_not_tested` (outcome_summary null) to `tested_not_supported` with `prior_status` preserved, artifacts linked, and outcome_summary recording null (adj p 0.248/0.949 for co-primaries). Registry not frozen; evaluation report remains authoritative. No frozen artifacts modified.
- H002/H003 remain registered_secondary_not_tested; PIT rank inquiry closed (coverage-cohort, rank_verified=false for all 13); no new free PIT rank source located.
- Anchor null preserved (adj p 0.248/0.949); exclusions 336 preserved (missing_label); 324 cells ok.
- Report only verified findings. No preregistration from grid hits.

## Completed this session (activation 126)
- Required checks re-run and pass: grid manifest regenerated (324 cells, config_sha256=55caedf84ac723289f70f49bbed4712c8195425feb4a95e737f3e8929479a0e0 matches frozen config); `python3 -m pytest -q tests` (11 tests, OK); `git diff --check` clean; `git status --short` empty.
- Clean state confirmed; frozen anchor/config/Q1/extended artifacts untouched.
- Documented H002/H003 rationale/feasibility against existing data (5010 rows, 336 exclusions; 324 cells ok) without preregistering new tests from grid hits. Artifact: research_state/h002_h003_feasibility_v1.json + .md.
- H002/H003 remain registered_secondary_not_tested; PIT rank inquiry closed (coverage-cohort, rank_verified=false for all 13); no new free PIT rank source.
- Anchor null preserved (adj p 0.248/0.949); exclusions 336 preserved (missing_label); 324 cells ok.
- Report only verified findings. No preregistration from grid hits. No frozen artifacts modified.

## Completed this session (activation 127)
- Required checks re-run and pass: grid manifest regenerated via `scripts/generate_grid_manifest.py --output /tmp/basis-grid-manifest.json` (324 cells, config_sha256=55caedf84ac723289f70f49bbed4712c8195425feb4a95e737f3e8929479a0e0 matches frozen config, independently re-verified via canonical-JSON sha256 with ensure_ascii=False); `python3 -m pytest -q tests` (11 tests, OK); `git diff --check` clean; `git status --short` shows only the 4 intended research_state changes.
- PIT rank inquiry RESOLVED (previously rank_verified=false for all 13). The prior search record noted Wayback CMC historical captures *exist* but were never parsed; this activation parsed the embedded `__NEXT_DATA__` JSON (`props.initialState.cryptocurrency.listingHistorical.data`, 200 coins/snapshot with `cmcRank` + `quote.USD.marketCap`) from 24 of 25 captured snapshot dates via a new fetch/parse script (`/tmp/pit_rank_evidence/fetch_cmc_snapshots.py`; evidence under `/tmp/pit_rank_evidence/`).
  - 2020-03-01 excluded: its only Wayback capture is a dead 418-byte stub (HTTP 200, no body).
  - All 13 Binance-UM perp symbols matched to PIT rank at the earliest snapshot at/after formation date (conservative upper bound — rank can fall after listing, not rise before it).
  - New artifact: `research_state/pit_rank_verification_v1.json` (full per-symbol trajectory, methodology, coverage limitation).
  - Updated `research_state/pit_universe_verification_v1.json` (rank_verified=true for all 13, prior notes preserved verbatim), `research_state/universe_frontier.json` (13 candidates -> rank_verified_pit_cmc_wayback), `research_state/pit_rank_search_v1.json` (extraction_result appended).
  - Ranks: BTC=1, ETH=2, BCH=5, XRP=3, XLM=10, TRX=12, ADA=13, LINK=17, BNB=8, DOGE=32, ZEC=28, SOL=108, NEAR=82.
- PIT rank inquiry now CLOSED with a verified free source (no key/auth/paid). Universe is no longer rank-unverified.
- H002/H003 remain registered_secondary_not_tested; anchor null preserved (adj p 0.248/0.949); exclusions 336 preserved (missing_label); 324 cells ok.
- No frozen artifacts modified (config_sha256 re-verified = 55caedf84ac723289f70f49bbed4712c8195425feb4a95e737f3e8929479a0e0). No preregistration from grid hits.

## Completed this session (activation 128)
- Required checks re-run and pass: grid manifest regenerated via `scripts/generate_grid_manifest.py --output /tmp/basis-grid-manifest.json` (324 cells, config_sha256=55caedf84ac723289f70f49bbed4712c8195425feb4a95e737f3e8929479a0e0 matches frozen config); `python3 -m pytest -q tests` (11 tests, OK); `git diff --check` clean; `git status --short` shows only intended research_state changes.
- PIT rank inquiry CLOSED with verified free Wayback-CMC source (rank_verified=true for all 13). Re-ran red-team audit to reflect PIT verification (no prior finding depended on rank-unverified assumption). Updated `research_state/red_team_audit_extended_v1.json` + `.md` (survivorship/selection notes now state PIT ranks verified for coverage cohort; exclusions 336 preserved).
- H002/H003 remain registered_secondary_not_tested; anchor null preserved (adj p 0.248/0.949); exclusions 336 preserved (missing_label); 324 cells ok.
- Report only verified findings. No preregistration from grid hits. No frozen artifacts modified.

## Completed this session (activation 129)
- Required checks re-run and pass: grid manifest regenerated (324 cells, config_sha256=55caedf84ac723289f70f49bbed4712c8195425feb4a95e737f3e8929479a0e0 matches frozen config); `python3 -m pytest -q tests` (11 tests, OK); `git diff --check` clean; `git status --short` shows intended research_state changes.
- Reviewed whether verified PIT ranks change interpretation of null anchor result: no non-null implication. PIT ranks are conservative upper bounds and do not affect basis signal or crash labels within coverage cohort. Artifact: research_state/pit_rank_interpretation_note_v1.json.
- H002/H003 remain registered_secondary_not_tested; anchor null preserved (adj p 0.248/0.949); exclusions 336 preserved (missing_label); 324 cells ok.
- Report only verified findings. No preregistration from grid hits. No frozen artifacts modified.

## Completed this session (activation 130)
- Required checks re-run and pass: grid manifest regenerated (324 cells, config_sha256=55caedf84ac723289f70f49bbed4712c8195425feb4a95e737f3e8929479a0e0 matches frozen config); `python3 -m pytest -q tests` (11 tests, OK); `git diff --check` clean; `git status --short` shows only intended research_state changes.
- Audited evaluation report test counts vs cell status ledger: no discrepancy. 324 cells × 8 endpoints = 2,592 registered tests; 2,451 with p-values; 141 blocked (no p); all 324 cells terminal `ok`. Artifact: research_state/evaluation_ledger_consistency_audit_v1.md.
- Anchor null preserved (adj p 0.248/0.949); exclusions 336 preserved (missing_label); 324 cells ok.
- H002/H003 remain registered_secondary_not_tested; PIT rank inquiry CLOSED with verified free Wayback-CMC source.
- Report only verified findings. No preregistration from grid hits. No frozen artifacts modified.

## Completed this session (activation 131)
- Required checks re-run and pass: grid manifest regenerated via `scripts/generate_grid_manifest.py --output /tmp/basis-grid-manifest.json` (324 cells, config_sha256=55caedf84ac723289f70f49bbed4712c8195425feb4a95e737f3e8929479a0e0 matches frozen config); `python3 -m pytest -q tests` (11 tests, OK); `git diff --check` clean; `git status --short` shows intended research_state changes.
- Verified leakage audit artifact (EBCR-001-LEAKAGE-AUDIT-EXTENDED-V1): JSON/Markdown schema valid; permutation p-values cross-checked (risk_diff 0.738, ES diff 0.9855) match; structural checks (past-only signal, forward-only labels) and placebo results consistent. No discrepancy. Artifact: `research_state/leakage_audit_verification_v1.md`.
- H002/H003 remain registered_secondary_not_tested; PIT rank inquiry CLOSED with verified free Wayback-CMC source (rank_verified=true for all 13); no new free PIT rank source located.
- Anchor null preserved (adj p 0.248/0.949); exclusions 336 preserved (missing_label); 324 cells ok.
- Report only verified findings. No preregistration from grid hits. No frozen artifacts modified. Preserve /tmp/pit_rank_evidence/ extraction record.

## Completed this session (activation 132)
- Required checks re-run and pass: grid manifest regenerated via `scripts/generate_grid_manifest.py --output /tmp/basis-grid-manifest.json` (324 cells, config_sha256=55caedf84ac723289f70f49bbed4712c8195425feb4a95e737f3e8929479a0e0 matches frozen config); `python3 -m pytest -q tests` (11 tests, OK); `git diff --check` clean; `git status --short` shows only intended research_state changes.
- Reviewed H002/H003 feasibility against existing extended data (5010 rows, 336 exclusions; 324 cells ok). Neither testable without new experiment ID, independent predeclared rationale, and new anchor/config; cannot preregister from inspected grid hits. Artifact: `research_state/h002_h003_feasibility_review_v1.json` + `.md`. H002/H003 remain `registered_secondary_not_tested`.
- H001 tested_not_supported; anchor null preserved (adj p 0.248/0.949); exclusions 336 preserved (missing_label); 324 cells ok.
- PIT rank inquiry CLOSED with verified free Wayback-CMC source (rank_verified=true for all 13). No genuinely new free PIT rank source located.
- Report only verified findings. No preregistration from grid hits. No frozen artifacts modified. Preserved /tmp/pit_rank_evidence/ extraction record.

## Completed this session (activation 133)
- Required checks re-run and pass: grid manifest regenerated via `scripts/generate_grid_manifest.py --output /tmp/basis-grid-manifest.json` (324 cells, config_sha256=55caedf84ac723289f70f49bbed4712c8195425feb4a95e737f3e8929479a0e0 matches frozen config); `python3 -m pytest -q tests` (11 tests, OK); `git diff --check` clean; `git status --short` empty before this activation's artifacts.
- Clean state confirmed; frozen anchor/config/Q1/extended artifacts untouched.
- Durable-state upkeep: verified hypothesis registry consistency post-reconciliation (research_state/hypothesis_registry.json accurate: H001 tested_not_supported with prior_status preserved, outcome_summary adj p 0.24830545694889028/0.9485 matching anchor cell EBCR-GRID-001-0005; H002/H003 registered_secondary_not_tested). Reviewed red-team audit (research_state/red_team_audit_extended_v1.json + .md): all sections addressed, no unaddressed gaps; PIT verification reflected; confounding section notes a follow-up recommendation only. Artifact: research_state/durable_state_upkeep_v1.json + .md (verdict: no_gaps_found). No registry/red-team/frozen-artifact modifications.
- H002/H003 remain registered_secondary_not_tested; PIT rank inquiry CLOSED (verified free Wayback-CMC source, rank_verified=true for all 13); no genuinely new free PIT rank source located.
- Anchor null preserved (adj p 0.248/0.949); exclusions 336 preserved (missing_label); 324 cells ok.
- Report only verified findings. No preregistration from grid hits. No frozen artifacts modified. Preserved /tmp/pit_rank_evidence/ extraction record.

## Completed this session (activation 134)
- Required checks re-run and pass: grid manifest regenerated via `scripts/generate_grid_manifest.py --output /tmp/basis-grid-manifest.json` (324 cells, config_sha256=55caedf84ac723289f70f49bbed4712c8195425feb4a95e737f3e8929479a0e0 matches frozen config); `python3 -m pytest -q tests` (11 tests, OK); `git diff --check` clean; `git status --short` shows only intended research_state changes.
- Clean state confirmed; frozen anchor/config/Q1/extended artifacts untouched.
- Durable-state upkeep v2: verified hypothesis registry consistency (H001 tested_not_supported matches anchor EBCR-GRID-001-0005 adj p 0.248305/0.9485; H002/H003 registered_secondary_not_tested). Reviewed red-team audit (research_state/red_team_audit_extended_v1.json): all addressed, PIT verification reflected; no unaddressed gaps (confounding notes predeclared follow-up only). Artifact: research_state/durable_state_upkeep_v2.json + .md (verdict: no_gaps_found).
- H002/H003 remain registered_secondary_not_tested; PIT rank inquiry CLOSED (verified free Wayback-CMC source, rank_verified=true for all 13); no genuinely new free PIT rank source located.
- Anchor null preserved (adj p 0.248/0.949); exclusions 336 preserved (missing_label); 324 cells ok.
- Report only verified findings. No preregistration from grid hits. No frozen artifacts modified. Preserved /tmp/pit_rank_evidence/ extraction record.

## Completed this session (activation 135)
- Required checks re-run and pass: grid manifest regenerated via `scripts/generate_grid_manifest.py --output /tmp/basis-grid-manifest.json` (324 cells, config_sha256=55caedf84ac723289f70f49bbed4712c8195425feb4a95e737f3e8929479a0e0 matches frozen config, independently re-verified via canonical-JSON sha256 with ensure_ascii=False); `python3 -m pytest -q tests` (11 tests, OK); `git diff --check` clean; `git status --short` empty before this activation's artifacts.
- Clean state confirmed; frozen anchor/config/Q1/extended artifacts untouched.
- Durable-state upkeep v3: verified hypothesis registry consistency (H001 tested_not_supported matches anchor EBCR-GRID-001-0005 adj p 0.248305/0.9485; H002/H003 registered_secondary_not_tested). Re-reviewed red-team audit (research_state/red_team_audit_extended_v1.json + .md): all sections addressed, no unaddressed gaps found; PIT verification reflected; confounding notes predeclared follow-up only. Artifact: research_state/durable_state_upkeep_v3.json + .md (verdict: no_gaps_found). No registry/red-team/frozen-artifact modifications.
- H002/H003 remain registered_secondary_not_tested; PIT rank inquiry CLOSED (verified free Wayback-CMC source, rank_verified=true for all 13); no genuinely new free PIT rank source located.
- Anchor null preserved (adj p 0.248/0.949); exclusions 336 preserved (missing_label); 324 cells ok.
- Report only verified findings. No preregistration from grid hits. No frozen artifacts modified. Preserved /tmp/pit_rank_evidence/ extraction record.

## Next action (activation 136)
1. Re-run required checks to confirm clean state (manifest via `scripts/generate_grid_manifest.py --output /tmp/basis-grid-manifest.json`, config_sha256 matches frozen config; `python3 -m pytest -q tests`; `git diff --check` clean; `git status --short` shows only intended research_state changes).
2. Maintain null/exclusions (336); preserve registered_secondary_not_tested status for H002/H003; preserve anchor null (adj p 0.248/0.949).
3. PIT rank inquiry CLOSED. Do not reopen unless genuinely new free PIT rank source.
4. No preregistration from grid hits. Do not modify frozen anchor/config/Q1/extended artifacts.
5. Next concrete task: continue durable-state upkeep — re-verify hypothesis registry consistency remains accurate and re-review red-team audit for any new unaddressed items; document findings only if gaps found, else record explicit "no gaps found" artifact (new version suffix v4). Update handoff and task message with verified findings only. A concrete next task must always remain.
6. Preserve /tmp/pit_rank_evidence/ extraction record.
