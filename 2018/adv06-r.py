import sys
import aoc
from collections import Counter

def solve1(data):
  b, count = aoc.bounds(data), Counter()
  smalldata = [(dy, dx) for dy, dx in data 
      if dy not in [b.miny, b.maxy] and dx not in [b.minx, b.maxx]]
  for j in range(b.miny, b.maxy + 1):
    for i in range(b.minx, b.maxx + 1):
      kset, kval = [], 1e6
      for k, (ky, kx) in enumerate(smalldata):
        if (d := abs(j - ky) + abs(i - kx)) < kval:
          kval = d
          kset = [k]
        elif d == kval:
          kset.append(k)
      if len(kset) == 1:
        count[kset[0]] += 1
  return max(count.values())

def solve2(data, n):
  b, area = aoc.bounds(data), 0
  for j in range(b.miny, b.maxy + 1):
    for i in range(b.minx, b.maxx + 1):
      if sum(abs(j - ky) + abs(i - kx) for ky, kx in data) < n:
        area += 1
  return area

data = [aoc.ints(line.strip().split(", ")) for line in sys.stdin]
aoc.cprint(solve1(data))
aoc.cprint(solve2(data, 10000))
