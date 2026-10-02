#my daily attempt to wage war against mediocrity 
# ============================================================
# RECALL · Thu Oct 1 · PT Ch 3 → 4.7 · 15 min, blank file
# No docs, notes, old code, or AI. Top-level code only (no def).
# Run as you go. Check the numbers at the bottom when done.
# ============================================================

# --- 1. Load + basics (3 min) ---
# Load names.txt into `words` with .read().splitlines().
# Print: the count, the first 5, the last 3 (negative index),
# and every 5000th name (one slice).
# Loop once (no min/max) to find the longest and shortest names.
# Sum all letters across names. Print the average with /, then the same total with // and %.
#1: 
with open("C:/Users/henme/.code_space/omscs-prep/week/01/data/names.txt", "r") as f:
     words = f.read().splitlines()

# print("count:", len(words))
# print("first five:", words[:5])
# print("last 3:", words[-3:])
# print("every 5000th name:", words[::5000])
# big = words[0]
# small = words[0]
# total = 0
# for w in words:
#     if len(w) < len(small):
#         small = w 
#     if len(w) > len(big):
#         big = w
#     total += len(w)

# print(big, small)
# print(total/len(words), total // len(words), total % len(words))


# --- 2. for / range / enumerate (2 min) ---
# enumerate the first 5 names: print "0 emma", "1 olivia", ...
# Print every 5000th name again, this time with range(start, stop, step).
# Build a new list `short` of names with 3 or fewer letters.

for i, name in enumerate(words[:5]):
    print(i,name)

for i in range(0, len(words), 5000):
     print(words[i])

a = []
for  i in words:
     if len(i) <=3:
          a.append(i)

print(len(a))
# --- 3. break / continue / loop-else (4 min) ---
# for/else: find the first name starting with "q" whose 2nd letter isn't "u".
#   Print the name and its index. The else prints "none found".
# Same structure: first name with 16+ letters (the else should run).
# continue: skip names under 4 letters and count the rest.
# Prime lengths: rebuild the tutorial's prime loop (nested for + else)
#   for lengths 2 up to the longest name's length, then count the names with a prime length.

for w in words:
     for i in w:
        if i[0] == 'q' and i[1] not 'q':
        print(w)
        break
        else: break
break
            
               

# --- 4. match (6 min) ---
# 4a. match name[0]: vowels in ONE case using |, then "y", then _.
#     Print the three counts.
# 4b. match list(name), cases in this order:
#       exactly two letters
#       palindrome (guard)
#       first == last (capture both, guard)
#       ends in "ey" or "ie" (one case, two patterns joined with |)
#       _ -> pass
#     Print the five counts. They should add up to the total.
# 4c. match (name[0], name[-1], len(name)):
#       starts and ends with "a" (capture length, track the longest)
#       ends in "n" with 12+ letters (capture first letter, guard, collect into a list)
#       2 | 3 inside the tuple, bound with `as t`
#       _


