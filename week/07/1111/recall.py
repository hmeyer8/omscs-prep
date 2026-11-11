# NOVEMBER 11, 2026 — FLUENT PYTHON CHAPTER 2 RECALL
# 20 minutes. Close notes, old code, and no AI autocomplete.
# Predict before running. Save your first attempt before looking anything up.

# 1. BUILT-IN SEQUENCES | 0:00–4:00
# For list, tuple, str, bytes, and bytearray, give two classifications:
# container or flat, and mutable or immutable.
# Container holds reference to the object they contain. 
# Flat is stored locally so we can only store rutimentary sequence types
# List is mutable, container. Tuple is immutable, container. 
# Str is immutable, flat. Byte is immutable, flat. Bytearray is mutable, flat
# What does a container sequence store that a flat sequence doesn't?
# references to the object
# Can you append to the list inside record = ("KC-135", [2.5])? No, tuple
# Can you replace record[1] with a different list? Explain both predictions. No, immutable

# Write your answers here.


# 2. BUILD BOTH ORDERS | 4:00–12:00
aircraft = ["KC-135", "C-17"]
checks = ["walkaround", "hydraulics", "avionics"]

# Use two list comprehensions to pair every aircraft with every check.
# Each item is a tuple with aircraft first and check second in BOTH lists.
# - by_aircraft: every check for the first aircraft, then the second.
# - by_check: both aircraft for the first check, then the next check.
# Preserve the input order within each group.
# Before running, write the first three pairs of each list in comments.
# Then print each list and compare it with your prediction.

# Write your code here.
from collections import namedtuple
Process = namedtuple('Process', ['ac', 'check'])
class ProcessChecks:
    aircraft = ["KC-135", "C-17"]
    checks = ["walkaround", "hydraulics", "avionics"]
    def __init__(self):
        self.by_aircraft = [Process(ac, check) for ac in aircraft for check in checks]
        self.by_check = [Process(ac, check) for check in checks for ac in aircraft]
    def print(self):
        print("by_aircraft:\n", self.by_aircraft)
        print("by_check:\n", self.by_check)

chk = ProcessChecks()
chk.print()
        
# 3. REBUILD ONE WITH LOOPS | 12:00–16:00
# Rebuild by_check with ordinary nested for loops and append.
# Use a new empty list and verify that it equals by_check in order and value.
# In one sentence, explain how you chose which loop went on the outside.

# Write your code and explanation here.


# 4. REPAIR THE PRINT LOOP | 16:00–19:00
cards = [("2", "spades"), ("3", "spades"), ("2", "hearts")]

# Predict what happens if this line is uncommented.
# print(rank, suit) for rank, suit in cards[:2]
# Rewrite it below so it prints the rank and suit of each of the first
# two cards on its own line. Unpack each pair in the loop.

# Write your prediction and code here.


# 5. LOG | 19:00–20:00
# What did I rebuild from memory?
# What is one specific thing I need to practice again?

# took longer than 20 minutes but that was my attempt at the recalls