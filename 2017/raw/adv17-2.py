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

def spin(rep, cycles):
  lock = deque([0])
  pos = 0
  qlen = 1
  first = 0
  for i in range(cycles):
    if i % 100000 == 0:
      print(i)
    pos = (pos + rep) % qlen
    if pos == 0:
      first = i + 1
      #print(i + 1)
    #lock.insert(pos, i + 1)
    qlen += 1
    pos = (pos + 1) % qlen
  return first

rep = int(sys.stdin.read().strip())
aoc.cprint(spin(rep, 50000000))
