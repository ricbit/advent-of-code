import sys
import string
import re
import itertools
import math
import aoc
import heapq
import functools
import copy
from collections import Counter, deque
from dataclasses import dataclass

# P1 18:16 P2+56:13

def run(code, ip, start):
  state = [0] * 6
  state[0] = start
  while state[ip] < len(code):
    #print(state[ip], state, code[state[ip]])
    line = code[state[ip]]
    match line.code, line.a, line.b, line.c:
      case "addr", a, b, c: 
        state[c] = state[a] + state[b]
      case "addi", a, b, c: 
        state[c] = state[a] + b
      case "mulr", a, b, c: 
        state[c] = state[a] * state[b]
      case "muli", a, b, c: 
        state[c] = state[a] * b
      case "banr", a, b, c: 
        state[c] = state[a] & state[b]
      case "bani", a, b, c: 
        state[c] = state[a] & b
      case "borr", a, b, c: 
        state[c] = state[a] | state[b]
      case "bori", a, b, c: 
        state[c] = state[a] | b
      case "setr", a, b, c: 
        state[c] = state[a]
      case "seti", a, b, c: 
        state[c] = a
      case "gtir", a, b, c: 
        state[c] = 1 if a > state[b] else 0
      case "gtri", a, b, c: 
        state[c] = 1 if state[a] > b else 0
      case "gtrr", a, b, c: 
        state[c] = 1 if state[a] > state[b] else 0
      case "eqir", a, b, c: 
        state[c] = 1 if a == state[b] else 0
      case "eqri", a, b, c: 
        state[c] = 1 if state[a] == b else 0
      case "eqrr", a, b, c: 
        state[c] = 1 if state[a] == state[b] else 0
      case "patch20", a, b, c:
        while True:
          state[2] = (state[3] + 1) * 256
          if state[2] > state[4]:
            break
          state[3] += 1
        state[2] = 1
        state[5] = 25
    state[ip] += 1
  print(state[ip], state)
  return state[0]

lines = [line.strip() for line in sys.stdin.readlines()]
ip = int(lines[0].split()[1])
code = aoc.retuple_read("code a_ b_ c_", r"(\w+) (\d+) (\d+) (\d+)", lines[1:])
aoc.cprint(run(code, ip, 2159153))
code[20] = aoc.retuple("code a_ b_ c_", r"(\w+) (\d+) (\d+) (\d+)", "patch20 0 0 0")
aoc.cprint(run(code, ip, 2159153))
 
