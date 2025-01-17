import sys
import aoc
from aoc.assembunny import Assembunny

def mul_patch(state, pc):
  state['a'] = state['b'] * state['d']
  state['c'] = state['d'] = 0
  pc = 10
  return state, pc

lines = [line.strip() for line in sys.stdin]

asm = Assembunny(lines.copy())
asm.apply_patch(4, mul_patch)
state = {"a": 7, "b": 0, "c": 0, "d": 0}
aoc.cprint(asm.simulate(state)['a'])

asm = Assembunny(lines.copy())
asm.apply_patch(4, mul_patch)
state = {"a": 12, "b": 0, "c": 0, "d": 0}
aoc.cprint(asm.simulate(state)['a'])

