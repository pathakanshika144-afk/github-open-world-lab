"""Validate the task data used by Open World Checklist."""

from __future__ import annotations

import json
import sys
from pathlib import Path


REQUIRED_FIELDS = {"id", "title", "category", "completed"}


def validate_tasks(path: Path) -> list[str]:
    try:
        tasks = json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        return [f"Task data file was not found: {path}"]
    except json.JSONDecodeError as error:
        return [f"Task data is not valid JSON: {error}"]

    if not isinstance(tasks, list):
        return ["Task data must be a JSON array."]

    errors: list[str] = []
    seen_ids: set[str] = set()
    for index, task in enumerate(tasks, start=1):
        if not isinstance(task, dict):
            errors.append(f"Task {index} must be an object.")
            continue

        missing_fields = REQUIRED_FIELDS - task.keys()
        if missing_fields:
            errors.append(f"Task {index} is missing: {', '.join(sorted(missing_fields))}.")
            continue

        if not isinstance(task["id"], str) or not task["id"].strip():
            errors.append(f"Task {index} must have a non-empty string id.")
            continue

        if task["id"] in seen_ids:
            errors.append(f"Duplicate task id: {task['id']}.")
        seen_ids.add(task["id"])

        for field in ("title", "category"):
            if not isinstance(task[field], str) or not task[field].strip():
                errors.append(f"Task {index} must have a non-empty {field}.")
        if not isinstance(task["completed"], bool):
            errors.append(f"Task {index} must have a boolean completed value.")

    return errors


def main() -> int:
    task_path = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("data/tasks.json")
    errors = validate_tasks(task_path)
    if errors:
        print("Task data validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1
    print(f"Task data validation passed: {task_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
