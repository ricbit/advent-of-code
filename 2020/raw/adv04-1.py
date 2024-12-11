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

required = set("".join(field) for field in itertools.batched("byriyreyrhgthcleclpid", 3))

def solve(passports):
  ans = 0
  for raw in passports:
    passport = set(re.findall(r"(\w{3}):\S+", " ".join(raw)))
    print(passport, required, "\n")
    if all(field in passport for field in required):
      ans += 1
  return ans

data = aoc.line_blocks()
aoc.cprint(solve(data))
