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

def simulate(mem, limit, early_stop=False):
  pc = 0
  acc = 0
  count = 0
  visited = set()
  while True:
    count += 1
    if pc == len(mem) or (early_stop and pc in visited):
      return acc
    if count > limit:
      return None
    visited.add(pc)
    match mem[pc]:
      case "nop", _: 
        pass        
      case "acc", value:
        acc += value
      case "jmp", value:
        pc = pc + value -1
    pc += 1

def search(mem):
  limit = 1000
  for i in range(len(mem)):
    if mem[i][0] == "nop":
      mem[i][0] = "jmp"
      if (ans := simulate(mem, limit)) is not None:
        return ans
      mem[i][0] = "nop"
    if mem[i][0] == "jmp":
      mem[i][0] = "nop"
      if (ans := simulate(mem, limit)) is not None:
        return ans
      mem[i][0] = "jmp"
  return None

data = [[x.opcode, x.value] for x in aoc.retuple_read("opcode value_", r"(\w+) ([-+0-9]+)")]
aoc.cprint(simulate(data, 1000, early_stop=True))
aoc.cprint(search(data))
