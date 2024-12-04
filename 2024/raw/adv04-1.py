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

def solve(t):
  dirs = [(0,1), (1,0), (0,-1),(-1,0),(1,-1),(1,1),(-1,1),(-1,-1)]
  ans = 0
  for j, i in t.iter_all():
    for dj, di in dirs:
      ok = True
      for k, w in enumerate("XMAS"):
        y, x = j + k * dj, i + k * di
        if t.valid(y, x) and t[y][x] == w:
          continue
        ok = False
      if ok:
        ans += 1

  return ans

data = aoc.Table.read()
aoc.cprint(solve(data))
