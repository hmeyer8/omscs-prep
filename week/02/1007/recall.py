# RECALL | October 7, 2026 | 20 minutes | NO ANSWERS
# Sources: https://github.com/hmeyer8/omscs-prep (commit 84bdc67)
# New material: week/01/1003/notes.md, updated October 6.
# Earlier practice: week/01/1003/recall.py and week/01/1002/notes.md.
#
# Work from memory: no notes, docs, old code, or AI.
# Move on when each section's time expires; leave unfinished work visible.
# Predictions: write them BEFORE running the question snippets.
# Run this as a script from your terminal, not at the Python >>> prompt.
# No packages or external files needed. Send back your completed file.


# 1. PREDICT: LISTS + MUTATION | 3 minutes
# Predict every printed line, then uncomment and run this snippet.

a = [3, 1]
b = a                 #b references a now
c = a.copy()          #c is a new copy of a
b.append([2, 4])      #a is now [3,1,[2,4]]
c.extend([2, 4])      #c is now [3,1,2,4]
print(a)              
print(c)
result = c.sort()     #result is [1,2,3,4]
print(c)              #c is still [3,1,2,4]
print(result)         #^^
#
# Predictions:
#
# Explain why changing b affects a but changing c does not here:
# because b points to a
# Explain the difference between append and extend:
# append concatenates one value to a list. In this instance[2,4] was seen as one value. extend() concatenates a list to a list.


# 2. REBUILD: CONTROL FLOW + A FUNCTION | 4 minutes
names = ["", "Henry", "Sam", "Alexandra", "Will", "", "Jo", "Henry"]
# Write categorize_names(names) with a one-sentence docstring.
# Return a tuple of three independent lists, preserving order and duplicates:
# - short: 1-3 letters; medium: 4-5 letters; long: 6+ letters.
# Use a regular loop, continue for blanks, and if/elif/else.
# Leave the input unchanged. Do not print inside the function.
# Call it, unpack its return value into three variables, and print them.
#
# YOUR CODE:

def categorize_names(names):
    """function to categorize the initial list of names"""
    short, medium, long = [],[],[]
            
    for n in names:
        if n == "": continue
        elif len(n) <=3:
            short.append(n)
        elif len(n) <=5:
            medium.append(n)
        else:
            long.append(n)
    return short,medium,long
short, medium, long = categorize_names(names)
print("short:{0}, medium:{1}, long:{2}".format(short,medium, long))

# 3. COMPREHENSIONS + ENUMERATE | 4 minutes
# Using names above:
# A. In ONE list comprehension, collect nonempty names of at least 4 letters.
# B. In ONE dict comprehension, map each nonempty name to its length.
# Print both. Explain what happens to the repeated Henry in each result.
# C. In a separate loop, use enumerate to print each nonempty name with its
# ORIGINAL zero-based index. Stop AFTER printing the first name over 7 letters.
#
# YOUR CODE:
lc = [n for n in names if len(n)<=4]
dc = {n: len(n) for n in names if n}

for i,v in enumerate(names):
    if v == "": continue
    print(i,v)
    if len(v) > 7: break
# Explanation of repeated names:
#


# 4. DICTIONARIES + ZIP | 5 minutes
words = ["apple", "bat", "apple", "bar", "bat", "atom"]
aircraft = ["Cessna", "Grumman", "Mooney"]
hours = [1.2, 0.8, 1.5]
# A. Write word_counts(words): return a dictionary of word -> occurrence count.
# Use a regular loop and dict.get; no Counter, count(), or imports.
# Call it and print each word and count using a loop over .items().
# B. Use zip to build aircraft_hours, a dictionary mapping aircraft to hours.
# Retrieve hours for "Pilatus" with a default of 0; print the result.
# C. In a comment, predict what zip would do if hours had only TWO entries.
#
# YOUR CODE:

def word_counts(words):
    unq= {}
    for n in words:
        unq[n] = unq.get(n,0) + 1
    return unq


# Prediction for unequal lengths:
#


# 5. SETS + TUPLE UNPACKING | 3 minutes
day_shift = {"Henry", "Sam", "Will"}
night_shift = {"Sam", "Jo"}
flight = ("Grumman", 1.4, "dual")
# A. Build and print sets for: people on both shifts; people only on days;
# everyone on either shift. Set display order does not matter.
# B. Unpack flight into plane, duration, and training_type, then print them.
# C. Can you replace flight[1] with 2.0? Can a list stored inside a tuple
# be changed? Explain both in comments; no need to run failing code.
#
# YOUR CODE:

# Tuple explanation:
#


# 6. STOP + LOG | 1 minute
# Finished without help:
# Got stuck on:
# Prediction that surprised me:
# One thing to revisit today:
# Actual time spent:
# STOP at 20 minutes. Keep mistakes and unfinished sections for review.
