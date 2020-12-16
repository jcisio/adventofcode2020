f = open('d12.in', 'r')


def navigate(instructions):
    circle = 'NESW'
    coord = [0, 0]
    current_dir = 1
    for (d, s) in instructions:
        if d in circle:
            di = circle.find(d)
            if di >= 2:
                di = di - 2
                s = -s
            coord[di] += s
        elif d in 'LR':
            si = (s if d == 'R' else 360 - s)//90
            current_dir = (current_dir + si) % 4
        else:
            coord[current_dir % 2] += s if current_dir < 2 else -s
    return abs(coord[0]) + abs(coord[1])


instructions = [(line[0], int(line[1:])) for line in f.read().strip().split('\n')]
print("Puzzle 1: ", navigate(instructions))
