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

def safe(data):
  diff = [a-b for a,b in zip(data, data[1:])]
  if (all(i>0 for i in diff) or all(i<0 for i in diff)) and all(abs(i)<=3 for i in diff):
    return 1
  else:
    return 0

def solve(x):
  if safe(x):
    return 1
  for i in range(len(x)+1):
    if safe(x[:i]+x[i+1:]):
      return 1
  return 0

ans = 0
for line in sys.stdin:
  x = aoc.ints(line.split())
  if solve(x):
    ans += 1

aoc.cprint(ans)
