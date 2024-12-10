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

def solve(data):
  fsys = []
  for i, v in enumerate(data):
    if i % 2 == 0:
      fsys.extend([i // 2] * v)
    else:
      fsys.extend([-1] * v)
  free = fsys.index(-1)
  used = len(fsys) - 1
  while fsys[used] == -1:
    used -= 1
  while free < used:
    fsys[used], fsys[free] = fsys[free], fsys[used]
    used -= 1
    while fsys[used] == -1:
      used -= 1
    free += 1
    while fsys[free] != -1:
      free += 1
  return sum(i * y for i, y in enumerate(x for x in fsys if x != -1))

data = aoc.ints(list(sys.stdin.read().strip()))
aoc.cprint(solve(data))
