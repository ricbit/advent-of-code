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

def simulate(prog):
  state = aoc.ddict(lambda: 0)
  tmax = 0
  for q in prog:
    a = state[q.vcond]
    if eval(f"{a} {q.cond} {q.ncond}"):
      match q.inc:
        case "inc":
          state[q.var] += q.value
        case "dec":
          state[q.var] -= q.value
    tmax = max(tmax, max(state.values()))
  return tmax

lines = [line.strip() for line in sys.stdin]
prog = []
for line in lines:
  q = aoc.retuple("var inc value_ vcond cond ncond_",
      r"(\w+) (inc|dec) ([-+]?\d+) if (\w+) (\S+) ([-+]?\d+)", line)
  prog.append(q)
aoc.cprint(simulate(prog))
