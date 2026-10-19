# Comprehensions and file error handling

### 23

```py
def transp(inp):
    """
    Use a nested comprehension to transpose a 3-by-3 matrix.

    Practice input: [[2, 4, 6], [1, 3, 5], [7, 8, 9]].
    Leave the original matrix unchanged.
    """
    out = [x for i in inp for x[n] in i; n=0, n++]
    return out
h = [[2, 4, 6], [1, 3, 5], [7, 8, 9]]
print(transp(h))
```
really had no clue how to put this in to python, worked problems like this in java and C and didnt know how to do it in Python. Claude told me first to use range instead of i++. So I did a list comprehension into another list comprehension. This was my final one: 
`out = [[row[x] for row in inp] for x in range(len(inp))]`
The thing I found out I could do here is make multiple lists within one list comprehension. 