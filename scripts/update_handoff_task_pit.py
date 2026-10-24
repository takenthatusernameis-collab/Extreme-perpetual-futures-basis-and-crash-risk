#!/usr/bin/env python3
import json, os
from datetime import datetime, timezone

# Update handoff
handoff_path = "research_state/agent_handoff.md"
with open(handoff_path) as f:
    handoff = f.read()

# Add PIT hardening section if not present
if "PIT hardening" not in handoff:
    handoff += "\n## PIT hardening (this session)\n"
    handoff += "- Reviewed free sources for historical market-cap/rank (CoinMetrics catalog, CoinPaprika, web archives). No bulk free PIT rank history located; confirmed discovery-only.\n"
    handoff += "- Listing evidence collected via Binance Vision S3 XML for mapped symbols (earliest/latest zips where present). See research_state/pit_universe_verification_v1.json.\n"
    handoff += "- All mapped symbols marked rank_verified=false; coverage cohort approach required per point-in-time rules. No current ranks projected backward.\n"

with open(handoff_path, "w") as f:
    f.write(handoff)

# Update task message
task_path = "research_state/agent_task_message.md"
with open(task_path) as f:
    task = f.read()

task = "# Next task — EBCR-001\n\n"
task += "Read AGENTS.md, SKILLS.md, research_state/agent_handoff.md, prompts/continuous_research_operating_contract_v1.md, docs/research_protocol.md, configs/basis_crash_grid_v1.json.\n\n"
task += "## Context\n"
task += "- Extended evaluation complete: anchor null (adj p 0.248, 0.949), 424/2451 Holm-significant with dependence caveats.\n"
task += "- Red-team audit done; negative results report done.\n"
task += "- PIT verification: listing evidence collected via S3 XML; rank_verified=false for all (no free PIT rank history found). research_state/pit_universe_verification_v1.json.\n"
task += "- Prior-only controls (exploratory): null preserved.\n"
task += "- Exclusions 336 preserved; all 324 cells ok.\n\n"
task += "## Immediate deliverables\n"
task += "1. Continue PIT hardening: search free sources (archived rankings, snapshot datasets) for defensible PIT rank history. If found, record source/timestamp/checksum and update verification; else document explicit gaps and keep rank-unverified.\n"
task += "2. If investigating alternative orientation (cheap-negative/absolute-extreme), preregister separately with its own anchor/config (do not modify frozen anchor/config). Document rationale.\n"
task += "3. Update handoff/next task with verified findings only; preserve null/failed/exclusions.\n\n"
task += "## Boundary\n"
task += "Free public data only. No fabrication. Preserve null/failed/exclusions. Complete horizons only. Do not modify Q1 artifacts, evaluation reports, or the frozen anchor/config.\n\n"
task += "## Commands\n"
task += "python3 scripts/generate_grid_manifest.py --output /tmp/basis-grid-manifest.json\n"
task += "python3 -m unittest discover -s tests -q\n"
task += "git diff --check\n"

with open(task_path, "w") as f:
    f.write(task)

print("done")
