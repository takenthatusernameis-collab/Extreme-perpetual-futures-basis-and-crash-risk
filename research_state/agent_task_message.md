# Agent task message (activation 1029)
## Task
Continue the next scheduled upkeep cycle from the durable handoff. Do not reopen closed items.

## Required actions
1. Re-run required checks: `python3 scripts/generate_grid_manifest.py --output /tmp/basis-grid-manifest.json`; `python3 -m unittest discover -s tests -q`; `python3 -m pytest -q tests` (if available); `git diff --check`; `git status --short`.
2. Maintain null/exclusions (336); preserve registered_secondary_not_tested for H002/H003/H004; preserve anchor null (adj p 0.24830545694889028/0.9485).
3. PIT rank inquiry CLOSED. Do not reopen without genuinely new free PIT rank source.
4. No preregistration from grid hits. Do not modify frozen anchor/config/Q1/extended artifacts.
5. Continue durable-state upkeep — re-verify hypothesis registry consistency (H001..H004) and re-review the on-disk audits for any new unaddressed items; if none found, create `research_state/durable_state_upkeep_v896.json` with verdict `no_gaps_found`; if gaps found, document explicitly with artifact paths and concrete next steps (no fixes to frozen artifacts).
6. PIT rank evidence: `research_state/pit_rank_verification_v1.json` (13 symbols, rank_verified=true).
7. Report only verified findings; do not commit changes unless explicitly asked.
8. Update `research_state/agent_handoff.md` to record activation 1029 completion and set next action for activation 1030.
9. Update `research_state/agent_task_message.md` with clear next task for activation 1030.

## Context
- Frozen config: configs/basis_crash_grid_v1.json (canonical sha256 55caedf84ac723289f70f49bbed4712c8195425feb4a95e737f3e8929479a0e0)
- Grid: 324 cells, all complete; anchor null preserved
- Hypotheses: H001 tested_not_supported; H002-H004 registered_secondary_not_tested
- Pre-existing UNRESOLVED: Contract listing/delisting/migration history; Data revision behavior
- Latest durable state: research_state/durable_state_upkeep_v895.json (verdict no_gaps_found, activation 1028)

(End of file - total 21 lines)
