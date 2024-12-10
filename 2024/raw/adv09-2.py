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

def solve2(data):
  fsys = []
  used = []
  pos = 0
  for i, v in enumerate(data):
    if i % 2 == 0:
      fsys.extend([i // 2] * v)
      used.append(((i//2), v, pos))
    else:
      fsys.extend([-1] * v)
    pos += v
  for uid, size, pos in reversed(used):
    print(uid, size, pos)
    for i in range(len(fsys)):
      if fsys[i] == -1:
        fsize = 1
        fpos = i + 1
        while fpos < len(fsys) and fsys[fpos] == -1 and fsize < size:
          fsize += 1
          fpos += 1
          if (fsize > 100):
            print(fsize, fpos)
        if fsize >= size and i < pos:
          for j in range(pos, pos + size):
            fsys[j] = -1
          for j in range(size):
            fsys[i + j] = uid
          break
  return sum((0 if y == -1 else (i * y)) for i, y in enumerate(fsys))
 
def solve(data):
  fsys = []
  for i, v in enumerate(data):
    if i % 2 == 0:
      fsys.extend([i // 2] * v)
    else:
      fsys.extend([-1] * v)
  free = fsys.index(-1)
  used = len(fsys) - 1
  while fsys[used] == -1:
    used -= 1
  while free < used:
    fsys[used], fsys[free] = fsys[free], fsys[used]
    used -= 1
    while fsys[used] == -1:
      used -= 1
    free += 1
    while fsys[free] != -1:
      free += 1
  return sum(i * y for i, y in enumerate(x for x in fsys if x != -1))

data = aoc.ints(list(sys.stdin.read().strip()))
aoc.cprint(solve2(data))
