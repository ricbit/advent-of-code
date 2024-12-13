import sys
import string
import re
import itertools
import math
import cmath
import aoc
import heapq
import functools
import copy
from collections import Counter, deque
from dataclasses import dataclass

def solve(blocks):
  allcost = 0
  for ba, bb, prize in blocks:
    ainc = aoc.retuple("x_ y_", r".*: X([-+0-9]+), Y([-+0-9]+)", ba)
    binc = aoc.retuple("x_ y_", r".*: X([-+0-9]+), Y([-+0-9]+)", bb)
    pos = aoc.retuple("x_ y_", r".*: X=(\d+), Y=(\d+)", prize)
    print(ainc, binc, pos)
    pnext = [(0, 0, 0, 0, 0)]
    visited = set()
    while pnext:
      cost, pressa, pressb, y, x = heapq.heappop(pnext)
      if y > pos.y or x > pos.x:
        continue
      if (y, x) == (pos.y, pos.x):
        allcost += cost
        print(cost, pressa, pressb)
        break
      if (y, x) in visited:
        continue
      visited.add((y, x))
      for dinc, dcost,ppa,ppb in [(ainc, 3, 1, 0), (binc,1, 0, 1)]:
        ny, nx = y + dinc.y, x + dinc.x
        if (ny, ny) not in visited:
          heapq.heappush(pnext, (cost + dcost, pressa+ppa, pressb+ppb, ny, nx))
  return allcost

data = aoc.line_blocks()
aoc.cprint(solve(data))
