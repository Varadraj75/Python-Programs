## Contributing

- Keep PRs small and focused (one script or feature per PR).
- Prefer argparse for new CLI features; validate user input.
- Preserve existing behavior unless you clearly improve UX.
- Include a short description and test steps in your PR body.
- Use informative commit messages and snake_case in Python.

### Local test checklist
- python3 -m py_compile path/to/script.py
- Run the script (interactive or with flags) and verify outputs.
