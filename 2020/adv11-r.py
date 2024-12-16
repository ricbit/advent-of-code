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
import multiprocessing
from collections import Counter, deque
from dataclasses import dataclass
import numpy
from scipy.signal import convolve2d


class Solver:
  def __init__(self, t, limit, loop=False):
    self.t = t.copy()
    self.out = t.copy()
    self.check = self.is_occupied if loop else self.is_occupied2
    self.limit = limit
    self.all_cdir = [1, -1, 1j, -1j, 1+1j, 1-1j, -1+1j, -1-1j]

  def is_occupied(self, t, pos, cdir):
    while True:
      pos += cdir
      if not t.cvalid(pos):
        return False
      if t.get(pos) == "#":
        return True
      if t.get(pos) == "L":
        return False

  def is_occupied2(self, t, pos, cdir):
    pos += cdir
    if not t.cvalid(pos):
      return False
    if t.get(pos) == "#":
      return True
    if t.get(pos) == "L":
      return False
    return False

  def process_line(self, j):
    changes = []
    for i in range(self.t.w):
      count = 0
      if self.t[j][i] != ".":
        for cdir in self.all_cdir:
            count += self.check(self.t, j * 1j + i, cdir)
      if self.t[j][i] == "L" and count == 0:
        changes.append(j * 1j + i)
      elif self.t[j][i] == "#" and count >= self.limit:
        changes.append(j * 1j + i)
    return changes

  def iter_round(self, pool):
    changes = aoc.flatten(pool.imap(self.process_line, range(self.t.h), int(sys.argv[1])))
    changed = False
    self.out = self.t.copy()
    for (c) in changes:
      self.out.put(c, "#" if self.t.get(c) == "L" else "L")
      changed = True
    return changed

  def solve(self, pool):
    p = 0
    while self.iter_round(pool):
      self.t, self.out = self.out, self.t
      p += 1
      print(p)
    return sum(self.t[j][i] == "#" for j, i in self.t.iter_all())

def oneround(walls, used):
  kernel = numpy.array([[1,1,1],[1,0,1],[1,1,1]])
  counters = convolve2d(used, kernel, mode="same", boundary="fill", fillvalue = 0)
  return walls * ( (counters == 0) + used * (counters < 4))

def manyrounds(walls, used):
  while True:
    mnext = oneround(walls, used)
    print()
    print(mnext)
    if numpy.count_nonzero(mnext != used):
      return used

data = [list(line) for line in sys.stdin.read().splitlines()]
a = numpy.array(data)
walls = (a != ".").astype(int)
used = (a == "#").astype(int)
print(walls)
print(used)
print(manyrounds(walls,used))
#with multiprocessing.Pool() as pool:
#  aoc.cprint(Solver(aoc.Table(data), 4, False).solve(pool))
#  aoc.cprint(Solver(aoc.Table(data), 5, True).solve(pool))
