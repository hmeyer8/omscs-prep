# ============================================================
# RECALL | October 3, 2026 | 15 minutes
# ============================================================
# Work from memory. No notes, docs, old code, or AI assistance.
# Prediction sections: write answers BEFORE running the snippets.
# When time expires, stop and mark unfinished work.
# Send back your whole file, including mistakes and predictions.


# ------------------------------------------------------------
# 1. LOOPS + INDEXING | 3 minutes
# ------------------------------------------------------------
names = ["", "Henry", "Sam", "Alexandra", "Will", "", "Jo"]

# Create three INDEPENDENT empty lists using multiple assignment:
# short_names, medium_names, long_names.
#
# Loop directly over names:
# - Skip empty strings using continue.
# - Categorize valid names:
#     short: 1–3 characters
#     medium: 4–5 characters
#     long: 6+ characters
# - Print the three lists.
#
# Then use enumerate() in a separate loop:
# - Skip empty strings.
# - Print each valid name with its ORIGINAL index.
# - Stop immediately AFTER printing the first name longer than 7 letters.

# YOUR CODE:
short, med, long = [],[],[]
def sort(name):
    for n in name:
        if len(n)<=3:
            short.append(n)
        print("short: ", n)

        elif len(n)<=5:
            med.append(n)
        print("medium: ", n)
        else: 
            long.append(n)
        print("long: ", n)

# ------------------------------------------------------------
# 2. FUNCTIONS FROM MEMORY | 5 minutes
# ------------------------------------------------------------
# Write collect_names(names, min_length=4).
#
# Requirements:
# - Include a one-sentence docstring.
# - Return a NEW list of nonempty names whose length is at least
#   min_length, preserving their original order.
# - Use a regular loop.
# - Leave the input list unchanged.
# - Do not print inside the function.
#
# Call it three ways and print each returned list:
# 1. Use the default min_length.
# 2. Supply min_length=3 positionally.
# 3. Supply both arguments by keyword, with min_length=6.
#
# Finally:
# - Assign the FUNCTION OBJECT to another name.
# - Call the function through that new name.

# YOUR CODE:


# ------------------------------------------------------------
# 3. PREDICT + EXPLAIN | 4 minutes
# ------------------------------------------------------------
# These snippets are questions, not model solutions.
# Predict EVERY printed line before running them.

# A. Local scope + implicit return
score = 10

def show_score():
    score = 3
    print(score)

# Prediction:
# Why?
#
# Uncomment ONLY after writing your prediction:
# result = show_score()
# print(score)
# print(result)


# B. When is a default value evaluated?
limit = 4

def show_limit(value=limit):
    return value

limit = 9

# Prediction:
# Why?
#
# Uncomment ONLY after writing your prediction:
# print(show_limit())
# print(show_limit(limit))


# C. Mutable defaults
def remember_name(name, saved=[]):
    saved.append(name)
    return saved

# Prediction:
# Why?
#
# Uncomment ONLY after writing your prediction:
# print(remember_name("Henry"))
# print(remember_name("Sam"))

# Now write a SEPARATE function, remember_name_fresh:
# - With no list supplied, each call must use a fresh list.
# - With a list supplied, append to and return that same list.
# - Demonstrate both behaviors with calls.
# Write it from memory.

# YOUR CODE:


# ------------------------------------------------------------
# 4. EXPLAIN IN YOUR OWN WORDS | 2 minutes
# ------------------------------------------------------------
# Answer briefly in comments.
#
# 1. How do break, continue, and pass differ?
# Answer:
#
# 2. How do printing a value and returning it differ?
# Answer:
#
# 3. If a function receives a list, how does appending to it
#    differ from assigning its parameter to a new list?
# Answer:


# ------------------------------------------------------------
# 5. STOP + LOG | 1 minute
# ------------------------------------------------------------
# Finished without help:
#
# Got stuck on:
#
# Predictions that differed from the actual output:
#
# One thing I need to revisit today:
#
# STOP at 15 minutes. Leave unfinished sections visible.