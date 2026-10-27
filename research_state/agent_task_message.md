Activation 430 task (for next agent):

1. Re-run required checks: `python3 scripts/generate_grid_manifest.py --output /tmp/basis-grid-manifest.json`; `python3 -m unittest discover -s tests -q`; `git diff --check`; `git status --short`. All must pass/clean.
2. Verify hypothesis registry: EBCR-H001 remains tested_not_supported with anchor null preserved (adj p 0.24830545694889028/0.9485); EBCR-H002/H003 remain registered_secondary_not_tested; next_hypothesis_sequence 4. Exclusions 336 (missing_label, source research_state/integrated_extended_v1.json; labels_sha256 a64134574206f246ca6943703aa06508bbae7a4bda6c4a2457247afa7158eb58) preserved.
3. Confirm PIT remains CLOSED (rank_verified true for all 13). Evidence: research_state/pit_rank_verification_v1.json. Do not reopen without genuinely new free PIT rank source.
4. Re-review audits for unaddressed items: evaluation_artifact_audit_v1.md, evaluation_ledger_consistency_audit_v1.md, leakage_audit_extended_v1.md, red_team_audit_extended_v1.md. If gaps found, document concretely with artifact paths; else create `research_state/durable_state_upkeep_v301.json` with verdict "no_gaps_found" and checks summary.
5. Do not modify frozen artifacts (config/Q1/extended/anchor). No preregistration from grid hits.
6. Update `research_state/agent_handoff.md` (activation 429 completion, next action for 430) and this file with clear next task. Report only verified findings; do not commit unless explicitly asked.
