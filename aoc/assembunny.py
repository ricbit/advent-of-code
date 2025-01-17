import sys
import re

def dummy(state, pc):
  return (state, pc)

class Assembunny:
  def __init__(self, lines):
    self.prog = self.parse(lines)
    self.patch = dummy

  def apply_patch(self, bp, patch_func):
    self.patch = patch_func
    self.prog[bp] = ("patch", "1")

  def isnum(self, reg):
    return reg.isdigit() or (reg[0] in "+-" and reg[1:].isdigit())

  def getoffset(self, offset, state):
    if self.isnum(offset):
      return int(offset)
    else:
      return state[offset]

  def simulate(self, state, breakpoint=None):
    pc = 0
    while pc < len(self.prog):
      if pc == breakpoint:
        return state
      match self.prog[pc]:
        case ("out", reg):
          pass
        case ("inc", reg):
          if not self.isnum(reg):
            state[reg] += 1
        case ("dec", reg):
          if not self.isnum(reg):
            state[reg] -= 1
        case ("tgl", offset):
          dest = pc + self.getoffset(offset, state)
          if 0 <= dest < len(self.prog):
            match self.prog[dest]:
              case ("inc", _):
                self.prog[dest][0] = "dec"
              case (_, _):
                self.prog[dest][0] = "inc"
              case ("jnz", _, _):
                self.prog[dest][0] = "cpy"
              case (_, _, _):
                self.prog[dest][0] = "jnz"
        case ("jnz", reg, offset):
          if (self.isnum(reg) and int(reg) != 0) or (not self.isnum(reg) and state[reg] != 0):
            pc += self.getoffset(offset, state) - 1
        case ("cpy", reg, dst):
          if not self.isnum(dst):
            state[dst] = self.getoffset(reg, state)
        case ("patch", _):
          state, pc = self.patch(state, pc)
          continue
      pc += 1
    return state

  def parse(self, lines):
    ans = []
    for line in lines:
      ins = re.match(r"(\w+) ([-+]?\w+)(?: ([+-]?\w+))?", line).groups()
      ins = [i for i in ins if i is not None]
      ans.append(ins)
    return ans

