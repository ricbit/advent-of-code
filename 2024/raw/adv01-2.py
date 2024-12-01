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

def solve(data):
  pass

aa, bb = [] , []
for line in sys.stdin:
  a, b =  map(int, line.strip().split())
  aa += [a]
  bb += [b]
hist = Counter()
for b in bb:
  hist[b] += 1
s = sum(a * hist[a] for a in aa)
aoc.cprint(s)
