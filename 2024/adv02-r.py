import aoc

def sign(x):
  return 1 if x > 0 else -1

def safe(data):
  diff = [a - b for a, b in zip(data, data[1:])]
  return all(sign(i) == sign(diff[0]) for i in diff) and all(0 < abs(i) < 4 for i in diff)

def almost_safe(x):
  return any(safe(x[:i] + x[i + 1:]) for i in range(len(x)))

part1, part2 = 0, 0
for data in aoc.ints_read():
  part1 += safe(data)
  part2 += almost_safe(data)

aoc.cprint(part1)
aoc.cprint(part2)
