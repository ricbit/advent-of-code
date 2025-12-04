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

def solve(table):
  ans = 0
  visited = set()
  for j, i in table.iter_all():
    if table[j][i] != "@":
      continue
    count = 0
    for jj, ii in table.iter_neigh8(j, i):
      if table[jj][ii] == "@":
        count += 1
    if count < 4:
      ans += 1
      visited.add((j, i))
  for j, i in visited:
    table[j][i] = "."
  return ans

def solve2(table):
  ans = 0
  while (incr := solve(table)) > 0:
    ans += incr
  return ans

data = aoc.Table.read()
aoc.cprint(solve2(data))
