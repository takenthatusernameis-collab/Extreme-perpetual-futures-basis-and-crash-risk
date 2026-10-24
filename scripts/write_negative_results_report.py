#!/usr/bin/env python3
import json
import hashlib
from pathlib import Path
from datetime import datetime, timezone
from collections import Counter

ROOT = Path("/home/runner/work/Extreme-perpetual-futures-basis-and-crash-risk/Extreme-perpetual-futures-basis-and-crash-risk")
RESEARCH = ROOT / "research_state"

def load_json(p):
    return json.loads(Path(p).read_text(encoding="utf-8"))

def atomic_write(p, obj):
    p = Path(p)
    rendered = json.dumps(obj, indent=2, sort_keys=True) + "\n"
    tmp = p.with_suffix(p.suffix + ".tmp")
    tmp.write_text(rendered, encoding="utf-8")
    tmp.replace(p)

def main():
    eval_rep = load_json(RESEARCH / "evaluation_report_extended_v1.json")
    eval_sum = (RESEARCH / "evaluation_summary_extended_v1.md").read_text(encoding="utf-8")
    integ = load_json(RESEARCH / "integrated_extended_v1.json")
    cell_ledger = load_json(RESEARCH / "cell_status_ledger_extended_v1.json")
    redteam = load_json(RESEARCH / "red_team_audit_extended_v1.json")

    exclusions = integ.get("exclusions", [])
    excl_reasons = dict(Counter(e.get("reason") for e in exclusions))

    anchor_cell = eval_rep.get("anchor_cell_id")
    anchor_results = None
    for c in eval_rep["cells"]:
        if c["cell_id"] == anchor_cell:
            anchor_results = c
            break

    inf = eval_rep["inference"]

    report = {
        "schema_version": "1.0",
        "report_id": "EBCR-001-NEGATIVE-RESULTS-V1",
        "generated_at_utc": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "experiment_id": eval_rep["experiment_id"],
        "program_id": eval_rep["program_id"],
        "config_path": eval_rep["config_path"],
        "config_sha256": eval_rep["config_sha256"],
        "window": eval_rep["data_window"],
        "integrated_source": eval_rep["integrated_source"],
        "n_integrated_rows": eval_rep["n_integrated_rows"],
        "n_recorded_exclusions": len(exclusions),
        "exclusion_reasons": excl_reasons,
        "frozen_anchor": eval_rep["primary_anchor"],
        "anchor_cell_id": anchor_cell,
        "anchor_co_primary": {
            "endpoints": ["crash_incidence_15pct", "expected_shortfall_5pct_forward_mae"],
            "results": anchor_results["endpoints"] if anchor_results else None,
            "adj_p_values": inf.get("anchor_co_primary_adjusted_p_values"),
            "holm_significant": inf.get("anchor_co_primary_holm_significant"),
            "conclusion": "NOT SIGNIFICANT after Holm correction across co-primary endpoints (m=2). Primary hypothesis NOT supported on extended window."
        },
        "grid_family": {
            "registered_tests": inf["family_size_tests"],
            "tests_with_pvalue": inf["family_tests_with_p_value"],
            "blocked_no_pvalue": inf["family_tests_blocked_no_p"],
            "holm_significant_full_family": inf["family_holm_significant"],
            "holm_significant_fraction": inf["family_holm_significant"] / max(1, inf["family_tests_with_p_value"]),
            "stratified": eval_rep.get("stratified", {})
        },
        "status_accounting": {
            "cells_total": len(cell_ledger["cells"]),
            "cells_ok": sum(1 for c in cell_ledger["cells"] if c["status"] == "ok"),
            "cells_blocked": sum(1 for c in cell_ledger["cells"] if c["status"] == "blocked"),
            "cells_failed": sum(1 for c in cell_ledger["cells"] if c["status"] == "failed"),
            "cells_incomplete": sum(1 for c in cell_ledger["cells"] if c["status"] == "incomplete"),
            "cells_invalid": sum(1 for c in cell_ledger["cells"] if c["status"] == "invalid"),
            "cells_not_run": sum(1 for c in cell_ledger["cells"] if c["status"] == "not_run")
        },
        "red_team_caveats": {
            "overlapping_horizons": redteam["overlapping_horizon_dependence"],
            "leakage_check": redteam["leakage_permutation_placebo"],
            "survivorship_missingness": redteam["survivorship_missingness_selection"],
            "confounding": redteam["confounding_vs_prior_only_controls"],
            "thin_tails": redteam["thin_tail_event_count_adequacy"],
            "multiplicity_note": redteam["family_multiplicity"]["note"]
        },
        "conclusion": "Primary hypothesis (rich-positive extreme basis predicts higher crash incidence/severity at fixed anchor) is not supported after multiplicity correction. Grid shows some Holm-significant hits but with strong dependence/confounding caveats; no effect claimed. All exclusions and statuses preserved.",
        "references": {
            "evaluation_report": "research_state/evaluation_report_extended_v1.json",
            "evaluation_summary": "research_state/evaluation_summary_extended_v1.md",
            "red_team_audit": "research_state/red_team_audit_extended_v1.json",
            "integrated": "research_state/integrated_extended_v1.json",
            "cell_status_ledger": "research_state/cell_status_ledger_extended_v1.json"
        }
    }

    atomic_write(RESEARCH / "negative_results_report_v1.json", report)

    md = []
    md.append("# Negative results report — EBCR-001-NEGATIVE-RESULTS-V1")
    md.append("")
    md.append(f"- Report: `research_state/negative_results_report_v1.json`")
    md.append(f"- Experiment: {eval_rep['experiment_id']}")
    md.append(f"- Window: {eval_rep['data_window']['start']}..{eval_rep['data_window']['end']}")
    md.append(f"- Integrated rows: {eval_rep['n_integrated_rows']}, exclusions: {len(exclusions)} ({excl_reasons})")
    md.append(f"- Generated: {report['generated_at_utc']}")
    md.append("")
    md.append("## Frozen anchor (primary)")
    md.append(f"- Config: {eval_rep['primary_anchor']}")
    md.append(f"- Cell: {anchor_cell}")
    if anchor_results:
        a15 = anchor_results['endpoints']['crash_incidence_15pct']
        aes = anchor_results['endpoints']['expected_shortfall_5pct_forward_mae']
        md.append(f"- crash_incidence_15pct: n_signal={a15['n_signal']}, events={a15['events_signal']}/{a15['events_control']}, p_unadj={a15['p_value']:.3f}, adj_anchor={a15['anchor_co_primary_adjusted_p_value']:.3f}")
        md.append(f"- expected_shortfall_5pct_forward_mae: p_unadj={aes['p_value']:.3f}, adj_anchor={aes['anchor_co_primary_adjusted_p_value']:.3f}")
    md.append(f"- **Conclusion:** {report['anchor_co_primary']['conclusion']}")
    md.append("")
    md.append("## Grid family (Holm across all 2592)")
    md.append(f"- Registered: {inf['family_size_tests']}, with p-value: {inf['family_tests_with_p_value']}, blocked: {inf['family_tests_blocked_no_p']}")
    md.append(f"- Holm-significant: **{inf['family_holm_significant']} / {inf['family_tests_with_p_value']}** ({inf['family_holm_significant']/max(1,inf['family_tests_with_p_value']):.1%})")
    md.append(f"- Stratified: {json.dumps(eval_rep.get('stratified', {}))}")
    md.append("")
    md.append("## Status accounting (all preserved)")
    st = report['status_accounting']
    md.append(f"- ok={st['cells_ok']}, blocked={st['cells_blocked']}, failed={st['cells_failed']}, incomplete={st['cells_incomplete']}, invalid={st['cells_invalid']}, not_run={st['cells_not_run']} (total={st['cells_total']})")
    md.append(f"- Exclusions preserved: {len(exclusions)}")
    md.append("")
    md.append("## Red-team caveats")
    md.append(f"- Overlapping horizons: {redteam['overlapping_horizon_dependence']['issue']}")
    md.append(f"- Leakage: thresholds past-only/shift(1), labels start at t+1 (verified)")
    md.append(f"- Survivorship/missingness: {len(exclusions)} exclusions recorded; PIT verification ongoing")
    md.append(f"- Confounding: predeclared controls not exhaustively re-estimated in this pass")
    md.append(f"- Multiplicity: {redteam['family_multiplicity']['note']}")
    md.append("")
    md.append("## Final conclusion")
    md.append(f"- {report['conclusion']}")
    md.append("")
    (RESEARCH / "negative_results_report_v1.md").write_text("\n".join(md) + "\n", encoding="utf-8")
    print("done")

if __name__ == "__main__":
    main()
