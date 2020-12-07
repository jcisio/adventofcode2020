import re

f = open('d03.in', 'r')

def findTrees(trees):
    c, i, j, l = 0, 0, 0, len(trees[0])
    while i < len(trees):
        if trees[i][j] == '#':
            c += 1
        i += 1
        j = (j + 3) % l
    return c

trees = list(f.read().strip().split('\n'))
print("Puzzle 1: ", findTrees(trees))
