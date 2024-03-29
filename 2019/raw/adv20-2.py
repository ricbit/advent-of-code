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
from aoc.refintcode import IntCode

def iter_codes(t):
  for j, i in t.iter_all():
    if t[j][i].isupper() and t[j + 1][i].isupper():
      if t[j - 1][i] == ".":        
        yield t[j][i] + t[j + 1][i], j - 1, i
      else:
        yield t[j][i] + t[j + 1][i], j + 2, i
    if t[j][i].isupper() and t[j][i + 1].isupper():
      if t[j][i - 1] == ".":
        yield t[j][i] + t[j][i + 1], j, i - 1
      else:
        yield t[j][i] + t[j][i + 1], j, i + 2

def build_maze(t):
  codes = aoc.ddict(lambda: [])
  teleport = {}
  for code, j, i in iter_codes(t):
    codes[code].append((j, i))
  start, end = None, None
  inv = {}
  for code, portals in codes.items():
    if len(portals) == 2:
      a, b = portals
      teleport[a] = b
      teleport[b] = a
      inv[a] = code
      inv[b] = code
    elif code == "AA":
      start = portals[0]
    elif code == "ZZ":
      end = portals[0]
  
  return teleport, start, end, inv

def solve(t, teleport, start, end, inv):
  visited = set()
  vnext = deque([(0, 0, start)])
  yborder = [3, t.h - 4]
  xborder = [3, t.w - 4]
  while vnext:
    k = vnext.popleft()
    print("ok", k)
    score, level, (y, x) = k
    if (level, (y, x)) == (0, end):
      return score
    if (level, y, x) in visited:
      continue
    visited.add((level, y, x))
    for j, i in t.iter_neigh4(y, x):
      if t[j][i] == "." and (level, j, i) not in visited:
        vnext.append((score + 1, level, (j, i)))
    if (y, x) in teleport:
      j, i = teleport[(y, x)]
      if (y in yborder) or (x in xborder):
        if ((level - 1, j, i) not in visited) and (level > 0):
          vnext.append((score + 1, level - 1, (j, i)))
      else:
        if (level + 1, j, i) not in visited:
          vnext.append((score + 1, level + 1, (j, i)))

def build_table(lines):
  size = len(lines[0])
  empty = [" "] * (size + 2)
  tt = [empty] + [" " + line + " " for line in lines] + [empty]
  return aoc.Table(tt)

t = build_table([line.rstrip("\n") for line in sys.stdin])
teleport, start, end, inv = build_maze(t)
aoc.cprint(solve(t, teleport, start, end, inv))
