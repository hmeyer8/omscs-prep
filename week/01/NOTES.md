9/28: Python Tutorial chapter 3 and 4

---

### Numbers

can make the intrepeter a calculator, div returns a float

floor division returns the full number (e.g. `7//3 = 2`), `%` operator returns the remainder (e.g. `7%3 = 1`)

powers are `**` (`2**7` is 2 to the power of 7)

you must define a variable or it will error (assign a value to a variable)

when doing multiple operations, `_` fills in the output of the last calculation

---

### Text

single quotes and double quotes build the same strings, the output is the same. Numbers enclosed in quotes are `str` data type

to use a quote in a string, we can "escape" it via `\'`

string definition vs output string:

```pycon
>>> s = 'first line, \nSecond line.'
>>> s #gives us the string definition
'first line, \nSecond line.'
>>> print(s) # output string
first line,
Second line.
```

`r` gives us the raw string if we dont want `\` to be intrepreted as special characters

```pycon
>>> print('C:\this\name')
C:      his
ame
>>> print(r'C:\this\name')
C:\this\name
```

triple quotes at the beginning and end for a string to span multiple lines

strings can be glued together with `+` and repeated with `*`

```pycon
>>> 3*'un'+'ium'
'unununium'
```

two or more string literals are automatically added if theyre next to each other, doesnt work for a literal and a variable, only works if theres a `+`

```pycon
>>> 'he''llo'
'hello'
>>> x = 'he'
>>> x'llo'
  File "<stdin>", line 1
    x'llo'
     ^^^^^
SyntaxError: invalid syntax
>>> x + 'llo'
'hello'
```

strings can also be indexed, first letter is index 0 right to left. We can count left to right with a negative index with the negative index starting at -1, not -0

```pycon
>>> words = "Airpwane"
>>> words[0]
'A'
>>> words[-0]
'A'
>>> words[-1]
'e'
```

slicing is also supported, note `s[:i] + s[i:] = s`

```pycon
>>> words[:2]
'Ai'
>>> words[3:]
'pwane'
>>> words[:4] + words[4:]
'Airpwane'
```

Heres a good visual for slicing and index:

```
 +---+---+---+---+---+---+
 | P | y | t | h | o | n |
 +---+---+---+---+---+---+
 0   1   2   3   4   5   6
-6  -5  -4  -3  -2  -1
```

Python strings cannot be changed, immutable

Heres a few other things we can do as well:

```pycon
>>> words[:2] == 'Ai'
True
>>> words[4:]
'wane'
>>> len(words)
8
```

---

### Lists

most versatile compound data type, below is the format. Like strings and all other **built in sequence types**, lists can be indexed and sliced. Lists also support concatenation

```pycon
>>> squares = [1, 4, 9, 16, 25]
>>> squares
[1, 4, 9, 16, 25]
>>> squares[4]
25
>>> squares[0:2]
[1, 4]
>>> squares + [36, 49]
[1, 4, 9, 16, 25, 36, 49]
```

unlike strings, lists are mutable

```pycon
>>> squares[1] = 100
>>> squares
[1, 100, 9, 16, 25]
```

can also add to the end of a list with the `list.append()` method

```pycon
>>> squares.append(36)
>>> squares
[1, 100, 9, 16, 25, 36]
```

assignment in python never copies data. When you assign a list to a variable it refers to an existing list object. any changes you make to a list through one variable will be seen through other variables as well. `len()` method also applies to lists

```pycon
>>> planes = [135, 17, 46, 22]
>>> planes = plns
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'plns' is not defined. Did you mean: 'planes'?
>>> plns = planes
>>> plns
[135, 17, 46, 22]
>>> planes[1] = 35
>>> plns
[135, 35, 46, 22]
>>> len(plns)
4
```

consider this loop:

```pycon
>>> a,b = 0,1
>>> while a<10:
...     print(a);
...     a,b = b, b+a;
...
0
1
1
2
3
5
8
```

this loop has a `while` statement. The body of the algorithm continues to cycle until the while condition is met. So the first thing that occurs is there is a multiple assignment of a = 0 and b = 1 (`a,b = 0,1`). then with every loop that occurs, a is printed. Directly after, there is a multiple assignment of a becoming b and b becoming a + b. and then loops until a becomes greater than a. Hence the list definition of:

```pycon
>>> a,b
(13, 21)
```

---

## ch4

if, elif, else
```pycon
>>> x = int(input("Please enter an integer: "))
Please enter an integer: 42
>>>if x < 0:
      x = 0
      print('Negative changed to zero')
  elif x == 0:
      print('Zero')
  elif x == 1:
      print('Single')
  else:
      print('More')
More
```
`for` statements: 
Pythons for statements iterate over the items of any sequence (a list or a string), in the order they appear in the sequence, e.g:

```pycon
>>> names = ['henry', 'dayton', 'sam']  
>>> for x in names:
...     print(x, len(x))
... 
henry 5
dayton 6
sam 3
```
if we are trying to modify a collection while iterating over the same collection, it is usually better to loop over a copy of the collection or create a new collection. The example below is showing how to loop over a new collection
```pycon
>>> users = {'Henry': 'active', 'Sam': 'inactive', 'Will': 'active'}   
>>> for user, status in users.copy().items():
...     if status =='inactive':
...             del users[user]
... 
>>> users
{'Henry': 'active', 'Will': 'active'}
```
This next one creates a new collection and puts the condition into the new collection. 
```pycon
>>> users
{'Henry': 'active', 'Sam': 'inactive', 'Will': 'active'}
>>> active_users = {}
>>> for user, status in users.items():
...     if status == 'active':
...             active_users[user] = status
>>> users
{'Henry': 'active', 'Sam': 'inactive', 'Will': 'active'}
>>> active_users
{'Henry': 'active', 'Will': 'active'}
```
the range function is also handy: 
```pycon
>>> for i in range(4):
...     print(i)
... 
0
1
2
3
>>> list(range(0,10,2))
[0, 2, 4, 6, 8]
```
we can also go and iterate over the indices of a sequence with range() and len(). with range we can only enumerate the range via `list(range(5))` or `for i in range(5)`
```pycon
>>> a = ['Mary', 'had', 'a', 'little', 'lamb']
>>> for i in range(len(a)):
...     print(i, a[i])
... 
0 Mary
1 had
2 a
3 little
4 lamb
```
okay so `break` breaks out of the innermost loop and into the next iteration of the outer loop, `continue`continues with the next iteration once the initial condition is met. 

```pycon
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
    else:
        # loop fell through without finding a factor
        print(n, 'is a prime number')
```
`pass` does nothing, commonly used to make minimal classes. Can also be used for a functional or conditional body when you are working on new code. 
