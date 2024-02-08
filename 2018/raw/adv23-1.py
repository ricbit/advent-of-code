import sys
import string
import re
import itertools
import math
import aoc
import heapq
import functools
import copy
from collections import Counter, deque
from dataclasses import dataclass

def solve(nano):
  j = max(nano, key=lambda q:q.r)
  ans = 0
  for i in nano:
    if abs(j.x - i.x) + abs(j.y - i.y) + abs(j.z - i.z) <= j.r:
      ans += 1
  return ans

data = [line.strip() for line in sys.stdin]
nano = aoc.retuple_read("x_ y_ z_ r_", r"pos=<([-+]?\d+),([-+]?\d+),([-+]?\d+)>, r=(\d+)", data)
print(nano)
aoc.cprint(solve(nano))
