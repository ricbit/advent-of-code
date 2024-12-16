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

def round(t):
  out = t.copy()
  change = False
  for j, i in t.iter_all():
    if t[j][i] == "L":
      if all(t[jj][ii] != "#" for jj, ii in t.iter_neigh8(j, i)):
        out[j][i] = "#"
        change = True
    elif t[j][i] == "#":
      if sum(t[jj][ii] == "#" for jj, ii in t.iter_neigh8(j, i)) >= 4:
        out[j][i] = "L"
        change = True
  return out, change


def solve(t):
  p = 0
  while (out := round(t))[1]:
    t, change = out
    p += 1
    print(p)
  return sum(t[j][i] == "#" for j, i in t.iter_all())

data = [list(line) for line in sys.stdin.read().splitlines()]
data = aoc.Table(data)
aoc.cprint(solve(data))
