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

def secret(n):
  while True:
    mult = n * 64
    f = mult ^ n
    n = f % 16777216
    mult = (n) // 32
    f = n ^ mult
    n = f % 16777216
    mult = n * 2048
    f = mult ^ n
    n = f % 16777216
    yield n

def solve(data):
  ans = 0
  for line in data:
    #print(line)
    for i, n in enumerate(itertools.islice(secret(line), 2000)):
      #print(n)
      pass
    #print(n)
    ans += n
  return ans

data = list(aoc.flatten(aoc.ints_read()))
print(data)
aoc.cprint(solve(data))
