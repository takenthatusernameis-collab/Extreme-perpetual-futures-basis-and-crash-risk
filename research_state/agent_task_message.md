# Agent task message (activation 132)

## Prior task (from handoff activation 131)
1. Re-run required checks to confirm clean state (manifest via `scripts/generate_grid_manifest.py --output /tmp/basis-grid-manifest.json`, config_sha256 matches frozen config; `python3 -m pytest -q tests`; `git diff --check` clean; `git status --short` shows only intended research_state changes).
2. Maintain null/exclusions (336); preserve registered_secondary_not_tested status for H002/H003; preserve anchor null (adj p 0.248/0.949).
3. PIT rank inquiry CLOSED with verified free Wayback-CMC source (rank_verified=true for all 13). Do not reopen unless a genuinely new free PIT rank source (no key/auth/paid) is located.
4. No preregistration from grid hits. Do not modify frozen anchor/config/Q1/extended artifacts.
5. Next concrete task: verify leakage audit artifact (EBCR-001-LEAKAGE-AUDIT-EXTENDED-V1) JSON/Markdown schema validity and cross-check permutation p-values against report; document any discrepancy. Update handoff and task message with verified findings only. A concrete next task must always remain.
6. Preserve the /tmp/pit_rank_evidence/ fetch script and per-date sha256 + JSON as the auditable extraction record.

## What was done (activation 131)
- Required checks re-run and pass: grid manifest regenerated (324 cells, config_sha256=55caedf84ac723289f70f49bbed4712c8195425feb4a95e737f3e8929479a0e0 matches frozen config); `python3 -m pytest -q tests` (11 tests, OK); `git diff --check` clean; `git status --short` shows intended research_state changes.
- Verified leakage audit artifact (EBCR-001-LEAKAGE-AUDIT-EXTENDED-V1): JSON/Markdown schema valid; permutation p-values cross-checked (risk_diff 0.738, ES diff 0.9855) match; structural checks and placebo consistent. No discrepancy. Artifact: research_state/leakage_audit_verification_v1.md.
- H002/H003 remain registered_secondary_not_tested; PIT rank inquiry CLOSED with verified free Wayback-CMC source.
- Anchor null preserved (adj p 0.248/0.949); exclusions 336 preserved (missing_label); 324 cells ok.
- Report only verified findings. No preregistration from grid hits. No frozen artifacts modified. Preserved /tmp/pit_rank_evidence/ extraction record.

## Durable state (verified)
- Frozen config: configs/basis_crash_grid_v1.json (sha256 55caedf84ac723289f70f49bbed4712c8195425feb4a95e737f3e8929479a0e0). Anchor EBCR-GRID-001-0005 null preserved. Exclusions 336. 324 cells ok.
- PIT: CLOSED with verified free Wayback-CMC source (rank_verified=true for all 13). Extraction record under /tmp/pit_rank_evidence/.
- Hypotheses: H001 tested_not_supported (reconciled); H002/H003 registered_secondary_not_tested; feasibility documented.
- Red-team audit updated for PIT verification; leakage audit complete (no structural leakage) and verified.
- Leakage verification: research_state/leakage_audit_verification_v1.md (no discrepancy).

## Next concrete task (for activation 132)
1. Re-run required checks to confirm clean state (manifest via `scripts/generate_grid_manifest.py --output /tmp/basis-grid-manifest.json`, config_sha256 matches frozen config; `python3 -m pytest -q tests`; `git diff --check` clean; `git status --short` shows only intended research_state changes).
2. Maintain null/exclusions (336); preserve registered_secondary_not_tested status for H002/H003; preserve anchor null (adj p 0.248/0.949).
3. PIT rank inquiry CLOSED. Do not reopen unless genuinely new free PIT rank source.
4. No preregistration from grid hits. Do not modify frozen anchor/config/Q1/extended artifacts.
5. Next concrete task: review H002/H003 feasibility artifact against registered secondary orientations and existing extended data; decide if any becomes testable without grid-hit preregistration or new experiment/config (if not feasible, document explicitly). Update handoff and task message with verified findings only. A concrete next task must always remain.
6. Preserve the /tmp/pit_rank_evidence/ fetch script and per-date sha256 + JSON as the auditable extraction record.
