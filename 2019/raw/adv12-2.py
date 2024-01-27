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

def get_state(planet, coord):
  state = []
  for p in planet:
    state.append(p[0][coord])
    state.append(p[1][coord])
  return tuple(state)

def simulate(planet, ticks, coord):
  state = get_state(planet, coord)
  for tick in range(ticks):
    for a, b in itertools.combinations(planet, 2):
      for d in range(3):
        if a[0][d] < b[0][d]:
          a[1][d] += 1
          b[1][d] -= 1
        elif a[0][d] > b[0][d]:
          a[1][d] -= 1
          b[1][d] += 1
    for p in planet:
      for d in range(3):
        p[0][d] += p[1][d]
    if get_state(planet, coord) == state:
      return tick + 1
    energy = sum(sum(abs(d) for d in p[0]) * sum(abs(d) for d in p[1]) for p in planet)
  return energy

data = aoc.retuple_read("x_ y_ z_", r"<x=(.*?), y=(.*?), z=(.*?)>", sys.stdin)
planet = [[[p.x, p.y, p.z], [0, 0, 0]] for p in data]
values = [simulate(planet, 1000000, i) for i in range(3)]
aoc.cprint(math.lcm(*values))
