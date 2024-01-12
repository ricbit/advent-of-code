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
  q=  min(c[a], c[b])
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
  print(c)
  return sum(c.values())

def dummy(step):
  pos = []
  match step:
      case "n": 
        pos[0] -= 1
      case "s": 
        pos[0] += 1
      case "ne":
        pos[0] -= 1
        pos[1] += 1
      case "se":
        pos[0] += 1
        pos[1] += 1
      case "nw":
        pos[0] -= 1
        pos[1] -= 1
      case "sw":
        pos[0] += 1
        pos[1] -= 1
  return abs(pos[0]) + abs(pos[1])

line = sys.stdin.read().strip()
steps = line.split(",")
aoc.cprint(count(steps))
