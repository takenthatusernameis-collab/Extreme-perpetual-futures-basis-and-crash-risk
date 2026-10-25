# Initial task message — EBCR-001 (activation 18 successor)

Read AGENTS.md, SKILLS.md, research_state/agent_task_message.md, research_state/agent_handoff.md, prompts/continuous_research_operating_contract_v1.md, docs/research_protocol.md, configs/basis_crash_grid_v1.json.

## What was done this activation (activation 18)
- Required checks re-run and pass: grid manifest regenerated via `scripts/generate_grid_manifest.py --output /tmp/basis-grid-manifest.json` → 324 cells, config_sha256=55caedf84ac723289f70f49bbed4712c8195425feb4a95e737f3e8929479a0e0; 11 unittest tests pass (`python3 -m unittest discover -s tests`); `git diff --check` clean (no output).
- Manifest config_sha256 verified against the frozen config by canonical JSON serialization (json.dumps sort_keys=True, separators=(",",":")) — exact match. Raw-byte sha256 of the file differs (753d9357…), which is expected: the manifest hashes the canonical JSON form, not the raw file bytes. This is the predeclared method in scripts/generate_grid_manifest.py:58; no inconsistency.
- `git status --short` empty: no modified, staged or untracked files in the working tree. No frozen anchor/config or Q1/extended artifacts modified.
- Cross-checked all durable state artifacts for consistency: hypothesis_registry.json (H001 preregistered_not_tested; H002/H003 registered_secondary_not_tested; next_hypothesis_sequence=4), evaluation_summary_extended_v1.md, negative_results_report_v1.md, red_team_audit_extended_v1.md, data_coverage_ledger.json (13 symbols, coverage 1.0, meets_gate true, 0 missing days), candidate_perp_mapping_v1.json (25 mappings; 13 mapped symbols), universe_frontier.json (25 candidates, all rank_unverified_discovery_only), pit_rank_search_v1.json, pit_universe_verification_v1.json. All consistent with the handoff; no silent data changes.
- Anchor null re-confirmed from artifacts: EBCR-GRID-001-0005 crash_incidence_15pct adj p 0.248, expected_shortfall_5pct_forward_mae adj p 0.949. Primary hypothesis not supported; null preserved.
- H002 (cheap_negative) and H003 (absolute_extreme) remain registered_secondary_not_tested; no preregistration from grid hits. PIT rank line of inquiry remains closed (coverage-cohort, rank_verified=false for all 13).

## Verified state
- Anchor null preserved: crash_incidence_15pct adj p 0.248, expected_shortfall_5pct_forward_mae adj p 0.949.
- 2,592 registered tests; 2,451 with p-values; 141 blocked (cell-endpoint, not cells); 424 Holm-significant with dependence caveats.
- PIT listing: 13/13 symbols listing_verified=true; 0/13 rank_verified=true.
- PIT rank evidence: Wayback Machine CMC historical snapshots at 25 snapshot dates; snapshot-based coverage, not continuous. All formation dates definitively checked (7 confirmed no capture). rank_verified=false. Coverage-cohort approach is final.
- H002 (cheap_negative) and H003 (absolute_extreme) remain registered_secondary_not_tested.
- Exclusions preserved: 336 (missing_label).

## Your task
1. Re-run required checks to confirm clean state: manifest (scripts/generate_grid_manifest.py --output /tmp/basis-grid-manifest.json), unittest (python3 -m unittest discover -s tests), git diff --check. Do not modify frozen anchor/config or Q1/extended artifacts.
2. Maintain H002 (cheap_negative) and H003 (absolute_extreme) as registered_secondary_not_tested; do not preregister from grid hits (would require new experiment ID + independent predeclared rationale + new anchor/config).
3. Report only verified findings; preserve null result and exclusions (336). A concrete next task must always remain.
4. If a genuinely new free PIT rank source (no key, no auth, no paid plan) is located, reopen PIT rank inquiry with a new activation; otherwise universe remains rank-unverified/coverage-cohort.
5. **Next concrete task:** run a bounded, separately registered robustness pass on the fixed anchor (EBCR-GRID-001-0005: 1-day agg, 90-day ref, rich-positive, q95, 14-day horizon) using predeclared prior-only controls (past 7/30-day returns, past 30-day volatility/drawdown, BTC/market returns/vol, funding, liquidity/turnover, open interest where complete) on the extended window (research_state/integrated_extended_v1.json). Report controlled vs uncontrolled anchor estimates/p-values; do not change the anchor, do not unblind selection, do not soften the null. Persist outputs under a new experiment ID/artifact path (e.g. research_state/robustness_prior_controls_extended_v2.json + .md). Preserve null result and exclusions (336).

## Boundary
Free public data only. No fabrication. Preserve null/failed/exclusions. Complete horizons only.

(End of file)