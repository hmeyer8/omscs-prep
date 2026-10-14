# PDA 3.3 finish up

### Bytes and Unicode with files

Default behavior for python files is text mode, which means we would want to work with python strings. This is different from binary mode which we can get to if we simply add a `b` 

consider the following: 
```py
>>> ord("ñ")                        # shows the character code according to Windows-1252
241
>>> list("ñ".encode("latin-1"))     #Windows-1252 is also a superset of latin-1
[241]
>>> list("ñ".encode("utf-8"))       #shows the decimal of the n tilde. Decimal and hexidecimal are two ways to write the same character
[195, 177]
>>> text = "ñ"
>>> text.encode("utf-8")            # shows the hexidecimal bytes associated with the n tilde
b'\xc3\xb1'
>>> len(text)                       # shows how  many characters for n tilde
1
>>> len(text.encode("utf-8"))       # then shows how many bytes which is the \xc3\xb1
2
>>> text
'ñ'
```
quick hexidecimal to decimal run through: for example lets do `\xf3`: 

\x shows hexidecimal
hexadecimal uses 16 digits: `0-9` then `A-F` where A = 10 and F = 15 
first digit is in the sixteens place so we multiply the digit by 16
f = 15; 15 * 16 = 240. The second digit is in the ones place, so hexidecimal f3 is equal to 243. 

Here python reads enough bytes (could be 10, could be 40) from the file to decode that many characters. If we open the file in 'rb' mode instead, read requests exactly that many bytes
```py
>>> path  
'C:/Users/henme/Downloads/fam.txt'
>>> with open(path, encoding = 'utf-8') as f:
...     chars = f.read(10)
... 
>>> chars
'sueña\nhenr'
>>> with open(path, 'rb') as w:
...     char1 = w.read(10)
... 
>>> char1
b'sue\xc3\xb1a\r\nhe'
```

depending on the text encoding we might be able to decode the bytes to a `str` object ourselves, but we need to ensure the encoded unicode characters is fully formed: 
```py
>>> char1
b'sue\xc3\xb1a\r\nhe'
>>> char1.decode('utf-8')
'sueña\r\nhe'
>>> char1
b'sue\xc3\xb1a\r\nhe'
>>> char1[4].decode('utf-8')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'int' object has no attribute 'decode'
```

the text mode combined with the encoding option of open shows a convenient way to convert to one unicode encoding to another: 
```py
In [236]: sink_path = 'sink.txt'
In [237]: with open(path) as source:
.....:     
with open(sink_path, 'xt', encoding='iso-8859-1') as sink:
.....:         
sink.write(source.read())
In [238]: with open(sink_path, encoding='iso-8859-1') as f:
.....:     
print(f.read(10))
Sueña el r
```


# PT CH 6 Modules

if we quit the interpreter and enter in it again we lose all the definitions, functions and variables. 
we are better to write scripts and even split it into different files for maintenance. 
Say we want to use a great function but dont want to constantly have to copy and paste it? Python has a way to put definitions in a file and use them in a script or in an interactive instance in the interpreter
Such file is a module. Definitions from a module can be imported into other modules or into the main module- which is the collection of variables you have access to at the top level. 

A module is a file containing python definitions and statements. The file name is the file name with the `.py` appended