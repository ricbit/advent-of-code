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
  nat = None
  lasty = None
  accept = False
  for tick in itertools.count(0):
    #print(f"tick {tick}")
    for i in range(50):
      cpus[i].run()
      #print(f"cpu {i}, cpustate {cpus[i].state}, state {state[i].state}")
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
              nat = (state[i].x, state[i].y)
              print(f"cpu {i} sent to the nat {nat}")
              accept = True
              continue
            state[state[i].addr].iq.append((state[i].x, state[i].y))
    if (all(not s.iq for s in state) and 
        all(cpu.state == cpu.INPUT for cpu in cpus) and
        all(s.state == 0 for s in state)):
      if nat is not None:
        print(nat)
        state[0].iq.append(nat)
        if accept:
          #if lasty == nat[1]:
          #  return nat[1]
          lasty = nat[1]
        accept = False



data = aoc.ints(sys.stdin.read().strip().split(","))
aoc.cprint(solve(data))
