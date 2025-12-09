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

def solve(points):
  maxrect = 0
  for p1, p2 in itertools.combinations(points, 2):
    if (m := (1 + abs(p1[0] - p2[0])) * (1 + abs(p1[1] - p2[1]))) > maxrect:
      maxrect = m
  return maxrect

data = sys.stdin.readlines()
tiles = [list(map(int, line.split(","))) for line in data]
aoc.cprint(solve(tiles))
