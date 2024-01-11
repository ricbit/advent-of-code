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

def bfs(jumps):
  pos = 0
  vnext = aoc.bq([0, pos])
  visited = set()
  while vnext:
    score, pos = vnext.pop()


def simple(jumps):
  pos = 0
  step = 0
  while 0 <= pos < len(jumps):
    npos = pos + jumps[pos]
    jumps[pos] += 1
    pos  = npos
    step += 1
  return step


lines = [int(line.strip()) for line in sys.stdin]
aoc.cprint(simple(lines))
