import sys
import re
import itertools
import math
import aoc
import heapq
import functools
import copy
from collections import deque
from dataclasses import dataclass

def spin1(rep, cycles):
  lock = deque([0])
  pos = 0
  for i in range(cycles):
    pos = (pos + rep) % len(lock)
    lock.insert(pos, i + 1)
    pos = (pos + 1) % len(lock)
  return lock[pos]

def spin2(rep, cycles):
  pos = 0
  qlen = 1
  first = 0
  for i in range(cycles):
    pos = (pos + rep) % qlen
    if pos == 0:
      first = i + 1
    qlen += 1
    pos = (pos + 1) % qlen
  return first

rep = int(sys.stdin.read().strip())
aoc.cprint(spin1(rep, 2017))
aoc.cprint(spin2(rep, 50000000))
