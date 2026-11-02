# Agent task message — EBCR-001 (activation 1709)
## Objective
Continue durable-state upkeep for EBCR-001 under state-change gate (v1.1). Do not reopen testing of EBCR-H001 (tested_not_supported; null preserved). Keep secondary hypotheses untested. Preserve frozen artifacts and invariants.

## State-change gate (run first)
Compare current code/test/config/grid/source/registry/frontier/audit hashes against latest verified state (research_state/durable_state_upkeep_v971.json). If unchanged and no new admissible source data or dated event exists, exit NO-OP: no repeated full tests, no new durable_state_upkeep_vNNN.json, no timestamp-only handoff update, no empty commit.

## Required checks (only if state changed or material milestone)
- `python3 scripts/generate_grid_manifest.py --output /tmp/basis-grid-manifest.json` -> 324 cells, 324 unique per-cell configuration_hash_sha256, config_sha256 matches frozen canonical; top-level `primary_anchor` present
- `python3 -m unittest discover -s tests -q` -> OK
- `python3 -m pytest -q tests` -> record unavailable if missing
- `git diff --check` -> clean
- `git status --short` -> clean

## Invariants to preserve
- Anchor null: crash_incidence_15pct adj p 0.24830545694889028; expected_shortfall_5pct_forward_mae adj p 0.9485
- Exclusions: n_recorded_exclusions=336
- Hypothesis registry: EBCR-H001 tested_not_supported; EBCR-H002/EBCR-H003/EBCR-H004 registered_secondary_not_tested (next_hypothesis_sequence 5)
- PIT rank: CLOSED. Do not reopen without genuinely new free PIT rank source.

## Audits
Review on-disk audits for any new unaddressed items only if state changed. Pre-existing UNRESOLVED preserved: Contract listing/delisting/migration history; Data revision behavior.

## Deliverables
1. Apply state-change gate; record outcome in research_state/agent_handoff.md as activation 1709.
2. If state changed, run required checks and record exact commands/results; re-verify hypothesis registry consistency; create next upkeep artifact only if new evidence/transition/issue/change reviewed.
3. Update research_state/agent_handoff.md with activation 1709 summary and concrete Next action (activation 1710) only if a real state transition occurred (or record NO-OP if none). Follow state-change gate strictly.
4. Report only verified findings; do not commit changes unless explicitly asked.
