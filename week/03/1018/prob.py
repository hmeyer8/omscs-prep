# COMPREHENSIONS: website exercises 5, 12, 17, 18
# Source: https://pynative.com/python-comprehensions-exercises/


def flatten_list(value):
    """
    Flatten a two-dimensional list with a nested list comprehension.

    Practice input: [[7, 3], [2], [], [8, 4]].
    Afterwards express the same transformation using ordinary nested loops.
    """
    out = [  w for x in value for w in x]

    # out = []
    # for x in value: 
    #     for w in x:
    #         out.append(w)
    return out
# v = [[7, 3], [2], [], [8, 4]]
# print(flatten_list(v))


def transp(inp):
    """
    Use a nested comprehension to transpose a 3-by-3 matrix.

    Practice input: [[2, 4, 6], [1, 3, 5], [7, 8, 9]].
    Leave the original matrix unchanged.
    """
    out = [[row[x] for row in inp] for x in range(len(inp))]
    return out
h = [[2, 4, 6], 
     [1, 3, 5], 
     [7, 8, 9]]
# print(transp(h))

def kvl(ky,vl):
    """
    Pair equal-length key and value lists in a dictionary comprehension.
    Replace None values with "N/A"; retain zero, False and empty strings.

    Practice keys: ["pilot", "hours", "solo", "note", "aircraft"].
    Practice values: ["Henry", 0, False, "", None].
    """
    dc = {k: ('N/A' if v is None else v) for k,v in zip(ky,vl)}
    # for k,v in zip(ky,vl):
    #     if v is None:
    #         v = "N/A"
    #     dc[k] = v
    return dc

ky = ["pilot", "hours", "solo", "note", "aircraft"]
vl = ["Henry", 0, False, "", None]
print(kvl(ky,vl))

def q25_comprehensions_18():
    """
    Use a set comprehension to collect numbers appearing in both lists.
    Each shared number should appear once.

    Practice lists: [2, 5, 5, 8, 11] and [5, 8, 8, 14].
    """
    pass


def q26_generators_20_adapted():
    """
    ADAPTED to our current scope: create a lazy expression for squares from
    1 through 1,000,000; retrieve just ten values with a loop. Then write
    an equivalent function using yield and demonstrate exhaustion.

    Omit the website's islice and memory-measurement requirements for now.
    """
    pass


# DAY 2 | ORIGINAL CONCEPT CHECKS FROM OUR PLAN


def day2_concept_checks():
    """
    A. Translate one nested comprehension into ordinary loops.
    B. Explain hashable keys; compare a tuple of integers with a tuple
       containing a list.
    C. Demonstrate grouping using an ordinary dictionary of lists.
    D. Explain return versus yield and when a generator executes.
    E. Rebuild a grouping function and generator from blank.
    """
    pass


# DAY 3 | FRIDAY, OCTOBER 16
# FILES AND EXCEPTIONS: website exercises 9, 18, 19, 20
# Source: https://pynative.com/python-file-handling-exercises/
# Create your own small files in a practice directory; use UTF-8.


def q27_files_09():
    """
    Attempt to read an absent file and handle FileNotFoundError
    with a useful message.

    Practice path: "practice_data/does_not_exist.txt".
    """
    pass


def q28_files_18():
    """
    Count alphabetic characters in a file, ignoring case and nonletters.

    Create "letters.txt" containing:
        Code, code!
        Fly.
    Store counts in an ordinary dictionary; also check an empty file.
    """
    pass


def q29_files_19():
    """
    Search a file for a term and display matching one-based line numbers.
    For this version, match substrings without case sensitivity.

    Create "search.txt" containing:
        Flight practice today.
        Working through Python.
        A quiet afternoon.
        More PYTHON tomorrow.
    Search for "python".
    """
    pass


def q30_files_20():
    """
    Read a file, trim each line's surrounding whitespace, and write
    the cleaned lines to a different file.

    Create "messy.txt" with padded lines, tabs and a blank line.
    Preserve line boundaries and leave the input file intact.
    """
    pass


# DAY 3 | ORIGINAL FUNCTIONAL LOGBOOK FROM OUR PLAN
# This is our readiness project, not copied from PYnative.
#
# Make a small UTF-8 input file with simple comma-separated rows:
# 2026-10-14,C172,1.2,dual
# 2026-10-15,PA28,0.8,solo
# 2026-10-16,C172,not-a-number,dual
# 2026-10-16,C172,-0.5,night
# 2026-10-16,C172,0.6,dual
#
# Assume no header and no fields with quoted commas.
# Keep dates as strings. A valid record is a dictionary with keys:
# date, aircraft, duration, type. Duration is numeric.
# The date's calendar validity is outside this task.


def parse_row(line):
    """Parse four fields; trim spaces; reject bad fields or negative duration."""
    pass


def read_flights(path):
    """Collect valid records; report rejected line numbers; handle missing input."""
    pass


def total_hours(flights):
    """Return the sum of durations; return zero for an empty collection."""
    pass


def hours_by_type(flights):
    """Return duration totals grouped by flight type."""
    pass


def write_summary(flights, path):
    """Write a readable UTF-8 report of total duration and totals by type."""
    pass


def day3_verification():
    """
    Hand-calculate expectations, then check:
    - ordinary valid records;
    - an empty input file;
    - a nonnumeric duration;
    - a negative duration;
    - a missing input file.

    Explain with, text versus binary input and characters versus UTF-8 bytes.
    Practice importing a calculation helper from another local module;
    consult a brief reference if modules are new.
    """
    pass


# OCTOBER 17 | RETENTION AND OOP READINESS
# Rebuild parse_row and hours_by_type in a separate blank file.
# Preserve working code and unchanged checks.
# Explain argument passing, mutation, grouping and error handling.
# Use no solutions, notes, old code or AI during the cold attempt.


if __name__ == "__main__":
    # Call the exercise you want to work on here.
    # Nothing runs or creates files until you add your own calls.
    pass