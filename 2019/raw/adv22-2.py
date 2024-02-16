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
from aoc.refintcode import IntCode

def parse(data, size):
  a, b = 1, 0
  for line in data:
    q = aoc.retuple("words value_", r"(.+?)( [-+]?\d+)?$", line)
    match q.words, q.value:
      case "cut", value:
        b -= value
      case "deal into new stack", _:
        a = -a
        b = -1 - b
      case "deal with increment", value:
        a = (a * value) % size
        b = (b * value) % size
  return a % size, b % size

def apply(data, size, value):
  a, b = parse(data, size)
  return (a * value + b) % size


data = [line.strip() for line in sys.stdin]
aoc.cprint(apply(data, 10007, 2019))
