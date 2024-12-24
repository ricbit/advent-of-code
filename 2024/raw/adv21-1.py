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
#import networkx as nx

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

def solve_number(line, py, px):
  ans = []
  for c in line:
    ny, nx = number[c]
    dy, dx = ny - py, nx - px
    if px == 0:
      if dx > 0:
        ans.extend([">"] * abs(dx))
    if dy > 0:
      ans.extend(["v"] * abs(dy))
    if dx < 0:
      ans.extend(["<"] * abs(dx))
    if dy < 0:
      ans.extend(["^"] * abs(dy))
    if px != 0:
      if dx > 0:
        ans.extend([">"] * abs(dx))
    ans.append("A")
    px, py = nx, ny
  return "".join(ans), py, px

small = {
    "^": (0, 1),
    "A": (0, 2),
    "<": (1, 0),
    "v": (1, 1),
    ">": (1, 2)
}

def solve_small(line, py, px):
  ans = []
  for c in line:
    ny, nx = small[c]
    dy, dx = ny - py, nx - px
    #print(ny, nx, dy, dx)
    if px == 0:
      if dx > 0:
        ans.extend([">"] * abs(dx))
    if dy > 0:
      ans.extend(["v"] * abs(dy))
    if dx < 0:
      ans.extend(["<"] * abs(dx))
    if dy < 0:
      ans.extend(["^"] * abs(dy))
    if px != 0:
      if dx > 0:
        ans.extend([">"] * abs(dx))
    ans.append("A")
    px, py = nx, ny
  return "".join(ans), py, px

def simulate_number(a):
  py, px = number["A"]
  d = aoc.get_dir("^")
  for c in a:
    if c == "A":
      continue
    dy, dx = d[c]
    py += dy
    px += dx
    if py == 3 and px == 0:
      print("panic")

def simulate_small(a):
  py, px = small["A"]
  d = aoc.get_dir("^")
  for c in a:
    if c == "A":
      continue
    dy, dx = d[c]
    py += dy
    px += dx
    if py == 0 and px == 0:
      print("panic")


def solve(data):
  ans = 0
  p1y, p1x = number["A"]
  p2y, p2x = small["A"]
  p3y, p3x = small["A"]
  for line in data:
    n, p1y, p1x = solve_number(line, p1y, p1x)
    simulate_number(n)
    n, p2y, p2x = solve_small(n, p2y, p2x)
    simulate_small(n)
    n, p3y, p3x = solve_small(n, p3y, p3x)
    simulate_small(n)
    print(line, len(n) , int(line[:3]), n)
    ans += len(n) * int(line[:3])
  return ans

data = sys.stdin.read().splitlines()
aoc.cprint(solve(data))
