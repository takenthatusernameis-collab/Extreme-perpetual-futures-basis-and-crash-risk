#!/usr/bin/env python3
"""Generate a deterministic manifest for the frozen 324-cell basis crash-risk grid."""
from __future__ import annotations

import argparse
import hashlib
import itertools
import json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_CONFIG = ROOT / "configs" / "basis_crash_grid_v1.json"
DEFAULT_OUTPUT = ROOT / "research_state" / "grid_manifest_v1.json"


def canonical_json(value: Any) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False)


def sha256_text(value: str) -> str:
    return hashlib.sha256(value.encode("utf-8")).hexdigest()


def generate_manifest(config: dict[str, Any]) -> dict[str, Any]:
    grid = config["grid"]
    axes = grid["axes"]
    keys = grid["enumeration_order"]
    if set(keys) != set(axes) or len(keys) != len(axes):
        raise ValueError("enumeration_order must contain every and only axis key")
    for key in keys:
        if not isinstance(axes[key], list) or not axes[key]:
            raise ValueError(f"axis {key!r} must be a non-empty list")
    cells = []
    for ordinal, values in enumerate(itertools.product(*(axes[key] for key in keys)), start=1):
        params = dict(zip(keys, values))
        config_hash = sha256_text(canonical_json({"grid_id": config["grid_id"], "parameters": params}))
        cells.append({
            "cell_id": f"EBCR-GRID-001-{ordinal:04d}",
            "ordinal": ordinal,
            "parameters": params,
            "configuration_hash_sha256": config_hash,
        })
    expected = grid["expected_configuration_count"]
    if len(cells) != expected:
        raise ValueError(f"expected {expected} cells, generated {len(cells)}")
    if len({cell["cell_id"] for cell in cells}) != len(cells):
        raise ValueError("cell IDs are not unique")
    if len({cell["configuration_hash_sha256"] for cell in cells}) != len(cells):
        raise ValueError("configuration hashes are not unique")
    if not any(cell["parameters"] == grid["primary_anchor"] for cell in cells):
        raise ValueError("primary anchor is missing from the grid")
    return {
        "schema_version": "1.0",
        "program_id": config["program_id"],
        "experiment_id": config["experiment_id"],
        "grid_id": config["grid_id"],
        "config_sha256": sha256_text(canonical_json(config)),
        "expected_configuration_count": len(cells),
        "primary_anchor": grid["primary_anchor"],
        "cells": cells,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", type=Path, default=DEFAULT_CONFIG)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--check", action="store_true", help="Fail if existing output differs from deterministic regeneration.")
    args = parser.parse_args()
    config = json.loads(args.config.read_text(encoding="utf-8"))
    manifest = generate_manifest(config)
    rendered = json.dumps(manifest, indent=2, sort_keys=True) + "\n"
    if args.check and args.output.exists():
        if args.output.read_text(encoding="utf-8") != rendered:
            raise SystemExit("manifest differs from deterministic regeneration")
        print(f"verified {manifest['expected_configuration_count']} cells: {args.output}")
        return 0
    args.output.parent.mkdir(parents=True, exist_ok=True)
    temp = args.output.with_suffix(args.output.suffix + ".tmp")
    temp.write_text(rendered, encoding="utf-8")
    temp.replace(args.output)
    print(f"generated {manifest['expected_configuration_count']} cells: {args.output}")
    print(f"config_sha256={manifest['config_sha256']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
