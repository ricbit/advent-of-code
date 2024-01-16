import sys
import string
import re
import itertools
import math
import aoc
import heapq
import functools
import copy
from collections import Counter, deque
from dataclasses import dataclass

def hundreds(n):
  return n // 100 % 10

def solve(serial):
  t = aoc.Table([[0] * 300 for _ in range(300)])
  for j, i in t.iter_all():
    rackid = (i + 10 + 1)
    power = hundreds((rackid* (j + 1) + serial) * rackid) - 5
    t[j][i] = power
  cur = (0, 0, 0)
  for j in range(len(t.table) - 2):
    for i in range(len(t.table[0]) - 2):
      ans = 0
      for jj in range(3):
        for ii in range(3):
          ans += t[j + jj][i + ii]
      if ans > cur[0]:
        cur = (ans, j, i)
  return f"{1 + cur[2]},{1 + cur[1]}"

data = sys.stdin.read().strip()
aoc.cprint(solve(int(data)))
