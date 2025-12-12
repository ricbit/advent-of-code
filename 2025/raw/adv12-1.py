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

class Solver:
  def __init__(self, rotated, required, x, y):
    self.rotated = rotated
    self.required = required
    self.x = x
    self.y = y

  def stamp(self, tt, shape, j, i):
    for jj in range(3):
      for ii in range(3):
        if shape[jj * 3 + ii] == "#":
          if tt[j + jj][i + ii] == "#":
            return False
          tt[j + jj][i + ii] = "#"
    return True 

  @functools.cache
  def search(self, grid, pos):
    if pos == len(self.required):
      #print(grid)
      return True
    t = aoc.Table([list(grid[i * self.x:(i + 1) * self.x]) for i in range(self.y)])
    #print(t)
    #print()
    for shape in self.rotated[self.required[pos]]:
      for j in range(1 + self.y - 3):
        for i in range(1 + self.x - 3):
          tt = t.copy()
          if self.stamp(tt, shape, j, i):
            #print(shape, j, i)
            #print(tt)
            newgrid = "".join("".join(i) for i in tt.table)
            if self.search(newgrid, pos + 1):
              return True
    return False

def solve(shapes, gifts):
  rotated = []
  for shape in shapes:
    unique = set()
    for b in range(4):
      shape = shape.clock90()
      unique.add("".join("".join(i) for i in shape.table))
      unique.add("".join("".join(i) for i in shape.flipx().table))
    rotated.append(unique)
  ans = 0
  for line in gifts:
    gift = aoc.retuple("x_ y_ spec", r"(\d+)x(\d+): (.*)$", line)
    amount = aoc.ints(gift.spec.split())
    required = list(itertools.chain(*[[i] * a for i, a in zip(range(len(amount)), amount)]))
    #x, y, rot = [], [], []
    #for i in range(len(required)):
    #  x.append(z3.Int(f"x{i}"))
    #  y.append(z3.Int(f"y{i}"))
    #  rot.append(z3.Int(f"rot{i}"))
    x = sum(aoc.first(rotated[i]).count("#") for i in required)
    if x <= gift.x * gift.y:
      ans += 1
    #s = Solver(rotated, required, gift.x, gift.y)
    #print(s.search("." * (gift.x * gift.y), 0))

  return ans

data = aoc.line_blocks()
print(data)
shapes = [aoc.Table(b[1:]) for b in data[:-1]]
gifts = data[-1]
aoc.cprint(solve(shapes, gifts))
