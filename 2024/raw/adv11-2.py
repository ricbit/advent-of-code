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
  for i in range(75):
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

@functools.lru_cache(None)
def rec(stone, depth):
  if depth == 0:
    return 1
  else:
    if stone == 0:
      value = rec(1, depth - 1)
    elif (x:= len(s:= str(stone))) % 2 == 0:
      value = rec(int(s[:x // 2]), depth - 1)
      value += rec(int(s[x // 2:]), depth - 1)
    else:
      value = rec(stone * 2024, depth -1)
  return value

class Stone:
  def __init__(self, stones):
    self.stones = stones
    self.cache = {}

  def solve(self):
    ans = 0
    for stone in self.stones:
      ans += self.rec(stone)
    return ans

data = aoc.ints(sys.stdin.read().split())
aoc.cprint(sum(rec(stone, 25) for stone in data))
aoc.cprint(sum(rec(stone, 75) for stone in data))
