#!/usr/bin/env python3
"""
Frontier advance v45: ranks 1126-1150
Fetches fresh CoinPaprika /v1/coins, deduplicates against known-id union (v1-v44 = 1012 ids),
writes research_state/universe_frontier_advance_v45.json
"""
import json
import hashlib
import requests
from datetime import datetime, timezone
from pathlib import Path

v44_path = Path("research_state/universe_frontier_advance_v44.json")

def load_all_frontier_ids():
    """Load all known IDs from v1-v44 frontier artifacts"""
    known_ids = set()
    research_state = Path("research_state")

    master = research_state / "universe_frontier.json"
    if master.exists():
        with open(master) as f:
            data = json.load(f)
            for item in data.get("candidates", []):
                known_ids.add(item["id"])

    for i in range(1, 45):
        path = research_state / f"universe_frontier_advance_v{i}.json"
        if path.exists():
            with open(path) as f:
                data = json.load(f)
            for item in data.get("candidates_discovered_delta", []):
                known_ids.add(item["id"])
            for item in data.get("duplicates_skipped", []):
                known_ids.add(item["id"])

    return known_ids

known_ids = load_all_frontier_ids()
print(f"Reconstructed known-id union (v1-v44): {len(known_ids)} ids")
assert len(known_ids) == 1012, f"Expected 1012 known IDs, got {len(known_ids)}"

url = "https://api.coinpaprika.com/v1/coins"
print(f"Fetching {url}...")
response = requests.get(url, timeout=30)
response.raise_for_status()

retrieved_at = datetime.now(timezone.utc).isoformat().replace('+00:00', 'Z')
raw_bytes = response.content
response_sha256 = hashlib.sha256(raw_bytes).hexdigest()
data = response.json()

total_items = len(data)
ranked_items = [item for item in data if item.get("rank") and item["rank"] >= 1]
ranked_items_count = len(ranked_items)

print(f"Total items: {total_items}, Ranked items (rank>=1): {ranked_items_count}")

ranked_items.sort(key=lambda x: x["rank"])

window_items = [item for item in ranked_items if 1126 <= item["rank"] <= 1150]
print(f"Items in rank window 1126-1150: {len(window_items)}")

candidates_delta = []
duplicates_skipped = []
symbol_collisions = []
seen_symbols = {}

for item in window_items:
    item_id = item["id"]
    rank = item["rank"]
    name = item["name"]
    symbol = item["symbol"]

    if item_id in known_ids:
        duplicates_skipped.append({
            "id": item_id,
            "rank": rank,
            "reason": "already in known-id union"
        })
    else:
        if symbol in seen_symbols:
            symbol_collisions.append({
                "symbol": symbol,
                "ids": [seen_symbols[symbol], item_id],
                "ranks": [next(c["rank"] for c in candidates_delta if c["id"] == seen_symbols[symbol]), rank]
            })
        else:
            seen_symbols[symbol] = item_id

        candidates_delta.append({
            "id": item_id,
            "rank": rank,
            "name": name,
            "symbol": symbol,
            "status": "rank_unverified_discovery_only"
        })
        known_ids.add(item_id)

print(f"Net new candidates: {len(candidates_delta)}")
print(f"Duplicates skipped: {len(duplicates_skipped)}")
print(f"Symbol collisions: {len(symbol_collisions)}")

with open(v44_path) as f:
    v44 = json.load(f)

window_populated = len(window_items)
window_note = (
    f"Rank window 1126-1150 was fully populated ({window_populated}/25) so the batch is complete; "
    "the ranked-count change is recorded as a source-behavior observation, not a gap."
    if window_populated == 25
    else
    f"Rank window 1126-1150 had {window_populated} items (25 ranks); the window was not fully populated "
    "(expected 25), recorded as a source-behavior observation."
)

artifact = {
    "artifact_id": "EBCR-001-UNIVERSE-FRONTIER-ADVANCE-V45",
    "schema_version": "1.0",
    "program_id": "EBCR-001",
    "created_at_utc": retrieved_at,
    "task_activation": 3395,
    "purpose": "Advance rank frontier discovery batch (ranks 1126-1150) after documented cooldown since v44 (v44 retrieval 2026-11-26T22:56:55Z; cooldown ~3.5h; current retrieval past deadline). Discovery-only; NOT PIT membership/rank.",
    "prior_artifact": {
        "path": "universe_frontier_advance_v44.json",
        "sha256_raw_bytes": "0a4201ba4cb75bd14ce8cc9f53d722c1533d44d45024f5c05e32cc8c590b11f6",
        "sha256_compact_content": "a505ed1a1405ceefed47c39890b725496efa22bc1ee2517617c3be9f754a6728",
        "discovered_id_count_v44": 1012,
        "top_rank_covered_v44": 1125,
        "next_batch_start_rank_v44": 1126
    },
    "source": {
        "name": "CoinPaprika public API",
        "endpoint": "https://api.coinpaprika.com/v1/coins",
        "retrieved_at_utc": retrieved_at,
        "response_sha256": response_sha256,
        "total_items_in_response": total_items,
        "ranked_items_in_response": ranked_items_count,
        "note": f"Current market-cap ranking for candidate discovery only; NOT historical PIT membership/rank. /v1/coins items carry an integer rank field but the response is not pre-sorted by rank; items were sorted by rank before window selection. Raw response not stored in-repo; only its checksum is recorded. Fresh retrieval at activation 3395, past the ~3.5h cooldown since v44 retrieval at 2026-11-26T22:56:55Z. Source observation: ranked_items_in_response (rank>=1) = {ranked_items_count} at this retrieval vs 11035 at v44, 11306 at v43 and 11588 at v42; total_items_in_response = {total_items} (v44: 62812). {window_note}"
    },
    "frontier_state": {
        "rank_window_scanned": [1126, 1150],
        "known_ids_before_dedup": 1012,
        "items_in_rank_window": len(window_items),
        "net_new_candidates": len(candidates_delta),
        "duplicates_skipped_count": len(duplicates_skipped),
        "symbol_collisions_count": len(symbol_collisions)
    },
    "discovery_method": "Set-difference deduplication by stable CoinPaprika asset id against the reconstructed v1-v44 observed-id union = 1012 known ids (25-id universe_frontier.json master frontier plus all v1-v44 delta entries). Current ranks used for discovery ordering only; status rank_unverified_discovery_only.",
    "candidates_discovered_delta": candidates_delta,
    "duplicates_skipped": duplicates_skipped,
    "symbol_collisions": symbol_collisions,
    "cursor": {
        "discovered_id_count": 1012 + len(candidates_delta),
        "top_rank_covered": 1150,
        "next_batch_start_rank": 1151,
        "next_batch_end_rank": 1175,
        "rank_frontier_exhausted": False
    }
}

output_path = Path("research_state/universe_frontier_advance_v45.json")
with open(output_path, "w") as f:
    json.dump(artifact, f, indent=2)

print(f"Artifact written to {output_path}")

compact_artifact = {k: v for k, v in artifact.items() if k not in ("artifact_id", "created_at_utc", "task_activation")}
compact_bytes = json.dumps(compact_artifact, sort_keys=True, separators=(',', ':')).encode()
compact_sha256 = hashlib.sha256(compact_bytes).hexdigest()
raw_sha256 = hashlib.sha256(json.dumps(artifact, indent=2).encode()).hexdigest()
print(f"Artifact raw sha256: {raw_sha256}")
print(f"Artifact compact content sha256: {compact_sha256}")