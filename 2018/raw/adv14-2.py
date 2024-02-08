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

def solve(size):
  recipes = [3, 7]
  pos1, pos2 = 0, 1
  for tick in itertools.count(0):
    new = recipes[pos1] + recipes[pos2]
    recipes.extend((int(i) for i in str(new)))
    pos1 = (pos1 + 1 + recipes[pos1]) % len(recipes)
    pos2 = (pos2 + 1 + recipes[pos2]) % len(recipes)
    for pos in range(max(0, len(recipes) - 20), len(recipes)):
      if "".join(str(i) for i in recipes[pos:][:len(size)]) == size:
        return pos

data = sys.stdin.read().strip()
aoc.cprint(solve(data))
