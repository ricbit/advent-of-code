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
import mip

class Machine:
  def __init__(self, goal, buttons, joltage):
    self.goal = tuple(joltage)
    self.buttons = buttons

  def search(self):
    m = mip.Model(sense=mip.MINIMIZE)
    m.verbose = 0
    button = [m.add_var(var_type=mip.INTEGER, name=f"b{i}") 
              for i in range(len(self.buttons))]
    for i in range(len(self.goal)):
      m += mip.xsum(button[b] for b in range(len(button)) 
                    if i in self.buttons[b]) == self.goal[i]
    m.objective = mip.minimize(mip.xsum(button))
    m.optimize()
    return int(m.objective_value)

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
  print(line.joltage)
  machines.append((line.goal, 
                   [list(map(int, b[1:-1].split(","))) for b in buttons],
                   list(map(int, line.joltage.split(",")))))

aoc.cprint(solve(machines))
