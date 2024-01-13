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
    if (y, x) in infected:
      vdir *= 1j
      infected.remove((y, x))
    else:
      vdir *= -1j
      infected.add((y, x))
      ans += 1
    print(y,x,vdir)
    p = (y * 1j + x) + vdir
    y = p.imag
    x = p.real
  return ans

t = aoc.Table.read()
infected = set()
for j, i in t.iter_all():
  if t[j][i] == "#":
    infected.add((j, i))
m = len(t.table) // 2
aoc.cprint(govirus(infected, m, m, -1j, 10000))
