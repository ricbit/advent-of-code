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

def solve(data, pos, py, px, doors):
  print(data)
  while data[pos] != "$":
    print(pos, data[pos], py, px)
    if data[pos] in aoc.DIRECTIONS3.keys():
      ny = py + aoc.DIRECTIONS3[data[pos]][0]
      nx = px + aoc.DIRECTIONS3[data[pos]][1]
      pos += 1
      doors[(py, px)].add((ny, nx))
      py, px = ny, nx
    elif data[pos] == "(":
      while data[pos] != ")":
        pos = solve(data, pos + 1, py, px, doors)
      pos += 1
    else:
      return pos
  return pos

def search(doors, py, px):
  vnext = deque([(0, py, px)])
  visited = set()
  msize = 0
  count = 0
  while vnext:
    size, py, px = vnext.popleft()
    print(f"-- {size} {py} {px}")
    if (py, px) in visited:
      continue
    visited.add((py, px))
    if size >= 1000:
      count += 1
    if msize < size:
      msize = size
    for ny, nx in doors[(py, px)]:
      if (ny, nx) not in visited:
        vnext.append((size + 1, ny, nx))
  return msize, count

data = re.search(r"\^(.*\$)", sys.stdin.read().strip()).group(1)
doors = aoc.ddict(lambda: set())
solve(data, 0, 0, 0, doors)
msize, count = search(doors, 0, 0)
aoc.cprint(msize)
aoc.cprint(count)
