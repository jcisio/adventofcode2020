f = open('d24.in', 'r')


def findCoordinates(tile):
    x, y = 0, 0
    moves = {'e': (2,0), 'w': (-2,0), 'ne': (1,1), 'nw': (-1,1), 'se': (1,-1), 'sw': (-1,-1)}
    i = 0
    while i < len(tile):
        move = tile[i]
        i += 1
        if move in 'ns':
            move += tile[i]
            i += 1
        x, y = x + moves[move][0], y + moves[move][1]
    return (x,y)


def findBlackTiles(tiles):
    swap = {}
    for tile in tiles:
        coordinates = findCoordinates(tile)
        if coordinates not in swap:
            swap[coordinates] = 0
        swap[coordinates] = 1 - swap[coordinates]
    return list(swap.values()).count(1)


tiles = f.read().strip().split('\n')
print("Puzzle 1: ", findBlackTiles(tiles))
