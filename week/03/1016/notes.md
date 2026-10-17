# Notes from Attempting Py prob

### 7
```py 
def rm_oc(x, y):
    """
    Remove every occurrence of a chosen value from a list.

    Practice input: values=[4, 9, 4, 2, 4, 7], target=4.
    Check adjacent matches, no matches and an empty list.
    """
    for n in x: 
        if n == y: 
            x.pop(y)
        else: continue
    return x
values=[4, 9, 4, 2, 4, 7]
rm_oc(values, 4)
print(values)
```
initial attempt, learned that .pop() removes the indexed item. Put into a loop and it looped to the 4th item until there was none. So it returned [4,9,4,2]. In the Python Tutorial it said to always make a new list when modifying a list and I remembered that when I figured out why it failed. Heres my final attempt:
```py
def rm_oc(x, y):
    """
    Remove every occurrence of a chosen value from a list.

    Practice input: values=[4, 9, 4, 2, 4, 7], target=4.
    Check adjacent matches, no matches and an empty list.
    """
    result = []
    for n in x: 
        if n != y: 
            result.append(n)
        else: continue
    return result
values=[4, 9, 4, 2, 4, 7]
values = rm_oc(values, 4)
print(values)
```
returned `[9,2,7]`


### 8

initial attempt, didnt know really what to do here: 
```py
def dup_in(inp):
    """
    Produce a list containing one copy of each input value.
    For this practice version, preserve first-appearance order.

    Practice input: [8, 3, 8, 5, 3, 1, 5].
    Check input with all equal values and input with no duplicates.
    """
    x = '[]''
    for n in inp:
        n = x
```
after thinking about it, we cannot have x be equal to a string, it simply has to be [] and we need to append 

once I understood the problem, I used a for loop and if then statements: 
```py
 x = []
    for n in inp:
        if n in x: continue
        else:
            x.append(n)
    return x
```
and also set operations for a faster way to make a new list: 
```py
def dup_in1(inp):
    """
    faster way to create a distinct list
    """
    st = set(inp)
    out = list(st)
    return out
```


### 9

initial attempt:

```py
def glue(x,y):
    """
    Use zip() to traverse two lists together and display each pair.

    Practice input: names=["Henry", "Maya", "Noah"], scores=[93, 86, 79].
    Repeat with unequal lengths and explain which items are visited.
    """
    z = [a,b: for a,b in x,y with a,b = zip(x,y)]
    return z
print(z)
```
tried to use list comprehension but forgot the syntax, looked it up and it is [expression for item in iterable if condition]

```py
def glue(x,y):
    """
    Use zip() to traverse two lists together and display each pair.

    Practice input: names=["Henry", "Maya", "Noah"], scores=[93, 86, 79].
    Repeat with unequal lengths and explain which items are visited.
    """
    z = [(a,b) for a,b in zip(x,y)]
    return z

names=["Henry", "Maya", "Noah"]
scores=[93, 86, 79]
print(glue(names,scores))

# the more direct answer would be the following: 
def glue1(x,y):
    for n,s in zip(x,y):
        print(n,s)
glue1(names,scores)
```

### 10
initial attempt:
```py
def convL(x):
    """
    Convert a list of lists into one flat list, retaining element order.

    Practice input: [[6, 2], [], [9], [4, 1, 8]].
    Handle two levels only; recursion is outside this exercise.
    """
    # .append() adds an item to a list, .extend() adds a list of items to a list
    nl = [nl.extend(y) for y in x]
    return nl
```
main problems here is having an extend() in the list comprehension that changes the list in place, so it would return `None`. the fix while using .extend is to not do a list comprehension although I show what the list comprehension version is:
```py
def convL(x):
    """
    Convert a list of lists into one flat list, retaining element order.

    Practice input: [[6, 2], [], [9], [4, 1, 8]].
    Handle two levels only; recursion is outside this exercise.
    """
    # .append() adds an item to a list, .extend() adds a list of items to a list
    nl = [] 
    for n in x:
        nl.extend(n)
    return nl
val = [[6, 2], [], [9], [4, 1, 8]]
print(convL(val))

# if we wanted to do list comprehension then we'd need a nested loop:
def convLu(x):
    return [item for sub in x for item in sub]
print(convLu(val))
```
list_comp = [expression for item in iterable if condition] 

### 11
got this one right away, they all add up to this

### 12

this one was rough. Had the logic correct but didnt know how to do it in code

```py
def hy_in(value):
    """
    Separate a hyphen-delimited string and display the resulting pieces.

    Practice input: "Henry-is-learning-Python".
    Check text with no hyphen and an empty string.
    """
    out = ""
    for n in value:
        if n != '-':
            out + n
        else: 
            print(out)
            out.del()
val = "Henry-is-learning-Python"
hy_in(val)
```
so logic was right for adding to out, then once we hit a `-` we print then delete. `out + n` computes a new string then throws it away since it is unassigned. So I did `out += n`. out.del() was a "I have no clue how to delete this" lol I found all I needed to do was to assign out to an empty string. Then finally the final 'python' never printed since the print function is within the `-` logic. I originally tried to find the len(value) and then the index of the final character to then print at that point but then I realized I just had to bring the print() to the outside of the loop. 

### 13

okay heres my initial attempt at a generator expression: 
```py

def triw(val):
    """
    Delete all ordinary spaces from a string, including internal spaces.

    Practice input: "  c o d e  ".
    Distinguish this requirement from trimming only the ends.
    """
    out = ''.join(va for va in val if not ' ')
    return out

value = " c o d e "
value = triw(value)
print(value)
```
main thing I missed here was I wasnt testing va for an empty space but was testing the string ' ' itself. So what I did was simply make it `if va != ' '` 