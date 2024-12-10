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

def walk(t, y, x):
  pnext = [((y, x),)]
  trails = set()
  fulltrails = set()
  while pnext:
    tupletrail = pnext[0]
    trail = list(pnext[0])
    pnext.pop(0)
    y, x = trail[-1]
    if tupletrail in trails:
      continue
    trails.add(tupletrail)
    if t[y][x] == 9:
      fulltrails.add(tupletrail)
    for j, i in t.iter_neigh4(y, x):
      if t[j][i] == t[y][x] + 1:
        pnext.append(tuple(trail +[(j, i)]))
  return len(fulltrails)


def solve(t):
  ans = 0
  for j, i in t.iter_all():
    if t[j][i] == 0:
      ans += walk(t, j, i)
  return ans

data = [[(int(i) if i != "." else -10) for i in j] for j in sys.stdin.read().splitlines()]
data = aoc.Table(data)
aoc.cprint(solve(data))
