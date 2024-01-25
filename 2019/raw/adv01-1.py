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

def solve(data):
  return 0

data = [line.strip() for line in sys.stdin]
ans = 0
for line in data:
  ans += int(line) // 3 - 2
aoc.cprint(ans)
