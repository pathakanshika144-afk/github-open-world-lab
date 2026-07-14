# Local setup

Open World Checklist has no package installation step.

1. Clone the repository.
2. Run `python3 -m http.server 8000` from the repository root.
3. Open `http://localhost:8000` and confirm that checklist tasks load.
4. Run `python3 scripts/validate_tasks.py data/tasks.json` before changing task data.

To check the test suite, run `python3 -m unittest tests/test_validate_tasks.py`.

## Keyboard verification

Use Tab to move through the filter buttons and task checkboxes. Every focused control should display a high-contrast orange outline before it is activated with Enter or Space.
