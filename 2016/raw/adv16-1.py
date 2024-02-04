import sys
import re
import itertools
import math
import aoc
import heapq
import functools
from collections import *

def double(a):
  b = [1 - x for x in reversed(a)]
  return a + [0] + b

def upto(seed, goal):
  while len(seed) < goal:
    seed = double(seed)
  return seed[:goal]

def checksum(disk):
  while True:
    if len(disk) % 2 == 1:
      return "".join(str(i) for i in disk)
    newdisk = []
    for a, b in itertools.batched(disk, 2):
      newdisk.append(int(a == b))
    disk = newdisk
  

seed = [int(i) for i in sys.stdin.read().strip()]
disk = upto(seed, 35651584)
aoc.cprint(checksum(disk))

