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

def solve(mem):
  pc = 0
  acc = 0
  visited = set()
  while True:
    if pc in visited:
      return acc
    visited.add(pc)
    match mem[pc].opcode, mem[pc].value:
      case "nop", _: 
        pass        
      case "acc", value:
        acc += value
      case "jmp", value:
        pc = pc + value -1
    pc += 1

data = aoc.retuple_read("opcode value_", r"(\w+) ([-+0-9]+)")
aoc.cprint(solve(data))
