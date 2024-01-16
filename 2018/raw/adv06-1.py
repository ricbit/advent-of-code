import sys
import string
import re
import itertools
import math
import aoc
import heapq
import functools
import copy
from collections import Counter, deque
from dataclasses import dataclass

def closest(j, i, data):
  return min((x for x in range(len(data))), 
      key=lambda x: abs(data[x][0] - j) + abs(data[x][1] - i))

def solve(data):
  miny = min(line[0] for line in data)
  maxy = max(line[0] for line in data)
  minx = min(line[1] for line in data)
  maxx = max(line[1] for line in data)
  count = Counter()
  for j in range(miny, maxy + 1):
    for i in range(minx, maxx + 1):
      kset, kval = set(), 1e6
      for k, (ky, kx) in enumerate(data):
        d = abs(j - ky) + abs(i - kx)
        if d < kval:
          kval = d
          kset = set([k])
        elif d == kval:
          kset.add(k)
      if len(kset) == 1:
        k = aoc.first(kset)
        if data[k][0] not in [miny, maxy] and data[k][1] not in [maxx, minx]:
          count[k] += 1
  print(count)
  return max(c for c in count.values())


data = [aoc.ints(line.strip().split(", ")) for line in sys.stdin]
aoc.cprint(solve(data))
