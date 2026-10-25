# Durable-state upkeep v23 (activation 155)

- Required checks (re-run): `scripts/generate_grid_manifest.py --output /tmp/basis-grid-manifest.json` -> 324 cells, config_sha256=55caedf84ac723289f70f49bbed4712c8195425feb4a95e737f3e8929479a0e0 (matches frozen canonical). `python3 -m pytest -q tests` -> 11 passed. `git diff --check` clean. `git status --short` clean of tracked changes.
- Config hash: canonical JSON hash matches frozen value (55caedf8...); raw file sha256 differs only by whitespace (previously noted). Content unchanged; frozen artifacts untouched.
- Hypothesis registry consistency: H001 tested_not_supported reconciled to anchor EBCR-GRID-001-0005 adj p 0.24830545694889028 / 0.9485 (null preserved). H002/H003 registered_secondary_not_tested. No changes made.
- Red-team audit (extended): reviewed research_state/red_team_audit_extended_v1.json + .md; PIT rank verification reflected (rank_verified=true for 13-symbol coverage cohort via free Wayback-CMC). No unaddressed gaps identified.
- State invariants: exclusions 336 preserved; 324 cells ok; PIT inquiry CLOSED (do not reopen without genuinely new free PIT rank source). No preregistration from grid hits. Frozen anchor/config/Q1/extended artifacts untouched. /tmp/pit_rank_evidence/ extraction record preserved.
- Verdict: no_gaps_found
