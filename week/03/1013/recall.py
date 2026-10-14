# make a new file that has no blank lines from file path

path = "C:/Users/henme/Downloads/fam.txt"
with open(path) as w:
    hi = w.readlines()
print(hi)
with open('temp.txt', 'w') as f:
    f.writelines(x for x in open(path) if len(x)>1)
with open('temp.txt') as l:
    lines = l.readlines()
print(lines)