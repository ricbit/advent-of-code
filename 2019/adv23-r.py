import sys
import aoc
from aoc.refintcode import IntCode
from dataclasses import dataclass

@dataclass(init=True)
class CpuState:
  iq: [(int, int)]
  output: [int]

def init(data):
  cpus = []
  state = []
  for i in range(50):
    cpu = IntCode(data)
    cpu.run()
    cpu.input = i
    cpus.append(cpu)
    state.append(CpuState([], []))
  return cpus, state

def idle(state, cpus):
  return (
      all(not s.iq for s in state) and
      all(cpu.state == cpu.INPUT for cpu in cpus))

def execute(data):
  cpus, state = init(data)
  nats = None
  while True:
    for i in range(50):
      cpus[i].run()
      match cpus[i].state:
        case IntCode.INPUT:
          if not state[i].iq:
            cpus[i].input = -1
          else:
            cpus[i].input = state[i].iq.pop(0)
        case IntCode.OUTPUT:
          state[i].output.append(cpus[i].output)
          if len(state[i].output) == 3:
            addr, x, y = state[i].output
            state[i].output.clear()
            if addr == 255:
              nats = (x, y)
            else:
              state[addr].iq.extend([x, y])
    if idle(state, cpus) and nats is not None:
      state[0].iq.extend(nats)
      yield nats[1]

def solve(data):
  nats = aoc.ddict(lambda: 0)
  it = execute(data)
  first = next(it)
  for y in it:
    nats[y] += 1
    if nats[y] > 3:
      return first, y
  return None

data = aoc.ints(sys.stdin.read().strip().split(","))
ans1, ans2 = solve(data)
aoc.cprint(ans1)
aoc.cprint(ans2)
