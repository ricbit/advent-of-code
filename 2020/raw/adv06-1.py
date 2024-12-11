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
  for block in data:
    ans += len(set("".join(block)))
  return ans

data = aoc.line_blocks()
aoc.cprint(solve(data))
