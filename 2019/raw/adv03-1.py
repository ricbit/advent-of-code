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
  visited = set()
  for c in cmd:
    vdir = c[0]
    size = int(c[1:])
    for i in range(size):
      pos += aoc.CDIRECTIONS[vdir]
      visited.add(pos)
  return visited

def dist(pos):
  return abs(pos.real) + abs(pos.imag)

cmd = [line.strip().split(",") for line in sys.stdin]
path = [solve(i) for i in cmd]
print(int(min(dist(i) for i in path[0].intersection(path[1]))))
