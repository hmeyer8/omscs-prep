# NOVEMBER 8 — FLUENT PYTHON CHAPTER 1
# 20 minutes. No notes, previous code, or AI autocomplete.
# Run your code for feedback, but predict results first.
# Move on when each block ends; leave TODOs where needed.
# Save your initial attempt BEFORE looking anything up.

from collections import namedtuple
from math import hypot


# ============================================================
# PART 1 — EXPLAIN | 0:00–2:00 (2 minutes)
# ============================================================
# Answer in comments.
#
# 1. What does the Python data model let custom classes do?
#    Give two examples involving built-ins or operators.
# Answer: Say for the FrenchDeck class, the Python Data Model allows us to route
#         the len() method to _card. Also for the iter() built in, being able to rewrite the __getitem__
#         special method for each instance of the FrenchDeck class allows usability of slicing/indexing
#         to be straightlined to the _card variable. 
#
# 2. Why normally write len(obj) instead of obj.__len__()?
#    Who normally invokes special methods?
# Answer: We normally write len(obj) because the CPython has code that makes the usability of the len() 
#         method more adaptable. Meta programmers normally use the special methods instead of built ins
# 3. How do __repr__ and __str__ differ?
#    What happens when you print an object with only __repr__?
# Answer: The cool part about dunder repr is that every object we try to inspect goes through that representation
#         method. The dunder str is only called when it is attached to an object.


# ============================================================
# PART 2 — REBUILD THE DECK | 2:00–8:00 (6 minutes)
# ============================================================
# Create:
#
# - A Card namedtuple with rank and suit fields.
# - A FrenchDeck class with its own list of 52 cards per instance.
# - Ranks: 2 through 10, then J, Q, K, A.
# - Suits: spades, diamonds, clubs, hearts.
# - Order: all spades, then diamonds, then clubs, then hearts.
#   Within each suit, ranks ascend.
#
# Implement ONLY the two special methods needed for:
# - Length.
# - Item access.
#
# Do not inherit from list.
#
# Your implementation:
Card = namedtuple( 'Card', ['rank', 'suit'])
class FrenchDeck:
    rank = [str(n) for n in range(2,11)] + list('JQKA')
    suit = 'spades clubs diamonds hearts'.split()
    def __init__(self):
        self._card = [Card(rank,suit) for rank in self.rank
                                      for suit in self.suit]
    def __len__(self):
        return len(self._card)
    def __getitem__(self, position):
        return self._card[position]

deck = FrenchDeck()
count = [n for n in deck]
print(count)
# Demonstrate using ordinary Python syntax:
# - Get the length.
# - Retrieve the first and last cards.
# - Retrieve the first three cards with a slice.
# - Iterate over those three cards and print their fields.
# - Check whether the queen of hearts belongs to the deck.
#
# Your demonstrations:


# Explain: you wrote no __iter__ or __contains__.
# How can iteration and membership still work?
# What tells Python that integer-index iteration has ended?
# Answer:


# ============================================================
# PART 3 — REBUILD VECTOR | 8:00–16:00 (8 minutes)
# ============================================================
# Create Vector with x and y coordinates, both defaulting to 0.
#
# Choose and implement the special methods that support:
#
# - repr(v): a readable string such as Vector(3, 4).
# - abs(v): its magnitude; you may use the imported hypot.
# - bool(v): False for the zero vector, True otherwise.
# - v + w: componentwise addition, returning a NEW Vector.
# - v * scalar: scaling, returning a NEW Vector.
#
# Leave the original objects unchanged.
# Assume another Vector for addition and a number for scaling.
# No equality, reflected multiplication, or validation required.
#
# Your implementation:


# Using v = Vector(3, 4) and w = Vector(1, -2):
#
# FIRST predict these results in comments:
# - repr(v)
# - abs(v)
# - bool(v)
# - bool(Vector())
# - repr(v + w)
# - repr(v * 3)
#
# THEN write and run demonstrations.
# Inspect v and w afterward to check that neither changed.
# Also demonstrate that arithmetic returned new objects.
#
# Predictions and demonstrations:


# ============================================================
# PART 4 — REASON | 16:00–19:00 (3 minutes)
# ============================================================
# 1. Describe the truth-testing order for a custom object:
#    first method, fallback method, and default behavior.
# Answer:
#
# 2. If you DELETE Vector's truth-testing method but keep its
#    magnitude method, will bool(Vector(0, 0)) still be False?
#    Explain.
# Answer:
#
# 3. What TYPE must the truth-testing method return?
#    Why might returning self.x or self.y directly be wrong?
# Answer:
#
# 4. What does !r in an f-string, or %r in percent formatting,
#    do to the value being formatted?
# Answer:
#
# 5. Could random.choice use your deck? What would it need?
#    Could random.shuffle mutate it with only your two methods?
#    Explain the missing capability.
# Answer:


# ============================================================
# PART 5 — REFLECT | 19:00–20:00 (1 minute)
# ============================================================
# Strongest thing I rebuilt or explained independently:
#
# One specific thing I could not retrieve:
#
# One question I want feedback on:
#
# STOP. Save this attempt before repair.