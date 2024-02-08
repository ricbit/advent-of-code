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

def solve(depth, y, x):
  geolevel = aoc.Table([[0] * (x + 1) for _ in range(y + 1)])
  erosion = aoc.Table([[0] * (x + 1) for _ in range(y + 1)])
  regtype = aoc.Table([[0] * (x + 1) for _ in range(y + 1)])
  for j in range(y + 1):
    for i in range(x + 1):
      if j == 0 and i == 0:
        geolevel[j][i] = 0
      elif y == j and i == x:
        geolevel[j][i] = 0
      elif j == 0:
        geolevel[j][i] = i * 16807
      elif i == 0:
        geolevel[j][i] = j * 48271
      else:
        geolevel[j][i] = erosion[j][i-1] * erosion[j-1][i]
      erosion[j][i] = (geolevel[j][i] + depth) % 20183
      regtype[j][i] = erosion[j][i] % 3
      #print(j, i, geolevel[j][i], erosion[j][i], regtype[j][i])
    d = {0:".", 1:"=", 2:"|"}
    print("".join(d[i] for i in regtype[j]))
  return sum(sum(line) for line in regtype)

data = [line.strip() for line in sys.stdin]
depth = int(data[0].split(": ")[1])
x, y = aoc.ints(data[1].split(":")[1].split(","))
#depth = 510
#y, x = 10, 10
aoc.cprint(solve(depth, y, x))
