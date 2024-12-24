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

number = {
    "7": (0,0),
    "8": (0,1),
    "9": (0,2),
    "4": (1,0),
    "5": (1,1),
    "6": (1,2),
    "1": (2,0),
    "2": (2,1),
    "3": (2,2),
    "0": (3,1),
    "A": (3,2)
}

def simulate_number(a, py, px):
  d = aoc.get_dir("^")
  for c in a:
    if c == "A":
      continue
    dy, dx = d[c]
    py += dy
    px += dx
    if py == 3 and px == 0:
      return False
  return True

def solve_number(line):
  best = 0
  py, px = number["A"]
  for c in line:
    valid = []
    for perm in itertools.permutations(range(4)):
      ans = []
      for p in perm:
        ny, nx = number[c]
        dy, dx = ny - py, nx - px
        if p == 0:
          if dx > 0:
            ans.extend([">"] * abs(dx))
        if p == 1:
          if dy > 0:
            ans.extend(["v"] * abs(dy))
        if p == 2:
          if dy < 0:
            ans.extend(["^"] * abs(dy))
        if p == 3:
          if dx < 0:
            ans.extend(["<"] * abs(dx))
      ans.append("A")
      ans = "".join(ans)
      print(perm, ans)
      if simulate_number(ans, py, px):
        valid.append(solve_small_all(ans, 0))
    py, px = ny, nx
    best += min(valid)
  return best

def solve_number_all(line):
  return solve_number(line)

small = {
    "^": (0, 1),
    "A": (0, 2),
    "<": (1, 0),
    "v": (1, 1),
    ">": (1, 2)
}

def simulate_small(moves, py, px):
  d = aoc.get_dir("^")
  for c in moves:
    if c == "A":
      continue
    dy, dx = d[c]
    py += dy
    px += dx
    if py == 0 and px == 0:
      return False
  return True

@functools.cache
def small_step(py, px, ny, nx, depth):
  dy, dx = ny - py, nx - px
  best = []
  for perm in itertools.permutations(range(4)):
    ans = []
    for p in perm:
      if p == 0:
        if dx > 0:
          ans.extend([">"] * abs(dx))
      if p == 1:
        if dy > 0:
          ans.extend(["v"] * abs(dy))
      if p == 2:
        if dx < 0:
          ans.extend(["<"] * abs(dx))
      if p == 3:
        if dy < 0:
          ans.extend(["^"] * abs(dy))
    ans.append("A")
    ans = "".join(ans)
    if simulate_small(ans, py, px):
      best.append(solve_small_all(ans, depth + 1))
  return min(best)

def solve_small(line, depth):
  py, px = small["A"]
  size = 0
  for c in line:
    ny, nx = small[c]
    size += small_step(py, px, ny, nx, depth)
    py, px = ny, nx
  return size

def solve_small_all(line, depth):
  if depth == 25:
    return len(line)
  ans = []
  #for p in itertools.permutations(range(4)):
  ans.append(solve_small(line, depth))
  return min(ans) #, key=len)
 
def solve(data):
  ans = 0
  for line in data:
    n = solve_number_all(line)
    print(n)
    ans += n * int(line[:3])
  return ans

# too low 257790352135130
data = sys.stdin.read().splitlines()
aoc.cprint(solve(data))
