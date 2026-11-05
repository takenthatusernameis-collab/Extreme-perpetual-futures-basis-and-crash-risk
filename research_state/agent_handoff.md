# Agent handoff — EBCR-001

## Latest verified state (compact)
- **Verified research baseline:** `research_state/durable_state_upkeep_v981.json` (commit `76256d1`). No successor upkeep artifact created (no research-material state change since v981).
- **Invariants preserved:** exclusions n=336 (v981); anchor null (crash_incidence_15pct adj p 0.24830545694889028; expected_shortfall_5pct_forward_mae adj p 0.9485); PIT rank CLOSED. EBCR-H001 `tested_not_supported`; EBCR-H002/EBCR-H003/EBCR-H004 `registered_secondary_not_tested`; hypothesis registry `next_hypothesis_sequence` 5.
- **Frozen config:** `configs/basis_crash_grid_v1.json` literal sha256 `753d9357e1d535ef4229a901e25ef059a751e4c4d56188247f5f2e0ef1debd16` (unchanged). Grid manifest verification (when run to `/tmp`): 324 cells, 324 unique `configuration_hash_sha256`, config_sha256 `55caedf84ac723289f70f49bbed4712c8195425feb4a95e737f3e8929479a0e0`.
- **Pre-existing UNRESOLVED (do not silently close):** contract listing/delisting/migration history; data revision behavior.
- **Last research-input commit:** `52b3e49` (2026-10-27). Post-v981 changes observed through activation 2580 are operational harness/checkpoint only (`.github/workflows/main.yml` `64f77cc` and harness checkpoint files: `research_state/agent_handoff.md`, `research_state/agent_task_message.md`, `research_state/durable_state_upkeep_v981.json` record).
- **Tests at last material verification (activation 2541, v981):** `python3 -m unittest discover -s tests` → 11 OK; `tests/test_controller_progress_accounting.py` function tests → 7 OK (run explicitly; not always collected by discover). `pytest` unavailable (`No module named pytest`).
- **Workflow diagnostics:** `research_state/workflow_run_diagnostics.jsonl` entries are harness workflow artifacts only (latest recorded: run 41998331220, conclusion failure, captured 2026-11-05T17:06:07Z), not research sources.

## Recent activations (summary)
- Activations 2542–2579: state-change-gate NO-OPs against v981/`76256d1`. No research-material code/test/config/grid/source/registry/frontier/audit changes detected; no new admissible source data or dated research events; no upkeep artifacts created; frozen artifacts not modified; no commits made when not requested.

## Activation 2580 (completed, 2026-11-05) — NO-OP
- **State-change gate** vs `research_state/durable_state_upkeep_v981.json` / commit `76256d1`: `git status --short` clean; `git diff --name-only 76256d1..HEAD` → `.github/workflows/main.yml`, `research_state/agent_handoff.md`, `research_state/agent_task_message.md`, `research_state/durable_state_upkeep_v981.json` only (operational harness/checkpoint, no research-material changes); `git diff --check` clean; `git ls-files --others --exclude-standard` empty.
- **Admissible source/data:** none (last research-input `52b3e49`, 2026-10-27). Workflow diagnostics are harness artifacts only.
- **Verified:** frozen config literal sha256 `753d9357...ebd16` matches disk; hypothesis registry consistent (EBCR-H001 `tested_not_supported`; EBCR-H002/EBCR-H003/EBCR-H004 `registered_secondary_not_tested`; `next_hypothesis_sequence` 5); v981 exclusions_n 336 preserved; anchor null/PIT CLOSED preserved per v981 baseline.
- **Tests:** not re-run per NO-OP (unchanged since activation 2541). `pytest` unavailable.
- **Unresolved preserved:** contract listing/delisting/migration history; data revision behavior. No new unaddressed audit items.
- **Exit:** NO-OP per state-change-driven cadence (v1.1 addendum) — no repeated full tests, no in-repo grid manifest regeneration, no new upkeep artifact (v982 not created), no frozen artifacts modified, no commit made (not requested). Latest verified upkeep remains `research_state/durable_state_upkeep_v981.json`.

## Next agent starting point (activation 2581)
- Continue state-change-driven upkeep; follow `research_state/agent_task_message.md` (activation 2581). Compare against `research_state/durable_state_upkeep_v981.json` and commit `76256d1`. **Expect NO-OP** unless research-material inputs change (code/test/config/grid/source/registry/frontier/audit) or a new admissible source/dated event appears.
- Preserve invariants: exclusions n=336 (v981), anchor null, PIT rank CLOSED, EBCR-H001 `tested_not_supported`, EBCR-H002-H004 `registered_secondary_not_tested`. Pre-existing UNRESOLVED: contract listing/delisting/migration history; data revision behavior.
- If controller progress code changes, run `tests/test_controller_progress_accounting.py` function tests explicitly in addition to `unittest discover`. If a source becomes admissible/reachable or config/grid/registry/frontier changes, follow full required gates; else exit NO-OP without creating upkeep artifacts or timestamp-only changes.

(End of file - total 44 lines)