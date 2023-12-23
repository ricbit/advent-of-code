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
    if len(support) == 1:
      required.add(list(support)[0])
    print(i, (a, b), support)
    print("\n".join("-".join(str(i) for i in row) for row in floor))
    print()
  return len(bricks) - len(required)

bricks = []
for line in sys.stdin:
  a, b = line.strip().split("~")
  a = [int(i) for i in a.split(",")]
  b = [int(i) for i in b.split(",")]
  if a[2] > b[2]:
    a, b = b, a
  bricks.append((a, b))
bricks.sort(key=lambda a: a[0][2])

print(drop_bricks(bricks))
  
