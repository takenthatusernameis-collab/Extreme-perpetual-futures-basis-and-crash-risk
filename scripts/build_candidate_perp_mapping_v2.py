#!/usr/bin/env python3
"""Map the 75 discovered candidate asset ids to Binance USD-M perpetual contracts.

Discovery only. The Binance USD-M ``exchangeInfo`` response is a live snapshot;
nothing in this artifact is historical point-in-time membership, listing evidence
or contract-continuity evidence. The frozen ``candidate_perp_mapping_v1.json``
is never modified.

The artifact is deterministic for a given exchangeInfo payload and source
metadata: candidate set, ranking and all contract fields are copied verbatim.

Usage:
    python3 scripts/build_candidate_perp_mapping_v2.py \
        --exchange-info /tmp/binance_um_exchangeinfo.json \
        --retrieved-at 2026-11-14T09:35:21Z \
        --output research_state/candidate_perp_mapping_v2.json

If ``--exchange-info`` is omitted the script fetches
``https://www.binance.com/fapi/v1/exchangeInfo`` with a bounded timeout.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import urllib.request
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
FRONTIER = ROOT / "research_state" / "universe_frontier.json"
FRONTIER_V1 = ROOT / "research_state" / "universe_frontier_advance_v1.json"
FRONTIER_V2 = ROOT / "research_state" / "universe_frontier_advance_v2.json"
FROZEN_MAPPING_V1 = ROOT / "research_state" / "candidate_perp_mapping_v1.json"
DEFAULT_ENDPOINT = "https://www.binance.com/fapi/v1/exchangeInfo"

STATUS_MAPPED = "mapped_discovery_only_unverified"
STATUS_NO_PERP = "no_perp_expected"
STATUS_NOT_LISTED = "not_listed_binance_um"
STATUS_NO_TRADING = "no_trading_perp"
STATUS_BLOCKED = "blocked_unknown"
ALLOWED_STATUSES = {
    STATUS_MAPPED,
    STATUS_NO_PERP,
    STATUS_NOT_LISTED,
    STATUS_NO_TRADING,
    STATUS_BLOCKED,
}

STABLECOINS = {
    "USDT", "USDC", "USDS", "DAI", "USD1", "USDG", "PYUSD", "USDF", "USDD",
    "BFUSD", "SUSDS", "SUSDE", "USDE", "SYRUPUSDC",
}
STAKED = {"STETH", "SUSDS", "SUSDE", "JITOSOL", "KHYPE"}
WRAPPED = {"WBTC", "CBBTC", "WETH", "WBETH", "WEETH", "WSTETH", "WBNB"}
# Assets that are not stablecoin/wrapped/staked but are known to be non-listed
# on Binance USD-M (recorded so the status is not inferred from a missing match).
KNOWN_NON_PERP = {
    "RAIN": "rain_protocol_no_binance_um_perp_listed",
    "CRO": "cronos_no_binance_um_perp_listed",
    "OKB": "okb_no_binance_um_perp_listed",
    "MNT": "mantle_no_binance_um_perp_listed",
    "LEO": "leo_no_binance_um_perp_listed",
    "WBT": "whitebit_no_binance_um_perp_listed",
    "BGB": "bitget_no_binance_um_perp_listed",
    "GT": "gatechain_no_binance_um_perp_listed",
}
# Single-letter or collision-prone tickers: mapping is a symbol-level match only.
AMBIGUOUS_SYMBOLS = {"M", "CC", "SKY", "GT", "GRAM"}


def sha256_bytes(payload: bytes) -> str:
    return hashlib.sha256(payload).hexdigest()


def iso_utc(timestamp_ms: int | None) -> str | None:
    if timestamp_ms is None:
        return None
    return datetime.fromtimestamp(timestamp_ms / 1000, tz=timezone.utc).isoformat().replace("+00:00", "Z")


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def discover_candidates() -> list[dict[str, Any]]:
    """Return the de-duplicated 75-candidate discovery frontier, preserving ranks."""
    frontier = load_json(FRONTIER)
    v1 = load_json(FRONTIER_V1)
    v2 = load_json(FRONTIER_V2)

    rows: list[dict[str, Any]] = []
    seen: set[str] = set()

    def add(entry: dict[str, Any], source: str) -> None:
        asset_id = entry["id"]
        if asset_id in seen:
            return
        seen.add(asset_id)
        rows.append({
            "rank": entry["rank"],
            "asset_id": asset_id,
            "asset_symbol": entry["symbol"],
            "asset_name": entry["name"],
            "discovery_source": source,
        })

    for entry in frontier["candidates_discovered"]:
        add(entry, "universe_frontier")
    for entry in v1["candidates_discovered_delta"]:
        add(entry, "universe_frontier_advance_v1")
    for entry in v2["candidates_discovered_delta"]:
        add(entry, "universe_frontier_advance_v2")

    rows.sort(key=lambda row: (row["rank"], row["asset_id"]))
    return rows


def fetch_exchange_info(endpoint: str, timeout: float) -> tuple[bytes, dict[str, Any]]:
    request = urllib.request.Request(endpoint, headers={"User-Agent": "ebcr-research/1.0"})
    with urllib.request.urlopen(request, timeout=timeout) as response:  # noqa: S310 - fixed public endpoint
        payload = response.read()
        status = response.status
    if status != 200:
        raise RuntimeError(f"exchangeInfo returned HTTP {status}")
    return payload, json.loads(payload)


def index_perpetuals(exchange_info: dict[str, Any]) -> dict[str, list[dict[str, Any]]]:
    by_base: dict[str, list[dict[str, Any]]] = {}
    for contract in exchange_info["symbols"]:
        if contract.get("contractType") not in {"PERPETUAL", "TRADIFI_PERPETUAL"}:
            continue
        by_base.setdefault(contract["baseAsset"], []).append(contract)
    return by_base


def match_candidates(
    rows: list[dict[str, Any]],
    by_base: dict[str, list[dict[str, Any]]],
) -> list[dict[str, Any]]:
    mappings: list[dict[str, Any]] = []
    for row in rows:
        symbol = row["asset_symbol"]
        contracts = by_base.get(symbol, [])
        multiplier_contracts = by_base.get(f"1000{symbol}", [])

        trading_usdt = [
            c for c in contracts
            if c.get("contractType") == "PERPETUAL"
            and c.get("status") == "TRADING"
            and c.get("quoteAsset") == "USDT"
        ]
        trading_multiplier = [
            c for c in multiplier_contracts
            if c.get("contractType") == "PERPETUAL"
            and c.get("status") == "TRADING"
            and c.get("quoteAsset") == "USDT"
        ]

        mapping: dict[str, Any] = {
            "rank": row["rank"],
            "asset_id": row["asset_id"],
            "asset_symbol": symbol,
            "asset_name": row["asset_name"],
            "discovery_source": row["discovery_source"],
            "binance_um_symbol": None,
            "contract_type": None,
            "contract_status": None,
            "quote_asset": None,
            "onboard_date_utc": None,
            "notional_multiplier": None,
            "match_basis": "none",
            "other_quote_variants": [],
            "excluded_near_matches": [],
            "status": None,
            "reason_code": None,
            "note": None,
        }

        def contract_view(contract: dict[str, Any]) -> dict[str, Any]:
            return {
                "symbol": contract["symbol"],
                "contract_type": contract["contractType"],
                "status": contract["status"],
                "quote_asset": contract["quoteAsset"],
                "margin_asset": contract.get("marginAsset"),
                "base_asset": contract["baseAsset"],
                "onboard_date_utc": iso_utc(contract.get("onboardDate")),
            }

        class_key = symbol.upper()
        excluded_near_matches = [contract_view(c) for c in contracts]

        if class_key in STABLECOINS:
            mapping.update({
                "status": STATUS_NO_PERP,
                "reason_code": "stablecoin_no_directional_perp_expected",
                "match_basis": "asset_class",
                "excluded_near_matches": excluded_near_matches,
                "note": "stablecoin; any base-asset contract is a stablecoin/stablecoin pair, not a directional crypto perp",
            })
        elif class_key in WRAPPED:
            mapping.update({
                "status": STATUS_NO_PERP,
                "reason_code": "wrapped_asset_no_direct_perp_expected",
                "match_basis": "asset_class",
            })
        elif class_key in STAKED:
            mapping.update({
                "status": STATUS_NO_PERP,
                "reason_code": "staked_derivative_no_direct_perp_expected",
                "match_basis": "asset_class",
            })
        elif trading_usdt:
            chosen = trading_usdt[0]
            mapping.update({
                "binance_um_symbol": chosen["symbol"],
                "contract_type": chosen["contractType"],
                "contract_status": chosen["status"],
                "quote_asset": chosen["quoteAsset"],
                "onboard_date_utc": iso_utc(chosen.get("onboardDate")),
                "match_basis": "baseAsset_exact_usdt_perpetual_trading",
                "status": STATUS_MAPPED,
                "reason_code": "usdt_perpetual_trading",
                "other_quote_variants": sorted({
                    c["symbol"] for c in contracts
                    if c.get("contractType") == "PERPETUAL"
                    and c.get("status") == "TRADING"
                    and c.get("quoteAsset") != "USDT"
                }),
            })
            if len(trading_usdt) > 1:
                mapping["note"] = "multiple TRADING USDT perpetuals matched; first retained"
        elif trading_multiplier:
            chosen = trading_multiplier[0]
            multiplier = 1000
            mapping.update({
                "binance_um_symbol": chosen["symbol"],
                "contract_type": chosen["contractType"],
                "contract_status": chosen["status"],
                "quote_asset": chosen["quoteAsset"],
                "onboard_date_utc": iso_utc(chosen.get("onboardDate")),
                "notional_multiplier": multiplier,
                "match_basis": f"baseAsset_{multiplier}_multiplier_usdt_perpetual_trading",
                "status": STATUS_MAPPED,
                "reason_code": "usdt_perpetual_trading_multiplier",
                "other_quote_variants": sorted({
                    c["symbol"] for c in multiplier_contracts
                    if c.get("contractType") == "PERPETUAL"
                    and c.get("status") == "TRADING"
                    and c.get("quoteAsset") != "USDT"
                }),
            })
        else:
            # No tradable USDT perpetual. Distinguish a settling/delisted
            # contract from a genuinely absent listing.
            all_perps = [c for c in contracts if c.get("contractType") == "PERPETUAL"]
            all_multiplier_perps = [
                c for c in multiplier_contracts if c.get("contractType") == "PERPETUAL"
            ]
            if all_perps or all_multiplier_perps:
                existing = (all_perps or all_multiplier_perps)[0]
                mapping.update({
                    "binance_um_symbol": existing["symbol"],
                    "contract_type": existing["contractType"],
                    "contract_status": existing["status"],
                    "quote_asset": existing["quoteAsset"],
                    "onboard_date_utc": iso_utc(existing.get("onboardDate")),
                    "match_basis": "baseAsset_exact_perpetual_not_trading",
                    "status": STATUS_NO_TRADING,
                    "reason_code": f"perpetual_status_{str(existing['status']).lower()}",
                    "note": "perpetual contract exists in the live snapshot but is not TRADING",
                })
            elif class_key in KNOWN_NON_PERP:
                mapping.update({
                    "status": STATUS_NOT_LISTED,
                    "reason_code": KNOWN_NON_PERP[class_key],
                    "match_basis": "no_perp_in_live_exchange_info",
                })
            else:
                mapping.update({
                    "status": STATUS_BLOCKED,
                    "reason_code": "no_match_and_asset_class_unclassified",
                    "match_basis": "none",
                })

        if symbol in AMBIGUOUS_SYMBOLS and mapping["status"] == STATUS_MAPPED:
            mapping["note"] = (
                "symbol-level base-asset match only; exchangeInfo carries no project name, "
                "so the contract is not independently confirmed to be the same project"
            )

        if row["asset_id"] == "toncoin-the-open-network" and mapping["status"] == STATUS_MAPPED:
            settling = [c for c in contracts if c.get("status") != "TRADING"]
            mapping["note"] = (
                "mapped to the current GRAM perpetual; the legacy TONUSDT perpetual is "
                f"present but {settling[0]['status'] if settling else 'not TRADING'}"
            )

        if row["asset_id"] in {"weth-weth", "eth-ethereum-token"}:
            mapping["note"] = (
                "WETH ticker collision: both CoinPaprika ids (weth-weth, eth-ethereum-token / "
                "Binance-Peg Ethereum Token) are wrapped-ETH variants; neither maps to a perp"
            )

        mappings.append(mapping)
    return mappings


def build_artifact(
    rows: list[dict[str, Any]],
    mappings: list[dict[str, Any]],
    exchange_info: dict[str, Any],
    payload: bytes,
    endpoint: str,
    retrieved_at: str,
) -> dict[str, Any]:
    status_counts: dict[str, int] = {status: 0 for status in sorted(ALLOWED_STATUSES)}
    for mapping in mappings:
        status_counts[mapping["status"]] += 1

    mapped = [m for m in mappings if m["status"] == STATUS_MAPPED]
    contracts = exchange_info["symbols"]
    return {
        "artifact_id": "EBCR-001-CANDIDATE-PERP-MAPPING-V2",
        "schema_version": "1.0",
        "program_id": "EBCR-001",
        "created_at_utc": retrieved_at,
        "task_activation": 2949,
        "purpose": (
            "Map the 75 discovered candidate asset ids (frontier v0 + advance v1/v2) to Binance "
            "USD-M perpetual contracts from a live exchangeInfo snapshot, with an explicit "
            "status per candidate. Discovery only: no historical PIT membership, listing or "
            "contract-continuity claim."
        ),
        "prior_artifact": {
            "path": "research_state/candidate_perp_mapping_v1.json",
            "sha256": sha256_bytes(FROZEN_MAPPING_V1.read_bytes()),
            "mapping_status": "discovery_only_unverified",
            "note": "frozen file is not modified by this artifact",
        },
        "source": {
            "name": "Binance USD-M Futures exchangeInfo",
            "endpoint": endpoint,
            "retrieved_at_utc": retrieved_at,
            "response_sha256": sha256_bytes(payload),
            "response_bytes": len(payload),
            "server_time_ms": exchange_info.get("serverTime"),
            "server_time_utc": iso_utc(exchange_info.get("serverTime")),
            "n_symbols": len(exchange_info["symbols"]),
            "note": (
                "live snapshot; fapi.binance.com returned HTTP 451 (geo-blocked) in this "
                "environment, www.binance.com/fapi/v1/exchangeInfo returned HTTP 200. The "
                "1.15 MB raw response is not stored in-repo; only its checksum is recorded."
            ),
        },
        "method": {
            "candidate_union": "universe_frontier.json + universe_frontier_advance_v1.json + universe_frontier_advance_v2.json, de-duplicated by stable asset id",
            "match_key": "baseAsset equals candidate symbol, contractType PERPETUAL, status TRADING, quoteAsset USDT",
            "multiplier_contracts": "1000SHIBUSDT and 1000PEPEUSDT matched to SHIB and PEPE (baseAsset 1000SHIB / 1000PEPE); notional_multiplier records 1000",
            "quote_variants": "USDT is the primary contract; USDC/USD1/BTC-quoted perpetuals are recorded in other_quote_variants and never used as the primary mapping",
            "status_taxonomy": {
                STATUS_MAPPED: "a TRADING USDT-quoted PERPETUAL exists for the base asset",
                STATUS_NO_PERP: "stablecoin / wrapped / staked / synthetic asset class; no directional perp expected",
                STATUS_NOT_LISTED: "tradable asset with no Binance USD-M PERPETUAL in the live snapshot (not a statement about other venues)",
                STATUS_NO_TRADING: "a PERPETUAL exists but status is not TRADING (SETTLING / PENDING_TRADING)",
                STATUS_BLOCKED: "no match and the asset class is unclassified; requires manual review",
            },
            "pit_status": "every row is discovery_only_unverified; exchangeInfo is a live snapshot and must never be used as historical point-in-time listing or membership evidence",
            "frozen_inputs_unchanged": [
                "research_state/universe_frontier.json",
                "research_state/universe_frontier_advance_v1.json",
                "research_state/universe_frontier_advance_v2.json",
                "research_state/candidate_perp_mapping_v1.json",
            ],
        },
        "counts": {
            "candidates": len(mappings),
            "by_status": status_counts,
            "mapped": len(mapped),
            "contracts_total": len(contracts),
            "contracts_perpetual": sum(
                1 for c in contracts if c.get("contractType") == "PERPETUAL"
            ),
            "contracts_trading": sum(
                1 for c in contracts if c.get("status") == "TRADING"
            ),
        },
        "exchange_info_symbol_index": [
            {
                "symbol": contract["symbol"],
                "base_asset": contract["baseAsset"],
                "quote_asset": contract["quoteAsset"],
                "contract_type": contract["contractType"],
                "status": contract["status"],
            }
            for contract in sorted(contracts, key=lambda c: c["symbol"])
        ],
        "mappings": mappings,
        "symbol_collisions": [
            {
                "symbol": "WETH",
                "asset_ids": ["weth-weth", "eth-ethereum-token"],
                "resolution": "both ids classified as wrapped-ETH variants with no perp; mapping keyed on stable asset id, not symbol",
            }
        ],
        "notes": [
            "Does not modify frozen research_state/candidate_perp_mapping_v1.json or the universe frontier artifacts.",
            "All mappings are discovery-only and rank-unverified for PIT purposes; current rank and current listing status must never be projected backward.",
            "A live exchangeInfo snapshot cannot establish listing/delisting dates; contract-lifecycle evidence is a separate registration decision.",
            "Assets without a Binance USD-M perpetual are preserved with an explicit status and reason; none are silently omitted.",
            "The 75-candidate frontier is the union of the 25-candidate frontier, the v1 delta (25 entries, 2 duplicates) and the v2 delta (27 new), matching the v2 cursor of 75 distinct ids.",
        ],
    }


def validate_artifact(artifact: dict[str, Any], exchange_info: dict[str, Any]) -> None:
    mappings = artifact["mappings"]
    assert len(mappings) == 75, len(mappings)
    assert len({m["asset_id"] for m in mappings}) == 75
    assert [m["rank"] for m in mappings] == sorted(m["rank"] for m in mappings)
    assert sum(m["status"] == STATUS_MAPPED for m in mappings) == artifact["counts"]["mapped"]
    assert sum(artifact["counts"]["by_status"].values()) == 75
    assert set(artifact["counts"]["by_status"]) == ALLOWED_STATUSES

    known_symbols = {c["symbol"]: c for c in exchange_info["symbols"]}
    for mapping in mappings:
        assert mapping["status"] in ALLOWED_STATUSES, mapping
        if mapping["status"] == STATUS_MAPPED:
            contract = known_symbols[mapping["binance_um_symbol"]]
            assert contract["contractType"] == "PERPETUAL", mapping
            assert contract["status"] == "TRADING", mapping
            assert contract["quoteAsset"] == "USDT", mapping
            assert mapping["notional_multiplier"] in (None, 1000), mapping
        else:
            assert mapping["binance_um_symbol"] is None or mapping["status"] == STATUS_NO_TRADING, mapping


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--exchange-info", type=Path, default=None)
    parser.add_argument("--retrieved-at", default=None)
    parser.add_argument("--timeout", type=float, default=30.0)
    parser.add_argument("--output", type=Path, default=ROOT / "research_state" / "candidate_perp_mapping_v2.json")
    parser.add_argument("--check", action="store_true", help="Fail if the existing output differs from regeneration")
    args = parser.parse_args()

    if args.exchange_info is not None:
        payload = args.exchange_info.read_bytes()
        exchange_info = json.loads(payload)
        retrieved_at = args.retrieved_at or datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")
    else:
        payload, exchange_info = fetch_exchange_info(DEFAULT_ENDPOINT, args.timeout)
        retrieved_at = args.retrieved_at or datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")

    rows = discover_candidates()
    by_base = index_perpetuals(exchange_info)
    mappings = match_candidates(rows, by_base)
    artifact = build_artifact(rows, mappings, exchange_info, payload, DEFAULT_ENDPOINT, retrieved_at)
    validate_artifact(artifact, exchange_info)

    rendered = json.dumps(artifact, indent=2, ensure_ascii=False) + "\n"
    if args.check and args.output.exists():
        if args.output.read_text(encoding="utf-8") != rendered:
            raise SystemExit("mapping differs from deterministic regeneration")
        print(f"verified mapping: {args.output}")
        return 0

    args.output.parent.mkdir(parents=True, exist_ok=True)
    temp = args.output.with_suffix(args.output.suffix + ".tmp")
    temp.write_text(rendered, encoding="utf-8")
    temp.replace(args.output)
    print(f"wrote {artifact['counts']['candidates']} candidates: {args.output}")
    for status, count in artifact["counts"]["by_status"].items():
        print(f"  {status}: {count}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())