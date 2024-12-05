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
  def comp(a, b):
    return -1 if a in rules[b] else 1
  for spage in pages:
    page = aoc.ints(spage.split(","))
    if not check(rules, page):
      page.sort(key=functools.cmp_to_key(comp))
      print(page)
      ans += page[len(page) // 2]
  return ans

data = aoc.line_blocks()
aoc.cprint(solve(data))
