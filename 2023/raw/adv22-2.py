import sys
import re
import itertools
import math

def flatten(x):
  return itertools.chain.from_iterable(x)

def drop_bricks(bricks):
  alli = list(flatten((a[0], b[0]) for a,b in bricks))
  allj = list(flatten((a[1], b[1]) for a,b in bricks))
  maxi = max(alli) + 1
  maxj = max(allj) + 1
  floor = [[0] * maxi for _ in range(maxj)]
  block = [[-1] * maxi for _ in range(maxj)]
  required = set()
  new_bricks = []
  for i, (a, b) in enumerate(bricks):
    y1, y2 = sorted([a[0], b[0]])
    x1, x2 = sorted([a[1], b[1]])
    maxh = 0
    support = set()
    for y in range(y1, y2 + 1):
      for x in range(x1, x2 + 1):
        if floor[y][x] == maxh:
          if block[y][x] >= 0:
            support.add(block[y][x])
        elif floor[y][x] >= maxh:
          maxh = floor[y][x]
          support = set()
          if block[y][x] >= 0:
            support.add(block[y][x])
    for y in range(y1, y2 + 1):
      for x in range(x1, x2 + 1):
        floor[y][x] = b[2] - a[2] + maxh + 1
        block[y][x] = i
    newa = (a[0], a[1], maxh + 1)
    newb = (b[0], b[1], b[2] - a[2] + maxh + 1)
    new_bricks.append((newa, newb))
  return new_bricks

bricks = []
for line in sys.stdin:
  a, b = line.strip().split("~")
  a = [int(i) for i in a.split(",")]
  b = [int(i) for i in b.split(",")]
  if a[2] > b[2]:
    a, b = b, a
  bricks.append((a, b))
bricks.sort(key=lambda a: a[0][2])
baseline = drop_bricks(bricks)
ans1, ans2 = len(baseline), 0
for i in range(len(bricks)):
  new_base = baseline.copy()
  new_base.pop(i)
  new_bricks = drop_bricks(new_base)
  d = sum(a[2] != c[2] for (a,b), (c,d) in zip(new_base, new_bricks))
  ans1 -= d > 0
  ans2 += d
print(ans1)
print(ans2)
    

  
