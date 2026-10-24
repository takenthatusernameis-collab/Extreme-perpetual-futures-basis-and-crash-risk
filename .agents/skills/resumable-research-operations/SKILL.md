---
name: resumable-research-operations
description: Execute long-running quantitative research with immutable IDs, bounded retries, complete cell ledgers and durable handoffs. Use for every session; never promise uninterrupted uptime or suppress failures.
---

# Resumable research operations

1. Read the task/handoff, grid manifest, frontier, registry, run ledger and recent workflow diagnostics.
2. Choose the highest-value unblocked task. Allocate a unique ID from the registry and preregister config/hash before calculating outcomes.
3. Run deterministic tests and source-coverage checks first. Refresh free public data only. Checkpoint bounded asset cohorts or grid batches.
4. Record each cell's stable ID, parameter hash, data cutoff, input hashes, code revision, status, reason, outputs and timestamps.
5. Use explicit timeouts, bounded retries, backoff for rate limits, atomic writes and idempotent resume. A failed cell must not erase completed cells or block unrelated work.
6. Never rerun a completed cell against silently changed inputs. New code/data/config requires a new version and output path.
7. Before committing, run tests, validate JSON/JSONL, inspect changed paths, run whitespace checks and confirm no secrets are staged.
8. Update handoff, next task, frontier, registry and run manifest as appropriate. Leave a concrete measurable next action.
9. Distinguish completed, attempted, blocked, failed, incomplete and not-run tasks. Workflow success proves automation health only, not an economic edge.
