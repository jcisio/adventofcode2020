f = open('d06.in', 'r')


def find_total_yes(groups):
    c = 0
    for group in groups:
        c += len(set(group.replace('\n', '')))
    return c


groups = f.read().strip().split('\n\n')
print("Puzzle 1: ", find_total_yes(groups))
