f = open('d09.in', 'r')


def testPosition(numbers, p):
    if p < 25:
        return True
    for i in range(p-25, p-1):
        for j in range(i+1, p):
            if numbers[i] != numbers[j] and numbers[i] + numbers[j] == numbers[p]:
                return True
    return False


def findOddNumber(numbers):
    p = 25
    while True:
        if not testPosition(numbers, p):
            return numbers[p]
        p += 1


numbers = list(map(int, f.read().strip().split('\n')))
print("Puzzle 1: ", findOddNumber(numbers))
