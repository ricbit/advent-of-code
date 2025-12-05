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

def solve(ranges, data):
  ranges = [[int(i) for i in r.split("-")] for r in ranges]
  ans = 0
  for k in data:
    ans += 1
    for a, b in ranges:
      if a <= int(k) <= b:
        break
    else:
      ans -= 1
  return ans

ranges, data = aoc.line_blocks()
print(ranges, aoc.ints(data))
aoc.cprint(solve(ranges, data))
