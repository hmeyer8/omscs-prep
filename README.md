# OMSCS Preparation

**Python foundations, problem solving, and software engineering practice for graduate study in computer science.**

I'm Henry Meyer, a machine learning engineer building stronger computer science foundations ahead of Georgia Tech's OMSCS program. This repository documents that work through dated exercises, recall attempts, and technical notes. My long-term focus is building reliable machine learning systems.

> If I can't rebuild it from a blank file, I don't know it yet.

[Selected work](#selected-work) · [Run examples](#run-examples) · [Learning journal](journal/README.md) · [Roadmap](docs/roadmap.md)

## Current scope

The committed work currently focuses on Python: functions, collections, object-oriented programming, inheritance, composition, and file handling. The dated folders preserve learning in progress, including experiments and unfinished exercises.

Algorithms, scientific Python, and machine learning projects are future learning targets in the [roadmap](docs/roadmap.md). They are not completed portfolio projects. The Flight/Logbook examples below are practice models; a packaged CLI and automated test suite are still future work.

## Selected work

Start here for a short tour of the code and the concepts behind it.

| Example | What to look for | Discussion point |
| --- | --- | --- |
| [Flight and Logbook](week/04/1025/recall.py) | A logbook stores Flight objects, sums logged hours, and tracks starting aircraft hours | Why each instance needs its own list; composition; logged versus cumulative hours |
| [Grouping flight hours](week/04/1022/logbook.py) | A loop builds a dictionary of totals by flight type | Aggregation in one pass; handling an empty logbook |
| [Vehicle and Truck](week/04/1024/vehicle.py) | A child class calls `super()`, inherits a cost method, and overrides `describe()` | What belongs in a shared parent and what belongs in a specialized child |
| [Birthday search in pi](week/05/1026/test.py) | Reads a text file, searches its decimal digits, and reports a one-based position | Working-directory assumptions; input checks; zero-based versus one-based indexing |

These examples show the learning progression. Input validation, import-safe demonstrations, and automated regression tests are next steps before promoting them into reusable projects.

## Run examples

The examples above use only the Python standard library. Use Python 3.11 or newer; no package installation is needed for these commands.

```bash
git clone https://github.com/hmeyer8/omscs-prep.git
cd omscs-prep
python week/04/1025/recall.py
python week/04/1024/vehicle.py
```

The logbook demonstration prints **3.5 logged hours**, **103.5 current aircraft hours**, and **0 logged hours** for the separate logbook.

The pi exercise opens a file relative to the working directory. Run it from its own folder:

```bash
cd week/05/1026
python test.py
```

Enter a sequence such as `1415`; it starts at decimal digit **1**. See [development notes](docs/development.md) for the optional uv environment and the distinction between practice scripts and automated tests.

## Repository guide

| Location | Contents |
| --- | --- |
| [`week/`](week/) | Dated practice under `week/NN/MMDD/`; code and notes currently extend through week 05, with later week placeholders |
| [`journal/`](journal/README.md) | Reflection workflow and templates for daily entries and weekly reviews |
| [`reps/`](reps/) | Placeholder for future repetition drills |
| [`docs/roadmap.md`](docs/roadmap.md) | Original learning targets and proposed projects, explicitly marked as planned |
| [`docs/development.md`](docs/development.md) | Setup, execution, and verification conventions |
| [`pyproject.toml`](pyproject.toml) / [`uv.lock`](uv.lock) | Python requirements and the locked scientific Python environment |

## Learning process

1. **Recall:** attempt a small implementation from a blank file before checking references.
2. **Build:** work through a concept and check a normal case plus an edge case.
3. **Explain:** describe the behavior, design choices, and limitations in plain language.
4. **Reflect:** record the bug, its cause, the fix, and the next independent rebuild in the [journal](journal/README.md).

Preserve initial attempts so improvements remain visible. Journal entries should distinguish independent work from work completed with a book, documentation, hints, or AI assistance. A successful run is evidence for that example, not proof that every case works.

## Next milestones

- Extract one Flight/Logbook example into an importable module with a separate demonstration.
- Add automated checks for empty logbooks, independent state, and totals by flight type.
- Build introductory algorithm exercises with written runtime and space analysis.
- Develop NumPy and probability foundations, then add documented ML experiments.

## Sources and coursework

This is a personal preparation repository. Book and web exercises belong to their respective sources; retain attribution when adapting them. The practice files include exercises based on *Python Crash Course* by Eric Matthes and PYnative prompts. Additional planned references are listed in the [roadmap](docs/roadmap.md).

Keep graded course work and restricted course materials out of this public repository. Follow each course's collaboration and AI-use policies when coursework begins.
