# Practice problems:

### 14
```py
def stod(value):
    """
    Build a dictionary counting each character in a string.

    Practice input: "level up".
    Include spaces as characters. Check empty input.
    """
    out = {}
    for i,v in enumerate(value):
        out[i] = v
    return out
print(stod("level up"))
```
originally had the logic as `out[n] = c` and it printed lev up, then I remembered the key cannot be repeated within its key: value pairs, same rules as a set. Switched those values and it worked 


### 15:
```py
def nd(d):
    """
    Create a new dictionary retaining entries whose scores exceed 60.
    Leave the original dictionary unchanged.

    Practice input: {"Henry": 88, "Maya": 60, "Noah": 41, "Ava": 75}.
    Check the threshold boundary.
    """
    new_dict = {}
    for i,v in d.items():
        if v>60:
            new_dict[i] = v
    return new_dict
values = {"Henry": 88, "Maya": 60, "Noah": 41, "Ava": 75}
print(nd(values))
```
for this problem we need to know the `.items()` method. The `.items()` method returns all (key,value) pairs of a dict as a tuple. It allows a view of these objects at the same time. Whereas the methods `.keys()` and `.values()` returns the values and keys. 

### 16

```py
def rev(d):
    """
    Reverse a dictionary's mapping while retaining duplicate-value groups:
    each original value becomes a key associated with a list of original keys.

    Practice input: {"apg": "day", "qa": "night", "hydro": "day"}.
    Use an ordinary dictionary, not defaultdict.
    """
    return dict(reversed(d.items()))
hi = {"apg": "day", "qa": "night", "hydro": "day"}
print(rev(hi))
```

Here we see that the `reversed()` method when used on a `dict.items()` reverses the dict with respect to the key

### 17

initial input: 

```py
def group_words(words):
    """
    Group words into lists indexed by their initial letter.

    Practice input: ["crew", "code", "flight", "fuel", "aircraft"].
    Assume words are nonempty; check an empty input list.
    """
    lst = {}
    if words == '':
        print("empty input")
    for n in words:
        if lst[n[0]] == lst.keys():
            lst[n[0]].append(n)
        else: lst[n[0]] = n
    return lst

words = ["crew", "code", "flight", "fuel", "aircraft"]
print(group_words(words))
```

main issue here is the first lst[n[0]] raises a key error since the key doesnt exist. 'c' is not in the dict yet so we need to do if n[0] in lst. Also lst.keys() would also be an error since there is nothing in lst. 
Also the else condition had lst[n[0]] = n be stored as a string, if we want to start a list(which we do), we add brackets: lst[n[0]] = [n]


