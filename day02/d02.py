import re

f = open('d02.in', 'r')

def countCorrectPasswords(lines):
    c = 0
    for line in lines:
        a,b,s,p = re.match(r'^(\d+)-(\d+) ([a-z]): (.*)$', line).groups()
        occurences = p.count(s)
        if int(a) <= occurences <= int(b):
            c += 1
    return c

lines = list(f.read().strip().split('\n'))
print("Puzzle 1: ", countCorrectPasswords(lines))
