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

def solve(data, ty, tx):
  m = [[0] * tx for _ in range(ty)]
  h = [0,0,0,0]
  for bot in data:
    y, x = bot.py, bot.px
    vy, vx = bot.vy, bot.vx
    n = 100
    y = (y + n * vy) % ty
    x = (x + n * vx) % tx
    print(y, x)
    m[y][x] += 1
    if y < ty // 2:
      if x < tx // 2:
        h[0] += 1
      elif x > tx // 2:
        h[1] += 1
    elif y > ty // 2:
      if x < tx // 2:
        h[2] += 1
      elif x > tx // 2:
        h[3] += 1
  #for y in m:
  #  print(y)
  return math.prod(h)

data = aoc.retuple_read("px_ py_ vx_ vy_", r"p=(-?\d+),(-?\d+) v=(-?\d+),(-?\d+)")
#aoc.cprint(solve(data, 7, 11))
aoc.cprint(solve(data, 103, 101))
