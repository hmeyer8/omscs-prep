# PDA 3.2 FUNctions

### Lambda funtions

- ways of of writing functions consisting of a single statement, result is the return value. 
defined with the `lambda` keyword which simply says "we are declaring this an anonymous function". 
consider the following function:

```py
def short_funnction(x):
    return x*2

equiv_anon = lambda x: x*2
```
we can also 

or if we want to sort by the length of distinct characters we can do this: 
```py
>>> strings = ['foo', 'card', 'bar', 'aaaa', 'abab']
>>> strings.sort(key = lambda x: len(set(list(x))))
>>> strings
['aaaa', 'foo', 'abab', 'bar', 'card']
```

### Currying

computer science jargon from mathematician Haskell Curry that means to derive new functions from existing ones by partal argument application. 
Say we have the following function: 
```py
>>> def add_numbers(x,y):
...     return x + y
... 
>>> add_numbers(4,5)
9
>>> add_five = lambda y: add_numbers(5,y)
>>> add_five(5,add_numbers(1,2))
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: <lambda>() takes 1 positional argument but 2 were given
>>> add_five(add_numbers(1,2))           
8
```
Nothing too fancy here other than us simply building off another function by calling it. The built-in functools module can simplify this process by usinng the partial function: 

```py
>>> from functools import partial
>>> add_five = partial(add_numbers,5)
>>> add_five(1,2)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: add_numbers() takes 2 positional arguments but 3 were given
>>> add_five(1)  
6
```

### Generators (POWER)

iterator: any object that yeilds objects to the python intrepreter when used in a context like a `for` loop. 
most methods expecting a list or list- like object will also accept any iterable object. Includes built in methods like `min`, `max`, and `sum` and even type constructors like `list` and `tuple`. 

Generator: concise way to construct a new iterable object
- normal functions execute and return a single object at a time, generators return a sequence of multiple results, pausing after each one until the next one is requested. 
to create a generator, use the `yield` keyword instead of `return` in a function:
```py
def squares(n=10):
...     print('generating squares from 1 to {0}'.format(n**2))
...     for i in range(1,n+1):
...             yield i**2
... 
>>> squares()
<generator object squares at 0x000002BDE05DB6A0>
>>> gen = squares()
>>> for x in gen:
...     print(x,end=' ')
... 
generating squares from 1 to 100
1 4 9 16 25 36 49 64 81 100
```
it is not until you request elements from the generator that it begins executing its code

another more concise way to make a generator is by using a generator expression. this is comparable to list, dict and set comprehensions
to create one, enclose what would otherwise be a list comprehension within parenthesis instead of brackets: 
```py
>>> jen = (x**2 for x in range(100))
>>> jen
<generator object <genexpr> at 0x000002BDE0114380>
```
this is comparable to the verbose generator: 
```py
>>> def _make_gen():        
...     for i in range(100):
...             yield i**2
... 
>>> gen = _make_gen()
```
generator expressions can also be used instead of list comprehensions as functions arguements in many cases:
```py
>>> sum(gen)
328350
>>> dict((i,i**2) for i in range(6))
{0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
```


itertools module: 
    this library has a collection of generators for many common data algorithms. E.g `groupby` takes any sequence and a function, grouping consecutive elements in the sequence by return value of the function:
```py
>>> import itertools
>>> first_letter = lambda x: x[0]
>>> names = ['Alan', 'Adam', 'Wes', 'Will', 'Albert', 'Steven']
>>> for letter, names in itertools.groupby(names,first_letter):
...     print(letter, list(names))
... 
A ['Alan', 'Adam']
W ['Wes', 'Will']
A ['Albert']
S ['Steven']
```
here is a few other itertools functions that are great: 

`combinations(iterable,k)`
    Generates a sequence of all possible k-tuples of elements in the iterable, ignoring order and without replacement (see also the companion function combinations_with_replacement)
`permutations(iterable,k)`
    Generates a sequence of all possible k-tuples of elements in the iterable, respecting order
`groupby(iterable[,keyfunc])`
    Generates (key, sub-iterator) for each unique key
`product(*iterables, repeat=1)`
    Generates the Cartesian product of the input iterables as tuples,similar to a nested for loop


## Errors and Exceptions handling:

handling python errors or exceptions gracefully is important when building robust programs. 

many functions only work on certain inputs. For example Python's `float` function is able to cast a string to a floating point number but returns a value error on improper inputs:
```py
>>> float('string')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: could not convert string to float: 'string'
```
say we wanted a version of `float()` that fails gracefully, returning the input arguement. We can do that via a try/except block:
```py
>>> def attempt_float(x):
...     try:
...             return float(x)
...     except:
...             return x
... 
>>> attempt_float('1.2432')
1.2432
>>> attempt_float('float') 
'float'
```
we can also suppress only TypeErrors and ValueErrors by writing a tuple of exception types: 

```py
>>> def attempt_float(x):
...     try:             
...             return float(x)
...     except (TypeError, ValueError):
...             return x
... 
>>> attempt_float((1,2))
(1, 2)
>>> attempt_float(('hi'))
'hi'
```
sometimes you may not want to suppress an exception, but you want some code to be executed regardless of whether the code in the `try` block succeeds or not. to do this use `finally`
```py 
f = open(path, 'w')
    try:
        write_to_file(f)
    finally:
        f.close()
```
that way the file always gets closed. We could also have code that executes only if the `try:` block succeeds using `else:`
```py
f = open(path, 'w')
    try:
        write_to_file(f)
    except:
        print('failed')
    else:
        print('succeeded')
    finally:
        f.close()
```
