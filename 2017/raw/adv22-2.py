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

def govirus(infected, y, x, vdir, n):
  ans = 0
  for _ in range(n):
    match infected[(y, x)]:
      case ".":
        vdir *= -1j
        infected[(y, x)] = "W"
      case "W":
        infected[(y, x)] = "#"
        ans += 1
      case "#":
        vdir *= 1j
        infected[(y, x)] = "F"
      case "F":
        vdir *= -1
        infected[(y, x)] = "."
    p = (y * 1j + x) + vdir
    y = p.imag
    x = p.real
  return ans

t = aoc.Table.read()
infected = aoc.ddict(lambda: ".")
for j, i in t.iter_all():
  if t[j][i] == "#":
    infected[(j, i)] = "#"
m = len(t.table) // 2
aoc.cprint(govirus(infected, m, m, -1j, 10000000))
