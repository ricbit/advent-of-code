import sys
import string
import re
import itertools
import math
import aoc
import heapq
import functools
import copy
from collections import Counter, deque
from dataclasses import dataclass

def solve(data):
  pos = 0
  while pos < len(data):
    if data[pos] == 1:
      a, b, c = data[pos + 1: pos + 4]
      data[c] = data[a] + data[b]
      pos += 4
    elif data[pos] == 2:
      a, b, c = data[pos + 1: pos + 4]
      data[c] = data[a] * data[b]
      pos += 4
    elif data[pos] == 99:
      break
  return data[0]


data = [int(i) for i in sys.stdin.read().split(",")]
data[1] = 12
data[2] = 2
aoc.cprint(solve(data))
