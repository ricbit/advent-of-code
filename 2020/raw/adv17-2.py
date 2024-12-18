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

class Cubes:
  def __init__(self, t, dim):
    self.initial = set()
    self.dim = dim
    for j, i in t.iter_all():
      if t[j][i] == "#":
        self.initial.add(tuple([j, i] + [0] * (dim - 2)))
    self.neighs = []
    for neighs in itertools.product([-1, 0, 1], repeat = self.dim):
      if not all(neigh == 0 for neigh in neighs):
        self.neighs.append(neighs)

  def iter_neigh(self, cube):
    for neighs in self.neighs:
      yield tuple(a + b for a, b in zip(cube, neighs))

  def iter_inactive(self, cubes):
    neighs = set()
    for cube in cubes:
      for neigh in self.iter_neigh(cube):
        if neigh not in cubes:
          neighs.add(neigh)
    yield from neighs

  def cycle(self, cubes):
    new_cubes = set()
    for cube in cubes:
      neighs = sum(neigh in cubes for neigh in self.iter_neigh(cube))
      if neighs in [2, 3]:
        new_cubes.add(cube)
    for cube in self.iter_inactive(cubes):
      neighs = sum(neigh in cubes for neigh in self.iter_neigh(cube))
      if neighs == 3:
        new_cubes.add(cube)
    return new_cubes

  def solve(self):
    cubes = self.initial.copy()
    for i in range(6):
      cubes = self.cycle(cubes)
    return len(cubes)

data = aoc.Table.read()
aoc.cprint(Cubes(data, 3).solve())
aoc.cprint(Cubes(data, 4).solve())
