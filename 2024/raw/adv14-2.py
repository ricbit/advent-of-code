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

def solve(data, ty, tx, n):
  m = [[0] * tx for _ in range(ty)]
  h = [0,0,0,0]
  #aoc.cls()
  #print(n)
  for bot in data:
    y, x = bot.py, bot.px
    vy, vx = bot.vy, bot.vx
    y = (y + n * vy) % ty
    x = (x + n * vx) % tx
    #print(y, x)
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
  for line in m:
    linex = "".join(str(i) for i in line)
    print(n)
    if ("11111111111") in linex:
      for line1 in m:
        print("".join(str(i) if i != 0 else "." for i in line1))
      print()
      return True
  return False

  #for y in m:
  #  print(y)
  return math.prod(h)

data = aoc.retuple_read("px_ py_ vx_ vy_", r"p=(-?\d+),(-?\d+) v=(-?\d+),(-?\d+)")
#aoc.cprint(solve(data, 7, 11))
#aoc.cprint(solve(data, 103, 101))
p = 0
for n in range(0, 35000):
  if solve(data, 103, 101, n):
    break
  #if p > 20:
  #  break
