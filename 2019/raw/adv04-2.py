import sys
import string
import re
import itertools
import math
import aoc
import heapq
import functools
import copy
from collections import Counter, deque
from dataclasses import dataclass

def same(pwd):
  for a, b in zip(pwd, pwd[1:]):
    if a == b:
      return True
  return False

def same2(pwd):
  for k, v in itertools.groupby(pwd):
    yield len(list(v)) == 2

data = [int(i) for i in sys.stdin.read().strip().split("-")]
ans1, ans2 = 0, 0
for pwd in range(data[0], 1 + data[1]):
  spwd = list(str(pwd))
  if same(spwd) and spwd == list(sorted(spwd)):
    ans1 += 1
  if any(same2(spwd)) and spwd == list(sorted(spwd)):
    ans2 += 1
aoc.cprint(ans1)
aoc.cprint(ans2)
