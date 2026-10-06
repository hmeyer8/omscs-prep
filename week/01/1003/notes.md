## Data structures PT (WOOOOO)

### More on Lists

quick overview of `/` and `*` in arguements. All arguements to the left of `/` are positional arguements. All arguements after the `/` are either positional or keyword unless there is a `*`, then those arguements are strictly only keyword. 

```py
def ex(a,b,/,c,d,*,e):
    ...

ex(1,2,3,d=4,e=5) # a and b are positional, c and d are either, e is strictly keyword
```

list.append(value, /)
Add an item to the end of the list. Similar to a[len(a):] = [x].

list.extend(iterable, /)
Extend the list by appending all the items from the iterable. Similar to a[len(a):] = iterable.

list.insert(index, value, /)
Insert an item at a given position. The first argument is the index of the element before which to insert, so a.insert(0, x) inserts at the front of the list, and a.insert(len(a), x) is equivalent to a.append(x).

list.remove(value, /)
Remove the first item from the list whose value is equal to value. It raises a ValueError if there is no such item.

list.pop(index=-1, /)
Remove the item at the given position in the list, and return it. If no index is specified, a.pop() removes and returns the last item in the list. It raises an IndexError if the list is empty or the index is outside the list range.

list.clear()
Remove all items from the list. Similar to del a[:].

list.index(value[, start[, stop]])
Return zero-based index of the first occurrence of value in the list. Raises a ValueError if there is no such item.

The optional arguments start and end are interpreted as in the slice notation and are used to limit the search to a particular subsequence of the list. The returned index is computed relative to the beginning of the full sequence rather than the start argument.

list.count(value, /)
Return the number of times value appears in the list.

list.sort(*, key=None, reverse=False)
Sort the items of the list in place (the arguments can be used for sort customization, see sorted() for their explanation).

list.reverse()
Reverse the elements of the list in place.

list.copy()
Return a shallow copy of the list. Similar to a[:].


### Can also see it as a Stack
"last in, first out"
the list.append(value) adds the value to the end, 'top of the stack'
list.pop() takes the last value, "top of the stack"

### Can also use a list as a queue

"first in, first out", very inefficient due to having to shift the whole list over one every time we add a value, but possible
```py
from collections import deque
queue = deque(["Eric", "John", "Michael"])
queue.append("Terry")           # Terry arrives
queue.append("Graham")          # Graham arrives
queue.popleft()                 # The first to arrive now leaves

queue.popleft()                 # The second to arrive now leaves

queue                           # Remaining queue in order of arrival
```
---
### List Comprehensions:

This is very clean code. Makes it so you are not taking up too much space in a codebase. 

consider the following loop:
```py
sqrt = []
for n in range(100):
    if n**0.5 %1==0:
        sqrt.append(n)
print(sqrt)
```
this can be shortened using list comprehension with the following:
```py
x = [n for n in range(100) if n**0.5 %1 == 0]
```
or 
```py
>>> n = [(x,x**2) for x in range(0,100,25)]
>>> n
[(0, 0), (25, 625), (50, 2500), (75, 5625)]
```
could even make it complex: 
```py
from math import pi
[str(round(pi, i)) for i in range(1, 6)]
```
### Nested List Comprehensions
when evaluating or even writing list comprehensions, work outside in

```py
>>> matrix = [
...     [1, 2, 3, 4],
...     [5, 6, 7, 8],
...     [9, 10, 11, 12],
... ]
>>> [[row[i] for row in matrix] for i in range(4)]
[[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]
>>> list(zip(*matrix))
[(1, 5, 9), (2, 6, 10), (3, 7, 11), (4, 8, 12)]
```

`del` statements remove an item from a list given its index, not its value. It can also remove slices from a list or clear an entire list. 
```py
>>> a = [1,2,3,4,5]
>>> del a[1]
>>> a
[1, 3, 4, 5]
>>> del a[2:4]
>>> a
[1, 3]
>>> del a
>>> a
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'a' is not defined
```

### Tuples

Tuples contain heterogeneous sequence of elements and are immutable. 
Lists contain homogenous sequence of elements and are mutable

```py
t = 12345, 54321, 'hello!'
t[0]

t

# Tuples may be nested:
u = t, (1, 2, 3, 4, 5)
u

# Tuples are immutable:
t[0] = 88888
# but they can contain mutable objects:
v = ([1, 2, 3], [3, 2, 1])
v
```
### Sets
set is an unordered sollection with no duplicate elements
basic uses include membership testing and eliminating duplicate entries. 
they also support math operations like union intersection defference and symmetric difference

```py
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)                      # show that duplicates have been removed

'orange' in basket                 # fast membership testing

'crabgrass' in basket


# Demonstrate set operations on unique letters from two words

a = set('abracadabra')
b = set('alacazam')
a                                  # unique letters in a

a - b                              # letters in a but not in b

a | b                              # letters in a or b or both

a & b                              # letters in both a and b

a ^ b                              # letters in a or b but not both
```
we can also do set comprehensions:
```py
>>> a = {x for x in 'abracadabra' if x not in 'abc'}
>>> a
{'r', 'd'}
```

### Dictionaries

indexed by keys, which can be any immutable type. The main operations are storing a value with some keys and extracting that value with the key. 
Best to think of a dict as a set of key:value pairs. 
Strings and numbers can always be used as keys, tuples can be used as kerys if they contain only strinngs, numbers or tuples. If a tuple contains any mutable object either directly or indirectly, it cannot be used as a key. Lists cannot be used as keys. 

Heres an example of using a dictionary:
```py
tel = {'jack': 4098, 'sape': 4139}
tel['guido'] = 4127
tel

tel['jack']

tel['irv']
print(tel.get('irv'))

del tel['sape']
tel['irv'] = 4127
tel

list(tel)

sorted(tel)

'guido' in tel

'jack' not in tel
```
the `dict()` constructor builds dictionaries directly from sequences of key value pairs:
```py
dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
```
dict comprehensions can also be used:
```py
{x: x**2 for x in (2, 4, 6)}
```
### Looping Techniques:

when looping through dictionaries the key and corresponding value can be retrieved ar the same time by using the .items() method: 
```py
names = {"henry": 1, "will": 2, "hannah": 3}
for name,num in names.items():
    print(name,num)
```
to loop over two or more sequences at the same time we could do the following: 
```py
questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
    print('What is your {0}?  It is {1}.'.format(q, a))
```
to loop over a sequence in reverse, first specify the sequence in a forward direction and then call the reversed function: 
```py
for i in reversed(range(1,10,2))
    print(i)
```

to loop over a sequence in sorted orer, use the sorted() function which returns a new sorted list while leaving the source unaltered
```py
for i in sorted(backet):
    print(i)
```
using set() on a sequence eliminated duplicate elements. The use of sorted() in combination with set() over a sequence is an idomatic war to loop over unique elements of the sequence in sorted order: 
```py
>>> a = ['a', 'd', 'v', 'a', 'c', 'd'] 
>>> for x in sorted(set(a)):
...     print(x)
... 
a
c
d
v
>>> 
```
it is normal to want to just change a list while looping over it, but it is simpler and safer to just make a new one instead. 
```py
import math
raw_data = [56.2, float('NaN'), 51.7, 55.3, 52.5, float('NaN'), 47.8]
filtered_data = []
for value in raw_data:
    if not math.isnan(value):
        filtered_data.append(value)

filtered_data
```
### more clarification:

the conditions used in while and if statements can contain any operators, not just comparisons. 

comparison operators `in` and `not in` are membership tests that determine whether a value is in or not in a container

the operators is and is not compare whether two objects are really the same objects. 

Comparisons can be chained. For example, a < b == c tests whether a is less than b and moreover b equals c.

Comparisons may be combined using the Boolean operators and and or, and the outcome of a comparison (or of any other Boolean expression) may be negated with not. These have lower priorities than comparison operators; between them, not has the highest priority and or the lowest, so that A and not B or C is equivalent to (A and (not B)) or C. As always, parentheses can be used to express the desired composition.

The Boolean operators and and or are so-called short-circuit operators: their arguments are evaluated from left to right, and evaluation stops as soon as the outcome is determined. For example, if A and C are true but B is false, A and B and C does not evaluate the expression C. When used as a general value and not as a Boolean, the return value of a short-circuit operator is the last evaluated argument.

It is possible to assign the result of a comparison or other Boolean expression to a variable. For example,

Copy
string1, string2, string3 = '', 'Trondheim', 'Hammer Dance'
non_null = string1 or string2 or string3
non_null
'Trondheim'


---
# Data Structures from Python for Data Analysis

## Tuple
tuple is a fixed length, immutable sequence of Python objects. Easiest way to create one is with a comma separated sequence of values

you can convert any sequence or iterator to a tuple by invoking tuple()

Objects may be stored in a tuple can be mutable themselves but once the tuple is created, it is not possible to modify which object is stored in each slot. 

if you try to assign to a tuple-like expression of variables, python will attempt to unpack the value on the righthand side of the equals sign

```py
tup = (4,5,6)
a,b,c = tup
b
out: 5
```
with multiple variable assigning, we can also swap that way:
```py
a,b = 1,2
b,a = a,b
```
this is another common use of variable unpacking by iterating over sequences of tuples or lists:
```py
seq = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
>>> for a,b,c in seq:
...     print('a = {0}, b = {1}, c = {2}'.format(a,b,c))
... 
a = 1, b = 2, c = 3
a = 4, b = 5, c = 6
a = 7, b = 8, c = 9
```
we can also use the syntax *rest to capture a long list of positional arguements:
```py
>>> a,*rest = seq
>>> a
(1, 2, 3)
>>> rest
[(4, 5, 6), (7, 8, 9)]
>>> 
```
Methods within tuples:
- since the size and contents of a tuple cannot be modified, it is very light on instance methods. A useful one is `count()` which counts the number of occurances of a value

```py
>>> a = (1,2,3,2,4,3,5,1) 
>>> a[1] = 4
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment
>>> a[1] ==2
True
>>> a.count(2)
2
```

## Lists

lists are variable-length and their contents can be modified in place
`gen = range(10)` doesnt make a list, we have to do `gen = list(range()`

Adding and removing elements:
`.append()` adds a value to the end of a list
`.insert(position,value)` adds the value to the specific location
- insert statements are very computationally expensive  If you need to insert elements at both the beginning and end of asequence, you may wish to explore collections.deque, a double-ended queue, for this purpose
`pop(position)` is the inverse to insert. removes at a specific position
`remove(value)` locates the first such value from the list
`in` keyword checks if a list contains a value. 
```py
'value' in list
```
`not in` are keywords used to negate `in`
`.extend()` is used to append multiple elements
```py
>>> a = [2,3,1]
>>> b = [5,6,10]
>>> a.extend(b)
>>> a
[2, 3, 1, 5, 6, 10]
```
`.sort()` is used to sort a list in-place (without creating a new object). 
```py
>>> a
[2, 3, 1, 5, 6, 10]
>>> a.sort()
>>> a
[1, 2, 3, 5, 6, 10]
```
sort has some options that end up being beneficial. e.g. sorting based off length`
```py
>>> b =['saw', 'small', 'He', 'foxes', 'six']  
>>> b.sort(key = len)
>>> b
['He', 'saw', 'six', 'small', 'foxes']
```
bisect finds the location where an elements should be inserted to keep it sorted
`bisect.bisect(list,value)` finds the location where an element should be located to keep it sorted. 
`bisect.insort(list,value)` inserts it sorted 
- the bisect module does not check whether the list is sorted because in doing so it would make it very computationally expensive. So using it in an unsorted list would succeed with no errors

slicing: we know slicing, but negative indices slice the sequence relative to the end. Also the value after the second colon is the step. A step of -1 is a clever way to reverse a list or tuple. 
```py
>>> b[::-1]
['foxes', 'small', 'six', 'saw', 'He']
```
## Built in sequence Functions:

`enumerate()` numbers values based off position and returns (i,value) tuples. 

```py
>>> b     
['He', 'saw', 'six', 'small', 'foxes']
>>> a = {}                  
>>> for i,value in enumerate(b):
...     a[value] = i
... 
>>> a
{'He': 0, 'saw': 1, 'six': 2, 'small': 3, 'foxes': 4}
```
`zip()` "pairs" up the elements of a number of lists, tuples, or other sequences to create a list of tuples. We can pair up as many lists as we want as well
we can also 'unzip' a sequence by converting a list of rows int a list of columns: 
```py
>>> pitchers = [('Nolan', 'Ryan'), ('Roger', 'Clemens'),('Schilling', 'Curt')]
>>> first_names, last_names = zip(*pitchers)
>>> first_names
('Nolan', 'Roger', 'Schilling')
>>> last_names
('Ryan', 'Clemens', 'Curt')
```
## dict

most important Python data structure
commonly referred to as a hash-map or associative array. 
we create them with curly braces and colons to separate keys and values
we can delete values either by using the del keyword or the `pop()` method
```py
ed = ['hi', 'my', 'name', 'is', 'henry']
>>> ded = {}
>>> for i in ed:
...     ded[i] = len(i)
>>> ded
{'hi': 2, 'my': 2, 'name': 4, 'is': 2, 'henry': 5}
>>> list(ded.keys())
['hi', 'my', 'name', 'is', 'henry']
>>> list(ded.values())
[2, 2, 4, 2, 5]
>>> ded.update({'hi':5})
>>> ded
{'hi': 5, 'my': 2, 'name': 4, 'is': 2, 'henry': 5}
>>> ded.pop('hi')
5
>>> ded
{'my': 2, 'name': 4, 'is': 2, 'henry': 5}
```
the update method changes dicts in place, so any existing keys in the data passed to update will have their old values discarded

it is common to have two sequences we want to pair up element wise in a dict. Here is a common code for that. 
```py
mapping = ()
for key, value in zip(key_list, value_list):
    mapping[key] = value
```
### Default Values:
it is normal to have logic like this: 
```py
if key in some_dict:
    value = some_dict[key]
else: 
    value = default_value
```
Dict methods `get` and `pop` can return a defaultvalue, so that block can be written as:
```py
value = some_dict.get(key,default_value)
```
`get` will return `None` if the key is not present, while pop will raise an exception

```py
>>> words = ['apple', 'bat', 'bar', 'atom', 'book']
>>> by_letter = {}                     
>>> for w in words:                
...     letter = words[0]
...     if letter not in by_letter:    
...             by_letter[letter] = [w]
...     else:
...             by_letter[letter].append(w)
... 
>>> 
>>> by_letter
{'apple': ['apple', 'bat', 'bar', 'atom', 'book']}
```