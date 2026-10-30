# DELAY-ELIMINATION OVERRIDE — ACTIVATION 1103 AND LATER

The handoff records repeated no-gap upkeep activations with unchanged state. This task now uses the state-change gate below instead of requiring a new numbered upkeep artifact on every activation.

1. Compare current code/test/config/grid/source/registry/frontier/audit hashes against the latest durable upkeep artifact.
2. If unchanged and no new admissible source data or dated event exists, exit NO-OP: no repeated full tests, no new durable_state_upkeep_vNNN.json, no timestamp-only handoff update, no empty commit.
3. If code/tests changed, run targeted affected tests first. If frozen config/grid/registry/frontier or source data changed, run the specific integrity validators affected. Run the full required gates only at a material milestone or when relevant inputs changed.
4. Create the next numbered upkeep artifact only when new evidence, a real state transition, a new integrity issue, or a code/config change was actually reviewed.
5. Do not re-open PIT rank verification or repeat source searches while the exact structural blocker is unchanged. Re-evaluate only with a genuinely new free PIT source, documented source schema/coverage change, or relevant provider change.
6. Preserve the frozen 324-cell grid, anchor null, 336 exclusions, H001 tested_not_supported, secondary hypotheses untested, and PIT-rank closed status.

See AGENTS.md and prompts/continuous_research_operating_contract_v1_1_addendum.md. Research design and evidence gates are unchanged.

---

# Agent task message — EBCR-001 (activation 1102)

## Objective
Continue durable-state upkeep for EBCR-001. Do not reopen testing of H001 (tested_not_supported; null preserved). Keep secondary hypotheses untested. Preserve frozen artifacts and invariants.

## Required checks (must pass)
- `python3 scripts/generate_grid_manifest.py --output /tmp/basis-grid-manifest.json` (expect 324 cells, 324 unique hashes, config_sha256_canonical matches frozen 55caedf84ac723289f70f49bbed4712c8195425feb4a95e737f3e8929479a0e0)
- `python3 -m unittest discover -s tests -q` (expect OK, 11 tests)
- `python3 -m pytest -q tests` (if available; otherwise record unavailable)
- `git diff --check` (clean)
- `git status --short` (clean)

## Invariants to preserve
- Anchor null: crash_incidence_15pct adj p 0.24830545694889028; expected_shortfall_5pct adj p 0.9485
- Exclusions: 336
- Hypothesis registry: H001 tested_not_supported; H002/H003/H004 registered_secondary_not_tested (next_seq 5)
- PIT rank: CLOSED (research_state/pit_rank_verification_v1.json). Do not reopen without genuinely new free PIT rank source.
- No preregistration from grid hits; do not modify frozen anchor/config/Q1/extended artifacts.

## Audits
Review on-disk audits for any new unaddressed items. Pre-existing UNRESOLVED preserved: Contract listing/delisting/migration history; Data revision behavior.

## Deliverables
1. Run required checks and record exact commands/results.
2. Re-verify hypothesis registry consistency.
3. If no gaps found, create `research_state/durable_state_upkeep_v969.json` with verdict `no_gaps_found` following the schema of prior upkeep artifacts (see research_state/durable_state_upkeep_v968.json). If gaps found, document explicitly with artifact paths and concrete next steps.
4. Update `research_state/agent_handoff.md` with activation 1102 summary and concrete Next action (activation 1103).
5. Report only verified findings; do not commit changes unless explicitly asked.