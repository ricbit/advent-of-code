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

#51:04+2:56 = 54:00

def check(state):
  d = state["d"]
  e = state["e"]
  b = state["b"]
  s = int(b ** 0.5) + 2
  for i in range(d, s):
    if b % i == 0 and e <= b // d <= b:
      return 0
  return 1

def maybe(state, x):
  if x.isalpha():
    return state[x]
  else:
    return int(x)

def simulate(prog):
  pc = 0
  state = {r: 0 for r in "abcdefgh"}
  state['a'] = 1
  count = 0
  while pc < len(prog):
    print(state, prog[pc])
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
      case "chk", x, y:
        state['f'] = check(state)
    pc += 1
  return state['h']

lines = [line.strip() for line in sys.stdin]
prog = []
for line in lines:
  prog.append(line.split(";")[0].strip().split(" "))
aoc.cprint(simulate(prog))
