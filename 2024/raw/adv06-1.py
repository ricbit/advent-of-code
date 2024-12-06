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
  for j, i in t.iter_all():
    if t[j][i] == "^":
      pos = j * 1j + i
      t[j][i] = "."
      vdir = -1j
  visited = set()
  while t.cvalid(pos):
    print(pos)
    visited.add(pos)
    if t.cvalid(pos + vdir) and t.get(pos + vdir) == "#":
      vdir *= 1j
    else:
      pos += vdir
  return len(visited)

data = aoc.Table.read()
aoc.cprint(solve(data))
