# Agent Task Message

## Next task (activation 645)

1. Re-run required checks:
   - `python3 scripts/generate_grid_manifest.py --output /tmp/basis-grid-manifest.json`
   - `python3 -m unittest discover -s tests -q`
   - `git diff --check`
   - `git status --short`
   All must pass/clean.
2. Maintain null/exclusions (336); preserve registered_secondary_not_tested status for H002/H003/H004; preserve anchor null (adj p 0.24830545694889028/0.9485).
3. PIT rank inquiry CLOSED. Do not reopen without genuinely new free PIT rank source.
4. No preregistration from grid hits. Do not modify frozen anchor/config/Q1/extended artifacts.
5. Continue durable-state upkeep — re-verify hypothesis registry consistency (H001..H004) and re-review the on-disk audits for any new unaddressed items; if none found, create `research_state/durable_state_upkeep_v516.json` with verdict `no_gaps_found`; if gaps found, document explicitly with artifact paths and concrete next steps (no fixes to frozen artifacts).
6. PIT rank evidence: durable record is research_state/pit_rank_verification_v1.json.
7. Report only verified findings; do not commit changes unless explicitly asked.
8. Update `research_state/agent_handoff.md` to record activation 645 completion and set next action for activation 646.
9. Update `research_state/agent_task_message.md` with clear next task for activation 646.
