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

def near(s):
  return abs(s) < 1e-4

def size(r):
  return (r.real ** 2 + r.imag ** 2) ** 0.5

def isinteger(r):
  return near(r - math.floor(r + 0.5))

def visible(ast, goal, asteroids):
  for a in asteroids:
    if a != ast and a != goal:
      gc = (goal[0] - ast[0]) * 1j + (goal[1] - ast[1])
      ac = (a[0] - ast[0]) * 1j + (a[1] - ast[1])
      r = ac / gc
      if near(r.imag) and 0 < size(r) < 1 and r.real > 0:
        return False
  return True

def solve(t):
  asteroids = [(j, i) for j, i in t.iter_all(lambda x: x in "#X")]
  for ast in asteroids:
    count = 0
    for goal in asteroids:
      if goal != ast:
        if visible(ast, goal, asteroids):
          count += 1
    yield (count, ast, asteroids)

def sort_ast(station):
  _, (sy, sx), asteroids = station
  polar = [(cmath.polar(((ax - sx) + (ay - sy) * 1j) * cmath.exp(-1j * (math.pi/ 2-0.001)))
    , ax, ay) for ay, ax in asteroids if (ay, ax) != (sy, sx)]
  polar.sort(key=lambda c: (c[0][1], c[0][0]))
  asts = aoc.ddict(lambda: [])
  for ((r, phase), y, x) in polar:
    asts[int(phase * 100000)].append((y, x))
  count = 200
  while True:
    for phase in sorted(asts.keys()):
      if asts[phase]:
        count -= 1
        x, y = asts[phase].pop(0)
        if count == 0:
          return x * 100 + y 
      else:
        continue

t = aoc.Table.read()
station = max(solve(t))
aoc.cprint(sort_ast(station))

