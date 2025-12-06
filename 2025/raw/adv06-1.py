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
  for i in range(len(table[0])):
    ps = list(map(int, (table[j][i] for j in range(size - 1))))
    if table[size - 1][i] == "+":
      ans += functools.reduce(lambda a, b: a + b, ps)
    else:
      ans += functools.reduce(lambda a, b: a * b, ps)
  return ans


data = sys.stdin.readlines()
data = [d.split() for d in data]
print(data)
print([len(x) for  x in data])
aoc.cprint(solve(data))
