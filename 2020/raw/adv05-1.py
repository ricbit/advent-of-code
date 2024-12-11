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

translation = {k:v for k,v in itertools.batched("F0B1L0R1", 2)}

def solve(lines):
  for line in lines:
    binary = "".join(translation[c] for c in line)
    yield (int(binary[:7], 2) * 8 + int(binary[7:], 2))

data = sys.stdin.read().splitlines()
aoc.cprint(max(solve(data)))
