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

class Machine:
  def __init__(self, goal, buttons):
    self.goal = tuple([(0 if c == "." else 1) for c in goal])
    self.buttons = buttons
    print(self.goal, self.buttons)

  def search(self):
    state = tuple([0] * len(self.goal))
    visited = set()
    queue = [(0, state)]
    while queue:
      flips, state = heapq.heappop(queue)
      if state == self.goal:
        return flips
      visited.add(state)
      state = list(state)
      for button in self.buttons:
        nstate = state[:]
        for pos in button:
          nstate[pos] = 1 - nstate[pos]
        tstate = tuple(nstate)
        if tstate not in visited:
          heapq.heappush(queue,(flips + 1, tstate))
    return None


def solve(machines):
  ans = 0
  for machine in machines:
    m = Machine(*machine)
    ans += m.search()
  return ans

data = aoc.retuple_read("goal buttons joltage", r"\[(.*?)\] (\(.*?\)\s+)\{(.*?)\}")
machines = []
for line in data:
  buttons = line.buttons.split()
  machines.append((line.goal, 
                   [list(map(int, b[1:-1].split(","))) for b in buttons]))

aoc.cprint(solve(machines))
