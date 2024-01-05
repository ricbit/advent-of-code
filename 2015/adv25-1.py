import sys
import re
import itertools
import math
import aoc
import heapq
import functools
from collections import *

def codes():
  code = 20151125
  while True:
    yield code
    code = code * 252533 % 33554393

def diagonal():
  for d in itertools.count(1):
    for i in range(d):
      yield (d - i, i + 1)

def find(row, col):
  for (j, i), code in zip(diagonal(), codes()):
    if (j, i) == (row, col):
      return code

row, col = map(int, re.match(r".*?(\d+).*?(\d+)", sys.stdin.read()).groups())
aoc.cprint(find(row, col))
