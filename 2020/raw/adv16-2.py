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

class Order:
  def __init__(self, tickets, rules, my_ticket):
    self.tickets = tickets
    self.rules = rules
    self.my_ticket = my_ticket

  def presolve(self):
    self.candidates = []
    for x in range(len(self.rules)):
      candidate = []
      for rule_index in range(len(self.rules)):
        r = self.rules[rule_index]
        if all(r.a <= ticket[x] <= r.b or r.c <= ticket[x] <= r.d
               for ticket in self.tickets):
          candidate.append(rule_index)
      self.candidates.append((x, candidate))
    self.candidates.sort(key=lambda x: len(x[1]))
    return self.candidates

  @functools.lru_cache(None)
  def valid(self, found):
    if len(found) > 17:
      print(len(found))
    left = set(range(len(self.rules))).difference(found)
    if not left:
      return found
    rleft = set(left).intersection(self.candidates[len(found)][1])
    for rule_index in rleft:
      check = self.valid(tuple(list(found) + [rule_index]))
      if check is not None:
        return check
    return None

  def solve(self):
    used = set()
    ans = 1
    departure = set(i for i, r in enumerate(self.rules) if r.name.startswith("departure"))
    for index, cand in self.candidates:
      c = set(cand).difference(used)
      if aoc.first(c) in departure:
        ans *= self.my_ticket[index]
      used.update(c)
    return ans

def solve(data):
  rules_lines, my_ticket, nearby_tickets = data
  rules = []
  for rule in rules_lines:
    r = aoc.retuple("name a_ b_ c_ d_", r"(.*): (\d+)-(\d+) or (\d+)-(\d+)", rule)
    rules.append(r)
  my_ticket = aoc.ints(my_ticket[1].split(","))
  ans = 0
  valid = []
  for ticket in nearby_tickets[1:]:
    ticket = aoc.ints(ticket.split(","))
    good = True
    for field in ticket:
      if not any(r.a <= field <= r.b or r.c <= field <= r.d for r in rules):
        good = False
        ans += field
    if good:
      valid.append(ticket)
    #print(ticket, good)
  order = Order(valid, rules, my_ticket)
  order.presolve()
  return ans, order.solve()

data = aoc.line_blocks()
aoc.cprint(solve(data))
