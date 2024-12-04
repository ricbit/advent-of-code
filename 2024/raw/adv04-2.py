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
  pos = [(-1,-1), (0,0), (1,1),(-1,1),(0,0),(1,-1)]
  ans = 0
  for j, i in t.iter_all():
    if all(t.valid(j+y, i+x) for y,x in pos):
      if t[j][i] != "A":
        continue
      if set([t[j-1][i-1], t[j+1][i+1]]) != set(["S", "M"]):
        continue
      if set([t[j+1][i-1], t[j-1][i+1]]) != set(["S", "M"]):
        continue
      ans += 1
  return ans

data = aoc.Table.read()
aoc.cprint(solve(data))
