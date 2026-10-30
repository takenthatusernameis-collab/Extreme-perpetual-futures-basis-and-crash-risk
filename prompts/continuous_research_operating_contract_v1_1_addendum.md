# Operational amendment v1.1 — state-change-driven continuation

This amendment changes only agent activation cadence. The v1 research design, 324-cell grid, eight endpoint family, holdout rules, PIT requirements, outcome definitions, and inference gates remain frozen.

## Activation gate
Before running the required checks or creating an upkeep artifact, compare the current state with the last verified durable-upkeep artifact:
- canonical grid/config hash;
- hypothesis registry and candidate frontier hashes/cursors;
- raw-data/source snapshot and exclusion-ledger hashes;
- code/test hashes;
- audit and open-blocker set.

If all relevant identities are unchanged and no external event has occurred, classify the activation as NO-OP. In that case:
- do not regenerate and compare the grid manifest just to re-assert the same 324 cells;
- do not rerun the full unittest/pytest suite if code/tests are unchanged;
- do not create the next numbered durable_state_upkeep artifact;
- do not rewrite the handoff or next-task message solely to refresh timestamps;
- do not create a checkpoint commit;
- exit with the previous verified state intact.

## Meaningful trigger
Run the targeted checks only when their inputs change. Run the complete required integrity/test checks and create a new upkeep artifact only after a material code/config/data/frontier/registry/audit change, newly available admissible source data, an actual hypothesis-state transition, or a documented integrity concern.

A source failure must not be re-probed on every activation. Recheck only after its documented cooldown or a meaningful provider/source/network change. Do not create tight polling loops.

## Work while blocked
When a real external gate remains closed, use available independent, permitted tasks that do not contaminate frozen evidence. If none exists, exit without manufacturing a test, audit, artifact, or score change.

## Hard boundary
Never shorten full-history or complete-horizon requirements, open/reuse a holdout, substitute current ranks for historical PIT ranks, alter the frozen grid/anchor, add outcome-informed hypotheses, fabricate/backfill data, or claim progress from green workflow status alone. The amendment removes repeated housekeeping, not research rigor.
