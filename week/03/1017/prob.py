"""
PYTHON PRACTICE | OCTOBER 14-16, 2026
29 selected PYnative exercises + 1 adapted generator exercise.
Prompts are paraphrased; examples below are original practice inputs.
Source URLs and exercise numbers identify the corresponding website problems.
No solution implementations are included.

WORKFLOW
- Complete every numbered exercise in its scheduled day.
- Replace each pass with your work. Define additional helper functions as needed.
- Call the exercise you are working on in the main block at the bottom.
- Check a normal case and an edge case; note any hint or reference used.
- Use ordinary Python. No pandas, NumPy, classes, Counter or defaultdict needed.
- Concept checks and the logbook are separate tasks from our Notion plan.
- Rebuild selected functions from blank on October 17.
"""

# DAY 1 | WEDNESDAY, OCTOBER 14
# FUNCTIONS: website exercises 3, 4, 7, 10, 17, 18
# Source: https://pynative.com/python-functions-exercise-with-solutions/


def calculation(a,b):
    """
    Write calculation(a, b) to return both their sum and their difference.
    Call it and unpack the two results into separate variables.

    Practice input: a=27, b=8.
    Check another case with a negative number.
    """
    x = a+b
    y = a-b
    add = print(f"operations with values {a} and {b}:\nadd: ", x)
    sub = print("sub: ", y)
    
# calculation(27,8)

def show_employee(name, salary = 9000):
    """
    Define show_employee(name, salary) with a default salary of 9000.
    Display the employee's name and salary. Try supplying and omitting salary.

    Practice calls: employee "Henry" with salary 80000; employee "Maya" without it.
    """
    n = print(f"name: ", name)
    s = print(f"salary: ", salary)

# show_employee("henry", 80000)
# show_employee("maya")


def display_student(name, age):
    """
    Create display_student(name, age), then assign that function to a second
    name and invoke it through the new name.

    Practice input: name="Henry", age=22.
    Explain whether assigning the function also calls it.
    """
    print(f"name: ", name)
    print(f"age: ", age)
second = display_student # assigning the function doesnt actually call it, it just simply assigns a new pointer to point to the object display_student
# second(name = "Henry", age = 22)


def describe_pet(animal_type, pet_name):
    """
    Define describe_pet(animal_type, pet_name) to display a description.
    Invoke it once positionally and once with named arguments.

    Practice input: animal_type="dog", pet_name="Scout".
    For the named call, reverse the argument order.
    """
    print(f"My pet is a {animal_type}, and her name is {pet_name}")
# describe_pet("dog", "Sadie")
# describe_pet(pet_name= "fluffy", animal_type= "venomous snake")


def srec(rec):
    """
    Sort student records by their numeric score using sorted() and a lambda.

    Practice records: [("Maya", 86), ("Henry", 93), ("Noah", 79)].
    Check equal scores and an empty list.
    """
    x = print(sorted(rec, key= lambda y: y[1]))
    return x
# srec([("Maya", 86), ("Henry", 93), ("Noah", 79)])

def apply_operation(func,x,y):
    """
    Implement apply_operation(func, x, y), returning the result of invoking
    the supplied function on the two numbers. Demonstrate two operations.

    Practice input: x=12, y=5.
    Supply addition and multiplication functions you write yourself.
    """
    return func(x,y)
def add(x,y):
    z = x + y
    return z
def mul(x,y):
    b = x*y
    return b
# print(apply_operation(add,2,3))
# print(apply_operation(mul,2,3))

# LISTS AND ITERATION: website exercises 18, 20, 23, 38, 42
# Source: https://pynative.com/python-list-exercise-with-solutions/


def rm_oc(x, y):
    """
    Remove every occurrence of a chosen value from a list.

    Practice input: values=[4, 9, 4, 2, 4, 7], target=4.
    Check adjacent matches, no matches and an empty list.
    """
    result = []
    for n in x: 
        if n != y: 
            result.append(n)
        else: continue
    return result
# values=[4, 9, 4, 2, 4, 7]
# values = rm_oc(values, 4)
# print(values)

def dup_in(inp):
    """
    Produce a list containing one copy of each input value.
    For this practice version, preserve first-appearance order.

    Practice input: [8, 3, 8, 5, 3, 1, 5].
    Check input with all equal values and input with no duplicates.
    """
    x = []
    for n in inp:
        if n in x: continue
        else:
            x.append(n)
    return x
# values = [8, 3, 8, 5, 3, 1, 5]
# values1 = dup_in(values)
# print(values1)


def dup_in1(inp):
    """
    faster way to create a distinct list
    """
    st = set(inp)
    out = list(st)
    return out
# v2 = dup_in1(values)
# print(v2)

def glue(x,y):
    """
    Use zip() to traverse two lists together and display each pair.

    Practice input: names=["Henry", "Maya", "Noah"], scores=[93, 86, 79].
    Repeat with unequal lengths and explain which items are visited.
    """
    z = [(a,b) for a,b in zip(x,y)]
    return z

# names=["Henry", "Maya", "Noah"]
# scores=[93, 86, 79]
# print(glue(names,scores))

# the more direct answer would be the following: 
def glue1(x,y):
    for n,s in zip(x,y):
        print(n,s)
# glue1(names,scores)


def convL(x):
    """
    Convert a list of lists into one flat list, retaining element order.

    Practice input: [[6, 2], [], [9], [4, 1, 8]].
    Handle two levels only; recursion is outside this exercise.
    """
    # .append() adds an item to a list, .extend() adds a list of items to a list
    nl = [] 
    for n in x:
        nl.extend(n)
    return nl
# val = [[6, 2], [], [9], [4, 1, 8]]
# print(convL(val))

# if we wanted to do list comprehension then we'd need a nested loop:
def convLu(x):
    return [item for sub in x for item in sub]
# print(convLu(val))

def fun(values, n):
    """
    Write a function that builds a list of n size starting from the beginning

    Practice input: values=[2, 4, 6, 8, 10, 12, 14], n=3.
    Check an empty list and n larger than the input length.
    """
    out = []
    if values == '':
        print("empty")
    if n > len(values):
        print('too large of n for this list')
    for v in values: 
        if values.index(v)<n:
            out.append(v)
        else: continue
    return out
# values=[2, 4, 6, 8, 10, 12, 14]
# n=1
# value = fun(values,n)
# print(value)


# STRINGS: website exercises 7, 13
# Source: https://pynative.com/python-string-exercise/


def hy_in(value):
    """
    Separate a hyphen-delimited string and display the resulting pieces.

    Practice input: "Henry-is-learning-Python".
    Check text with no hyphen and an empty string.
    """
    out = ""
    for n in value:
        if n != '-':
            out += n
        
        else: 
            print(out)
            out=''
    print(out)
# val = "Henry-is-learning-Python"
# hy_in(val)

def triw(val):
    """
    Delete all ordinary spaces from a string, including internal spaces.

    Practice input: "  c o d e  ".
    Distinguish this requirement from trimming only the ends.
    """
    return ''.join(va for va in val if va != ' ')
print(triw(" c o d e "))
# simpler way is to use replace() and strip(). strip() goes and takes the trailing
# and leading white spaces. replace replaces the spaces with nothing

# val = " c o d e "
# s = val.strip()
# r = val.replace(' ', '')
# print(f"strip:{s}")
# print(f"replace:{r}")

# DAY 1 | ORIGINAL CONCEPT CHECKS FROM OUR PLAN
# These are supplementary tasks, not additional PYnative exercises.


def day1_concept_checks():
    """
    A. Demonstrate print versus return and tuple unpacking.
    B. Show local rebinding versus modifying a list passed into a function.
    C. Predict assignment, shallow copying and nested-list mutation.
    D. Reproduce a mutable-default-list bug; fix it using a None default.
    E. Demonstrate enumerate, slicing, lower and join on small inputs.
    F. After a break, rebuild two completed functions without looking.

    Write your explanations as comments alongside your demonstrations.
    """
    pass


# DAY 2 | THURSDAY, OCTOBER 15
# DICTIONARIES: website exercises 15, 19, 36, 38
# Source: https://pynative.com/python-dictionary-exercise-with-solutions/


def stod(value):
    """
    Build a dictionary counting each character in a string.

    Practice input: "level up".
    Include spaces as characters. Check empty input.
    """
    out = {}
    for i,v in enumerate(value):
        out[i] = v
    return out
# print(stod("level up"))


def nd(d):
    """
    Create a new dictionary retaining entries whose scores exceed 60.
    Leave the original dictionary unchanged.

    Practice input: {"Henry": 88, "Maya": 60, "Noah": 41, "Ava": 75}.
    Check the threshold boundary.
    """
    new_dict = {}
    for i,v in d.items():
        if v>60:
            new_dict[i] = v
    return new_dict
# values = {"Henry": 88, "Maya": 60, "Noah": 41, "Ava": 75}
# print(nd(values))


def rev(d):
    """
    Reverse a dictionary's mapping while retaining duplicate-value groups:
    each original value becomes a key associated with a list of original keys.

    Practice input: {"apg": "day", "qa": "night", "hydro": "day"}.
    Use an ordinary dictionary, not defaultdict.
    """
    return dict(reversed(d.items()))
# hi = {"apg": "day", "qa": "night", "hydro": "day"}
# print(rev(hi))


def group_words(words):
    """
    Group words into lists indexed by their initial letter.

    Practice input: ["crew", "code", "flight", "fuel", "aircraft"].
    Assume words are nonempty; check an empty input list.
    """
    lst = {}
    if words == '':
        print("empty input")
    for n in words:
        if n[0] in lst:
            lst[n[0]].append(n)
        else: lst[n[0]] = [n]
    return lst

# words = ["crew", "code", "flight", "fuel", "aircraft"]
# print(group_words(words))


# SETS: website exercises 5, 6, 7, 8
# Source: https://pynative.com/python-set-exercise-with-solutions/
# Shared practice input: 
a,b ={2, 5, 8, 11}, {5, 11, 14}


def union(a,b):
    """
    Find the union of the two practice sets.
    Keep the originals unchanged.
    """
    un = a.union(b)
    return un
# c = union(a,b)
# print(f"a: {a}\nb: {b}\nc:{c}")


def int(a,b):
    """
    Find their intersection.
    Also try two sets with no common members.
    """
    e = {6,7,9}
    c = a&b
    d = a&e
    print(f"c: {c}\nd: {d}")
# int(a,b)


def a_not_b(a,b):
    """
    Find the members of a absent from b.
    Reverse the order and explain the difference.
    """
    c = a ^ b
    print(f"c: {c}")
# a_not_b(a,b)


def q21_sets_08():
    """
    Find members belonging to exactly one of the two sets.
    Also try identical sets.
    """
    pass


# COMPREHENSIONS: website exercises 5, 12, 17, 18
# Source: https://pynative.com/python-comprehensions-exercises/


def flatten_list(value):
    """
    Flatten a two-dimensional list with a nested list comprehension.

    Practice input: [[7, 3], [2], [], [8, 4]].
    Afterwards express the same transformation using ordinary nested loops.
    """
    out = [w for x in value for w in x]

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
    out = [x for i in inp for x[n] in i; n=0, n++]
    return out
h = [[2, 4, 6], [1, 3, 5], [7, 8, 9]]
print(transp(h))

def q24_comprehensions_17():
    """
    Pair equal-length key and value lists in a dictionary comprehension.
    Replace None values with "N/A"; retain zero, False and empty strings.

    Practice keys: ["pilot", "hours", "solo", "note", "aircraft"].
    Practice values: ["Henry", 0, False, "", None].
    """
    pass


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

