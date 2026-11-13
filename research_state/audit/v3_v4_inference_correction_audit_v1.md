# Evidence audit: V3→V4 inference correction — EBCR-H004 controlled re-estimation

Audit date (UTC): 2026-11-13T23:00:00Z
Program: EBCR-001
Activation: 2939

## Scope

Audit of the V3→V4 inference correction for EBCR-H004 controlled re-estimation. Confirms V4 output reproducibility from preregistration, verifies panel statistics against preregistration, and documents the V3 inference bug as a preserved red-team finding. No frozen artifacts, configs, or V3 outputs modified.

## Artifacts audited

- Preregistration: `research_state/h004_controlled_rereg_v2.json` (sha256 ef53d9f8f9c7cf18389560c263b5495e2eeea2e3b11c223943608320c6316364)
- V4 output JSON: `research_state/robustness_controlled_v4.json`
- V4 output MD: `research_state/robustness_controlled_v4.md`
- V4 script: `scripts/robustness_controlled_v4.py`
- V3 output JSON (preserved): `research_state/robustness_controlled_v3.json`
- V3 output MD (preserved): `research_state/robustness_controlled_v3.md`
- V3 preregistration (preserved): `research_state/h004_controlled_rereg_v1.json`

## Reproduction check

Command: `.venv/bin/python scripts/robustness_controlled_v4.py`
Result: reproduces `research_state/robustness_controlled_v4.json` and `.md` with identical Holm results:
- crash_incidence_15pct controlled cluster p = 0.4931717622839955 (Holm threshold 0.05, not significant)
- expected_shortfall_5pct_forward_mae controlled cluster p = 0.4571603439994524 (Holm threshold 0.025, not significant)

Panel confirmed: 4014 obs, 11 symbols, 156 clusters, exclusions preserved n=336.
Integrated source sha256: 8c826687da2fa91ce45313189dee24cedaa279348934ca8f1f910b1c07f00707 (matches V4 output and preregistration data_source).
Frozen config sha256: 55caedf84ac723289f70f49bbed4712c8195425feb4a95e737f3e8929479a0e0 (matches config canonical).

## Red-team finding: V3 inference bug (preserved evidence, not deleted)

V3 experiment `EBCR-001-ROBUST-CTRL-V3` used a hand-rolled `cluster_robust_se` with bread `(X'X)^-1` for both OLS and Logit. That bread matrix is misspecified for Logit (inverse Hessian of the log-likelihood is required).

V3 vs V4 comparison — crash_incidence_15pct controlled:
| Metric | V3 (invalid) | V4 (corrected) |
|---|---|---|
| Cluster SE | 0.0336 | 0.2663 |
| Cluster p-value | 5.65e-08 | 0.4932 |
| Holm threshold | 0.025 | 0.05 |
| Holm significant | TRUE | FALSE |
| Model-based SE p (reference) | 0.3118 | N/A |

V3's Holm-significant claim (p=5.65e-08) was invalid; the SE was understated ~8x. The model-based p-value V3 also reported (0.3118) was consistent with V4's corrected cluster result (p=0.4932) — both not significant. V3 outputs are preserved untouched as evidence; the invalid claim is documented as corrected, not deleted.

V3 vs V4 comparison — expected_shortfall_5pct_forward_mae controlled:
| Metric | V3 | V4 |
|---|---|---|
| Cluster SE | 0.00649 | 0.00649 |
| Cluster p-value | 0.4572 | 0.4572 |
| Holm significant | FALSE | FALSE |

OLS inference was unaffected (same SE and p-value in both versions), consistent with the misspecification being Logit-specific.

## Invariant checks

- exclusions n = 336: preserved
- Anchor co-primary crash_incidence_15pct adj p = 0.24830545694889028: preserved
- Anchor co-primary expected_shortfall_5pct_forward_mae adj p = 0.9485: preserved
- PIT rank: CLOSED
- EBCR-H001 status: tested_not_supported
- EBCR-H002/H003/H004 status: registered_secondary_not_tested
- next_hypothesis_sequence: 5
- No frozen artifacts modified
- No V3 outputs modified
- New experiment ID and output paths only (V4)
- Preregistration written before computing outcomes

## Conclusion

The V3→V4 correction is confirmed: V4's statsmodels `cov_type='cluster'` (symbol-month) inference correctly replaces V3's misspecified hand-rolled bread. Null result preserved — EBCR-H004's robustness-to-controls claim is supported, no significance overturning H001. V3 outputs preserved as evidence of the corrected invalid claim.

## Next steps for audit directory

This is the first artifact in `research_state/audit/`. Recommended follow-up audits:
- Verify exclusion accounting (n=336) against integrated_extended_v1.json row counts
- Confirm contract listing/delisting/migration history evidence (pre-existing unresolved)
- Confirm data revision behavior evidence (pre-existing unresolved)
