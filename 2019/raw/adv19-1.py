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
from aoc.refintcode import IntCode

def solve(data):
  ans = 0
  for j in range(50):
    for i in range(50):
      cpu = IntCode(data)
      state = 0
      while cpu.run():
        match cpu.state:
          case cpu.INPUT:
            print(j,i,state)
            if state == 0:
              cpu.input = j
              state = 1
            elif state == 1:
              cpu.input = i
              state = 2
          case cpu.OUTPUT:
            print(j,i,cpu.output)
            state = 0
            if cpu.output == 1:
              ans += 1
            if j == 49 and i == 49:
              return ans

data = aoc.ints(sys.stdin.read().split(","))
aoc.cprint(solve(data))
