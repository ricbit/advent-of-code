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
  words = line.split()
  if len(words) == len(set(words)):
    ans1 += 1
  words = ["".join(sorted(w)) for w in words]
  if len(words) == len(set(words)):
    ans2 += 1
aoc.cprint(ans1)
aoc.cprint(ans2)
