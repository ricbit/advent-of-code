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

def count(fuel):
  a = fuel // 3 - 2
  print(a)
  if a > 0:
    return a + count(a)
  return 0

data = [line.strip() for line in sys.stdin]
ans = 0
for line in data:
  ans += count(int(line))
aoc.cprint(ans)
