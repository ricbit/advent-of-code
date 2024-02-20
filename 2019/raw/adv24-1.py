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

def solve(t):
  visited = set()
  while True:
    tt = copy.deepcopy(t)
    for j, i in t.iter_all():
      n = sum(t[jj][ii] == "#" for jj, ii in t.iter_neigh4(j, i))
      if t[j][i] == "#":
        if n != 1:
          tt[j][i] = "."
        else:
          tt[j][i] = "#"
      else:
        if 1 <= n <= 2:
          tt[j][i] = "#"
        else:
          tt[j][i] = "."
    t3 = tuple(tuple(line) for line in tt.table)
    if t3 in visited:      
      score = sum(2 ** i for i, c in enumerate(aoc.flatten(tt.table)) if c == "#")
      for line in tt.table:
        print(line)
      return score
    visited.add(t3)
    print("--")
    t = tt
  return 0

t = aoc.Table.read()
aoc.cprint(solve(t))
