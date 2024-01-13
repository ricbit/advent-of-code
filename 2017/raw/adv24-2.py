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

@functools.lru_cache(maxsize=None)
def build(ports, pos, used, size):
  ans = []
  for i, port in enumerate(ports):
    mask = 1 << i
    if mask & used != 0:
      continue
    if port[0] == pos or port[1] == pos:
      npos = port[0] + port[1] - pos
      nsize, nstr = build(ports, npos, used + mask, size)
      ans.append((nsize + 1, port[0] + port[1] + nstr))
  return max(ans) if ans else (0, 0)
  




lines = [line.strip() for line in sys.stdin]
ports = []
for line in lines:
  ports.append(tuple(int(i) for i in line.split("/")))  
aoc.cprint(build(tuple(ports), 0, 0, 0)[1])
