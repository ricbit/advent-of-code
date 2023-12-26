import sys
import aoc
from collections import defaultdict

def max_item(bricks, i):
  return max(aoc.flatten((a[i], b[i]) for a, b in bricks))

def drop_bricks(bricks):
  maxj = max_item(bricks, 0) + 1
  maxi = max_item(bricks, 1) + 1
  floor = [[0] * maxi for _ in range(maxj)]
  block = [[-1] * maxi for _ in range(maxj)]
  for i, (a, b) in enumerate(bricks):
    y1, y2 = sorted([a[0], b[0]])
    x1, x2 = sorted([a[1], b[1]])
    maxh, support = 0, set()
    for y in range(y1, y2 + 1):
      for x in range(x1, x2 + 1):
        if floor[y][x] > maxh:
          support = set()
        if floor[y][x] >= maxh:
          maxh = floor[y][x]
          if block[y][x] >= 0:
            support.add(block[y][x])
    yield support
    for y in range(y1, y2 + 1):
      for x in range(x1, x2 + 1):
        floor[y][x] = b[2] - a[2] + maxh + 1
        block[y][x] = i

def invert_supports(supports):
  inverted = defaultdict(lambda: set())
  for base, support in enumerate(supports):
    for top in support:
      inverted[top].add(base)
  return inverted

def disintegrate(bricks, bases, tops):
  ans = 0
  for i in range(len(bases)):
    removed = defaultdict(lambda: [])
    vnext = [i]
    while vnext:
      brick = vnext.pop(0)
      for top in tops[brick]:
        removed[top].append(brick)
        if len(removed[top]) == len(bases[top]):
          vnext.append(top)
          ans += 1
  return ans

bricks = []
for line in sys.stdin:
  a, b = line.strip().split("~")
  a = [int(i) for i in a.split(",")]
  b = [int(i) for i in b.split(",")]
  if a[2] > b[2]:
    a, b = b, a
  bricks.append((a, b))
bricks.sort(key=lambda a: a[0][2])
supports = list(drop_bricks(bricks))
flat = aoc.flatten(list(s) for s in supports if len(s) == 1)
print(len(bricks) - len(set(flat)))
tops = invert_supports(supports)
print(disintegrate(bricks, supports, tops))
