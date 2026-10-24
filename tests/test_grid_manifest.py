import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from scripts.generate_grid_manifest import DEFAULT_CONFIG, generate_manifest


class GridManifestTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.config = json.loads(DEFAULT_CONFIG.read_text(encoding="utf-8"))
        cls.manifest = generate_manifest(cls.config)

    def test_expected_grid_size_and_unique_identity(self):
        cells = self.manifest["cells"]
        self.assertEqual(len(cells), 324)
        self.assertEqual(len({cell["cell_id"] for cell in cells}), 324)
        self.assertEqual(len({cell["configuration_hash_sha256"] for cell in cells}), 324)

    def test_primary_anchor_is_in_grid(self):
        anchor = self.config["grid"]["primary_anchor"]
        self.assertIn(anchor, [cell["parameters"] for cell in self.manifest["cells"]])

    def test_cartesian_product_has_expected_size(self):
        axes = self.config["grid"]["axes"]
        count = 1
        for values in axes.values():
            count *= len(values)
        self.assertEqual(count, 324)
        self.assertEqual(count, len(self.manifest["cells"]))

    def test_configuration_hashes_are_stable(self):
        again = generate_manifest(self.config)
        self.assertEqual(self.manifest["config_sha256"], again["config_sha256"])
        self.assertEqual(
            [cell["configuration_hash_sha256"] for cell in self.manifest["cells"]],
            [cell["configuration_hash_sha256"] for cell in again["cells"]],
        )

    def test_cells_use_only_declared_axis_values(self):
        axes = self.config["grid"]["axes"]
        for cell in self.manifest["cells"]:
            self.assertEqual(set(cell["parameters"]), set(axes))
            for key, value in cell["parameters"].items():
                self.assertIn(value, axes[key])


if __name__ == "__main__":
    unittest.main()
