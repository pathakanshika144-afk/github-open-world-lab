# Local setup

Open World Checklist has no package installation step.

1. Clone the repository.
2. Run `python3 -m http.server 8000` from the repository root.
3. Open `http://localhost:8000` and confirm that checklist tasks load.
4. Run `python3 scripts/validate_tasks.py data/tasks.json` before changing task data.

To check the test suite, run `python3 -m unittest tests/test_validate_tasks.py`.
