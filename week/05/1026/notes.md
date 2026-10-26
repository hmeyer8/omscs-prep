# File work: 

consider the following: 
```py
with open('pi.txt', 'r') as file_object:
    contents = file_object.read()
    print(contents)
```
to do any work we first need to open the file with `open()`
`with` keyword closes the file when the code is complete. 
`read()` returns an empty string at the end of a file; this empty string shows up as a blank line but we can throw in the `rstrip()` function to take care of that

### relative paths: 

the `with open('pi.txt') as file_object:` line looks in the current directory. If you want to go deeper into a folder that is in the current directory we can use a **relative path**. What that does is just guide python to look for a file inside a deeper directory. 
we would do this via `with open('text_files\pi.txt')`. Linux or OS X you would have the forward slash

If the file we are tapping into was in a different folder alltogether then we would have to use an **absolute file path**: 
```py
# on Linux and OS X
file_path = '/home/ehmatthes/other_files/text_files/filename.txt'
with open(file_path) as file_object:
# and on Windows they look like this:
file_path = 'C:\Users\ehmatthes\other_files\text_files\filename.txt'
with open(file_path) as file_object:
```


to read line by line we can loop over each line via a simple loop: 
```py
with open('pi.txt', 'r') as file_object:
    for x in file_object:
        print(x.rstrip())
```
here I was able to take out the extra line that occurs when we just simply print it

also while using `with` we can only access the data within the file

### Working a files contents: 

lets try to build a single string containing all the digits of pi.txt. Here we will take out the new lines and delete all extra spaces that occur when we do that

```py
pi_str = ''
with open('pi.txt') as file_object:
    lines = file_object.readlines()
    for x in lines:
        pi_str += x.rstrip()
    print(pi_str)
    print(len(pi_str))
```

now lets try to build a program that finds your birthday in the first million digits of pi

```py
filename = 'pi_mil.txt'
with open(filename) as file_object:
    lines = file_object.readlines()
    birthday = input("Enter your birthday, in the form mmddyy: ")
    if birthday in lines:
        print("Your birthday appears in the first million digits of pi!")
    else:
        print("Your birthday does not appear in the first million digits of pi.")
```
