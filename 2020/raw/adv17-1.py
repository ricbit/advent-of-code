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

def iter_active(cubes):
  for (x, y, z) in cubes:
    yield (x, y, z)

def iter_neigh(cube):
  x, y, z = cube
  for dx, dy, dz in itertools.product([-1, 0, 1], repeat = 3):
    if dx == dy == dz == 0:
      continue
    yield (x + dx, y + dy, z + dz)

def iter_inactive(cubes):
  neighs = set()
  for cube in cubes:
    for neigh in iter_neigh(cube):
      if neigh not in cubes:
        neighs.add(neigh)
  yield from neighs

def cycle(cubes):
  new_cubes = set()
  for cube in cubes:
    neighs = sum(neigh in cubes for neigh in iter_neigh(cube))
    if neighs in [2, 3]:
      new_cubes.add(cube)
  for cube in iter_inactive(cubes):
    neighs = sum(neigh in cubes for neigh in iter_neigh(cube))
    if neighs == 3:
      new_cubes.add(cube)
  return new_cubes

def solve(t):
  cubes = set()
  for j, i in t.iter_all():
    if t[j][i] == "#":
      cubes.add((j, i, 0))
  print(len(cubes))
  for i in range(6):
    cubes = cycle(cubes)
    print(i, len(cubes))
  return len(cubes)

data = aoc.Table.read()
aoc.cprint(solve(data))
