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

def search(banks, comp):
  steps = 0
  visited = {}
  while True:
    if tuple(banks) in visited:
      return comp(steps, visited[tuple(banks)])
    visited[tuple(banks)] = steps
    steps += 1
    d = max(range(len(banks)), key=lambda x: banks[x])
    a = banks[d]
    banks[d] = 0
    for i in range(a):
      banks[(d + i + 1) % len(banks)] += 1

lines = aoc.ints(sys.stdin.read().strip().split())
aoc.cprint(search(lines, lambda a, b: a))
aoc.cprint(search(lines, lambda a, b: a - b))
