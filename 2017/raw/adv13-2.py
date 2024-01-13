import sys
import re
import itertools
import math
import aoc
import heapq
import functools
import copy
from collections import *
from dataclasses import dataclass

# 45:25 + 5:15 = 50:35

def walk(layers):
  m = max(layers)
  x = [0] * (m + 1)
  d = [1] * (m + 1)
  while True:
    yield x[:]
    for j in range(m + 1):
      if j in layers:
        x[j] += d[j]
        if x[j] >= layers[j]:
          x[j] = layers[j] - 2
          d[j] = -1
        elif x[j] < 0:
          x[j] = 1
          d[j] = 1

def canwalk(series, layers, m):
  for i in range(m + 1):
    if series[i][i] == 0 and i in layers:
      return False
  return True

def walkseries(layers):
  m = max(layers)
  walk_iter = walk(layers)
  series = list(itertools.islice(walk_iter, m + 1))
  delay = 0
  while True:
    if canwalk(series, layers, m):
      return delay
    if delay % 100000 == 0:
      print(delay)
    delay += 1
    series[0:-1]  = series[1:m+1]
    series[-1] = next(walk_iter)

lines = [line.strip() for line in sys.stdin]
layers = {}
for line in lines:
  index, value = aoc.ints(line.split(": "))
  layers[index] = value
aoc.cprint(walkseries(layers))
