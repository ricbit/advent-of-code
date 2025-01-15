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

def solve(data):
  rules_lines, my_ticket, nearby_tickets = data
  rules = []
  for rule in rules_lines:
    r = aoc.retuple("a_ b_ c_ d_", r".*: (\d+)-(\d+) or (\d+)-(\d+)", rule)
    rules.append(r)
  ans = 0
  for ticket in nearby_tickets[1:]:
    ticket = aoc.ints(ticket.split(","))
    good = True
    for field in ticket:
      if not any(r.a <= field <= r.b or r.c <= field <= r.d for r in rules):
        good = False
        ans += field
        print(field)
    print(ticket, good)

  return ans

data = aoc.line_blocks()
aoc.cprint(solve(data))
