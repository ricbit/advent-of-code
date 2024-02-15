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
  while cpu.run():
    match cpu.state:
      case cpu.INPUT:
        value = cpu.input
      case cpu.OUTPUT:
        cpu.output = value

data = aoc.ints(sys.stdin.read().strip().split(","))
aoc.cprint(solve(data))
