# Durable state upkeep v25 (activation 157)

- Required checks re-run and pass: grid manifest regenerated (324 cells, config_sha256 matches frozen canonical hash 55caedf8...); `python3 -m pytest -q tests` (11 passed); `git diff --check` clean; `git status --short` clean of tracked changes.
- Clean state confirmed; frozen anchor/config/Q1/extended artifacts untouched.
- Durable-state upkeep v25: verified hypothesis registry consistency (H001 tested_not_supported matches anchor EBCR-GRID-001-0005 adj p 0.24830545694889028/0.9485; H002/H003 registered_secondary_not_tested). Re-reviewed red-team audit (extended) — PIT verification reflected; no unaddressed gaps identified. Artifact: research_state/durable_state_upkeep_v25.json + .md (verdict: no_gaps_found). No registry/red-team/frozen-artifact modifications.
- Config hash note: manifest config_sha256 is canonical-JSON hash (55caedf8...); raw file sha256 (753d9357...) differs only by whitespace. Canonical hash matches frozen value; config content unchanged.
- H002/H003 remain registered_secondary_not_tested; PIT rank inquiry CLOSED (verified free Wayback-CMC). Anchor null preserved (adj p 0.248/0.949); exclusions 336 preserved; 324 cells ok.
- Report only verified findings. No preregistration from grid hits. No frozen artifacts modified. Preserved /tmp/pit_rank_evidence/ extraction record.

Verdict: no_gaps_found
