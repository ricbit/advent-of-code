import sys
import re
import itertools
import math
import aoc
import heapq
import functools
import copy
from collections import Counter, deque
from dataclasses import dataclass

lines = [line.strip() for line in sys.stdin]
quads = []
mx, my = 0, 0
for line in lines:
  quads.append(aoc.retuple("x_ y_ w_ h_", r".*?@ (\d+),(\d+): (\d+)x(\d+)$", line))
  mx = max(mx, quads[-1].x + quads[-1].w + 10)
  my = max(my, quads[-1].y + quads[-1].h + 10)
t = aoc.Table([[-1] * mx for _ in range(my)])
double = set()
for n, quad in enumerate(quads):
  misc = 0
  for j in range(quad.h):
    for i in range(quad.w):
      if t[j + quad.y][i + quad.x] == -1:
        t[j + quad.y][i + quad.x] = n
      elif t[j + quad.y][i + quad.x] >= 0:
        misc = 1
        double.add(t[j + quad.y][i + quad.x])
        double.add(n)
        t[j + quad.y][i + quad.x] = n
for i in range(len(quads)):
  if i not in double:
    aoc.cprint(i + 1)

