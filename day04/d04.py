import re

f = open('d04.in', 'r')

def countValidPassport(documents):
    required_fields = 'byr iyr eyr hgt hcl ecl pid'.split()
    c = 0
    for document in documents:
        missed_fields = False
        for field in required_fields:
            if not re.search(rf'\b{field}:', document):
                missed_fields = True
                break
        if not missed_fields:
            c += 1
    return c

documents = list(f.read().strip().split('\n\n'))
print("Puzzle 1: ", countValidPassport(documents))
