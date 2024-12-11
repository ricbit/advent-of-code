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
  y, x = 0, 0
  ans = 0
  while y < t.h - 1:
    y += 1
    x = (x + 3) % t.w
    if t[y][x] == "#":
      ans += 1
  return ans

data = aoc.Table.read()
aoc.cprint(solve(data))
