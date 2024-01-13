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

def walk(t):
  vdir = 1j
  vpos = t.table[0].index("|")
  steps = 0
  seq = []
  while t.get(vpos) != " ":
    old = vpos
    vpos += vdir
    if t.get(vpos).isalpha():
      seq.append(t.get(vpos))
    if t.get(vpos) == "+":
      alldir = 0
      for y, x in t.iter_neigh4(int(vpos.imag), int(vpos.real)):
        if t[y][x] != " ":
          alldir += (y - old.imag) * 1j + (x - old.real)
      alldir -= vdir
      if alldir == 0:
        return steps, seq
      vdir = alldir
    steps += 1
  return steps, seq

lines = [list(line) for line in sys.stdin]
t = aoc.Table(lines)
steps, seq = walk(t)
aoc.cprint("".join(seq))
aoc.cprint(steps)
