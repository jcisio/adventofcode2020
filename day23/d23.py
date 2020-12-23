f = open('d23.in', 'r')


def makeAMove(circle, current):
    L = len(circle)
    cup_current = circle[current]
    if current <= L-4:
        new_circle = circle[0:current+1] + circle[current+4:L]
        extract = circle[current+1:current+4]
    else:
        new_circle = circle[4+current-L:current+1]
        extract = circle[current+1:L] + circle[0:4+current-L]
    cup_destination = int(cup_current)
    while True:
        cup_destination -= 1
        if cup_destination == 0:
            cup_destination = L
        if str(cup_destination) in new_circle:
            break
    destination = new_circle.index(str(cup_destination))
    new_circle = new_circle[0:destination+1] + extract + new_circle[destination+1:]
    current = (new_circle.index(cup_current) + 1) % L
    return new_circle, current


def findPuzzle1(circle):
    current = 0
    for i in range(100):
        circle, current = makeAMove(circle, current)
    return (circle+circle)[circle.index('1')+1:circle.index('1')+len(circle)]


circle = f.read().strip()
print("Puzzle 1: ", findPuzzle1(circle))
