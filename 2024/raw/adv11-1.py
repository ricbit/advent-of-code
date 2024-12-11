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

def solve(stones):
  for i in range(25):
    newstones = []
    print(i)
    for stone in stones:
      if stone == 0:
        newstones.append(1)
      elif (x:= len(s:= str(stone))) % 2 == 0:
        newstones.append(int(s[:x // 2]))
        newstones.append(int(s[x // 2:]))
      else:
        newstones.append(stone * 2024)
    stones = newstones
  return len(stones)

data = aoc.ints(sys.stdin.read().split())
print(data)
aoc.cprint(solve(data))
