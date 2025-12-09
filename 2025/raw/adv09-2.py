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
from atcoder.fenwicktree import FenwickTree as FT

def solve(points):
  maxrect = 0
  for p1, p2 in itertools.combinations(points, 2):
    if (m := (1 + abs(p1[0] - p2[0])) * (1 + abs(p1[1] - p2[1]))) > maxrect:
      maxrect = m
  return maxrect

def fill(t, y, x):
  pnext = [(y, x)]
  visited = set()
  visited.add((y, x))
  while pnext:
    j, i = pnext.pop()
    t[j][i] = "x"
    for jj, ii in t.iter_neigh4(j, i):
      if t[jj][ii] == "." and (jj, ii) not in visited:
        visited.add((jj, ii))
        pnext.append((jj, ii))

def solve2(points):
  reduced = set([p[0] for p in points] + [p[1] for p in points])
  reduced = sorted(reduced)
  inverse = {v: i for i, v in enumerate(reduced)}
  pmax = max(inverse.values()) + 1
  t = aoc.Table([["."] * pmax for _ in range(pmax)])
  for y, x in points:
    j = inverse[y]
    i = inverse[x]
    t[j][i] = "x"
  for p1, p2 in zip(points, points[1:] + [points[0]]):
    if p1[0] == p2[0]:
      # h
      j = inverse[p1[0]]
      p1i = inverse[p1[1]]
      p2i = inverse[p2[1]]
      for i in range(min(p1i, p2i), 1 + max(p1i, p2i)):
        t[j][i] = "x"
    else:
      # v
      i = inverse[p1[1]]
      p1j = inverse[p1[0]]
      p2j = inverse[p2[0]]
      for j in range(min(p1j, p2j), 1 + max(p1j, p2j)):
        t[j][i] = "x"
  fill(t, inverse[p1[0]] + 1, inverse[p1[1]] + 1)
  ft = [FT(t.w) for _ in range(t.h)]
  for j in range(t.h):
    for i in range(t.w):
      ft[j].add(i, 1 if t[j][i] == "." else 0)
  #for line in t.table:
  #  print("".join(line))
  maxr = 0
  for p1, p2 in itertools.combinations(points, 2):
    p1j, p1i = inverse[p1[0]], inverse[p1[1]]
    p2j, p2i = inverse[p2[0]], inverse[p2[1]]
    a, b = min(p1i, p2i), max(p1i, p2i)
    for j in range(min(p1j, p2j), 1 + max(p1j, p2j)):
      if ft[j].sum(a, b) > 0:
        break
    else:
      area = (1 + abs(p1[0] - p2[0])) * (1 + abs(p1[1] - p2[1]))
      if area > maxr:
        maxr = area
  return maxr

data = sys.stdin.readlines()
tiles = [list(map(int, line.split(","))) for line in data]
aoc.cprint(solve(tiles))
aoc.cprint(solve2(tiles))
