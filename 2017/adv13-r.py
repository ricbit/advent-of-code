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

def ypos(size, time):
  yoyo = size + size - 2
  t = time % yoyo
  if t < size:
    return t
  else:
    return yoyo - t

def walk(x, time, layers):
  for i, size in layers.items():
    x[i] = ypos(size, time)

def canwalk(series, layers, m, offset):
  return all(series[(i + offset) % m][i] != 0 for i in range(m))

def walkseries(layers):
  m = max(layers) + 1
  series = [[1] * m for _ in range(m)]
  for i in range(m):
    walk(series[i], i, layers)
  delay = 0
  while True:
    if canwalk(series, layers, m, delay):
      return delay
    if delay % 100000 == 0:
      print("--", delay)
    walk(series[delay % m], delay + m, layers)
    delay += 1

lines = [line.strip() for line in sys.stdin]
layers = {}
for line in lines:
  index, value = aoc.ints(line.split(": "))
  layers[index] = value
aoc.cprint(walkseries(layers))
