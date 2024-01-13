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

def gen(start, mult, mod):
  pos = start
  while True:
    pos = (pos * mult) % 2147483647
    if pos % mod == 0:
      yield pos

lines = [line.strip() for line in sys.stdin]
n = []
for line in lines:
  q = aoc.retuple("s_", r".*?(\d+)", line)
  n.append(q.s)
ans = 0
#m = 2000
m = 5000000
for i, x, y in zip(range(m), gen(n[0], 16807,4), gen(n[1], 48271,8)):
  if (x & 0xFFFF) == (y & 0xFFFF):
    ans += 1
aoc.cprint(ans)
