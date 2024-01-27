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

def near(s):
  return abs(s) < 1e-4

def size(r):
  return (r.real ** 2 + r.imag ** 2) ** 0.5

def isinteger(r):
  return near(r - math.floor(r + 0.5))

def visible(ast, goal, asteroids):
  for a in asteroids:
    if a != ast and a != goal:
      #gy, gx = goal[0] - ast[0], goal[1] - ast[1]
      #ay, ax = a[0] - ast[0], a[1] - ast[1]
      #if math.gcd(gy, ay) > 1 and math.gcd(gx, ax) > 1:
      #  if 0 < ax <= gx and 0 < ay <= gy:
      #    return False
      gc = (goal[0] - ast[0]) * 1j + (goal[1] - ast[1])
      ac = (a[0] - ast[0]) * 1j + (a[1] - ast[1])
      r = ac / gc
      if near(r.imag) and 0 < size(r) < 1 and r.real > 0:
        #print(ast, goal, " block by ", ac)
        return False
  return True

def solve(t):
  asteroids = [(j, i) for j, i in t.iter_all(lambda x: x == "#")]
  for ast in asteroids:
    count = 0
    for goal in asteroids:
      if goal != ast:
        if visible(ast, goal, asteroids):
          #print(ast, goal)
          count += 1
    #print()
    yield (count, ast)

t = aoc.Table.read()
aoc.cprint(max(solve(t))[0])
