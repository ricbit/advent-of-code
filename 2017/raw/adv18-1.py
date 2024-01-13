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

def maybe(state, y):
  if y[0].isalpha():
    return state[y]
  else:
    return int(y)

def execute(prog):
  freq = 0
  state = aoc.ddict(lambda: 0)
  pc = 0
  i = 0
  while True:
    i += 1
    if i % 1000 == 0:
      print(i, pc, prog[pc], state)
    match prog[pc]:
      case "snd", x:
        freq = maybe(state, x)
      case "set", x, y:
        state[x] = maybe(state, y)
      case "add", x, y:
        state[x] += maybe(state, y)
      case "mul", x, y:
        state[x] *= maybe(state, y)
      case "mod", x, y:
        state[x] %= maybe(state, y)
      case "rcv", x:
        if state[x]:
          state[x] = freq
          return freq
      case "jgz", x, y:
        if state[x] > 0:
          pc += maybe(state, y) - 1
    pc += 1

lines = [line.strip() for line in sys.stdin]
prog = []
for line in lines:
  prog.append(line.split())
aoc.cprint(execute(prog))
