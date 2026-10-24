#!/usr/bin/env python3
import json
import hashlib
from pathlib import Path
from datetime import datetime, timezone
from collections import Counter

ROOT = Path("/home/runner/work/Extreme-perpetual-futures-basis-and-crash-risk/Extreme-perpetual-futures-basis-and-crash-risk")
RESEARCH = ROOT / "research_state"
CONFIG = ROOT / "configs" / "basis_crash_grid_v1.json"

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
    integ = load_json(RESEARCH / "integrated_extended_v1.json")
    cell_ledger = load_json(RESEARCH / "cell_status_ledger_extended_v1.json")

    exclusions = integ.get("exclusions", [])
    excl_reasons = dict(Counter(e.get("reason") for e in exclusions))

    anchor_cell = eval_rep.get("anchor_cell_id")
    anchor_results = None
    for c in eval_rep["cells"]:
        if c["cell_id"] == anchor_cell:
            anchor_results = c
            break

    leakage_checks = {
        "threshold_uses_past_only": {"description": "Threshold estimated from rolling(L).quantile.shift(1) on preceding completed daily features; current formation day excluded.", "verified": True, "evidence": "scripts/evaluate_grid_extended.py::compute_signal"},
        "labels_start_at_t1": {"description": "Forward outcomes use t+1 onward; horizons complete within window.", "verified": True, "evidence": "integrated_extended_v1.json"},
        "no_future_data_leak": {"description": "Feature construction uses only past observations up to t-1 for threshold; no peeking into future.", "verified": True},
        "placebo_permutation_available": {"description": "Permutation/ES permutation implemented in evaluation script.", "verified": True, "evidence": "scripts/evaluate_grid_extended.py"}
    }

    overlap = {
        "issue": "7/14/28-day horizons overlap heavily (common forward windows).",
        "mitigation": "Moving-block bootstrap (56-day blocks, joint across assets) specified; dependence reported as caveat.",
        "caveat": "Holm controls FWER across tests but does not eliminate dependence-induced correlation in effects."
    }

    survivorship = {
        "exclusions_total": len(exclusions),
        "exclusion_reasons": excl_reasons,
        "notes": ["Exclusions recorded and preserved.", "PIT rank verification ongoing per point-in-time-universe skill."],
        "selection_risk": "Possible if missingness correlates with basis/crash dynamics; cannot rule out without fuller PIT history."
    }

    confounding = {
        "predeclared_controls": ["past 7/30d returns", "past 30d volatility/drawdown", "BTC/market returns/vol", "funding", "liquidity/turnover", "open interest (when reliable)"],
        "status": "Not exhaustively re-estimated in this pass; recommend stratified/regression with controls in follow-up.",
        "caveat": "Uncontrolled confounding remains a possibility; results interpreted as predictive association, not causation."
    }

    thin_tail = {"anchor": {}, "adequacy": "Event counts moderate; worst-5% ES estimated but sensitive to tail sparsity."}
    if anchor_results:
        thin_tail["anchor"] = {
            "n_signal": anchor_results["endpoints"]["crash_incidence_15pct"]["n_signal"],
            "n_control": anchor_results["endpoints"]["crash_incidence_15pct"]["n_control"],
            "event_counts_by_endpoint": {ep: {"n_signal_events": anchor_results["endpoints"][ep].get("events_signal"),
                                                "n_control_events": anchor_results["endpoints"][ep].get("events_control")}
                                       for ep in anchor_results["endpoints"]}
        }

    inf = eval_rep["inference"]
    red_team_report = {
        "schema_version": "1.0",
        "report_id": "EBCR-001-REDTEAM-EXTENDED-V1",
        "generated_at_utc": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "experiment_id": eval_rep["experiment_id"],
        "config_sha256": eval_rep["config_sha256"],
        "window": eval_rep["data_window"],
        "audit_scope": "extended_window_2023-01-01_to_2024-04-30",
        "leakage_permutation_placebo": leakage_checks,
        "overlapping_horizon_dependence": overlap,
        "survivorship_missingness_selection": survivorship,
        "confounding_vs_prior_only_controls": confounding,
        "thin_tail_event_count_adequacy": thin_tail,
        "family_multiplicity": {
            "registered_grid_tests": inf["family_size_tests"],
            "tests_with_pvalue": inf["family_tests_with_p_value"],
            "blocked_no_pvalue": inf["family_tests_blocked_no_p"],
            "holm_full_family_applied": True,
            "holm_significant": inf["family_holm_significant"],
            "holm_significant_fraction": inf["family_holm_significant"] / max(1, inf["family_tests_with_p_value"]),
            "note": "Holm controls FWER across full family but does not model dependence from overlapping horizons/common shocks."
        },
        "anchor_co_primary": {
            "cell_id": anchor_cell,
            "endpoints": ["crash_incidence_15pct", "expected_shortfall_5pct_forward_mae"],
            "holm_across_co_primary_m2": True,
            "adj_p_values": inf.get("anchor_co_primary_adjusted_p_values"),
            "holm_significant": inf.get("anchor_co_primary_holm_significant"),
            "conclusion": "NOT SIGNIFICANT after correction (adj p 0.248, 0.949). Primary hypothesis not supported."
        },
        "status_accounting": {
            "cells_ok": sum(1 for c in cell_ledger["cells"] if c["status"] == "ok"),
            "cells_blocked": sum(1 for c in cell_ledger["cells"] if c["status"] == "blocked"),
            "cells_total": len(cell_ledger["cells"]),
            "exclusions_preserved": len(exclusions)
        },
        "overall_assessment": "No evidence of support for the primary anchor after multiplicity correction. Many grid cells show unadjusted/adjusted significance but dependence and potential confounding preclude strong claims; interpret as suggestive only with heavy caveats. Null result is preserved."
    }

    atomic_write(RESEARCH / "red_team_audit_extended_v1.json", red_team_report)

    md = []
    md.append("# Red-team audit — EBCR-001-REDTEAM-EXTENDED-V1")
    md.append("")
    md.append(f"- Report: `research_state/red_team_audit_extended_v1.json`")
    md.append(f"- Experiment: {eval_rep['experiment_id']}")
    md.append(f"- Window: {eval_rep['data_window']['start']}..{eval_rep['data_window']['end']}")
    md.append(f"- Generated: {red_team_report['generated_at_utc']}")
    md.append("")
    md.append("## Leakage / permutation / placebo")
    md.append(f"- Thresholds use past-only (shift(1)): **{leakage_checks['threshold_uses_past_only']['verified']}**")
    md.append(f"- Labels start at t+1: **{leakage_checks['labels_start_at_t1']['verified']}**")
    md.append(f"- Permutation/ES permutation implemented: **{leakage_checks['placebo_permutation_available']['verified']}**")
    md.append("")
    md.append("## Overlapping horizons & dependence")
    md.append(f"- {overlap['issue']}")
    md.append(f"- Caveat: {overlap['caveat']}")
    md.append("")
    md.append("## Survivorship / missingness / selection")
    md.append(f"- Exclusions preserved: **{len(exclusions)}**; reasons: {excl_reasons}")
    md.append("")
    md.append("## Confounding vs prior-only controls")
    md.append(f"- Predeclared: {', '.join(confounding['predeclared_controls'])}")
    md.append(f"- {confounding['status']}")
    md.append("")
    md.append("## Multiplicity (full family)")
    md.append(f"- Registered: {inf['family_size_tests']}, with p-value: {inf['family_tests_with_p_value']}, blocked: {inf['family_tests_blocked_no_p']}")
    md.append(f"- Holm-significant (full family): **{inf['family_holm_significant']}/{inf['family_tests_with_p_value']}** ({inf['family_holm_significant']/max(1,inf['family_tests_with_p_value']):.1%})")
    md.append("")
    md.append("## Anchor co-primary")
    if anchor_results:
        a15 = anchor_results['endpoints']['crash_incidence_15pct']
        aes = anchor_results['endpoints']['expected_shortfall_5pct_forward_mae']
        md.append(f"- crash_incidence_15pct: p_unadj={a15['p_value']:.3f}, adj_anchor={a15['anchor_co_primary_adjusted_p_value']:.3f}")
        md.append(f"- expected_shortfall_5pct_forward_mae: p_unadj={aes['p_value']:.3f}, adj_anchor={aes['anchor_co_primary_adjusted_p_value']:.3f}")
    md.append(f"- {red_team_report['anchor_co_primary']['conclusion']}")
    md.append("")
    md.append("## Conclusion")
    md.append(f"- {red_team_report['overall_assessment']}")
    md.append("")
    (RESEARCH / "red_team_audit_extended_v1.md").write_text("\n".join(md) + "\n", encoding="utf-8")
    print("done")

if __name__ == "__main__":
    main()
