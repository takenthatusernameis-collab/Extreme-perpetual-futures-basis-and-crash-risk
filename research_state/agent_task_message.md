# Next task — EBCR-001

Read `AGENTS.md`, `SKILLS.md`, this file, `research_state/agent_handoff.md`, the operating contract, grid config, source guide and relevant skills.

## Immediate deliverables
1. Run `python3 -m pytest -q tests` and `python3 scripts/generate_grid_manifest.py --output research_state/grid_manifest_v1.json`. Verify 324 unique IDs/hashes and the locked anchor.
2. Review official free source endpoints; verify actual coverage, timestamps, rank-history availability, contract lifecycle and limitations. Persist cutoff, retrieval time, raw hash and gaps before calculating outcomes.
3. Implement a reproducible data-coverage and candidate mapping ledger. Separate descending market-cap candidate discovery from point-in-time historical eligibility. The frontier has no fixed top-N cutoff.
4. Build timestamp/lifecycle gates, freeze cutoff/splits, and run the grid on development only. Validation and historical holdout are anchor-only.
5. Record every cell's status and reason. If a source is blocked, persist the blocker and continue with other candidate discovery, code/tests, integrity checks or red-team tasks.

## Boundary
Use only free public data and open-source tools. No paid services, keys/secrets, exchange credentials, live/paper trading or orders. Never fabricate coverage or metrics. Preserve negative, null, failed and not-run results. Finish with an updated handoff and next measurable task.
