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

def solve(lines):
  hit = Counter()
  for line in lines:
    steps = re.findall(r"(w|e|ne|nw|se|sw)", line)
    start = (0, 0)
    for step in steps:
      diff = aoc.HEX2[step]
      start = (start[0] + diff[0], start[1] + diff[1])
    hit[start] ^= 1
  print(hit)
  return sum(hit.values())

lines = sys.stdin.read().splitlines()
aoc.cprint(solve(lines))
#272 too low
