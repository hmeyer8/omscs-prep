# PDA 3.3 File and the Operating System

Normally we use `pandas.read_csv` to read data files from disk into python data structures. But it is important to know the basics: 

to open a file: 
```py
path = 'C:/Users/henme/.code_space/omscs-prep/week/01/data/names.txt'
f = open(path)
```
by default this is in read only mode `'r'`. We can then treat the file handle `f` like a list and iterate over the lines like so:
```py
for lines in f:
    pass
```

it is important to close the file when finished. Closing the file releases its resources back to the operating system. we can use `f.close()` or `with`:

```py
path = 'C:/user/.../names.txt'
with open(path) as f:
    lines = [line for _,line in zip(range(10),f)]
```
if you write `f = open(path, 'w')` a new file would be created, overwriting any file in its place so be careful. 
most commonly used methods  for readable files are `read`, `seek`, and `tell`
`read` returns a certain number of characters from the file, what constitutes as a "character" is determined by a files encoding: UTF-8 or simply raw bytes if the file is opened in binary mode

```py
>>> with open(path, 'rb') as f:
...     f.read(10)
...     f.tell()
... 
b'emma\nolivi'
10
>>> with open(path) as f:
...     f.read(10)
...     f.tell()
... 
'emma\nolivi'
10
>>> import sys              
>>> sys.getdefaultencoding()
'utf-8'
```

Mode Description
r       Read-only mode
w       Write-only mode; creates a new file (erasing the data for any file with the same
name)
x       Write-only mode; creates a new file, but fails if the file path already exists
a       Append to existing file (create the file if it does not already exist)
r+      Read and write
b       Add to mode for binary files (i.e., 'rb' or 'wb')
t       Text mode for files (automatically decoding bytes to Unicode). This is the default if not specified. Add t to other modes to use this (i.e., 'rt' or 'xt')


to write text to a file we can use the file's write or writelines method. For example we can create type of method that makes a file with no blank lines below: 
```py
with open('tmp.txt', 'w') as handle:
    handle.writelines(x for x in open(path) if len(x) > 1)
with open('tmp.txt') as f:   
    lines = f.readlines()
```
here is the main important file methods: 
read([size])        Return data from file as a string, with optional size argument indicating the number of bytes to read
readlines([size])   Return list of lines in the file, with optional size argument
write(str)          Write passed string to file
writelines(strings) Write passed sequence of strings to the file
close()             Close the handle
flush()             Flush the internal I/O buffer to disk
seek(pos)           Move to indicated file position (integer)
tell()              Return current file position as integer
closed              True if the file is closed
