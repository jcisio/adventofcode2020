f = open('d10.in', 'r')


def findDifference(adapters):
    diff = [0]*4
    current = 0
    for adapter in adapters:
        diff[adapter-current] += 1
        current = adapter
    diff[3] += 1 # built-in adapter
    return diff[1] * diff[3]


adapters = sorted(list(map(int, f.read().strip().split('\n'))))
print("Puzzle 1: ", findDifference(adapters))
