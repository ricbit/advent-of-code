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

class Grow:
  def __init__(self, t):
    self.t = t
    self.mask = t.copy()

  def grow(self, y, x):
    pnext = [(y, x)]
    visited = set()
    area, perimeter = 0, 0
    while pnext:
      y, x = pnext.pop()
      if (y, x) in visited:
        continue
      visited.add((y, x))
      self.mask[y][x] = 0
      area += 1
      perimeter += 4
      for j, i in self.t.iter_neigh4(y, x):
        if (j, i) in visited:
          perimeter -= 2
      for j, i in self.t.iter_neigh4(y, x):
        if self.t[j][i] == self.t[y][x] and self.mask[j][i] != 0:
          pnext.append((j, i))
    return area * perimeter

  def solve(self):
    ans = 0
    for j, i in self.t.iter_all():
      if self.mask[j][i] != 0:
        ans += self.grow(j, i)
    return ans

data = aoc.Table.read()
g = Grow(data)
aoc.cprint(g.solve())
