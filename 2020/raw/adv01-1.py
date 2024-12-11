import math
import sys
import aoc
import itertools

def solve(data, size):
  for x in itertools.combinations(data, size):
    if sum(x) == 2020:
      return math.prod(x)

data = aoc.ints(sys.stdin.read().splitlines())
print(solve(data, 2))
print(solve(data, 3))
