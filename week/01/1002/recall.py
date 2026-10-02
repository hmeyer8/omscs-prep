# 10/02 Python Recall — PT through §4.7
#
# Do this from a blank file.
# Do not use notes, the Python tutorial, old code, or AI until you finish your first attempt.
#
# 1. Create a list of at least 8 names, including one empty string.
names = ['Henry', 'sam', 'Will', '', 'fred', 'frank', 'luke', 'cam']
print("names = ", len(names))
#
# 2. Create three empty lists using multiple assignment.
short, med, long = [], [], []

# 3. Loop directly over the names.
# 4. Use continue to skip the empty name.
#
# 5. Use len() with if / elif / else to categorize each name as
#    short, medium, or long.
# 6. After the loop, print the first and last valid names using indexing.
for n in names:
    if n == '':
        continue
    if len(n) < 4:
        short.append(n)
    elif len(n) == 4:
        med.append(n)
    else: 
        long.append(n)

print("first: ", names[:1])
print("last: ", names[len(names)-1:])

# 7. Write a second loop using range() that prints the index
#    and corresponding name.
num = {}
for i in range(len(names)):
    print(i, names[i])
    if i ==3:
        pass
    
# 8. In the second loop, use break to stop once you encounter
#    a name longer than 7 characters.
#
# 9. Write one intentionally empty conditional branch using pass.
#
# 10. Write this function:
#
def describe_name(name, category="unknown"):
    return type(name)
#
# Have it return a useful formatted string describing the name.
#
# 11. Call describe_name() several times using:
#     - positional arguments
#     - keyword arguments
#     - the default value for category
#
# 12. Before running the file, predict the exact output below.
#
#
# MEMORY CHECK
#
# Answer these from memory in comments:
#
# 1. What is the difference between break, continue, and pass?
# break breaks out of the innermost loop, continue moves onto the next iteration and pass makes a function a placeholder
# 2. Why is:
#
#       for name in names:
#
#    often preferable to:
#
#       for i in range(len(names)):
# because we could use enumerate on the first one? ends up being cleaner and faster.
#
# 3. What does names[-1] mean?

# returns the final name
# 4. What happens when a function reaches return?
# 
# 5. What is a default argument?
#
# 6. What is the difference between a positional argument
#    and a keyword argument?
# position is found through indexing, keyword is found through ==?
#
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