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

def solve(data):
  return 0

def run_real(code):
  state = [0] * 4
  t= {2:12, 0:4, 6:1, 14:13, 7:0, 11:6, 12:8, 1:2, 3:3, 15:11, 9:9, 13:10, 10:14, 8:7, 4:15, 5:5}
  x ={}
  for a, b in t.items():
    x[b]=a
  for op, p1, p2, p3 in code:
    match x[op], p1, p2, p3:
      case 0, a, b, c: 
        # addr
        state[c] = state[a] + state[b]
      case 1, a, b, c: 
        # addi
        state[c] = state[a] + b
      case 2, a, b, c: 
        # mulr
        state[c] = state[a] * state[b]
      case 3, a, b, c: 
        # muli
        state[c] = state[a] * b
      case 4, a, b, c: 
        # banr
        state[c] = state[a] & state[b]
      case 5, a, b, c: 
        # bani
        state[c] = state[a] & b
      case 6, a, b, c: 
        # borr
        state[c] = state[a] | state[b]
      case 7, a, b, c: 
        # bori
        state[c] = state[a] | b
      case 8, a, b, c: 
        # setr
        state[c] = state[a]
      case 9, a, b, c: 
        # seti
        state[c] = a
      case 10, a, b, c: 
        # gtir
        state[c] = 1 if a > state[b] else 0
      case 11, a, b, c: 
        # gtri
        state[c] = 1 if state[a] > b else 0
      case 12, a, b, c: 
        # gtrr
        state[c] = 1 if state[a] > state[b] else 0
      case 13, a, b, c: 
        # gtir
        state[c] = 1 if a == state[b] else 0
      case 14, a, b, c: 
        # gtri
        state[c] = 1 if state[a] == b else 0
      case 15, a, b, c: 
        # gtrr
        state[c] = 1 if state[a] == state[b] else 0
  return state[0]


def parse_opcode(block):
  before = eval(block[0].split(" ", 1)[1])
  opcode = aoc.ints(block[1].split())
  after = eval(block[2].split(" ", 1)[1])
  return before, opcode, after

blocks = aoc.line_blocks()
code = []
for line in blocks[-1]:
  code.append(aoc.ints(line.split()))
aoc.cprint(run_real(code))
