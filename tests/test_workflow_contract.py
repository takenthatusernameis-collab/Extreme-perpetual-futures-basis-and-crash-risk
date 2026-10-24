import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class WorkflowContractTests(unittest.TestCase):
    def test_complete_controller_and_free_model_route_present(self):
        workflow = (ROOT / ".github/workflows/main.yml").read_text(encoding="utf-8")
        self.assertGreater(len(workflow), 70_000)
        self.assertIn('cron: "*/5 * * * *"', workflow)
        self.assertIn("timeout-minutes: 360", workflow)
        self.assertIn("kilo/kilo-auto/free", workflow)
        self.assertIn("workflow_run_diagnostics.jsonl", workflow)

    def test_workflow_runs_the_repository_test_suite(self):
        workflow = (ROOT / ".github/workflows/main.yml").read_text(encoding="utf-8")
        self.assertIn("-m pytest -q tests", workflow)
        self.assertNotIn("tests/test_controller_progress_accounting.py", workflow)


if __name__ == "__main__":
    unittest.main()
