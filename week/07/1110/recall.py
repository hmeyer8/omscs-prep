# NOVEMBER 10, 2026 — FLUENT PYTHON, CHAPTER 1
# 20 minutes | first attempt | no answers included
#
# Based on your latest committed deck recall and Vector practice.
# Recall ONLY Chapter 1. Start Chapter 2 after this attempt.
# Close notes, old code, and AI autocomplete. Running your code is allowed.
# Predict before running. Move on at each time limit; leave TODOs if stuck.
# Save this first attempt before looking anything up. Repair in another file.

from collections import namedtuple
from math import hypot


# PART 1 — EXPLAIN | 0:00–2:00
# Answer in your own words, as comments.
#
# 1. Give two examples of ordinary Python syntax or built-ins that
#    a custom class can support through special methods.
# Answer:
def __len__(self):
    return len(self._card)
def __getitem__(self, position):
    return self._card[position]
#
# 2. How do repr(obj) and str(obj) differ in purpose?
#    If a class defines only __repr__, what happens with print(obj)?
# Answer:
#   it appears normally. If that repr wasnt there then it would say class at <0x....>
# 3. Why normally write len(obj) instead of calling obj.__len__()?
# Answer: because the built in would call the CPython that already has len of an object stored


# PART 2 — A CHANGED DECK | 2:00–8:00
# Create a Card namedtuple with rank and suit fields.
# Create MiniDeck, with its OWN list of 12 Card objects per instance.
# Ranks: '2', '3', '4', '5'. Suits: 'spades', 'hearts', 'clubs'.
# Required order: ALL spades in ascending rank, then ALL hearts,
# then ALL clubs. Pay attention to the nesting of your loops.
#
# Implement only the special methods needed for length and item access.
# Do not inherit from list or add __iter__ / __contains__.
#
# Your implementation:
Card = namedtuple('Card', ['rank', 'suit'])
class MiniDeck:
    ranks = [str(n) for n in range(2,6)]
    suits = 'spades hearts clubs'.split()
    def __init__(self):
        self._card = [Card(rank,suit) for rank in self.ranks
                                      for suit in self.suits]
    def __len__(self):
        return len(self._card)
    def __getitem__(self, position):
        return self._card[position]   
deck = MiniDeck()
print(len(deck))
print(deck[:1])
print(deck[-1:])
print(deck[:4])
print(d,r) for rank, suit in deck[:4]
# Write predictions in comments FIRST, then write demonstrations using
# ordinary Python syntax to:
# - Get the length, first card, and last card.
# - Slice out the first four cards.
# - Iterate over that slice and print each card's rank and suit.
# - Check membership for Card('4', 'hearts') and Card('A', 'hearts').
#
# Predictions and demonstrations:


# Explain why iteration can work without your defining __iter__.
# What exception signals the end of integer-index iteration?
# Answer:


# PART 3 — VECTOR FROM MEMORY | 8:00–15:00
# Create Vector(x=0, y=0). Choose the special methods needed for:
# - repr(v): a readable representation such as Vector(6, 8).
# - abs(v): magnitude; you may use the imported hypot.
# - bool(v): False for the zero vector, True otherwise.
# - v + w: componentwise addition, returning a NEW Vector.
# - v * number: scaling, returning a NEW Vector.
#
# Assume valid operands. No validation, equality, or reflected operators.
# Your implementation:


# Use v = Vector(6, 8) and w = Vector(-2, 1).
# Predict repr(v), abs(v), bool(v), bool(Vector()), repr(v + w),
# and repr(v * 2). Then write code to check your predictions.
# Finally inspect v and w to check that arithmetic did not mutate them.
#
# Predictions and demonstrations:


# PART 4 — TRUTH TESTING | 15:00–19:00
# Answer in comments. Verify only AFTER recording your predictions.
#
# 1. In what order does Python decide the truth value of an object?
#    Include the default when neither relevant special method exists.
# Answer:
#
# 2. Suppose you remove Vector's __bool__ method and it has no __len__.
#    It still defines __abs__. Predict bool(Vector(0, 0)) and explain.
# Answer:
#
# 3. A class defines __len__ returning 0 and __bool__ returning True.
#    Predict bool(instance) and explain which method takes priority.
# Answer:
#
# 4. What type must __bool__ return? Why is returning self.x directly
#    an unreliable implementation for Vector?
# Answer:


# PART 5 — LOG | 19:00–20:00
# Strongest independent rebuild or explanation:
#
# One specific gap to repair:
#
# Evidence: independent / with hints or docs / not yet
#
# Actual minutes:
#
# STOP. Save this attempt. Then repair separately and start Chapter 2.
