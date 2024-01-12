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

def apply(line):
  q = list(range(256))
  pos = 0
  skip = 0
  for n in line:
    qq = q[:]
    for i in range(0, n):
      qq[(pos + i) % len(q)] = q[(pos + n - 1 - i + len(q)) % len(q)]
    q = qq
    pos += n + skip
    skip += 1
  return q


line = aoc.ints(sys.stdin.read().strip().split(","))
q = apply(line)
aoc.cprint(q[0] * q[1])
