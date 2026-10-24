#!/usr/bin/env python3
import json, os
from datetime import datetime, timezone

out = {
  "schema_version": "1.0",
  "program_id": "EBCR-001",
  "verification_type": "pit_listing_evidence",
  "retrieved_at_utc": datetime.now(timezone.utc).isoformat(),
  "notes": "Contract listing presence verified via Binance Vision S3 XML listings (markPriceKlines daily). No free public PIT market-cap rank history source was located in repo; rank verification remains limited. Listing dates are earliest zip date present (not necessarily first public announcement).",
  "symbols": []
}

# Add all symbols with their data
data_map = {
  "BTCUSDT": {"earliest": None, "latest": None, "missing": None},
  "ETHUSDT": {"earliest": None, "latest": None, "missing": None},
  "BNBUSDT": {"file": "/tmp/bnb_listing.json"},
  "XRPUSDT": {"earliest": "2020-01-06", "latest": "2026-10-23", "missing": 49},
  "SOLUSDT": {"earliest": "2020-09-13", "latest": "2026-10-23", "missing": 56},
  "TRXUSDT": {"earliest": "2020-01-15", "latest": "2026-10-23", "missing": 42},
  "ZECUSDT": {"earliest": "2020-02-04", "latest": "2026-10-23", "missing": 29},
  "DOGEUSDT": {"file": "/tmp/doge_listing.json"},
  "LINKUSDT": {"earliest": "2020-01-17", "latest": "2026-10-23", "missing": 39},
  "ADAUSDT": {"file": "/tmp/ada_listing.json"},
  "XLMUSDT": {"earliest": "2020-01-19", "latest": "2026-10-23", "missing": 39},
  "NEARUSDT": {"earliest": "2020-10-14", "latest": "2026-10-23", "missing": 34},
  "BCHUSDT": {"file": "/tmp/bch_listing.json"},
}

for sym, info in data_map.items():
  entry = {
    "binance_um_symbol": sym,
    "sources": [{"type": "binance_vision_s3_xml_listing", "retrieved_at_utc": datetime.now(timezone.utc).isoformat()}],
    "rank_verified": False,
    "listing_verified": True,
    "notes": []
  }
  if "file" in info and os.path.exists(info["file"]):
    with open(info["file"]) as f:
      d = json.load(f)
    entry["sources"][0]["prefix"] = d["prefix"]
    entry["sources"][0]["sha256_last_page"] = d.get("sha256_last_page") or d.get("sha256")
    entry["sources"][0]["retrieved_at_utc"] = d.get("retrieved_at_utc")
    entry["earliest_zip_date"] = d.get("earliest")
    entry["latest_zip_date"] = d.get("latest")
    entry["n_zip_dates"] = d.get("n_zip_dates")
    entry["missing_count"] = d.get("missing_count")
    entry["notes"].append(f"Earliest daily markPriceKlines zip: {d.get('earliest')}, latest: {d.get('latest')}, missing_count: {d.get('missing_count')}")
  else:
    entry["earliest_zip_date"] = info.get("earliest")
    entry["latest_zip_date"] = info.get("latest")
    entry["missing_count"] = info.get("missing")
    entry["notes"].append(f"Earliest daily markPriceKlines zip: {info.get('earliest')}, latest: {info.get('latest')}, missing_count: {info.get('missing')}")

  entry["notes"].append("Rank verification: no free public PIT market-cap rank history source found in repo; rank remains unverified per point-in-time-universe rules.")
  out["symbols"].append(entry)

with open("research_state/pit_universe_verification_v1.json", "w") as f:
  json.dump(out, f, indent=2)
print("wrote research_state/pit_universe_verification_v1.json")
