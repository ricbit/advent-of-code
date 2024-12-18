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

def search(t):
  pnext = deque([(0, 0, 0)])
  visited = {}
  end = t.w + t.h * 1j -1 -1j
  while pnext:
    cost, pos, prev = pnext.popleft()
    if pos in visited:
      continue
    visited[pos] = prev
    if pos == end:
      return True
    y, x = int(pos.imag), int(pos. real)
    for j, i in t.iter_neigh4(y, x):
      if t[j][i] == ".":
        pnext.append((cost + 1, j * 1j + i, pos))
  return False

def outer(t, data):
  for i, (x, y) in enumerate(data):
    print(i)
    t[y][x] = "#"
    if i > 1024 and not search(t):
      return x, y

def solve(data):
  h = 71
  w = 71
  t = [["."] * w for _ in range(h)]
  t = aoc.Table(t)
  return outer(t, data)
  pos = end
  ans = 0
  while pos != 0:
    ans += 1
    pos = visited[pos]
    y, x = int(pos.imag), int(pos. real)
    t[y][x] = "O"

  for line in t.table:
    print("".join(line))
    
  return ans

data = [aoc.ints(x.split(",")) for x in sys.stdin.read().splitlines()]
aoc.cprint(solve(data))
