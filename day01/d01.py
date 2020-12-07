f = open('d01.in', 'r')

def findTwoEntriesProduct(lines, needed_sum):
  lines.sort()
  i, j = 0, len(lines)-1
  while i <= j:
    if lines[i] + lines[j] == needed_sum:
      return lines[i] * lines[j]
    elif lines[i] + lines[j] < needed_sum:
      i += 1
    else:
      j -= 1
  return -1

lines = list(map(int, f.read().strip().split('\n')))
print("Puzzle 1: ", findTwoEntriesProduct(lines, 2020))
