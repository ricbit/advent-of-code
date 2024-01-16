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

line = aoc.ints(sys.stdin.read().strip().split("\n"))
start = 0
seen = set([0])
for i in itertools.cycle(line):
  start += i
  if start in seen:
    aoc.cprint(start)
    break
  seen.add(start)
