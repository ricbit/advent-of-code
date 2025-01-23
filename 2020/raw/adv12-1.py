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

def solve(actions):
  cdir = aoc.get_cdir("N")
  pdir = 1
  pos = 0
  print(cdir)
  for action in actions:
    if action.cdir in cdir:
      pos += cdir[action.cdir] * action.value
    elif action.cdir == "F":
      pos += pdir * action.value
    elif action.cdir == "R":
      pdir = pdir * (1j) ** (action.value // 90)
    elif action.cdir == "L":
      pdir = pdir * (-1j) ** (action.value // 90)
    print(pos, pdir)
  return int(abs(pos.real) + abs(pos.imag))

data = aoc.retuple_read("cdir value_", r"(.)(\d+)")
aoc.cprint(solve(data))
