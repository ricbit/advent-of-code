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

def read(reg, state):
  match re.match(r"([-+]?\d+)|(\w)", reg).groups():
    case a, None:
      return int(a)
    case None, b:
      return state[b]

def simulate(lines, values):
  state = {c: 0 for c in "xyzw"}
  values = values[:]
  for line in lines:
    match line.split():
      case "inp", reg:
        state[reg] = values.pop(0)
      case "add", a, b:
        state[a] += read(b, state)
      case "mul", a, b:
        state[a] *= read(b, state)
      case "div", a, b:
        state[a] /= read(b, state)
      case "mod", a, b:
        state[a] %= read(b, state)
      case "eql", a, b:
        state[a] = int(state[a] == read(b, state))
  return state['z'] == 0

lines = [line.strip() for line in sys.stdin]
for i in range(10**13+1, 10**13+9):
  print(i, simulate(lines, list(map(int, str(i)))))
