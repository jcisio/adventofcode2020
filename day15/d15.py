f = open('d15.in', 'r')


def findRound(rounds, n):
    current = len(rounds)
    while current < n:
        rounds.reverse()
        try:
            i = rounds.index(rounds[0], 1)
        except ValueError:
            i = 0
        rounds.reverse()
        rounds.append(i)
        current += 1
    return rounds[-1]

rounds = list(map(int, f.read().strip().split(',')))
print("Puzzle 1: ", findRound(rounds, 2020))
