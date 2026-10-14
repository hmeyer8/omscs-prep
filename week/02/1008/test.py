states = ['   Alabama ', 'Georgia!', 'Georgia', 'georgia', 'FlOrIda', ' .....:         ' , 'south   carolina##', 'West virginia?']

def distinct_character(strings):
    result = []
    for value in strings:
        x = value.upper()
        for n in x:
            n.upper()
            result.append(n)
    print(set(result))
distinct_character(states)