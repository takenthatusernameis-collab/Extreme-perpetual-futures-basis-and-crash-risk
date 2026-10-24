# Architecture

## Layers
- **Instruction:** short always-on invariants in `AGENTS.md`, with procedures indexed by `SKILLS.md` and loaded from atomic `SKILL.md` files.
- **Specification:** the operating contract defines hypotheses, signal, outcomes, splits, inference, gates and continuity rules.
- **Experiment:** the JSON grid is the immutable source of truth; a deterministic generator emits stable IDs and parameter hashes.
- **Data:** source snapshots, normalized time series, point-in-time instrument mapping, coverage reports and provenance.
- **Inference:** registered estimators, multiplicity correction, block uncertainty and red-team checks.
- **State:** frontier, hypothesis registry, run manifest and handoff make sessions resumable.
- **Automation:** the scheduled workflow tests changes, collects diagnostics, invokes the free model route, checkpoints repo changes and preserves recovery evidence.

## Data flow
```text
free market-cap sources (descending discovery rank)
  -> candidate frontier + raw hashes
  -> PIT rank, lifecycle, spot/index and perpetual mapping
  -> timestamp and coverage gates
  -> frozen 324-cell manifest (stable IDs + hashes)
  -> development grid and anchor-only validation/holdout
  -> block-aware estimates + full-family correction
  -> immutable artifacts + registry/frontier/handoff
  -> next evidence-led task
```

## Storage rules
Keep small derived reports/manifests in Git. Use permitted free workflow artifacts or source links for bulky data. Never commit private credentials or uncontrolled raw caches. Every result must be reproducible from code revision, immutable config, source cutoff and input hashes. Missing results are not evidence of no effect; record why data or tests were unavailable.
