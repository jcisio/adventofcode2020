f = open('d11.in', 'r')


def stabilizeSeats(seats):
    L = len(seats)
    N = len(seats[0])
    extended_seats = ['.'*(N+2)]
    for n in range(L):
        extended_seats.append('.' + seats[n] + '.')
    extended_seats.append('.'*(N+2))
    nearby = [(-1,-1), (-1,1), (1,-1), (1,1), (0,1), (0,-1), (1,0), (-1,0)]
    while True:
        changed = False
        new_seats = ['.'*(N+2)]*(L+2)
        for j in range(L):
            for i in range(N):
                if extended_seats[j+1][i+1] == '.':
                    continue
                c = sum([1 if extended_seats[j+1+x][i+1+y] == '#' else 0 for (x, y) in nearby])
                if extended_seats[j+1][i+1] == '#' and c >= 4:
                    new_seat = 'L'
                    changed = True
                elif extended_seats[j+1][i+1] == 'L' and c == 0:
                    new_seat = '#'
                    changed = True
                else:
                    new_seat = extended_seats[j+1][i+1]
                new_seats[j+1] = new_seats[j+1][:i+1] + new_seat + new_seats[j+1][i+2:]

        if not changed:
            break
        extended_seats = new_seats
    return sum([1 if extended_seats[j+1][i+1] == '#' else 0 for i in range(N) for j in range(L)])


seats = list(f.read().strip().split('\n'))
print("Puzzle 1: ", stabilizeSeats(seats))
