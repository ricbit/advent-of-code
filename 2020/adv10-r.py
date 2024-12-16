import sys
import aoc
import functools
from collections import Counter

def score(path):
  hist = Counter()
  for a, b in zip(path, path[1:]):
    hist[abs(a - b)] += 1
  return hist[1] * hist[3]

@functools.cache
def count(start, end, path):
  if end == start:
    return 1
  ans = 0
  for i in path:
    if start - 3 <= i < start:
      ans += count(i, 0, path)
  return ans

def count_paths(path):
  start = max(path) + 3
  return count(start, 0, tuple(path + [0]))

def part1(data):
  data = data + [max(data) + 3, 0]
  data.sort()
  return score(data)

data = aoc.ints(sys.stdin.read().strip().splitlines())
aoc.cprint(part1(data))
aoc.cprint(count_paths(data))
