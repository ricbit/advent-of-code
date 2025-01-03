import sys
import re
import aoc

def simulate(prog, state):
  pc = 0
  while pc < len(prog):
    match re.match(r"(\w+) ([-+]?\w+)(?:, ([-+]\w+))?", prog[pc]).groups():
      case ("inc", reg, _):
        state[reg] += 1
      case ("tpl", reg, _):
        state[reg] *= 3
      case ("hlf", reg, _):
        state[reg] >>= 1
      case ("jmp", offset, _):
        pc += int(offset) - 1
      case ("jie", reg, offset):
        if state[reg] % 2 == 0:
          pc += int(offset) - 1
      case ("jio", reg, offset):
        if state[reg] == 1:
          pc += int(offset) - 1
    pc += 1
  return state["b"]

prog = [line.strip() for line in sys.stdin]
state = {"a": 0, "b": 0}
aoc.cprint(simulate(prog, state))
state = {"a": 1, "b": 0}
aoc.cprint(simulate(prog, state))
