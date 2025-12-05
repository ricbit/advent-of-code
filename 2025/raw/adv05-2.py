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

def add_inter(all_inter, i):
  #print(all_inter, i)
  for a in all_inter:
    print(list(a.inter(i)))
    if (a.begin <= i.begin <= a.end or
        a.begin <= i.end <= a.end or
        i.begin <= a.begin <= i.end or
        i.begin <= a.end <= i.end):
      print(f"inter {a} {i}")
      for x in i.sub(a):
        add_inter(all_inter, x)
      return
  all_inter.append(i)

def solve(ranges, data):
  ranges = [[int(i) for i in r.split("-")] for r in ranges]
  all_inter = []
  for a, b in ranges:
    add_inter(all_inter, aoc.Interval(a, b))
  print(all_inter)
  return sum(i.end - i.begin + 1 for i in all_inter)

ranges, data = aoc.line_blocks()
print(ranges, aoc.ints(data))
aoc.cprint(solve(ranges, data))
