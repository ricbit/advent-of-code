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

def solve(data):
  return data

data = aoc.ints(sys.stdin.read().strip().split(","))
data = aoc.ints_read()
data = aoc.Table.read()
data = aoc.line_blocks()
aoc.cprint(solve(data))
