# Evidence audit: exclusion accounting (n=336) vs integrated row counts

Audit date (UTC): 2026-11-13T23:10:00Z
Program: EBCR-001
Activation: 2941
Scope: option (C) extension requested in the activation-2940 task message.

## Scope

Audit of the exclusion ledger in `research_state/integrated_extended_v1.json` (n_exclusions = 336)
against the upstream basis and label ledgers, the per-symbol row counts, and the join fidelity of the
5,010 analysis rows. Verifies that no observation is silently omitted or synthesized and that the
exclusion reason taxonomy is accurate. No frozen artifact, config, anchor, prior result, or
evaluation report was modified.

## Artifacts audited

- `research_state/basis_computation_extended_v1.json` (basis stage; n_computations = 5,346)
- `research_state/crash_labels_extended_v1.json` (label stage; n_basis_obs = 5,318, n_exclusions = 308, n_labels_ok = 5,010)
- `research_state/integrated_extended_v1.json` (integration; n_basis_obs = 5,346, n_rows = 5,010, n_exclusions = 336)
- `research_state/evaluation_report_extended_v1.json` (n_recorded_exclusions = 336; recorded_exclusion_reasons = ["missing_label"])

## Reconciliation result

The exclusion ledger is arithmetically complete and consistent at the integration stage:

| Quantity | Value |
|---|---|
| Basis computations | 5,346 |
| Label-stage `ok` basis observations (n_basis_obs) | 5,318 |
| Label-stage exclusions (`incomplete_forward_horizon`) | 308 |
| Labels OK (n_labels_ok) | 5,010 |
| Integration rows | 5,010 |
| Integration exclusions (n_exclusions) | 336 |

Verified identities:

- `5,346 = 5,010 + 336` (basis observations = rows + exclusions). ✔
- `5,318 = 5,010 + 308` (label stage). ✔
- Integrated exclusion set **exactly equals** the disjoint union of
  `basis_incomplete` (28) and `label_incomplete` (308): set difference both directions = 0; overlap = 0. ✔
- Row key set (5,010) equals the label `ok` key set (5,010); no duplicate row keys; no row key appears
  in the exclusion set. ✔
- Join fidelity: all 5,010 rows match the label file's `mae` (h7/h14/h28) exactly (0 mismatches) and the
  basis file's `basis_pct` exactly (0 mismatches). ✔
- No forward fill / no synthesized rows: for every symbol the count of missing calendar days between the
  first and last row date equals the number of `basis_incomplete` observations for that symbol. ✔

## Per-symbol decomposition

| symbol | rows | basis_incomplete | label_incomplete | total_excl | basis_obs |
|---|---|---|---|---|---|
| ADAUSDT | 455 | 3 | 28 | 31 | 486 |
| BCHUSDT | 455 | 3 | 28 | 31 | 486 |
| BNBUSDT | 451 | 7 | 28 | 35 | 486 |
| DOGEUSDT | 456 | 2 | 28 | 30 | 486 |
| LINKUSDT | 456 | 2 | 28 | 30 | 486 |
| NEARUSDT | 456 | 2 | 28 | 30 | 486 |
| SOLUSDT | 456 | 2 | 28 | 30 | 486 |
| TRXUSDT | 456 | 2 | 28 | 30 | 486 |
| XLMUSDT | 457 | 1 | 28 | 29 | 486 |
| XRPUSDT | 455 | 3 | 28 | 31 | 486 |
| ZECUSDT | 457 | 1 | 28 | 29 | 486 |
| **TOTAL** | **5,010** | **28** | **308** | **336** | **5,346** |

## Audit finding: exclusion reason taxonomy conflates two exclusion causes

`integrated_extended_v1.json` labels **all 336** exclusions with the single reason `missing_label`,
and `evaluation_report_extended_v1.json` inherits `recorded_exclusion_reasons = ["missing_label"]`.

In fact the 336 comprise two distinct upstream causes:

1. **28 `basis_incomplete` observations** — present in the basis file with `status != "ok"`
   (missing component coverage). These were dropped **before** the label stage and never appear in
   `crash_labels_extended_v1.json` (neither as a label nor as an exclusion). They are not "missing
   labels"; the label was never computed because the basis input was incomplete.
2. **308 `incomplete_forward_horizon` observations** — genuine label-stage exclusions, correctly
   recorded in `crash_labels_extended_v1.json` (forward horizon not fully closed).

Consequences (documentation-level, not result-level):

- The field `n_basis_obs` means different things across stages: 5,346 at the basis/integration stage
  vs 5,318 at the label stage. This is internally consistent (28 basis-incomplete dropped before labels)
  but is not documented in the integrated file.
- The integrated exclusion reason string `missing_label` misattributes the 28 basis-incomplete
  exclusions. The more accurate decomposition is 28 `basis_incomplete` + 308 `incomplete_forward_horizon`.

Impact on results: **none.** The anchor and all cell estimates are computed only from the 5,010 joined
rows; exclusions are never used as data. The primary anchor null is unaffected. This is an
evidence-labeling precision issue, preserved here as an audit finding rather than edited into the frozen
integrated artifact.

## Invariant checks

- exclusions n = 336: preserved (reconciled as 28 + 308; total unchanged)
- Anchor co-primary crash_incidence_15pct adj p = 0.24830545694889028: preserved (unaffected; rows-only)
- Anchor co-primary expected_shortfall_5pct_forward_mae adj p = 0.9485: preserved
- PIT rank: CLOSED
- EBCR-H001 `tested_not_supported`; EBCR-H002/H003/H004 `registered_secondary_not_tested`; next_hypothesis_sequence 5
- No frozen artifact, config, anchor, integrated file, evaluation report, or upstream ledger modified
- `git diff --check` clean; 18 pytest tests pass; manifest 324 cells / canonical sha256 55caedf… verified

## Conclusion

The exclusion accounting is **complete and correct at the total level**: 5,346 = 5,010 + 336, with no
silent omissions, no double counting, no forward fill, and exact label/basis join fidelity. The only
defect is presentational: the single `missing_label` reason conflates 28 `basis_incomplete` drops with
308 `incomplete_forward_horizon` label exclusions. No result changes. Recommend that any future
integration-stage regeneration (new experiment ID, not this frozen artifact) carry a two-level reason
taxonomy (`basis_incomplete` vs `incomplete_forward_horizon`) and report per-stage `n_basis_obs`
explicitly.