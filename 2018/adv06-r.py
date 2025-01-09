import sys
import aoc
from collections import Counter
import multiprocessing

def closest(j, i, points):
  kset, kval = set(), 1e6
  for ky, kx in points:
    if (d := abs(j - ky) + abs(i - kx)) < kval:
      kval = d
      kset = set([(ky, kx)])
    elif d == kval:
      kset.add((ky, kx))
  return kset

def forbidden_mask_x(points, y, bounds):
  mask = (closest(y, x, points) for x in [bounds.xmin, bounds.xmax])
  return set.union(*mask)

def forbidden_mask_y(points, x, bounds):
  mask = (closest(y, x, points) for y in [bounds.ymin, bounds.ymax])
  return set.union(*mask)

def find_forbidden(points, bounds, pool):
  forbidden = set()
  yrange = range(bounds.ymin, bounds.ymax + 1)
  mask = pool.starmap(forbidden_mask_x, ((points, y, bounds) for y in yrange))
  forbidden.update(*mask)
  xrange = range(bounds.xmin, bounds.xmax + 1)
  mask = pool.starmap(forbidden_mask_y, ((points, x, bounds) for x in xrange))
  forbidden.update(*mask)
  return forbidden

def solve1_y(bounds, j, points, forbidden):
  count = Counter()
  for i in range(bounds.xmin, bounds.xmax + 1):
    kset = closest(j, i, points)
    if len(kset) == 1 and (q := aoc.first(kset)) not in forbidden:
      count[q] += 1
  return count

def solve1(points, pool):
  bounds, count = aoc.bounds(points), Counter()
  forbidden = find_forbidden(points, bounds, pool)
  yrange = range(bounds.ymin, bounds.ymax + 1)
  star_range = ((bounds, y, points, forbidden) for y in yrange)
  for mask in pool.starmap(solve1_y, star_range):
    count.update(mask)
  return max(count.values())

def solve2(points, n):
  b, area = aoc.bounds(points), 0
  for j in range(b.ymin, b.ymax + 1):
    for i in range(b.xmin, b.xmax + 1):
      if sum(abs(j - ky) + abs(i - kx) for ky, kx in points) < n:
        area += 1
  return area

points = [aoc.ints(line.strip().split(", ")) for line in sys.stdin]
with multiprocessing.Pool() as pool:
  aoc.cprint(solve1(points, pool))
  aoc.cprint(solve2(points, 10000))
