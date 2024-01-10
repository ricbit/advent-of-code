import sys
import re
import itertools
import math
import aoc
import heapq
import functools
import copy
from collections import *
from dataclasses import dataclass

def grow(goal):
  m = [[1]]
  stride = 1
  pos = (0, 0)
  cur = 1
  for i in itertools.count(2):
    m = [[0] * (2 * stride + 1)] + [[0] + rest + [0] for rest in m] + [[0] * (2 * stride + 1)]
    pos = (stride, 2 * stride + 1 - 1)
    for j in range(2*stride-1, pos[0] - stride -1, -1):
      m[j][pos[1]] = cur + 1
      cur += 1
    for j in range(2 * stride - 1, -1, -1):
      m[0][j] = cur + 1
      cur += 1
    for j in range(1, 2 * stride + 1):
      m[j][0] = cur + 1
      cur += 1
    for j in range(1, 2 * stride + 1):
      m[-1][j] = cur + 1
      cur += 1
    stride += 1
    if any(goal in line for line in m):
      for i, line in enumerate(m):
        if goal in line:
          print(line.index(goal), i)
          return abs(line.index(goal) - stride +1) + abs(i - stride +1) 
      break

line = sys.stdin.read().strip()
ans = grow(int(line))
aoc.cprint(ans)
