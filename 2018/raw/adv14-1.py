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
  for i in range(size + 10):
    new = recipes[pos1] + recipes[pos2]
    recipes.extend((int(i) for i in str(new)))
    pos1 = (pos1 + 1 + recipes[pos1]) % len(recipes)
    pos2 = (pos2 + 1 + recipes[pos2]) % len(recipes)
  return "".join(str(i) for i in recipes[size:size + 10])

data = sys.stdin.read().strip()
aoc.cprint(solve(int(data)))
