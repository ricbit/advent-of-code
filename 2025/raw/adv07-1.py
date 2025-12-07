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
