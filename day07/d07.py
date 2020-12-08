import re

f = open('d07.in', 'r')


def read_rules(lines):
    rules = {}
    for line in lines:
        outer, inner = line.strip('.').split(' contain ')
        if inner == 'no other bags':
            continue
        outer = outer[:-5]# ' bags'
        inner = inner.split(', ')
        rules[outer] = set([re.match(r'\d+ (.+?) bags?', e).group(1) for e in inner])
    return rules


def find_shiny_gold(rules):
    bags = set(['shiny gold'])
    found = True
    while found:
        found = False
        for bag in rules:
            if bag not in bags and len(bags.intersection(rules[bag])) > 0:
                found = True
                bags.add(bag)
    return len(bags)-1


rules = read_rules(f.read().split('\n'))
print("Puzzle 1: ", find_shiny_gold(rules))
