# I want to recall for, continue, break, pass, multiple assignments, indexing. I think I will use names.txt from makemore
# 1. Make a small names list manually.
# 2. Create three empty lists with multiple assignment.
# 3. Loop over names directly.
# 4. Skip blank names with continue.
# 5. Categorize based on len(name).
# 6. Write a second loop that breaks on the first name longer than 1 letters.

with open("C:/Users/henme/.code_space/omscs-prep/week/01/data/names.txt", "r") as f:
    names = f.read().splitlines()

small, med, large = [], [], []
for n in names: 
    if len(n) == "":
        continue
    elif len(n) < 3:
        small.append(n)
    elif len(n) > 13:
        large.append(n)
        print(f"{n} is {len(n)} characters long")
    else: pass
