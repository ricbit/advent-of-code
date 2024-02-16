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
from aoc.refintcode import IntCode

@dataclass(init=True)
class CpuState:
  state: int
  x: int
  y: int
  addr: int
  iq: [(int, int)]

def solve(data):
  cpus = []
  state = []
  for i in range(50):
    cpu = IntCode(data)
    while cpu.run():
      match cpu.state:
        case cpu.OUTPUT:
          print(cpu.output)
        case cpu.INPUT:
          cpu.input = i
          break
    cpus.append(cpu)
    state.append(CpuState(0, 0, 0, 0, []))
  for tick in itertools.count(0):
    print(f"tick {tick}")
    for i in range(50):
      cpus[i].run()
      print(f"cpu {i}, cpustate {cpus[i].state}, state {state[i].state}")
      match cpus[i].state:
        case cpu.INPUT:
          if state[i].state == 0:
            if not state[i].iq:
              cpus[i].input = -1
            else:
              cpus[i].input = state[i].iq[0][0]
              state[i].state = 10
          elif state[i].state == 10:
            cpus[i].input = state[i].iq[0][1]
            state[i].state = 0
            state[i].iq.pop(0)
        case cpu.OUTPUT:
          if state[i].state == 0:
            state[i].addr = cpus[i].output
            state[i].state = 1
          elif state[i].state == 1:
            state[i].x = cpus[i].output
            state[i].state = 2
          elif state[i].state == 2:
            state[i].y = cpus[i].output
            state[i].state = 0
            if state[i].addr == 255:
              return cpus[i].output
            state[state[i].addr].iq.append((state[i].x, state[i].y))

data = aoc.ints(sys.stdin.read().strip().split(","))
aoc.cprint(solve(data))
