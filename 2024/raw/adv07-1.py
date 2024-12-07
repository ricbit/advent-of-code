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

def solve(data):
  sol = 0
  for line in data:
    goal, v = line.split(":")
    v = aoc.ints(v.split())
    for b in itertools.product([0, 1], repeat=len(v) - 1):
      ans = v[0]
      for op, value in zip(b, v[1:]):
        if op:
          ans = ans + value
        else:
          ans = ans * value
      if ans == int(goal):
        print(ans)
        sol += ans
        break
  return sol

aoc.cprint(solve(sys.stdin.readlines()))
