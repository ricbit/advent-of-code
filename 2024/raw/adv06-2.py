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

def is_loop(t):
  for j, i in t.iter_all():
    if t[j][i] == "^":
      start = j * 1j + i
      t[j][i] = "."
      vdir = -1j
  pos = start
  visited = set()
  while t.cvalid(pos) and (pos, vdir) not in visited:
    visited.add((pos, vdir))
    while t.cvalid(pos + vdir) and t.get(pos + vdir) == "#":
      vdir *= 1j
    pos += vdir
  t[int(start.imag)][int(start.real)] = "^"
  return t.cvalid(pos)

def solve(t):
  ans = 0
  for j, i in t.iter_all():
    if t[j][i] == ".":
      print(j,i)
      t[j][i] = "#"
      if is_loop(t):
        print("yes")
        ans += 1
      t[j][i] = "."
  return ans

data = aoc.Table.read()
aoc.cprint(solve(data))
