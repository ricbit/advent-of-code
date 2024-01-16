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
  m = 300
  t = aoc.Table([[0] * m for _ in range(m)])
  for j, i in t.iter_all():
    rackid = (i + 10 + 1)
    power = hundreds((rackid* (j + 1) + serial) * rackid) - 5
    t[j][i] = power
  #for line in t.table:
  #  print(line)
  #print()
  tsum = aoc.Table([[0] * m for _ in range(m)])
  curline = [0] * m
  for j in range(m):
    curpos = 0
    for i in range(m):
      curpos += t[j][i]
      tsum[j][i] = curpos + curline[i]
      curline[i] = tsum[j][i]
  #for line in tsum.table:
  #  print(line)
  for j in range(m):
    for i in range(m):
      best = (0, 0, 0, 0)
      cur = t[j][i]
      for size in range(1, m):
        if j + size >= m or i + size >= m:
          break
        py, px = j + size, i + size
        cur = tsum[py][px] - tsum[py][i] - tsum[j][px] + tsum[j][i]
        if cur > best[0]:
          best = (cur, j, i, size)
      yield best


data = sys.stdin.read().strip()
cur = max(solve(int(data)))
aoc.cprint(f"{2+cur[2]},{2+cur[1]},{cur[3]}")
#aoc.cprint(f"{1 + cur[2]},{1 + cur[1]}")
