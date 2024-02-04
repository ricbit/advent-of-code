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
  visited = set()
  ans = []
  while pc < len(prog):
    #print(pc, state, prog)
    vstate = (pc, tuple(sorted(state.items())))
    if vstate in visited:
      print(ans)
      return False
    visited.add(vstate)
    match prog[pc]:
      case ("out", reg):
        #print(state["a"])
        ans.append(state["a"])
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
        if reg == "0" and offset == "0":
          print(state)
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
for i in itertools.count(1):
  state = {"a": i, "b": 0, "c": 0, "d": 0}
  print(i)
  print(simulate(copy.deepcopy(prog), state))

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
13 : jnz b 2 : 16
14 : jnz 1 6 : 21
15 : dec b
16 : dec c
17 : jnz c -4 : 13
18 : inc a
19 : jnz 1 -7 : 12
20 : cpy 2 b
21 : jnz c 2 : 24
22 : jnz 1 4 : 27
23 : dec b
24 : dec c
25 : jnz 1 -4 : 21
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
