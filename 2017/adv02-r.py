import sys
import re
import itertools
import math
import aoc
import heapq
import functools
import copy
from collections import *
from dataclasses import dataclass

lines = [line.strip() for line in sys.stdin]
ans1, ans2 = 0, 0
for line in lines:
  numbers = [int(i) for i in line.strip().split()]
  ans1 += max(numbers) - min(numbers)
  for a in itertools.combinations(numbers, 2):
    if max(a) % min(a) == 0:
      ans2 += max(a) // min(a)
aoc.cprint(ans1)
aoc.cprint(ans2)
