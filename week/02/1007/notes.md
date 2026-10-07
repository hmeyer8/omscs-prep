## 3.1 PDA cont.

### Set
- an unordered collection of unique elements. 
comparable to dicts but instead keys with no values. 
can be created two ways:
```py
>>> a = [1,2,3,4,3,2,3,2]
>>> a = set(a)
>>> a
{1, 2, 3, 4}
>>> b = {1,2,3,4,3,2,3,4}
>>> b
{1, 2, 3, 4} 
```
Sets support set operations like union, intersection, difference, and symmetric difference. 
**union** of two sets is the set of distinct elements occuring in either set. This can be computed with the `union` method or the | binary operator: 
```py
>>> a       
{1, 2, 3, 4}
>>> b = {2,4,4,7,8}
>>> a | b
{1, 2, 3, 4, 7, 8}
>>> a
{1, 2, 3, 4}
>>> b
{8, 2, 4, 7}
>>> a.union(b)
{1, 2, 3, 4, 7, 8}
```
**intersection** contains the elements occuring in both sets. The & operator or the `intersection` method can be used:
```py
>>> a
{1, 2, 3, 4}
>>> b
{8, 2, 4, 7}
>>> a.intersection(b)
{2, 4}
>>> a&b
{2, 4}
```
### Set Operations methods: 

`a.add(x)` - add element x to set a
`a.clear()` - reset the set a to an empty state, discarding of the elements
`a.remove(x)` - remove element x from set a
`a.pop()` - remove an arbritrary elements from set a. Raises KeyError if set is empty
`a.union(b)`, or `a|b` - shows all the unique elements in a and b. 
`a.update(b)` or `a|=b` - sets the contents of a to be the union of the elements of a and b
`a.intersection(b)` or `a&b` - all the elements in both a and b
`a.intersection_update(b)` or `a&=b` - set the contents of a to be the intersection of the elements in a and b
`a.difference(b)` or `a-b`the elements in a that are not in b
`a.difference_update(b)` or `a-=b` - set a to the elements in a that are not in b
`a.symmetric_difference(b)` or `a^b` - all of the elements in either a or b but **not** both
`a.symmetric_difference_update(b)` or `a ^= b` - set a to contain the elements in either a or b but not both
`a.issubset(b)` - True if the elements of a are all contained in b
`a.issuperset(b)` - True if the elements of b are all contained in a
`a.isdisjoint(b)` - True if a and b have no elements in common

set elements must be immutable, so for us to have list like elements we have to convert it to a tuple: 

### List, Dict, and set comprehensions:

List Comprehensions:
allows us to concisely form a new list by filtering the elements of a collection, transforning the elements passing the filter in one concise expression
takes the basic expression of: 
- [expr for val in collection if condition]
equivalent to: 
```py
result = []
for val in collection:
    if condition:
        result.append(expr)
```
set and dict comprehensions are similar. Dict comprehensions are as follows: 
```py
dict_comp = {key-expr : value-expr for value in collection if condition}
set_comp = {expr for value in collection if condition}
```
set comprehension looks like the equivalent list comprehension except with curly braces 

we could also create a lookup map for the strings using this as well: 
```py
>>> strings
['hi', 'my', 'name', 'is', 'russel']
>>> lkmp = {key: value for key,value in enumerate(strings)}
>>> lkmp
{0: 'hi', 1: 'my', 2: 'name', 3: 'is', 4: 'russel'}
```

## 3.2 PDA Functions

Most important method of code organization and reuse in Python
General rule of thumb: if you anticipate needing to repeat the same or very similar code more than once, write a reusable function. 
Also makes your code more readable by giving a name to a group of Python statements. 

Declared with the `def` keyword and returned with the `return` keyword. 
It is okay to have multiple return statements, but if there is no return statements, then `None` will be return

### Namespaces, Scope and Local Functions

Two ways a function can access a variable: global and local. 
Namespaces describe a variable scope within Python. 
It is any variabble that is assigned within a function by default is the local namespace. 
It is created when the function is called and destroyed after. 

when we define a variable outside the functions scope, the variable must be declared as a global keyword: 

```py
>>> a = None
>>> def var():
...     global a
...     a = []
...     
>>> var()
>>> print(a)
[]
```
dont use a lot of global variables, that is when we start getting into OOP

we can return multiple values and unpack into multiple variables:
```py
>>> def f():
...     a = 5
...     b = 6
...     c = 7
...     return a,b,c
... 
>>> d,e,f = f()
>>> d
5
```
