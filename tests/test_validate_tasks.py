import json
import tempfile
import unittest
from pathlib import Path

from scripts.validate_tasks import validate_tasks


class ValidateTasksTests(unittest.TestCase):
    def write_tasks(self, tasks):
        directory = tempfile.TemporaryDirectory()
        self.addCleanup(directory.cleanup)
        path = Path(directory.name) / "tasks.json"
        path.write_text(json.dumps(tasks), encoding="utf-8")
        return path

    def test_accepts_unique_identifiers(self):
        path = self.write_tasks(
            [
                {"id": "one", "title": "One", "category": "Start", "completed": False},
                {"id": "two", "title": "Two", "category": "Start", "completed": True},
            ]
        )
        self.assertEqual(validate_tasks(path), [])

    def test_rejects_duplicate_identifiers(self):
        path = self.write_tasks(
            [
                {"id": "duplicate", "title": "One", "category": "Start", "completed": False},
                {"id": "duplicate", "title": "Two", "category": "Start", "completed": False},
            ]
        )
        self.assertIn("Duplicate task id: duplicate.", validate_tasks(path))


if __name__ == "__main__":
    unittest.main()
