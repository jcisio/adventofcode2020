f = open('d14.in', 'r')


def applyInstruction(memory, mask, name, value):
    address = name[4:-1]
    data = 0
    multiplier = 1
    for bitmask in mask[-1::-1]:
        bit = value % 2
        value = value // 2
        if bitmask != 'X':
            bit = int(bitmask)
        data = data + bit*multiplier
        multiplier *= 2
    memory[address] = data
    return memory


def findSum(instructions):
    memory = {}
    for name, value in instructions:
        if name == 'mask':
            mask = value
        else:
            memory = applyInstruction(memory, mask, name, int(value))
    return sum(memory.values())


instructions = [line.split(' = ') for line in f.read().strip().split('\n')]
print("Puzzle 1: ", findSum(instructions))
