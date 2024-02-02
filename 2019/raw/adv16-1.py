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

def pattern(size):
  first = True
  for b in itertools.cycle([0, 1, 0, -1]):
    for r in range(size + 1):
      if not first:
        yield b
      first = False

def conv(x):
  return abs(x) % 10

def solve(data):
  size = len(data)
  for t in range(100):
    ans = []
    for d in range(size):
      ans.append(conv(sum(a * b for a, b in zip(data, pattern(d)))))
    data = ans
  return "".join(str(i) for i in data[:8])

data = aoc.ints(sys.stdin.read().strip())
aoc.cprint(solve(data))
