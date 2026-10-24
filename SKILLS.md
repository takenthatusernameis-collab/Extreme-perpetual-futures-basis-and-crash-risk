# Research skills index

Load the matching skill for the task; keep this file as an index rather than duplicating full procedures.

- `.agents/skills/basis-crash-risk-research/SKILL.md` — preregister and evaluate the basis-to-crash hypothesis; use for any experiment or interpretation.
- `.agents/skills/point-in-time-universe/SKILL.md` — discover candidates in descending market-cap rank and construct defensible historical universe membership; use for sourcing and lifecycle work.
- `.agents/skills/statistical-red-team/SKILL.md` — audit leakage, overlapping horizons, multiplicity, survivorship and sparse-tail inference; use before accepting results.
- `.agents/skills/resumable-research-operations/SKILL.md` — checkpoint experiments, handle failures, version artifacts and write handoffs; use for each autonomous activation.

## General procedure
Discovery: choose the skill by its name/description. Activation: read the complete `SKILL.md`. Execution: use only referenced scripts and data that the skill explicitly requires. Skills define procedures; GitHub Actions, public HTTP APIs and local scripts provide execution and data access. Never assume an optional dependency, paid service or secret exists.
