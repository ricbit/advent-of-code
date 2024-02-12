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
from aoc.refintcode import IntCode

def solve(data):
  cpu = IntCode(data)
  table = []
  line = []
  while cpu.run():
    match cpu.state:
      case cpu.OUTPUT:
        if cpu.output == 10:
          print("".join(line))
          line = ["#"] + line + ["#"]
          table.append(line)
          line = []
        else:
          line.append(chr(cpu.output))
  print(table)
  t = aoc.Table(table[:-1])
  ans = 0
  for j, i in t.iter_all():
    if t[j][i] == "#":
      count = 0
      for jj, ii in t.iter_neigh4(j, i):
        if t[jj][ii] == "#":
          count += 1
      if count == 4:
        ans += j * i
  return ans

data = aoc.ints(sys.stdin.read().split(","))
aoc.cprint(solve(data))
