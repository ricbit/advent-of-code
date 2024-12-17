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

def combo(regs, val):
  if val < 4:
    return val
  return regs[val - 4]


def solve(data):
  register, program = data
  regs = {}
  for line in register:
    x = aoc.retuple("name val_", r"Register (\w): (\d+)", line)
    regs[ord(x.name) - ord("A")] = x.val
  print(program[0].split(":"))
  program = aoc.ints(program[0].split(":")[1].strip().split(","))
  pc = 0
  ans = []
  while True:
    match program[pc]:
      case 0: # adv
        d = regs[0] // (2 ** combo(regs, program[pc + 1]))
        regs[0] = d
      case 1: # bxl
        regs[1] ^= program[pc + 1]
      case 2: # bst
        regs[1] = combo(regs, program[pc + 1]) % 8
      case 3: # jnz
        if regs[0] != 0:
          pc = program[pc + 1] - 2
      case 4: # bxc
        regs[1] ^= regs[2]
      case 5: # out
        ans.append(combo(regs, program[pc + 1]) % 8)
      case 6: # bdv
        d = regs[0] // (2 ** combo(regs, program[pc + 1]))
        regs[1] = d
      case 7: # cdv
        d = regs[0] // (2 ** combo(regs, program[pc + 1]))
        regs[2] = d
    pc += 2
    if pc >= len(program):
      break
  return ",".join(str(i) for i in ans)

data = aoc.line_blocks()
aoc.cprint(solve(data))
