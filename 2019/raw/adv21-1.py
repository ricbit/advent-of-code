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
    - ###.###
    WALK
  """
  pcode = []
  for line in code.split("\n"):
    if line.strip() and not line.strip().startswith("-"):
      pcode.append(line.strip() + chr(10))
  pcode = "".join(pcode)
  print([ord(i) for i in pcode])
  pos = 0
  while cpu.run():
    match cpu.state:
      case cpu.INPUT:
        cpu.input = ord(pcode[pos])
        print(cpu.input)
        pos += 1
        # value = cpu.input
      case cpu.OUTPUT:
        last = cpu.output
        #print(chr(cpu.output), end="", flush=True)
  return last

data = aoc.ints(sys.stdin.read().strip().split(","))
aoc.cprint(solve(data))
