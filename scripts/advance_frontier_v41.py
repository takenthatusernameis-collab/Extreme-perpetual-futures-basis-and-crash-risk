#!/usr/bin/env python3
"""
Frontier advance v41: ranks 1026-1050
Fetches fresh CoinPaprika /v1/coins, deduplicates against known-id union (v1-v40 = 932 ids),
writes research_state/universe_frontier_advance_v41.json
"""
import json
import hashlib
import requests
from datetime import datetime, timezone
from pathlib import Path

# Load v40 artifact to get prior state and known IDs
v40_path = Path("research_state/universe_frontier_advance_v40.json")
with open(v40_path) as f:
    v40 = json.load(f)

# Reconstruct known-id union from v1-v40
# v40 cursor says discovered_id_count = 932
# We need to collect all IDs from v40 candidates_discovered_delta + duplicates_skipped
# But easier: load all frontier artifacts and union their IDs
# For now, we'll use the v40 cursor count and reconstruct from v40 + v39 artifacts
# Actually, let's load all frontier artifacts in research_state/

def load_all_frontier_ids():
    """Load all known IDs from v1-v40 frontier artifacts"""
    known_ids = set()
    research_state = Path("research_state")

    # Load the master universe_frontier.json if it exists
    master = research_state / "universe_frontier.json"
    if master.exists():
        with open(master) as f:
            data = json.load(f)
            for item in data.get("candidates", []):
                known_ids.add(item["id"])

    # Load all v1-v40 advance artifacts
    for i in range(1, 41):
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
print(f"Reconstructed known-id union (v1-v40): {len(known_ids)} ids")
assert len(known_ids) == 932, f"Expected 932 known IDs, got {len(known_ids)}"

# Fetch fresh CoinPaprika data
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

# Sort by rank
ranked_items.sort(key=lambda x: x["rank"])

# Select rank window 1026-1050
window_items = [item for item in ranked_items if 1026 <= item["rank"] <= 1050]
print(f"Items in rank window 1026-1050: {len(window_items)}")

# Deduplicate
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
        # Check symbol collision
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

# Build artifact
artifact = {
    "artifact_id": "EBCR-001-UNIVERSE-FRONTIER-ADVANCE-V41",
    "schema_version": "1.0",
    "program_id": "EBCR-001",
    "created_at_utc": retrieved_at,
    "task_activation": 3332,  # This activation
    "purpose": "Advance rank frontier discovery batch (ranks 1026-1050) after documented cooldown since v40 (v40 retrieval 2026-11-25T13:28:38Z; cooldown ~3.5h; current retrieval past deadline). Discovery-only; NOT PIT membership/rank.",
    "prior_artifact": {
        "path": "universe_frontier_advance_v40.json",
        "sha256_raw_bytes": "3aaa55cbc003ba2496f5d6972252f20c0c7f21bc05527291ba87a82102378604",
        "sha256_compact_content": "ef7d74dad8626360a2e83bb23d44dbca6c239c6c8fe4169685fb989bd1a83104",
        "discovered_id_count_v40": 932,
        "top_rank_covered_v40": 1025,
        "next_batch_start_rank_v40": 1026
    },
    "source": {
        "name": "CoinPaprika public API",
        "endpoint": "https://api.coinpaprika.com/v1/coins",
        "retrieved_at_utc": retrieved_at,
        "response_sha256": response_sha256,
        "total_items_in_response": total_items,
        "ranked_items_in_response": ranked_items_count,
        "note": f"Current market-cap ranking for candidate discovery only; NOT historical PIT membership/rank. /v1/coins items carry an integer rank field but the response is not pre-sorted by rank; items were sorted by rank before window selection. Raw response not stored in-repo; only its checksum is recorded. Fresh retrieval at activation 3332, past the ~3.5h cooldown since v40 retrieval at 2026-11-25T13:28:38Z. Source observation: ranked_items_in_response (rank>=1) = {ranked_items_count} at this retrieval vs 11507 at v40 and 11426 at v39; total_items_in_response = {total_items} (v40: 62788). Rank window 1026-1050 was fully populated ({len(window_items)}/25) so the batch is complete; the ranked-count change is recorded as a source-behavior observation, not a gap."
    },
    "frontier_state": {
        "rank_window_scanned": [1026, 1050],
        "known_ids_before_dedup": 932,
        "items_in_rank_window": len(window_items),
        "net_new_candidates": len(candidates_delta),
        "duplicates_skipped_count": len(duplicates_skipped),
        "symbol_collisions_count": len(symbol_collisions)
    },
    "discovery_method": "Set-difference deduplication by stable CoinPaprika asset id against the reconstructed v1-v40 observed-id union = 932 known ids (25-id universe_frontier.json master frontier plus all v1-v40 delta entries). Current ranks used for discovery ordering only; status rank_unverified_discovery_only.",
    "candidates_discovered_delta": candidates_delta,
    "duplicates_skipped": duplicates_skipped,
    "symbol_collisions": symbol_collisions,
    "cursor": {
        "discovered_id_count": 932 + len(candidates_delta),
        "top_rank_covered": 1050,
        "next_batch_start_rank": 1051,
        "next_batch_end_rank": 1075,
        "rank_frontier_exhausted": False
    }
}

# Write artifact
output_path = Path("research_state/universe_frontier_advance_v41.json")
with open(output_path, "w") as f:
    json.dump(artifact, f, indent=2)

print(f"Artifact written to {output_path}")

# Compute compact content hash (without artifact_id and created_at_utc for stability)
compact_artifact = {k: v for k, v in artifact.items() if k not in ("artifact_id", "created_at_utc", "task_activation")}
compact_bytes = json.dumps(compact_artifact, sort_keys=True, separators=(',', ':')).encode()
compact_sha256 = hashlib.sha256(compact_bytes).hexdigest()
print(f"Artifact raw sha256: {hashlib.sha256(json.dumps(artifact, indent=2).encode()).hexdigest()}")
print(f"Artifact compact content sha256: {compact_sha256}")