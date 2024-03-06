import sys
import aoc
from collections import Counter

def closest(j, i, points):
  kset, kval = set(), 1e6
  for ky, kx in points:
    if (d := abs(j - ky) + abs(i - kx)) < kval:
      kval = d
      kset = set([(ky, kx)])
    elif d == kval:
      kset.add((ky, kx))
  return kset

def find_forbidden(points, bounds):
  forbidden = set()
  for y in range(bounds.ymin, bounds.ymax + 1):
    for x in [bounds.xmin, bounds.xmax]:
      forbidden |= closest(y, x, points)
  for x in range(bounds.xmin, bounds.xmax + 1):
    for y in [bounds.ymin, bounds.ymax]:
      forbidden |= closest(y, x, points)
  return forbidden

def solve1(points):
  bounds, count = aoc.bounds(points), Counter()
  forbidden = find_forbidden(points, bounds)
  for j in range(bounds.ymin, bounds.ymax + 1):
    for i in range(bounds.xmin, bounds.xmax + 1):
      kset = closest(j, i, points)
      if len(kset) == 1 and (q := aoc.first(kset)) not in forbidden:
        count[q] += 1
  return max(count.values())

def solve2(points, n):
  b, area = aoc.bounds(points), 0
  for j in range(b.ymin, b.ymax + 1):
    for i in range(b.xmin, b.xmax + 1):
      if sum(abs(j - ky) + abs(i - kx) for ky, kx in points) < n:
        area += 1
  return area

points = [aoc.ints(line.strip().split(", ")) for line in sys.stdin]
aoc.cprint(solve1(points))
aoc.cprint(solve2(points, 10000))
