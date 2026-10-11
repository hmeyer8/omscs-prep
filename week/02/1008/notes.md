# 3.2 cont: FUNctions

### FUNctions are objects

lets do some data cleaning:
```py
states = ['   Alabama ', 'Georgia!', 'Georgia', 'georgia', 'FlOrIda', ' .....:         ' , 'south   carolina##', 'West virginia?']
import re
def clean_strings(strings):
    result = []
    for value in strings:
        value = value.strip()
        value = re.sub('[!#.?:]', '', value)
        value = value.title()
        result.append(value)
    return print(result)
clean_strings(states)
out: ['Alabama', 'Georgia', 'Georgia', 'Georgia', 'Florida', '', 'South   Carolina', 'West Virginia']
```
### Lambda functions: 
Also called anonymous functions
These are a way to write functions consisting of a single statement