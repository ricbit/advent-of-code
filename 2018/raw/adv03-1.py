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
t = aoc.Table([[0] * mx for _ in range(my)])
for quad in quads:
  for j in range(quad.h):
    for i in range(quad.w):
      if t[j + quad.y][i + quad.x] == 0:
        t[j + quad.y][i + quad.x] = 1
      elif t[j + quad.y][i + quad.x] > 0:
        t[j + quad.y][i + quad.x] = 2
ans = 0
for j, i in t.iter_all():
  if t[j][i] == 2:
    ans += 1
print(ans)
