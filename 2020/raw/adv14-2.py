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

def solve(lines):
  mem = aoc.ddict(lambda: 0)
  for line in lines:
    if line.startswith("mask"):
      mask = line.split("=")[1].strip()
      xs = [2 ** i for i, v in enumerate(mask[::-1]) if v == "X"]
      mand = int("".join("0" if i == "X" else "1" for i in mask), 2)
      mor = int("".join("0" if i == "X" else i for i in mask), 2)
    else:
      op = aoc.retuple("addr_ value_", r"mem\[(\d+)\] = (\d+)", line)
      base_addr = (op.addr & mand) | mor
      for bits in itertools.product([0, 1], repeat=len(xs)):
        new_addr = base_addr + sum(b * v for b, v in zip(bits, xs))
        mem[new_addr] = op.value
  return sum(mem.values())

data = sys.stdin.read().splitlines()
aoc.cprint(solve(data))
