import sys
import re
import itertools
import math
import aoc
import heapq
import functools
import copy
from collections import Counter
from dataclasses import dataclass

def cancel(c, x, y):
  a = min(c[x], c[y])
  c[x] -= a
  c[y] -= a

def triang(c, a, b, x):
  q = min(c[a], c[b])
  c[a] -= q #e222
  c[b] -=q
  c[x] += q

def count(steps):
  c = Counter()
  for step in steps:
    c[step] += 1
  cancel(c,'s', 'n')
  cancel(c,'ne', 'sw')
  cancel(c,'se', 'nw')
  triang(c, 'se', 'sw', 's')
  triang(c, 'ne', 'nw', 'n')
  triang(c, 'ne', 's', 'se')
  triang(c, 'nw', 's', 'sw')
  triang(c, 'se', 'n', 'ne')
  triang(c, 'sw', 'n', 'nw')
  return sum(c.values())

def walk(steps):
  for i in range(1, len(steps) + 1):
    yield count(steps[:i])

line = sys.stdin.read().strip()
steps = line.split(",")

aoc.cprint(max(walk(steps)))
