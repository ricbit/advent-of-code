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

def spin(rep, cycles):
  lock = [0]
  pos = 0
  for i in range(cycles):
    pos = (pos + rep) % len(lock)
    lock = lock[:pos] + [i + 1] + lock[pos:]
    pos = (pos + 1) % len(lock)
  return lock[pos]

rep = int(sys.stdin.read().strip())
aoc.cprint(spin(rep, 2017))
