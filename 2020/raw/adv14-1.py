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
      mand = int("".join("1" if i == "X" else "0" for i in mask), 2)
      mor = int("".join("0" if i == "X" else i for i in mask), 2)
    else:
      op = aoc.retuple("addr_ bits", r"mem\[(\d+)\] = (\w+)", line)
      mem[op.addr] = (int(op.bits) & mand) | mor
  return sum(mem.values())

data = sys.stdin.read().splitlines()
aoc.cprint(solve(data))
