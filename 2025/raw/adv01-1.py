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
  pos = 50
  ans = 0
  for line in data:
    d, size = line[0], int(line[1:])
    if d == "L":
      pos -= size
    else:
      pos += size
    if pos % 100 == 0:
      ans += 1
  return ans

data = sys.stdin.readlines()
aoc.cprint(solve(data))
