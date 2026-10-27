# Agent task message — EBCR-001 (for activation 461)

## Prior task (from handoff activation 460)
Complete required checks, verify hypothesis registry/frozen artifacts/PIT closed state, perform durable-state upkeep (create v331), update handoff (record 460, set next for 461), and write clear task message for next agent.

## Task for activation 461
1. Re-run required checks:
   - `python3 scripts/generate_grid_manifest.py --output /tmp/basis-grid-manifest.json` (expect 324 cells, 324 unique configuration hashes, config_sha256 55caedf8...)
   - `python3 -m unittest discover -s tests -q` (expect 11 tests OK)
   - `git diff --check` (clean)
   - `git status --short` (clean)
2. Preserve invariants: exclusions 336 preserved; H001 tested_not_supported (anchor adj p 0.24830545694889028/0.9485); H002/H003/H004 registered_secondary_not_tested (next_hypothesis_sequence 5); PIT rank inquiry CLOSED (research_state/pit_rank_verification_v1.json, rank_verified true for all 13). Do not modify frozen artifacts (configs/basis_crash_grid_v1.json, evaluation_report_extended_v1.json, integrated_extended_v1.json).
3. Durable-state upkeep: re-verify hypothesis registry consistency (H001..H004) and re-review on-disk audits for new unaddressed items. If none found, create `research_state/durable_state_upkeep_v332.json` with verdict `no_gaps_found` following the structure/style of v331 (include checks, audit_consistency). If gaps found, document explicitly with artifact paths and concrete next steps (no fixes to frozen artifacts).
4. Update `research_state/agent_handoff.md`: record activation 461 completion and set next action for activation 462.
5. Update `research_state/agent_task_message.md`: write clear next task for activation 462.
6. Report only verified findings; do not commit changes unless explicitly asked.

## Key artifacts
- Config (frozen): configs/basis_crash_grid_v1.json (literal 753d9357..., canonical 223498aa..., manifest 55caedf8...)
- Extended results (frozen): research_state/evaluation_report_extended_v1.json (literal 9487b36d08cad6eeb5b1af2a4748f959e6d0e47bd629024d4b29dbde60926cd4), research_state/integrated_extended_v1.json (literal 28ec0163a95c857073c35c6d908fa2b62f9e1117d2e84b686150de02cce0fabf), research_state/cell_status_ledger_extended_v1.json
- Registry: research_state/hypothesis_registry.json (H001 tested_not_supported, H002/H003/H004 registered_secondary_not_tested)
- PIT: research_state/pit_rank_verification_v1.json (CLOSED, all 13 verified)
- Exclusions: 336 (missing_label) preserved
- Latest durable-state upkeep: research_state/durable_state_upkeep_v331.json (verdict: no_gaps_found)

(End of file)
