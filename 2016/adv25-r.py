import sys
import re
import aoc

def isnum(reg):
  return reg.isdigit() or (reg[0] in "+-" and reg[1:].isdigit())

def getoffset(offset, state):
  if isnum(offset):
    return int(offset)
  else:
    return state[offset]

def simulate(prog, state):
  pc = 0
  while pc < len(prog):
    if pc == 9:
      return state["a"]
    match prog[pc]:
      case ("out", reg):
        pass
      case ("inc", reg):
        if not isnum(reg):
          state[reg] += 1
      case ("dec", reg):
        if not isnum(reg):
          state[reg] -= 1
      case ("tgl", offset):
        dest = pc + getoffset(offset, state)
        if 0 <= dest < len(prog):
          match prog[dest]:
            case ("inc", _):
              prog[dest][0] = "dec"
            case (_, _):
              prog[dest][0] = "inc"
            case ("jnz", _, _):
              prog[dest][0] = "cpy"
            case (_, _, _):
              prog[dest][0] = "jnz"
      case ("jnz", reg, offset):
        if (isnum(reg) and int(reg) != 0) or (not isnum(reg) and state[reg] != 0):
          pc += getoffset(offset, state) - 1
      case ("cpy", reg, dst):
        if not isnum(dst):
          state[dst] = getoffset(reg, state)
    pc += 1
  return state["a"]

def parse(lines):
  ans = []
  for line in lines:
    ins = re.match(r"(\w+) ([-+]?\w+)(?: ([+-]?\w+))?", line).groups()
    ins = [i for i in ins if i is not None]
    ans.append(ins)
  return ans

prog = parse((line.strip() for line in sys.stdin))
state = {"a": 0, "b": 0, "c": 0, "d": 0}
base = simulate(prog, state)
size = (len(bin(base)) - 2) // 2
out = int("10" * size, 2) - base
aoc.cprint(out)
