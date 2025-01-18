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
  pos = 0
  size = len(data)
  for move in range(100):
    save = [data[(pos + i) % size] for i in range(1, 4)]
    dstlabel = data[pos] - 1
    if dstlabel == 0:
      dstlabel = size
    while dstlabel in save:
      dstlabel = dstlabel - 1
      if dstlabel == 0:
        dstlabel = size
    dst = (pos + 1) % size
    src = (pos + 4) % size
    print(data, save, dstlabel, dst, src)
    while True:
      data[dst] = data[src]
      if dstlabel == data[dst]:
        break
      dst = (dst + 1) % size
      src = (src + 1) % size
    print(data, dst, src)
    dst = (dst + 1) % size
    for i in range(3):
      data[(dst + i) % size] = save[i]
    pos = (pos + 1) % size
    print(move, data)
  ans = "".join(str(i) for i in data) * 2
  start = ans.index("1")
  return ans[start + 1:start + size]

data = aoc.ints(list(sys.stdin.read().strip()))
aoc.cprint(solve(data))
