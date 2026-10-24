import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class ResearchContractTests(unittest.TestCase):
    def test_grid_registers_324_configs_and_2592_endpoint_tests(self):
        cfg = json.loads((ROOT / "configs/basis_crash_grid_v1.json").read_text(encoding="utf-8"))
        n = 1
        for values in cfg["grid"]["axes"].values():
            n *= len(values)
        self.assertEqual(n, 324)
        self.assertEqual(cfg["evaluation"]["grid_inference"]["total_registered_grid_tests"], 324 * 8)
        self.assertEqual(len(cfg["outcomes"]["endpoints"]), 8)

    def test_primary_claim_is_tail_risk_not_mean_return(self):
        prompt = (ROOT / "prompts/continuous_research_operating_contract_v1.md").read_text(encoding="utf-8")
        self.assertIn("Average returns may be flat or positive", prompt)
        self.assertIn("2,592", prompt)
        self.assertIn("Frozen primary anchor", prompt)

    def test_point_in_time_and_expanding_universe_rules_exist(self):
        prompt = (ROOT / "prompts/continuous_research_operating_contract_v1.md").read_text(encoding="utf-8")
        self.assertIn("with no fixed top-N cutoff", prompt)
        self.assertIn("Current rank must never be projected backward", prompt)
        frontier = json.loads((ROOT / "research_state/universe_frontier.json").read_text(encoding="utf-8"))
        self.assertIsNone(frontier["fixed_top_n"])
        self.assertFalse(frontier["rank_frontier_exhausted"])

    def test_historical_only_free_service_boundaries(self):
        prompt = (ROOT / "prompts/continuous_research_operating_contract_v1.md").read_text(encoding="utf-8")
        self.assertIn("No paid APIs", prompt)
        self.assertIn("exchange credentials", prompt)
        self.assertIn("live trading or paper trading", prompt)


if __name__ == "__main__":
    unittest.main()
