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
  cpu = IntCode(data)
  code = """
    - .ABCD..
    - ##...##
    - ####.##
    - ##.#.##
    - #.#..##
    NOT C T
    NOT D J
    NOT J J
    AND T J
    NOT A T
    OR T J
    NOT B T
    AND D T
    OR T J
    - ###.###
    WALK
  """
  code = """
    - .ABCD..
    - ##...##
    - ####.##
    - ##.#.##
    - #.#..##
    NOT C J
    AND D J
    AND H J
    - 
    NOT B T
    AND D T
    OR T J
    - J = C=0 D=1 H=1
    NOT A T
    OR T J
    - ###.###
    RUN
  """
  pcode = []
  for line in code.split("\n"):
    if line.strip() and not line.strip().startswith("-"):
      pcode.append(line.strip() + chr(10))
  pcode = "".join(pcode)
  pos = 0
  while cpu.run():
    match cpu.state:
      case cpu.INPUT:
        cpu.input = ord(pcode[pos])
        pos += 1
        # value = cpu.input
      case cpu.OUTPUT:
        last = cpu.output
        if cpu.output < 128:
          print(chr(cpu.output), end="", flush=True)
  return last

data = aoc.ints(sys.stdin.read().strip().split(","))
aoc.cprint(solve(data))
