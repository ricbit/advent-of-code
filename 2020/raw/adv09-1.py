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

def check(window, value):
  for x in window:
    if (value - x) in window and value != 2 * x:
      return True
  return False

def solve(data, preamble):
  window = set(data[:preamble])
  for i in range(preamble, len(data)):
    if not check(window, data[i]):
      return data[i]
    window.remove(data[i - preamble])
    window.add(data[i])

data = aoc.ints(sys.stdin.read().splitlines())
preamble = 25
aoc.cprint(solve(data, preamble))
