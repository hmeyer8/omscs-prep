# Ch 2 of FP

### Overview of Built in Sequences:

container sequences- hold references to the objects they contain, can be of any type
- list, tuple, and collections.deque can hold items of different types

flat sequences- physically store the value of each item within its own memory space, not as distinct objects
- str, bytes, bytearray, memoryview, and array.array hold items of one type

flat sequences are more compact but are limited to holding primitive values like characters, bytes, and numbers

mutable sequences:
- list, bytearray, array.array, collections.deque, and memoryview
immutable sequences:
- tuple, str, and bytes

keeping in mind the common traits -- mutable vs immutable and container vs flat-- is very helpful to extrapolate what you know about one sequence type to others

### Listcomps

```py
colors = ['black', 'white']
sizes = ['S', 'M', 'L']

tshirts1 = [(color,size) for color in colors for size in sizes]

tshirts2 = [(color,size) for size in sizes for color in colors]
print("tshirt1 = ", tshirts1)
print("tshirt2 = ", tshirts2)
```
tshirt1 =  [('black', 'S'), ('black', 'M'), ('black', 'L'), ('white', 'S'), ('white', 'M'), ('white', 'L')]
tshirt2 =  [('black', 'S'), ('white', 'S'), ('black', 'M'), ('white', 'M'), ('black', 'L'), ('white', 'L')]

this makes a list of tuples
different way to sort the listcomp based off order of for loops

we did this in the FrenchDeck class: 
```py
self._cards = [Cards(rank, suit) for suit in self.suits
                                 for rank in self.rank]
```

