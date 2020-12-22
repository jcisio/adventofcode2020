f = open('d22.in', 'r')


def findScore(player1, player2):
    while player1 and player2:
        if (player1[0] > player2[0]):
            player1 = player1[1:] + [player1[0], player2[0]]
            player2 = player2[1:]
        else:
            player2 = player2[1:] + [player2[0], player1[0]]
            player1 = player1[1:]
    winner = player1 if player1 else player2
    return sum([winner[i]*(len(winner)-i) for i in range(len(winner))])


lines = f.read().strip().split('\n')
cards = (len(lines) - 3)//2
player1 = list(map(int, lines[1:cards+1]))
player2 = list(map(int, lines[cards+3:]))
print("Puzzle 1: ", findScore(player1, player2))
