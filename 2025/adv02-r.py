import sys
import math
import aoc

small_primes = [2, 3, 5, 7, 11, 13]

class Solver:
  def __init__(self, max_split):
    self.max_split = max_split

  def mask(self, size, p):
    ans = 0
    for n in range(p):
      ans = ans * 10 ** (size // p) + 1
    return ans

  def add(self, a, b):
    if len(a) < len(b):
      return self.add(a, "9" * len(a)) + self.add("1" + "0" * len(a), b)
    a, b = int(a), int(b)
    size = len(str(a))
    ans = set()
    for p in small_primes:
      if p > self.max_split or size % p > 0:
        continue
      mask = self.mask(size, p)
      start = math.ceil(a / mask) * mask
      while start <= b:
        ans.add(start)
        start += mask
    return sum(ans)

def solve(data, max_split):
  ans = 0
  solver = Solver(max_split)
  for line in data:
    a, b = line.split("-")
    ans += solver.add(a, b)
  return ans

data = sys.stdin.read().strip().split(",")
aoc.cprint(solve(data, 2))
aoc.cprint(solve(data, len(data)))
