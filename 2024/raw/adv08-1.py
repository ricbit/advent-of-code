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

def check(t, x):
  return 0 <= x. real < t.w and 0 <= x.imag < t.h

def solve(t):
  pos = aoc.ddict(list)
  for j, i in t.iter_all():
    if t[j][i] != '.':
      pos[t[j][i]].append(j * 1j + i)
  anti = set()
  for k, v in pos.items():
    for a, b in itertools.combinations(v, 2):
      if check(t, 2*b-a):
        anti.add(2*b-a)
      if check(t, 2*a-b):
        anti.add(2*a-b)
  return len(anti)

data = aoc.Table.read()
aoc.cprint(solve(data))
