import sys
import string
import bisect
import numpy as np
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
from aoc.refintcode import IntCode

def check(j, i, data):
  cpu = IntCode(data[:])
  state = 0
  while cpu.run():
    match cpu.state:
      case cpu.INPUT:
        if state == 0:
          cpu.input = j
          state = 1
        elif state == 1:
          cpu.input = i
          state = 2
      case cpu.OUTPUT:
        state = 0
        return cpu.output

def cbounds(x, bounds):
  j, xmin, xmax = bounds
  return xmin <= x < xmax

def get_bounds(data):
  last = 5
  sup = 1500
  bounds = [(j, 0, 0) for j in range(8)]
  for j in range(8, sup):
    imin = bisect.bisect_left(range(sup), 1, lo=0, hi=last + 2, key=lambda x:check(j,x,data))
    imax = bisect.bisect_left(range(sup), 1, lo=last+2, hi=sup, key=lambda x:1-check(j,x,data))
    last = imin
    bounds.append((j, imin, imax))
    print(j, imin, imax)
  return bounds

def check_all(horiz, vert, y, x, size):
  for k in range(size):
    if vert[y, x + k] < size:
      return False
  for k in range(size):
    if horiz[y + k, x] < size:
      return False
  return True
          
def print_neigh(data, y, x):
  print(y, x)
  for j in range(-2, 3):
    line = []
    for i in range(-2, 3):
      line.append(str(check(y + j, x + i, data)))
    print("".join(line))
  print("----")

def accumulate(beam, data):
  beam = np.array(beam)
  vert = beam.copy()
  for j in range(len(beam) - 2, -1, -1):
    vert[j, :] = (vert[j, :] + vert[j + 1, :]) * beam[j, :]
  np.set_printoptions(threshold=sys.maxsize)
  horiz = beam.copy()
  for i in range(len(beam) - 2, -1, -1):
    horiz[:, i] = (horiz[:, i] + horiz[:, i + 1]) * beam[:, i]
  np.set_printoptions(threshold=sys.maxsize)
  print(vert)
  print(horiz)
  size = 100
  for d in range(3 * len(beam)):
    for s in range(1 + d):
      j = d - s 
      i = s
      if j >= len(beam):
        continue
      if i >= len(beam):
        break
      if horiz[j, i] >= size and vert[j, i] >= size:
        if check_all(horiz, vert, j, i, size):
          print_neigh(data, j, i)
          print_neigh(data, j, i + size - 1)
          print_neigh(data, j + size - 1, i)
          print_neigh(data, j + size - 1, i + size - 1)
          return j, i
  return 0

def check_box(bounds):
  xstart = bounds[-1][1]
  ystart = bounds[-100][0]
  dist = (1e18, 0, 0)
  for j in range(100):
    for i in range(100):
      dist = min(dist, (math.hypot(j + ystart, i + xstart), j + ystart, i + xstart))
  _, y, x = dist
  print("---", y, x)
  for i in range(0, 1500):
    print(i, check(y, i))
    pass
  return dist

def read_fake():
  lines = [[int(bool(c != ".")) for c in line.strip()] for line in sys.stdin]
  for line in lines:
    print(line)
  return [line[:len(lines)] for line in lines]

def get_beam(bounds):
  size = len(bounds)
  beam = np.zeros((size, size))
  for j, imin, imax in bounds:
    beam[j, imin:imax] = 1
  return beam

def brute_force(data):
  m = []
  for j in range(950, 1200):
    line = []
    print(j, flush=True)
    for i in range(700, 1100):
      line.append(str(check(j, i, data)))
    m.append("".join(line))
  for line in m:
    print(line)



data = aoc.ints(sys.stdin.read().split(","))
#brute_force(data)
aoc.cprint(accumulate(get_beam(get_bounds(data)), data))
#aoc.cprint(accumulate(read_fake()))



