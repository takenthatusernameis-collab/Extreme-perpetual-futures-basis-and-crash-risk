# Durable state upkeep v6 (activation 138)

- Required checks re-run and pass: grid manifest regenerated via `scripts/generate_grid_manifest.py --output /tmp/basis-grid-manifest.json` (324 cells, config_sha256=55caedf84ac723289f70f49bbed4712c8195425feb4a95e737f3e8929479a0e0 matches frozen config); `python3 -m pytest -q tests` (11 tests, OK); `git diff --check` clean; `git status --short` empty before this activation's artifacts.
- Clean state confirmed; frozen anchor/config/Q1/extended artifacts untouched.
- Durable-state upkeep v6: verified hypothesis registry consistency (H001 tested_not_supported matches anchor EBCR-GRID-001-0005 adj p 0.248305/0.9485; H002/H003 registered_secondary_not_tested). Re-reviewed red-team audit (research_state/red_team_audit_extended_v1.json + .md): all sections addressed, no unaddressed gaps found; PIT verification reflected; confounding notes predeclared follow-up only. Artifact: research_state/durable_state_upkeep_v6.json + .md (verdict: no_gaps_found). No registry/red-team/frozen-artifact modifications.
- H002/H003 remain registered_secondary_not_tested; PIT rank inquiry CLOSED (verified free Wayback-CMC source, rank_verified=true for all 13); no genuinely new free PIT rank source located.
- Anchor null preserved (adj p 0.248/0.949); exclusions 336 preserved (missing_label); 324 cells ok.
- Report only verified findings. No preregistration from grid hits. No frozen artifacts modified. Preserved /tmp/pit_rank_evidence/ extraction record.
