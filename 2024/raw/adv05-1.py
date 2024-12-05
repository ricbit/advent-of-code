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

def check(rules, page):
  for i in range(len(page)):
    for j in range(i + 1, len(page)):
      if page[i] in rules[page[j]]:
        return False
  return True

def solve(data):
  rules1, pages = data
  rules = aoc.ddict(list)
  for rule in rules1:
    a,b = rule.split("|")
    rules[int(a)].append(int(b))
  ans = 0
  for spage in pages:
    page = aoc.ints(spage.split(","))
    if check(rules, page):
      print(page)
      ans += page[len(page) // 2]
  return ans

data = aoc.line_blocks()
aoc.cprint(solve(data))
