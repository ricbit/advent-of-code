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

def score(path):
  hist = Counter()
  for a, b in zip(path, path[1:]):
    hist[abs(a - b)] += 1
  return hist[1] * hist[3]

def solve(data):
  data.append(0)
  start = max(data) + 3
  data.append(start)
  data = set(data)
  pnext = [(start, tuple())]
  visited = set()
  while pnext:
    pos, path = pnext.pop()
    if path in visited:
      continue
    visited.add(path)
    for i in range(max(0, pos - 3), pos + 3):
      if i in data and i not in path:
        pnext.append((i, (new_path := tuple(list(path) + [i]))))
        if len(new_path) == len(data) and i == 0:
          return score(new_path)
  return None

data = aoc.ints(sys.stdin.read().strip().splitlines())
aoc.cprint(solve(data))
