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
aa.sort()
bb.sort()
s = sum(abs(a-b) for a, b in zip(aa,bb))
aoc.cprint(s)
