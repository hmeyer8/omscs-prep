4.8 in Python tutorial: Defining Functions

```pycon
def fib(n):
    """this is stored as a docstring, this will be attached to the function as documentation"""
    a,b = 0,1
    while a<n:
        print(a, end = ' ')
        a,b = b, a + b
    print(a)

fib(2000)
```
the first statement of the function body can optionally be a string literal, called a docstring. That statement is stored as documentation

a function implements a new symbol table that is used for the local variables of the function. When a script reads a variable, python looks in this order and stops at the first match: 
1. The functions own local variables
2. Any function that encloses it (if it is nested)
3. Global Variables (the module level)
4. Pythons built in names (like print or len)

the consequence: a function can read variables from outside itself, but it cant change them by simple assignment. Assigning creates a new local variable with the same name. **if you do want to change an outside variable, you have to declare it first**
`global x` for a global variable
`nonlocal x` for a variable in an enclosing function

the parameters to a function call are added into the local symbol table of the called function when it is called. 

In functions, the arguements(parameters) are passed using _call by value_. Same pointer, different reference value. 

when we make a function via `def`, python does two things:
1. creates a function object
2. creates a name that points to that object
same as `x = [1,2,3]`
the object itself knows it is a function, if i ran 
```pycon
>>>print(fib)
>>><function fib at 0x0000021E345C0540>
```
we get an object that says it is a function at a certain address. Other names can also point to it via `x = fib`

the `return` statement returns the value from a function. `return` without an expression arguement returns `None`. 

consider the following:
```pycon
>>> x = [1,2,3]
>>> x.append(4)
>>> x
[1, 2, 3, 4]
```
`.append(4)` is a method of list object `result`. A method belongs to an object and is named `obj.methodname`. We can also define our own object types and methods using Classes. 
---

### Default Arg Values

Consider the following code:
```pycon
def ask_ok(prompt, retries=4, reminder='Please try again!'):
    while True:
        reply = input(prompt)
        if reply in {'y', 'ye', 'yes'}:
            return True
        if reply in {'n', 'no', 'nop', 'nope'}:
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError('invalid user response')
        print(reminder)
```
Given this function, we can call it multiple different ways. 
`ask_okay('Do you really want to quit?')` or
`ask_okay('Do you really want to quit?', 3, 'Only yes or no')`
The default arguement values are given in the parameters, but when we call the function we can change them here. 

This also includes the `in` keyword. This tests whether a sequence contains a certain value. 

Default values are also only evaluated at the point of funnction definition as seen below:
```pycon
>>> def f(arg = i):
...     print(arg) 
... 
>>> i = 6
>>> f()
5
```
The default value is evaluated only once, this changes things for mutable objects such as lists, dicts, etc. 
```py
>>> def f(a, L = []):
...     L.append(a)
...     return L
... 
>>> print(f(1))
[1]
>>> print(f(2))
[1, 2]
```
if we want the default args to be shared between subsequent calls we can write a function like this: 
```py
def f(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L
```
we can have positional arguments and keyword args. 
```py
f(L = 5) # keyword
f(2,3) # positional, makes a,L = 2,3
```
---

 Lambda expressions

A lambda is a function written in one line without a name. Its a shortcut for a simple def. 

```py
def add(a,b):
    return a + b

add = lambda a,b: a+b
```
form is `lambda <parameters>: <expression>

here is a function within a function:
```py
def make_incrementor(n):
    return lambda x:x+n

f = make_incrementor(42)
print(f(3))
45
```