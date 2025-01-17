import sys
import re
import itertools
import math
import aoc
import heapq
import functools
import copy
from collections import *

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
base = simulate(copy.deepcopy(prog), state)
size = (len(bin(base)) - 2) // 2
out = int("10" * size, 2) - base
aoc.cprint(out)

"""
0 : cpy a d
1 : cpy 15 c
2 : cpy 170 b
3 : inc d
4 : dec b
5 : jnz b -2
6 : dec c
7 : jnz c -5
8 : cpy d a
--- a = d  # 2550 + input
9 : jnz 0 0
10 : cpy a b
11 : cpy 0 a
12 : cpy 2 c
13 : jnz b 2 : 15
14 : jnz 1 6 : 20
15 : dec b
16 : dec c
17 : jnz c -4 : 13
18 : inc a
19 : jnz 1 -7 : 12
--- a = b // 2
--- c = 2 for b even
---     1 for b odd
20 : cpy 2 b
21 : jnz c 2 : 23
22 : jnz 1 4 : 26
23 : dec b
24 : dec c
25 : jnz 1 -4 : 21
--- b = b % 2 (original b)
26 : jnz 0 0
27 : out b
28 : jnz a -19 : 11
29 : jnz 1 -21 : 9

d = a
c = 15
b = 170
1:
2:
d += 1
b -= 1
jnz b 1a
dec c
jnz c 2a

b = a
a = 0
c = 2
jnz b 2b
jnz 1 6b
2:
  
6:
b = 2
jnz c 2b
#jnz 1 4
2


"""
