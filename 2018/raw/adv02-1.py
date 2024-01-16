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
ans = 0
has2, has3 = 0, 0
for line in lines:
  line = list(line)
  line.sort()
  h2, h3 = 0, 0
  for k, v in itertools.groupby(line):
    v = list(v)
    if len(v) == 2:
      h2 = 1
    elif len(v) == 3:
      h3 = 1
  has2 += h2
  has3 += h3
aoc.cprint(has2 * has3)
