import sys
import aoc
import math
import functools

@functools.cache
def search(s, pos, left):
  if left == 0:
    return 0
  if pos == len(s):
    return -math.inf
  skip = search(s, pos + 1, left)
  use = int(s[pos]) * 10 ** (left - 1) + search(s, pos + 1, left - 1)
  return max(skip, use)

def solve(data, size):
  return sum(search(line.strip(), 0, size) for line in data)

data = sys.stdin.readlines()
aoc.cprint(solve(data, 2))
aoc.cprint(solve(data, 12))
