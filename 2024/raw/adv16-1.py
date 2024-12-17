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

def toint(c):
  return (c.imag, c.real)

def solve(t):
  sy, sx = t.find("S")
  ey, ex = t.find("E")
  t[sy][sx] = "."
  t[ey][ex] = "."
  pos = sy * 1j + sx
  end = ey * 1j + ex
  pnext = [(0, toint(pos), toint(1))]
  visited = {}
  while pnext:
    score, pos, pdir = heapq.heappop(pnext)
    pos = pos[0] * 1j + pos[1]
    pdir = pdir[0] * 1j + pdir[1]
    if (pos, pdir) in visited:
      continue
    visited[(pos, pdir)] = score
    if pos == end:
      return score
    for turn in [1j, -1j]:
      heapq.heappush(pnext, (score + 1000, toint(pos), toint(pdir * turn)))
    if t.get(pos + pdir) != "#":
      heapq.heappush(pnext, (score + 1, toint(pos + pdir), toint(pdir)))

  return data

data = aoc.Table.read()
aoc.cprint(solve(data))
