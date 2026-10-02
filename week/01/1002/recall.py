# 10/02 Python Recall — PT through §4.7
#
# Do this from a blank file.
# Do not use notes, the Python tutorial, old code, or AI until you finish your first attempt.
#
# 1. Create a list of at least 8 names, including one empty string.

names = ['Henry', 'sam', 'Will', '', 'fred', 'Alexander', 'luke', 'cam']

print("number of names:", len(names))


# 2. Create three empty lists using multiple assignment.

short, med, long = [], [], []


# 3. Loop directly over the names.
# 4. Use continue to skip the empty name.
# 5. Use len() with if / elif / else to categorize each name as
#    short, medium, or long.

for name in names:
    if name == '':
        continue

    if len(name) < 4:
        short.append(name)
    elif len(name) == 4:
        med.append(name)
    else:
        long.append(name)


print("short:", short)
print("medium:", med)
print("long:", long)


# 6. After the loop, print the first and last valid names using indexing.
#
# names[0] gives one element.
# names[-1] gives the last element.

print("first:", names[0])
print("last:", names[-1])


# 7. Write a second loop using range() that prints the index
#    and corresponding name.
#
# 8. In the second loop, use break to stop once you encounter
#    a name longer than 7 characters.
#
# 9. Write one intentionally empty conditional branch using pass.

for i in range(len(names)):
    print(i, names[i])

    if i == 3:
        pass

    if len(names[i]) > 7:
        break


# 10. Write this function:
#
# def describe_name(name, category="unknown"):
#
# Have it return a useful formatted string describing the name.

def describe_name(name, category="unknown"):
    return name + " is in the " + category + " category."


# 11. Call describe_name() several times using:
#     - positional arguments
#     - keyword arguments
#     - the default value for category

print(describe_name("Henry", "long"))

print(describe_name(
    name="sam",
    category="short"
))

print(describe_name("Will"))


# 12. Before running the file, predict the exact output below.


# MEMORY CHECK
#
# 1. What is the difference between break, continue, and pass?
#
# break exits the innermost loop.
# continue skips the rest of the current iteration and moves to the next one.
# pass does nothing. It can be used as a placeholder statement.
#
#
# 2. Why is:
#
#       for name in names:
#
#    often preferable to:
#
#       for i in range(len(names)):
#
# Direct iteration is cleaner when I only need the elements themselves.
# If I need both the index and the element, I can use enumerate().
#
#
# 3. What does names[-1] mean?
#
# It returns the last element in the list.
#
#
# 4. What happens when a function reaches return?
#
# The function immediately stops running and sends a value
# back to wherever the function was called.
#
#
# 5. What is a default argument?
#
# A default argument is a value Python uses when the caller
# does not provide a value for that parameter.
#
#
# 6. What is the difference between a positional argument
#    and a keyword argument?
#
# A positional argument is matched to a parameter based on its position.
# A keyword argument explicitly names the parameter using parameter=value.
#
#
# PARAMETERS VS ARGUMENTS
#
# In:
#
# def describe_name(name, category="unknown"):
#
# name and category are parameters.
#
# In:
#
# describe_name("Henry", "long")
#
# "Henry" and "long" are arguments.


# PREDICTED OUTPUT
#
# Write your prediction here before running the program:
#
#
# GATE
#
# Only run the file after you have completed the first attempt.
# Fix syntax errors yourself first.
# Then compare your predicted output with the actual output.