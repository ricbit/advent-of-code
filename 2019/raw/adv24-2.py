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

FRAC = {
  1: [(0, 2, 6), (1, 8, 12)],
  2: [(0, 1, 7, 3), (1, 8)],
  3: [(0, 2, 8, 4), (1, 8)],
  4: [(0, 3, 9, 5), (1, 8)],
  5: [(0, 4, 10), (1, 8, 14)],
  6: [(0, 1, 7, 11), (1, 12)],
  7: [(0, 2, 6, 8, 12)],
  8: [(0, 3, 7, 9), (-1, 1, 2, 3, 4, 5)],
  9: [(0, 4, 8, 14, 10)],
  10: [(0, 5, 15, 9), (1, 14)],
  11: [(0, 6, 12, 16), (1, 12)],
  12: [(0, 7, 11, 17), (-1, 1, 6, 11, 16, 21)],
  14: [(0, 19, 15, 9), (-1, 5, 10, 15, 20, 25)],
  15: [(0, 10, 14, 20), (1, 14)],
  16: [(0, 11, 21, 17), (1, 12)],
  17: [(0, 12, 16, 18, 22)],
  18: [(0, 17, 23, 19), (-1, 21, 22, 23, 24, 25)],
  19: [(0, 14, 18, 24, 20)],
  20: [(0, 15, 25, 19), (1, 14)],
  21: [(0, 22, 16), (1, 18, 12)],
  22: [(0, 21, 17, 23), (1, 18)],
  23: [(0, 22, 18, 24), (1, 18)],
  24: [(0, 23, 19, 25), (1, 18)],
  25: [(0, 24, 20), (1, 18, 14)],
}

def single_neigh(level, j, i):
  c = j * 5 + i + 1
  for group in FRAC[c]:
    head, *tail = group
    for t in tail:
      cc = t - 1
      jj = cc // 5
      ii = cc % 5
      yield (level + head, jj, ii)

def neigh(bugs, t):
  ans = set()
  for level, j, i in bugs:
    for n in single_neigh(level, j, i):
      ans.add(n)
  return ans

def bug_iterator(t):
  bugs = set()
  for j, i in t.iter_all():
    if t[j][i] == "#":
      bugs.add((0, j, i))
  while True:
    newbugs = set()
    for level, j, i in neigh(bugs, t):
      n = sum((l2, jj, ii) in bugs for l2, jj, ii in single_neigh(level, j, i))
      if (level, j, i) in bugs:
        if n == 1:
          newbugs.add((level, j, i))
      else:
        if 1 <= n <= 2:
          newbugs.add((level, j, i))
    bugs = newbugs
    yield bugs

def solve2(t):
  for i, bugs in enumerate(bug_iterator(t)):
    if i == 49:
      return len(bugs)

t = aoc.Table.read()
aoc.cprint(solve2(t))
