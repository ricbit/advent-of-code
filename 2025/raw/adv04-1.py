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
  for j, i in table.iter_all():
    if table[j][i] != "@":
      continue
    count = 0
    for jj, ii in table.iter_neigh8(j, i):
      if table[jj][ii] == "@":
        count += 1
    if count < 4:
      ans += 1
  return ans

data = aoc.Table.read()
aoc.cprint(solve(data))
