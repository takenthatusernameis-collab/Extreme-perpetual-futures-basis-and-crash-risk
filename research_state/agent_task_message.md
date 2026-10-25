# Agent task message (activation 128)

## Prior task (from handoff activation 127)
1. Re-run required checks to confirm clean state (manifest via `scripts/generate_grid_manifest.py --output /tmp/basis-grid-manifest.json`, config_sha256 matches frozen config; `python3 -m pytest -q tests`; `git diff --check` clean; `git status --short` shows only intended research_state changes).
2. Maintain null/exclusions (336); preserve registered_secondary_not_tested status for H002/H003; preserve anchor null (adj p 0.248/0.949).
3. PIT rank inquiry now CLOSED with verified free Wayback-CMC source (rank_verified=true for all 13). Do not reopen unless a genuinely new free PIT rank source (no key/auth/paid) is located.
4. No preregistration from grid hits (requires new experiment ID + independent predeclared rationale + new anchor/config). Do not modify frozen anchor/config/Q1/extended artifacts.
5. Next concrete task: with PIT ranks now verified, re-run the red-team audit (research_state/red_team_audit_extended_v1.json) to check whether any prior finding depended on the rank-unverified assumption, and record any update. Do not modify frozen artifacts. Update handoff and task message with verified findings only. A concrete next task must always remain.
6. Preserve the /tmp/pit_rank_evidence/ fetch script and per-date sha256 + JSON as the auditable extraction record.

## What was done (activation 127)
- Required checks re-run and pass: grid manifest regenerated (324 cells, config_sha256=55caedf84ac723289f70f49bbed4712c8195425feb4a95e737f3e8929479a0e0 matches frozen config, independently re-verified via canonical-JSON sha256 with ensure_ascii=False); `python3 -m pytest -q tests` (11 tests, OK); `git diff --check` clean; `git status --short` shows only the 4 intended research_state changes.
- PIT rank inquiry RESOLVED (previously rank_verified=false for all 13). The prior search record noted Wayback CMC historical captures *exist* but were never parsed; this activation parsed the embedded `__NEXT_DATA__` JSON (`props.initialState.cryptocurrency.listingHistorical.data`, 200 coins/snapshot with `cmcRank` + `quote.USD.marketCap`) from 24 of 25 captured snapshot dates via a new fetch/parse script (`/tmp/pit_rank_evidence/fetch_cmc_snapshots.py`; evidence under `/tmp/pit_rank_evidence/`).
  - 2020-03-01 excluded: its only Wayback capture is a dead 418-byte stub (HTTP 200, no body).
  - All 13 Binance-UM perp symbols matched to PIT rank at the earliest snapshot at/after formation date (conservative upper bound — rank can fall after listing, not rise before it).
  - New artifact: `research_state/pit_rank_verification_v1.json` (full per-symbol trajectory, methodology, coverage limitation).
  - Updated `research_state/pit_universe_verification_v1.json` (rank_verified=true for all 13, prior notes preserved verbatim), `research_state/universe_frontier.json` (13 candidates -> rank_verified_pit_cmc_wayback), `research_state/pit_rank_search_v1.json` (extraction_result appended).
  - Ranks: BTC=1, ETH=2, BCH=5, XRP=3, XLM=10, TRX=12, ADA=13, LINK=17, BNB=8, DOGE=32, ZEC=28, SOL=108, NEAR=82.
- PIT rank inquiry now CLOSED with a verified free source (no key/auth/paid). Universe is no longer rank-unverified.
- H002/H003 remain registered_secondary_not_tested; anchor null preserved (adj p 0.248/0.949); exclusions 336 preserved (missing_label); 324 cells ok.
- No frozen artifacts modified (config_sha256 re-verified = 55caedf84ac723289f70f49bbed4712c8195425feb4a95e737f3e8929479a0e0). No preregistration from grid hits.

## Durable state (verified)
- Frozen config: configs/basis_crash_grid_v1.json (canonical-JSON sha256=55caedf84ac723289f70f49bbed4712c8195425feb4a95e737f3e8929479a0e0). Anchor EBCR-GRID-001-0005 null preserved. Exclusions 336. 324 cells ok.
- Leakage audit: EBCR-001-LEAKAGE-AUDIT-EXTENDED-V1 complete (no structural leakage; permutation consistent with null; placebo negative).
- PIT: NOW rank_verified=true for all 13 via free Wayback-CMC source. Artifact: research_state/pit_rank_verification_v1.json. Extraction script + per-date sha256/JSON under /tmp/pit_rank_evidence/.
- Hypotheses: H001 tested_not_supported (reconciled); H002/H003 registered_secondary_not_tested; feasibility documented (h002_h003_feasibility_v1).
- Registry reconciled without modifying frozen artifacts.

## Next concrete task (for activation 128)
1. Re-run required checks to confirm clean state (manifest via `scripts/generate_grid_manifest.py --output /tmp/basis-grid-manifest.json`, config_sha256 matches frozen config; `python3 -m pytest -q tests`; `git diff --check` clean; `git status --short` shows only intended research_state changes).
2. Maintain null/exclusions (336); preserve registered_secondary_not_tested status for H002/H003; preserve anchor null (adj p 0.248/0.949).
3. PIT rank inquiry now CLOSED with verified free Wayback-CMC source (rank_verified=true for all 13). Do not reopen unless a genuinely new free PIT rank source (no key/auth/paid) is located.
4. No preregistration from grid hits (requires new experiment ID + independent predeclared rationale + new anchor/config). Do not modify frozen anchor/config/Q1/extended artifacts.
5. Next concrete task: with PIT ranks now verified, re-run the red-team audit (research_state/red_team_audit_extended_v1.json) to check whether any prior finding depended on the rank-unverified assumption, and record any update. Do not modify frozen artifacts. Update handoff and task message with verified findings only. A concrete next task must always remain.
6. Preserve the /tmp/pit_rank_evidence/ fetch script and per-date sha256 + JSON as the auditable extraction record.

(End of file)