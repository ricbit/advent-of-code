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

def sequence(values, target):
  for pos in range(len(values), target):
    speak = values[-1]
    if speak in values[:-1]:
      allspeak = [i for i, v in enumerate(values) if v == speak]
      values.append(allspeak[-1] - allspeak[-2]) 
    else:
      values.append(0)
  return values[-1]

def solve(data):
  return sequence(data, 2020)

data = aoc.ints(sys.stdin.read().strip().split(","))
aoc.cprint(solve(data))
