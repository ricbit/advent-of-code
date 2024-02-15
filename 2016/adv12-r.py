import sys
import re
import aoc

def isnum(reg):
  return reg.isdigit() or (reg[0] in "+-" and reg[1:].isdigit())

def simulate(prog, state):
  pc = 0
  while pc < len(prog):
    match re.match(r"(\w+) ([-+]?\w+)(?: ([+-]?\w+))?", prog[pc]).groups():
      case ("inc", reg, _):
        state[reg] += 1
      case ("dec", reg, _):
        state[reg] -= 1
      case ("jnz", reg, offset):
        if (isnum(reg) and int(reg) != 0) or state[reg] != 0:
          pc += int(offset) - 1
      case ("cpy", reg, dst):
        if isnum(reg):
          state[dst] = int(reg)
        else:
          state[dst] = state[reg]
    pc += 1
  return state["a"]

prog = [line.strip() for line in sys.stdin]
state = {"a": 0, "b": 0, "c": 0, "d": 0}
aoc.cprint(simulate(prog, state))
state = {"a": 0, "b": 0, "c": 1, "d": 0}
aoc.cprint(simulate(prog, state))

