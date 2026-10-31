# Agent task message — EBCR-001 (activation 1188)

## Objective
Continue durable-state upkeep for EBCR-001 under the state-change gate. Do not reopen testing of H001 (tested_not_supported; null preserved). Keep secondary hypotheses untested. Preserve frozen artifacts and invariants.

## State-change gate (run first)
Compare current code/test/config/grid/source/registry/frontier/audit hashes against the latest verified state (research_state/durable_state_upkeep_v969.json). If unchanged and no new admissible source data or dated event exists, exit NO-OP: no repeated full tests, no new durable_state_upkeep_vNNN.json, no timestamp-only handoff update, no empty commit.

## Required checks (only if state changed or material milestone)
- `python3 scripts/generate_grid_manifest.py --output /tmp/basis-grid-manifest.json` → 324 cells, 324 unique per-cell configuration_hash_sha256, config_sha256 matches frozen 55caedf84ac723289f70f49bbed4712c8195425feb4a95e737f3e8929479a0e0; top-level `primary_anchor` present
- `python3 -m unittest discover -s tests -q` → OK, 11 tests
- `python3 -m pytest -q tests` → No module named pytest (if available; otherwise record unavailable)
- `git diff --check` → clean
- `git status --short` → clean

## Invariants to preserve
- Anchor null: crash_incidence_15pct adj p 0.24830545694889028; expected_shortfall_5pct adj p 0.9485
- Exclusions: 336
- Hypothesis registry: H001 tested_not_supported; H002/H003/H004 registered_secondary_not_tested (next_seq 5)
- PIT rank: CLOSED (research_state/pit_rank_verification_v1.json). Do not reopen without genuinely new free PIT rank source.
- No preregistration from grid hits; do not modify frozen anchor/config/Q1/extended artifacts.

## Audits
Review on-disk audits for any new unaddressed items only if state changed. Pre-existing UNRESOLVED preserved: Contract listing/delisting/migration history; Data revision behavior.

## Deliverables
1. Apply state-change gate; record outcome.
2. If state changed, run required checks and record exact commands/results; re-verify hypothesis registry consistency; create next upkeep artifact only if new evidence/transition/issue/change reviewed.
3. Update research_state/agent_handoff.md with activation 1188 summary and concrete Next action (activation 1189) only if a real state transition occurred.
4. Report only verified findings; do not commit changes unless explicitly asked.

(End of file)
" filePath">
research_state/agent_task_message.md