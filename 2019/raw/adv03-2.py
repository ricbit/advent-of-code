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

def solve(cmd):
  pos = 0
  visited = {}
  dist = 1
  for c in cmd:
    vdir = c[0]
    size = int(c[1:])
    for i in range(size):
      pos += aoc.CDIRECTIONS[vdir]
      visited[pos] = dist
      dist += 1
  return visited

def dist(pos):
  return abs(pos.real) + abs(pos.imag)

def intersect(path):
  inter = set(path[0].keys()).intersection(set(path[1].keys()))
  for i in inter:
    yield path[0][i] + path[1][i]

cmd = [line.strip().split(",") for line in sys.stdin]
path = [solve(i) for i in cmd]
print(int(min(intersect(path))))
