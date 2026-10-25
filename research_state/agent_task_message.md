# Agent task message (activation 129)

## Prior task (from handoff activation 128)
1. Re-run required checks to confirm clean state (manifest via `scripts/generate_grid_manifest.py --output /tmp/basis-grid-manifest.json`, config_sha256 matches frozen config; `python3 -m pytest -q tests`; `git diff --check` clean; `git status --short` shows only intended research_state changes).
2. Maintain null/exclusions (336); preserve registered_secondary_not_tested status for H002/H003; preserve anchor null (adj p 0.248/0.949).
3. PIT rank inquiry now CLOSED with verified free Wayback-CMC source (rank_verified=true for all 13). Do not reopen unless a genuinely new free PIT rank source (no key/auth/paid) is located.
4. No preregistration from grid hits (requires new experiment ID + independent predeclared rationale + new anchor/config). Do not modify frozen anchor/config/Q1/extended artifacts.
5. Next concrete task: with PIT ranks now verified, re-run the red-team audit (research_state/red_team_audit_extended_v1.json) to check whether any prior finding depended on the rank-unverified assumption, and record any update. Do not modify frozen artifacts. Update handoff and task message with verified findings only. A concrete next task must always remain.
6. Preserve the /tmp/pit_rank_evidence/ fetch script and per-date sha256 + JSON as the auditable extraction record.

## What was done (activation 128)
- Required checks re-run and pass: grid manifest regenerated (324 cells, config_sha256=55caedf84ac723289f70f49bbed4712c8195425feb4a95e737f3e8929479a0e0 matches frozen config); `python3 -m pytest -q tests` (11 tests, OK); `git diff --check` clean; `git status --short` shows only intended research_state changes.
- Re-ran red-team audit with PIT ranks now verified. Updated `research_state/red_team_audit_extended_v1.json` + `.md`: survivorship/selection notes state PIT ranks verified for coverage cohort via free Wayback-CMC source (rank_verified=true for all 13); selection risk reduced for cohort; exclusions 336 preserved. No finding depended on rank-unverified assumption.
- H002/H003 remain registered_secondary_not_tested; anchor null preserved (adj p 0.248/0.949); exclusions 336 preserved (missing_label); 324 cells ok.
- Report only verified findings. No preregistration from grid hits. No frozen artifacts modified. Preserved /tmp/pit_rank_evidence/ extraction record.

## Durable state (verified)
- Frozen config: configs/basis_crash_grid_v1.json (canonical-JSON sha256=55caedf84ac723289f70f49bbed4712c8195425feb4a95e737f3e8929479a0e0). Anchor EBCR-GRID-001-0005 null preserved. Exclusions 336. 324 cells ok.
- Leakage audit: EBCR-001-LEAKAGE-AUDIT-EXTENDED-V1 complete (no structural leakage).
- PIT: CLOSED with verified free Wayback-CMC source (rank_verified=true for all 13). Artifacts: research_state/pit_rank_verification_v1.json, updated pit_universe_verification_v1.json, universe_frontier.json, pit_rank_search_v1.json. Extraction script + per-date sha256/JSON under /tmp/pit_rank_evidence/.
- Hypotheses: H001 tested_not_supported (reconciled); H002/H003 registered_secondary_not_tested; feasibility documented.
- Red-team audit updated for PIT verification.

## Next concrete task (for activation 129)
1. Re-run required checks to confirm clean state (manifest via `scripts/generate_grid_manifest.py --output /tmp/basis-grid-manifest.json`, config_sha256 matches frozen config; `python3 -m pytest -q tests`; `git diff --check` clean; `git status --short` shows only intended research_state changes).
2. Maintain null/exclusions (336); preserve registered_secondary_not_tested status for H002/H003; preserve anchor null (adj p 0.248/0.949).
3. PIT rank inquiry now CLOSED with verified free Wayback-CMC source (rank_verified=true for all 13). Do not reopen unless a genuinely new free PIT rank source (no key/auth/paid) is located.
4. No preregistration from grid hits (requires new experiment ID + independent predeclared rationale + new anchor/config). Do not modify frozen anchor/config/Q1/extended artifacts.
5. Next concrete task: review whether the verified PIT ranks change any interpretation of the null anchor result (coverage-cohort only; ranks are conservative upper bounds). Document findings in a short note artifact if any non-null implication arises, else explicitly confirm no change. Do not preregister new tests from grid hits. Update handoff and task message with verified findings only. A concrete next task must always remain.
6. Preserve the /tmp/pit_rank_evidence/ fetch script and per-date sha256 + JSON as the auditable extraction record.

(End of file)
