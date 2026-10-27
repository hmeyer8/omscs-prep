# Development notes

## Python environment

Use Python 3.11 or newer. `.python-version` selects Python 3.11 for tools that read it.
The linked examples in the [README](../README.md) need only the standard library.

For work that uses the scientific Python stack, install [uv](https://docs.astral.sh/uv/getting-started/installation/) and run this from the repository root:

```bash
uv sync --locked
uv run python week/04/1025/recall.py
```

`pyproject.toml` declares dependencies and `uv.lock` records resolved versions.
Use `--locked` to detect a mismatch instead of silently rewriting the lockfile.

## Running practice

Read a script before running or importing it. Many dated exercises print a demonstration
at module scope; some prompt for input or depend on a local text file. Scripts opening
`pi_mil.txt`, for example, need to run from `week/05/1026/`.

`week/NN/MMDD/` is a chronological practice archive. A file called `test.py` in that
archive is a scratch exercise, not a pytest test suite. These filenames do not match
pytest's default `test_*.py` or `*_test.py` patterns. There is no maintained automated
regression suite yet, so repository-wide pytest is not currently a useful verification command.

When adding real tests, use a dedicated `tests/` directory, descriptive `test_*.py` names,
and narrow discovery to those tests. Give reusable modules import-safe demonstrations
under `if __name__ == "__main__":` before including them in test collection.

## Finishing an exercise

- Check the expected output and at least one edge case. Record actual results.
- Explain important assumptions, units, and mutation of inputs or instance state.
- Attribute adapted prompts and note any help used.
- Keep the first attempt; describe the repair in a journal entry or follow-up commit.
- Add a README link only when the artifact exists and its run instructions have been checked.

For the Flight/Logbook work, useful future automated checks include an empty logbook,
independent instance lists, the 4.25-hour fixed dataset, and per-type totals. Decide and
document what negative, nonnumeric, or nonfinite durations should do before adding validation.

## Commits

Use short messages that describe the change, for example:

```text
feat: aggregate flight hours by type
fix: create a separate flights list per logbook
docs: explain the working directory in the pi exercise
journal: reflect on composition and independent state
rebuild: reproduce logbook totals without references
```

Reserve `rebuild:` for an actual independent recall attempt. The
[pull request template](../.github/pull_request_template.md) prompts for behavior,
verification, and limitations when a change is ready to review.
