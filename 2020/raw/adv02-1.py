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

def solve(data):
  ans = 0
  for line in data:
    if line.a <= line.password.count(line.goal) <= line.b:
      ans += 1
  return ans

data = aoc.retuple_read("a_ b_ goal password", r"(\d+)-(\d+) (.): (.*)")
aoc.cprint(solve(data))
