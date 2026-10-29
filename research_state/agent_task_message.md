# Agent task message — EBCR-001 (activation 786)

## Objective
Complete the next durable upkeep action per handoff: re-verify state, run required checks, create durable-state upkeep v657 if no gaps found, update handoff and this task message for activation 787.

## Prior context (read-only)
- Program: EBCR-001. H001 tested_not_supported (adj p 0.24830545694889028 / 0.9485). H002/H003/H004 registered_secondary_not_tested (next seq 5). No preregistration from grid hits.
- Frozen config: configs/basis_crash_grid_v1.json (canonical sha256 55caedf84ac723289f70f49bbed4712c8195425feb4a95e737f3e8929479a0e0; raw 753d9357e1d535ef4229a901e25ef059a751e4c4d56188247f5f2e0ef1debd16). Grid manifest 324 cells / 324 hashes / expected_configuration_count 324.
- PIT rank CLOSED (13 symbols), evidence research_state/pit_rank_verification_v1.json. Exclusions 336 preserved.
- Anchor null preserved. No preregistration from grid hits. Frozen artifacts untouched. Pre-existing UNRESOLVED items in source_audit context preserved (Contract listing/delisting/migration history; Data revision behavior).
- Durable upkeep v627-v656 created (verdict no_gaps_found). Activation 785 required checks passed (manifest 324/324/324, config sha match; unittest 11 OK; pytest unavailable; git diff --check clean; git status clean). Upkeep v656 created (verdict no_gaps_found).

## Required actions
1. Run required checks: `python3 scripts/generate_grid_manifest.py --output /tmp/basis-grid-manifest.json`; `python3 -m unittest discover -s tests -q`; `git diff --check`; `git status --short`. Also run `python3 -m pytest -q tests` if available.
2. Re-verify hypothesis registry consistency (H001..H004). Maintain null/exclusions (336); preserve registered_secondary_not_tested for H002/H003/H004; preserve anchor null.
3. Re-review on-disk audits for new unaddressed items. PIT rank inquiry CLOSED — do not reopen without genuinely new free PIT rank source. Do not modify frozen artifacts.
4. If no gaps found, create `research_state/durable_state_upkeep_v657.json` with verdict `no_gaps_found` and checks; validate JSON. If gaps found, document explicitly with artifact paths and concrete next steps (no fixes to frozen artifacts).
5. Update `research_state/agent_handoff.md`: record activation 785 completion and set Next action (activation 786) per operating contract.
6. Update `research_state/agent_task_message.md` with clear next task for activation 787.
7. Report only verified findings; do not commit changes unless explicitly asked.

## Constraints
- Free public data/open-source tools only. Preserve immutable configs/snapshots/hashes/raw inputs/prior results.
- Use completed UTC observations only; no synthesis/forward-fill/silent omission.
- Every grid cell terminal status preserved by design; no selection by raw p-value/best return/inspected holdout.
- Preserve unfavorable/null/contradictory/failed evidence.
- Do not commit secrets/private paths/unredacted credentials/large raw data.

(End of file)
