import collections
# Card line creates a new class
Card = collections.namedtuple('Card', ['rank', 'suit'])
# namedtuple can be used to build classes of objects that are just
# bundles of attributes with no custon methods, like a database record
class FrenchDeck:
    ranks = [str(n) for n in range(2,11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()
    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                                        for rank in self.ranks]
    def __len__(self):
        return len(self._cards)
    def __getitem__(self, position):
        return self._cards[position]

deck = FrenchDeck()
print(len(deck))
from random import choice
print(choice(deck))
