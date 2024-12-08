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
      d = b-a
      for i in itertools.count(0):
        if t.cvalid(a+i*d):
          anti.add(a+i*d)
        else:
          break
      for i in itertools.count(-1, -1):
        if t.cvalid(a+i*d):
          anti.add(a+i*d)
        else:
          break
       
  return len(anti)

data = aoc.Table.read()
aoc.cprint(solve(data))
