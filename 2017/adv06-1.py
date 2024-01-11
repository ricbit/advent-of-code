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

def search(banks):
  steps = 0
  visited = set()
  while True:
    if tuple(banks) in visited:
      return steps
    steps += 1
    visited.add(tuple(banks))
    d = max(range(len(banks)), key=lambda x: banks[x])
    a = banks[d]
    banks[d] = 0
    for i in range(a):
      banks[(d + i + 1) % len(banks)] += 1

lines = aoc.ints(sys.stdin.read().strip().split())
aoc.cprint(search(lines))
