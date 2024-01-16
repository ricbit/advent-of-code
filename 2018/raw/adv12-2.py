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

def solve(initial, rules):
  field = set(i for i, c in enumerate(initial) if c == "#")
  old = sum(field)
  for gen in range(2000):
    newfield = set()
    for x in range(min(field) - 5, max(field) + 5):
      pots = []
      for i in range(5):
        pots.append("#" if (x + i) in field else ".")
      if rules.get("".join(pots), ".") == "#":
        newfield.add(x + 2)
    d = sum(field) - old
    #print(gen, d)
    if d == -201:
      break
    old = sum(field)
    field = newfield
  return sum(field) + (50000000000 - gen) * 22

data = aoc.line_blocks()
initial = data[0][0].split(": ")[1]
rules = {}
for line in data[1]:
  q = aoc.retuple("src dst", r"(.+) => (.)", line)
  rules[q.src] = q.dst
aoc.cprint(solve(initial, rules))
