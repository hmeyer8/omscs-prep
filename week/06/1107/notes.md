# FP ch 1 finish up

special methods are supposed to be called by the python interpreter. we dont write `my_object.__len__()`, we write `len(my_object)`. 

Then if `my_object` is an instance of a user defined class, python would call the `__len__` method we implemented. 

built in objects already keep track of their length, so len() retrieves the stored number very quickly

CPython- the standard implementation of Python, written largely in C

C struct- bundle of named pieces of data- roughly like an objects attributes

`PyVarObject`- internal structure containing basic object information plus a size field

`ob_size` - internal size field; for a list it records the number of items

SO take FrenchDeck for example: 

```py
import collections
Card = collections.namedtuple('Card', ['rank', 'suit'])
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
```

when we call `len(deck)`, two things happen under the hood of Python: 
1. Python invokes the `FrenchDeck.__len__`, since deck is an instance of FrenchDeck
2. Our method then calls `len(self._cards)`. Because `_cards` is a built in list, Python retrieves its stored length through its C implementation. 

The statement `for i in x:` invokes `iter(x)` which in turn may call `x.__iter__()` if it is available. 

Our code should not have many direct calls to special methods. Unless we are doing a lot of metaprogramming we should be implementing special methods more often than than invoking them explicitly.

The only special method that is frequently called by user code directly is `__init__` to invoke the initializer of the superclass in your own `__init__` implementation. 

Say for example we wanted to initialize an arguement in a Flight class: 

```py
class Flight: 
    def __init__(self, hours):
        self.hours = hours
```
that is normal. Say we wanted to make a child class that pulls the parents initializer on the same object: 
```py
class TrainingFlight(Flight):
    def __init__(self, hours, instructor):
        super().__init__(hours)
        self.instructor = instructor
```

Whenever we are calling a special method, it is better to call the related built in function. The built-ins call the corresponding special method but also provide other services and -for built in types- are faster than method calls.

### String Representation

Consider the following: 
```py
from math import hypot
class Vector: 
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y
    def __repr__(self):
        return 'Vector(%r, %r)' % (self.x, self.y)
    def __abs__(self):
        return hypot(self.x, self.y)
    def __bool__(self):
        return bool(abs(self))
    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x,y)
    def __mul__(self,scalar):
        return Vector(self.x * scalar, self.y * scalar)
```

`__repr__` is used to make a string ready for inspection. Say I commented out the repr def and made a vector 
`v = Vector(3,2)` then did `print(v)`, we would get: 
`<__main__.Vector object at 0x000001E3FA0C8410>`

Repr here makes the objects readable during object oriented progranmming. `__str__` is a good way to do that too but with the built ins with repr it is easiest to do it this way. 

Now with repr uncommented we get `Vector(3,2)`

Here are some different ways we can implement it:
```py
def __repr__(self):
    return f"Vector({self.x!r}, {self.y!r})"
```
or a little more cleanly
```py 
def __repr__(self):
    return 'Vector(%r, %r)' % (self.x, self.y)
```
Two things happen in the function above:
1. %r asks for the individual coordinates
2. The % then performs the formatting 

### arithmetic operators 

In the test.py for today we showed + and * operators to show the usage of `__add__` and `__mul__`. In both cases, the methods create and return new instances of the Vector method and doesnt modify either operand-- `self` and `other` are merely read. 
This is also normal for infix operators: 
1. to create new objects and 
2. to not touch the operands

By default, instances of user defined classes are considered truthy unless either `__bool__` or `__len__` is implemented. When `bool(x)` is called it invokes `x.__bool__()` and uses the result

If `__bool__` is not implemented, Python will try to invoke `x.__len__()` and if it returns zero, bool returns false. Otherwise, true. 

In test.py, our implementation is simple- it returns false if the magnitude is zero and true if not. 

We convert the magnitude to a boolean using bool(abs(self)) because `__bool__` is expected to return a boolean

A faster implementation of `Vector.__bool__` is this: 
```py
def __bool__(self):
    return bool(self.x or self.y) 
```
in this it is harder to read but it is faster because we lose the trip to the abs, `__abs__`, the squares, and square root. The bool operand is necessary because `or` 

Category                    Method names 
              
String/bytes representation  `__repr__, __str__, __format__, __bytes__`
Conversion to number         `__abs__, __bool__, __complex__, __int__, __float__, __hash__,__index__`
Emulating collections        `__len__, __getitem__, __setitem__, __delitem__, __contains__`
Iteration                    `__iter__, __reversed__, __next__`
Emulating callables          `__call__`
Context management           `__enter__, __exit__`
Instance creation and dest   `__new__, __init__, __del__`
Attribute management         `__getattr__, __getattribute__, __setattr__, __delattr__, __dir__`
Attribute descriptors        `__get__, __set__, __delete__`
Class services               `__prepare__, __instancecheck__, __subclasscheck__`


### Special Method Names for Operators
Category                        Method names and related operators
Unary numeric operators         `__neg__ -, __pos__ +, __abs__ abs()`
Rich comparison operators       `__lt__ <, __le__ <=, __eq__ ==, __ne__ !=, __gt__ >, __ge__ >=`
Arithmetic operators            `__add__ +, __sub__ -, __mul__ *, __truediv__ /, __floordiv__ //, __mod__ %, __divmod__ divmod() , __pow__ ** or pow(), __round__ round()`
Reversed arithmetic operators   `__radd__, __rsub__, __rmul__, __rtruediv__, __rfloordiv__, __rmod__, __rdivmod__, __rpow__`
Augmented assignment arithmetic operators
                                `__iadd__, __isub__, __imul__, __itruediv__, __ifloordiv__,__imod__, __ipow__`
Bitwise operators               `__invert__ ~, __lshift__ <<, __rshift__ >>, __and__ &, __or__ |, __xor__ ^`
