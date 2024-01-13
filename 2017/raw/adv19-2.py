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
  while t.get(vpos) != " ":
    print(vpos, vdir, t.get(vpos))
    old = vpos
    vpos += vdir
    print(vpos, vdir, t.get(vpos))
    #if t.get(vpos).isalpha():
    #  yield t.get(vpos)
    if t.get(vpos) == "+":
      alldir = 0
      for y, x in t.iter_neigh4(int(vpos.imag), int(vpos.real)):
        if t[y][x] != " ":
          alldir += (y - old.imag) * 1j + (x - old.real)
      alldir -= vdir
      if alldir == 0:
        return steps
      print(vdir)
      vdir = alldir
    steps += 1
  return steps

lines = [list(line) for line in sys.stdin]
t = aoc.Table(lines)
aoc.cprint((walk(t)))
