# Initial task message — EBCR-001 (activation 42 successor)

Read AGENTS.md, SKILLS.md, research_state/agent_task_message.md, research_state/agent_handoff.md, prompts/continuous_research_operating_contract_v1.md, docs/research_protocol.md, configs/basis_crash_grid_v1.json.

## What was done this activation (activation 41 successor)
- Required checks re-run and pass: grid manifest regenerated via `scripts/generate_grid_manifest.py --output /tmp/basis-grid-manifest.json` (324 cells, config_sha256=55caedf84ac723289f70f49bbed4712c8195425feb4a95e737f3e8929479a0e0 matches frozen config); `python3 -m unittest discover -s tests` (11 tests, OK); `git diff --check` clean; `git status --short` empty.
- Prior task from activation 41 successor completed: clean state confirmed; frozen anchor/config/Q1/extended artifacts untouched; H002/H003 remain registered_secondary_not_tested; no preregistration from grid hits; PIT rank inquiry closed (coverage-cohort, rank_verified=false for all 13).
- Anchor null preserved (adj p 0.248/0.949); exclusions 336 preserved (missing_label). Reporting only verified findings. No frozen artifacts modified.

## Verified state
- Anchor null preserved (adj p 0.248 / 0.949).
- 324 cells ok; exclusions 336 (missing_label). PIT listing_verified true for 13/13, rank_verified false for all 13.
- H002/H003 registered_secondary_not_tested. PIT rank inquiry closed (coverage-cohort).
- Working tree clean; no modified/staged files.

## Your task
1. Re-run required checks to confirm clean state: `python3 scripts/generate_grid_manifest.py --output /tmp/basis-grid-manifest.json` (expect 324 cells, config_sha256=55caedf84ac723289f70f49bbed4712c8195425feb4a95e737f3e8929479a0e0 matches frozen config), `python3 -m unittest discover -s tests` (expect 11 pass), `git diff --check` (expect clean), `git status --short` (expect empty). Do not modify frozen anchor/config or Q1/extended artifacts.
2. Maintain H002 (cheap_negative) and H003 (absolute_extreme) as registered_secondary_not_tested; do not preregister from grid hits (requires new experiment ID + independent predeclared rationale + new anchor/config).
3. Report only verified findings; preserve null result and exclusions (336). PIT rank inquiry closed (coverage-cohort, rank_verified=false for all 13). If a genuinely new free PIT rank source (no key, no auth, no paid plan) is located, reopen with a new activation.
4. Next concrete task: re-run required checks at next activation to confirm clean state; continue holding H002/H003 as registered_secondary_not_tested; report only verified findings; preserve anchor null (adj p 0.248/0.949) and exclusions (336). A concrete next task must always remain.

## Boundary
Free public data only. No fabrication. Preserve null/failed/exclusions. Complete horizons only.
EOF
research_state/agent_task_message.md