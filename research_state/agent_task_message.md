# Next task — EBCR-001

Read AGENTS.md, SKILLS.md, research_state/agent_handoff.md, prompts/continuous_research_operating_contract_v1.md, docs/research_protocol.md, configs/basis_crash_grid_v1.json.

## Context
The full EBCR-001 grid has been evaluated on the extended window (2023-01-01..2024-04-30, 11 symbols, 5010 integrated rows, 336 exclusions). Holm correction across all 2592 cell-endpoint tests and anchor co-primary Holm (m=2) is complete:
- research_state/evaluation_report_extended_v1.json (full report)
- research_state/evaluation_summary_extended_v1.md (summary)

Key results:
- Anchor (1d agg, 90d ref, rich-positive, q95, 14d) co-primary: **not significant** — crash_incidence_15pct adj p 0.248, expected_shortfall_5pct_forward_mae adj p 0.949. Primary hypothesis NOT supported. Preserve as a null/negative finding.
- Grid family: 424/2451 Holm-significant (141 blocked, no p-value invented).
- Stratified: absolute_extreme 224, rich_positive 135, cheap_negative 65 (by orientation); 7d 186, 14d 129, 28d 109 (by horizon).

## Immediate deliverables
1. Run the `statistical-red-team` audit on the extended results: leakage/permutation/placebo, overlapping-horizon dependence, survivorship/missingness selection, confounding vs prior-only controls, thin-tail/event-count adequacy.
2. Write a formal negative-results report `research_state/negative_results_report_v1.json` (+ md) documenting the anchor null, grid hits with dependence caveats, exclusions (336) and blocked states (0). Do not soften the null.
3. Update handoff and this task with red-team findings and the next concrete unblocked task.

## Boundary
Free public data only. No fabrication. Preserve null/failed/exclusions. Complete horizons only. Do not modify Q1 artifacts or the evaluation report.

## Commands
python3 scripts/generate_grid_manifest.py --output /tmp/basis-grid-manifest.json
python3 -m unittest discover -s tests -q
git diff --check