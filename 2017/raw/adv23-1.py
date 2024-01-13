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

def maybe(state, x):
  if x.isalpha():
    return state[x]
  else:
    return int(x)

def simulate(prog):
  pc = 0
  state = {r: 0 for r in "abcdefgh"}
  count = 0
  while pc < len(prog):
    print(prog[pc])
    match prog[pc]:
      case "set", x, y:
        state[x] = maybe(state, y)
      case "sub", x, y:
        state[x] -= maybe(state, y)
      case "mul", x, y:
        state[x] *= maybe(state, y)
        count += 1
      case "jnz", x, y:
        if maybe(state, x):
          pc += maybe(state, y) - 1
    pc += 1
  return count

lines = [line.strip() for line in sys.stdin]
prog = []
for line in lines:
  prog.append(line.split())
aoc.cprint(simulate(prog))
