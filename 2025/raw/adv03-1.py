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

def iter_jolts(s):
  for i in range(len(s)):
    for j in range(i + 1, len(s)):
      yield int(s[i] + s[j])

def solve(data):
  ans = 0
  for line in data:
    ans += max(iter_jolts(line.strip()))
  return ans

data = sys.stdin.readlines()
aoc.cprint(solve(data))
