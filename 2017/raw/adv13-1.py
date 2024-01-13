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

def walk(layers):
  m = max(layers)
  x = [0] * (m + 1)
  d = [1] * (m + 1)
  ans = 0
  for i in range(m + 1):
    if x[i] == 0 and i in layers:
      ans += i * layers[i]
    for j in range(m + 1):
      if j in layers:
        x[j] += d[j]
        if x[j] >= layers[j]:
          x[j] = layers[j] - 2
          d[j] *= -1
        if x[j] < 0:
          x[j] = 1
          d[j] *= -1
  return ans

lines = [line.strip() for line in sys.stdin]
layers = {}
for line in lines:
  index, value = aoc.ints(line.split(": "))
  layers[index] = value

aoc.cprint(walk(layers))
