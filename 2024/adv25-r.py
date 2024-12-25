import itertools
import aoc

def solve(data):
  keys = []
  for block in data:
    b = [int("".join("1" if x == "#" else "0" for x in line), 2)
         for line in aoc.transpose(block)]
    keys.append(b)
  ans = 0
  for a, b in itertools.combinations(keys, 2):
    if all(x & y == 0 for x, y in zip(a, b)):
      ans += 1
  return ans

data = aoc.line_blocks()
aoc.cprint(solve(data))
