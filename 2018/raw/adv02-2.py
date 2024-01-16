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

def find(a, b):
  f = "a"
  count = 0
  for i in range(len(a)):
    if a[i] != b[i]:
      f = a[i]
      count += 1
  if count == 1:
    return a[:a.index(f)] + a[a.index(f) + 1:]
  return None

lines = [line.strip() for line in sys.stdin]
for a, b in itertools.combinations(lines, 2):
  ans = 0
  if (c := find(a, b)) is not None:
    aoc.cprint(c)
    break
