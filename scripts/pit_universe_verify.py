#!/usr/bin/env python3
import json, os, sys
from datetime import datetime, timezone

# Use the already fetched listing results
symbols = ["BTCUSDT", "ETHUSDT", "BNBUSDT", "XRPUSDT", "SOLUSDT", "TRXUSDT",
           "ZECUSDT", "DOGEUSDT", "LINKUSDT", "ADAUSDT", "XLMUSDT", "NEARUSDT", "BCHUSDT"]

out = {
  "schema_version": "1.0",
  "program_id": "EBCR-001",
  "verification_type": "pit_listing_evidence",
  "retrieved_at_utc": datetime.now(timezone.utc).isoformat(),
  "notes": "Contract listing presence verified via Binance Vision S3 XML listings (markPriceKlines daily). No free public PIT market-cap rank history source was located in repo; rank verification remains limited. Listing dates are earliest zip date present (not necessarily first public announcement).",
  "symbols": []
}

# Read the files we just created
mapping = {
  "ADAUSDT": "/tmp/ada_listing.json",
  "BCHUSDT": "/tmp/bch_listing.json",
  "BNBUSDT": "/tmp/bnb_listing.json",
  "DOGEUSDT": "/tmp/doge_listing.json",
}

for sym in symbols:
  entry = {
    "binance_um_symbol": sym,
    "sources": [],
    "rank_verified": False,
    "listing_verified": False,
    "notes": []
  }
  # Try to load from files
  if sym in mapping and os.path.exists(mapping[sym]):
    with open(mapping[sym]) as f:
      data = json.load(f)
    entry["sources"].append({
      "type": "binance_vision_s3_xml_listing",
      "prefix": data["prefix"],
      "sha256_last_page": data.get("sha256_last_page") or data.get("sha256"),
      "retrieved_at_utc": data.get("retrieved_at_utc")
    })
    entry["listing_verified"] = True
    entry["earliest_zip_date"] = data.get("earliest")
    entry["latest_zip_date"] = data.get("latest")
    entry["n_zip_dates"] = data.get("n_zip_dates")
    entry["missing_count"] = data.get("missing_count")
    entry["notes"].append(f"Earliest daily markPriceKlines zip: {data.get('earliest')}, latest: {data.get('latest')}, missing_count: {data.get('missing_count')}")
  else:
    # For others we saw in grep output
    entry["notes"].append("Listing metadata from inline check in session")
  out["symbols"].append(entry)

os.makedirs("research_state", exist_ok=True)
with open("research_state/pit_universe_verification_v1.json", "w") as f:
  json.dump(out, f, indent=2)
print("wrote research_state/pit_universe_verification_v1.json")
