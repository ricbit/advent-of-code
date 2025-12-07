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


class Search:
  def __init__(self, table):
    self.table = table

  @functools.cache
  def search(self, j, i):
    while j < len(self.table.table) - 1 and self.table[j][i] != "^":
      j += 1
    if self.table[j][i] != "^":
      return 1
    return self.search(j, i - 1) + self.search(j, i + 1)

def solve2(table):
  j, i = table.find("S")
  s = Search(table)
  return s.search(j, i)

def solve(table):
  for j in range(1, len(table.table)):
    for i in range(len(table[0])):
      if table[j - 1][i] == "S":
        table[j][i] = "|"
      elif table[j - 1][i] == "|" and table[j][i] == ".":
        table[j][i] = "|"
    for i in range(len(table[0])):
      if i < len(table[0]) - 1 and table[j][i] == "." and table[j][i + 1] == "^" and table[j - 1][i + 1] == "|":
        table[j][i] = "|"
      if i > 0 and table[j][i] == "." and table[j][i - 1] == "^" and table[j - 1][i - 1] == "|":
        table[j][i] = "|"
  splits = 0
  for j, i in table.iter_all():
    if table[j][i] == "^" and table[j - 1][i] == "|":
      splits += 1
  return splits


data = aoc.Table.read()
aoc.cprint(solve(data))
aoc.cprint(solve2(data))
