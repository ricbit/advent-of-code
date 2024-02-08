import sys
import string
import re
import itertools
import math
import aoc
import heapq
import functools
import copy
from collections import Counter, deque
from dataclasses import dataclass

def build_cave(depth, y, x, factor):
  geolevel = aoc.Table([[0] * (factor * x + 1) for _ in range(factor *y + 1)])
  erosion = aoc.Table([[0] * (factor *x + 1) for _ in range(factor *y + 1)])
  regtype = aoc.Table([[0] * (factor *x + 1) for _ in range(factor *y + 1)])
  for j in range(factor * y + 1):
    for i in range(factor * x + 1):
      if j == 0 and i == 0:
        geolevel[j][i] = 0
      elif y == j and i == x:
        geolevel[j][i] = 0
      elif j == 0:
        geolevel[j][i] = i * 16807
      elif i == 0:
        geolevel[j][i] = j * 48271
      else:
        geolevel[j][i] = erosion[j][i-1] * erosion[j-1][i]
      erosion[j][i] = (geolevel[j][i] + depth) % 20183
      regtype[j][i] = erosion[j][i] % 3
  return regtype

def risk(regtype):
  return sum(sum(line) for line in regtype)

def heuristic(cave, y, x, j, i):
  return abs(y - j) + abs(x - i)

def mindist(cave, gy, gx):
  # torch 0  - gear  1  - neither 2
  allowed = {0: set([0, 1]), 1: set([1, 2]), 2: set([0, 2])}
  vnext = aoc.bq([(heuristic(cave, gy, gx, 0, 0), 0, 0, 0, 0)], size=5000)
  visited = set()
  while vnext:
    _, score, tool, y, x = vnext.pop()
    if (tool, y, x) in visited:
      continue
    if tool == 0 and y == gy and x == gx:
      return score
    visited.add((tool, y, x))
    for t in range(3):
      if t != tool and t in allowed[cave[y][x]]:
        if (t, y, x) not in visited:
          vnext.push((score + 7 + heuristic(cave, y, x, gy, gx), score + 7, t, y, x))
    for j, i in cave.iter_neigh4(y, x):
      if tool in allowed[cave[j][i]]:
        if (tool, j, i) not in visited:
          vnext.push((score + 1 + heuristic(cave, j, i, gy, gx), score + 1, tool, j, i))

data = [line.strip() for line in sys.stdin]
depth = int(data[0].split(": ")[1])
x, y = aoc.ints(data[1].split(":")[1].split(","))
cave = build_cave(depth, y, x, 1)
aoc.cprint(risk(cave))
cave = build_cave(depth, y, x, 5)
aoc.cprint(mindist(cave, y, x))
