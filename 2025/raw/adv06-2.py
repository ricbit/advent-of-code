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
  size = len(table)
  ops = []
  for i, op in enumerate(table[-1]):
    if op in "+*":
      ops.append(i)
  for i, pos in enumerate(ops):
    if i == len(ops) - 1:
      npos = len(table[0]) - 2
    else:
      npos = ops[i + 1] - 2
    ps = []
    for j in range(pos, npos + 1):
      n = 0
      for jj in range(size - 1):
        if table[jj][j] == " ":
          continue
        digit = int(table[jj][j])
        n = n * 10 + digit
      ps.append(n)
    print(ps)
    if table[-1][pos] == "+":
      ans += functools.reduce(lambda a, b: a + b, ps)
    else:
      ans += functools.reduce(lambda a, b: a * b, ps)
  return ans


data = sys.stdin.readlines()
aoc.cprint(solve(data))
