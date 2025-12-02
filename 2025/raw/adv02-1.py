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
  invalid = [str(i) * 2 for i in range(10)]
  print(invalid)
  ans = 0
  for line in data:
    r = aoc.retuple("a_ b_", r"(\d+)-(\d+)", line)
    for i in range(r.a, r.b + 1):
      s = str(i)
      if len(s) % 2 == 1:
        continue
      half = len(s) // 2
      if s[:half] == s[half:]:
        print(i)
        ans += i
  return ans

data = sys.stdin.read().strip().replace("\n", "").split(",")
aoc.cprint(solve(data))
