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

class Solver:
  def __init__(self, data):
    colors, stripes = data
    self.colors = set([color.strip() for color in colors[0].split(",")])
    self.stripes = [x.strip() for x in stripes]

  @functools.cache
  def search(self, line):
    ans = 0
    if line in self.colors:
      ans += 1
    for i in range(len(line)):
      if line[:i] in self.colors and (x := self.search(line[i:])):
        ans += x
    return ans

  def solve(self):
    ans = 0
    for line in self.stripes:
      ans += self.search(line)
      
    return ans

data = aoc.line_blocks()
s = Solver(data)
aoc.cprint(s.solve())
