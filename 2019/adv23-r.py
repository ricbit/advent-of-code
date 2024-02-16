import sys
import itertools
import aoc
from aoc.refintcode import IntCode
from dataclasses import dataclass

@dataclass(init=True)
class CpuState:
  state: int
  x: int
  y: int
  addr: int
  iq: [(int, int)]

def init(data):
  cpus = []
  state = []
  for i in range(50):
    cpu = IntCode(data)
    cpu.run()
    cpu.input = i
    cpus.append(cpu)
    state.append(CpuState(0, 0, 0, 0, []))
  return cpus, state

def solve(data):
  cpus, state = init(data)
  nat = None
  lasty = [0, 0]
  firsty = None
  for tick in itertools.count(0):
    for i in range(50):
      cpus[i].run()
      match cpus[i].state:
        case IntCode.INPUT:
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
        case IntCode.OUTPUT:
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
              if firsty is None:
                firsty = state[i].y
              continue
            state[state[i].addr].iq.append((state[i].x, state[i].y))
    if (all(not s.iq for s in state) and 
        all(cpu.state == cpu.INPUT for cpu in cpus) and
        all(s.state == 0 for s in state)):
      if nat is not None:
        state[0].iq.append(nat)
        if lasty[0] == nat[1]:
          lasty[1] += 1
        else:
          lasty[0] = nat[1]
        if lasty[1] > 3:
          return firsty, lasty[0]

data = aoc.ints(sys.stdin.read().strip().split(","))
ans1, ans2 = solve(data)
aoc.cprint(ans1)
aoc.cprint(ans2)
