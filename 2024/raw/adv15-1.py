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
  maze, moves = data
  moves = "".join(s.strip() for s in moves)
  t = aoc.Table([list(p.strip()) for p in maze])
  cdir = aoc.get_cdir(">")
  for j, i in t.iter_all():
    if t[j][i] == "@":
      t[j][i] = "."
      pos = j * 1j + i
  for move in moves:
    pdir = cdir[move]
    #print(move, pdir)
    if t.get(pos + pdir) == ".":
      pos += pdir
    elif t.get(pos + pdir) == "O":
      walk = pos + pdir
      while t.get(walk) == "O":
        walk += pdir
      if t.get(walk) != "#":
        t.put(pos, ".")
        t.put(walk, "O")
        pos += pdir
    t.put(pos, "@")
    #for line in t:
    #  print("".join(line))
    #print()
    t.put(pos, ".")
  ans = 0
  for j, i in t.iter_all():
    if t[j][i] == "O":
      ans += j * 100 + i
  return ans

data = aoc.line_blocks()
aoc.cprint(solve(data))
