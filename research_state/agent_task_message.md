# Agent task message (for next activation)

## Objective
Activate for EBCR-001 (activation 436). Complete the next action from the durable handoff.

## Prior context (read first)
- Handoff: research_state/agent_handoff.md (activation 435 completed)
- Contract: prompts/continuous_research_operating_contract_v1.md
- Protocol: docs/research_protocol.md
- Skills: SKILLS.md (basis-crash-risk-research, point-in-time-universe, resumable-research-operations, statistical-red-team)
- Frozen: configs/basis_crash_grid_v1.json (sha256 55caedf84ac723289f70f49bbed4712c8195425feb4a95e737f3e8929479a0e0), evaluation_report_extended_v1.json, integrated_extended_v1.json
- Hypothesis registry: research_state/hypothesis_registry.json (H001 tested_not_supported, adj p 0.24830545694889028/0.9485; H002/H003 registered_secondary_not_tested)
- PIT: CLOSED (research_state/pit_rank_verification_v1.json, all 13 rank_verified)
- Exclusions: 336 (missing_label), labels_sha256 a64134574206f246ca6943703aa06508bbae7a4bda6c4a2457247afa7158eb58

## Required actions (activation 436)
1. Re-run required checks: `python3 scripts/generate_grid_manifest.py --output /tmp/basis-grid-manifest.json`; `python3 -m unittest discover -s tests -q`; `git diff --check`; `git status --short`. All must pass/clean.
2. Maintain null/exclusions (336); preserve H002/H003 as registered_secondary_not_tested; preserve anchor null.
3. PIT rank inquiry CLOSED — do not reopen without genuinely new free PIT rank source.
4. No preregistration from grid hits. Do not modify frozen anchor/config/Q1/extended artifacts.
5. Durable-state upkeep: re-verify hypothesis registry consistency and re-review on-disk audits for new unaddressed items; if none found, create `research_state/durable_state_upkeep_v307.json` with verdict `no_gaps_found` and concrete checks; if gaps found, document explicitly with artifact paths and concrete next steps (no fixes to frozen artifacts).
6. Update `research_state/agent_handoff.md` to record activation 436 completion and set next action for activation 437.
7. Update this file (`research_state/agent_task_message.md`) with clear next task for activation 437.
8. Report only verified findings. Do not commit unless explicitly asked.

## Constraints
- Free public data/open-source only. No paid APIs/trials/compute/private endpoints/credentials/trading.
- Preserve immutable configs/snapshots/hashes/raw inputs/prior results. New experiment/config/data version => new experiment ID and output path.
- Every grid cell terminal status tracked; apply correction across complete registered family; never select by raw p/best return/inspected holdout.
- Preserve unfavorable/null/contradictory/failed evidence.
- Use only completed UTC observations, causal timestamps, fully closed horizons.

(End of file - total 31 lines)