import sys
import re
import itertools
import math
import aoc
import heapq
import functools
from collections import *

DIRS = {"U": 0, "D": 1, "L": 2, "R": 3}

def isopen(path, name):
  doors = [(ord(i) > ord("a")) for i in aoc.md5(path)[:4]]
  return doors[DIRS[name]]

def search(seed):
  vnext = deque([(0, 0, seed)])
  long = ""
  while vnext:
    y, x, path = vnext.popleft()
    if (y, x) == (3, 3):
      if len(path) > len(long):
        long = path
      continue
    for name, (dj, di) in aoc.DIRECTIONS.items():
      j, i = y + dj, x + di
      if i < 0 or j < 0 or i > 3 or j > 3:
        continue
      if isopen(path, name):
        vnext.append((j, i, path + name))
  return len(long) - len(seed)

seed = sys.stdin.read().strip()
aoc.cprint(search(seed))

