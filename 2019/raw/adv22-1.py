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

def solve(data):
  size = 10007
  cards = deque(list(range(size)))
  for _ in range(4):
    for line in data:
      q = aoc.retuple("words value_", r"(.+?)( [-+]?\d+)?$", line)
      match q.words, q.value:
        case "cut", value:
          cards.rotate(-value)
        case "deal into new stack", _:
          cards = deque(reversed(cards))
        case "deal with increment", value:
          n = [0] * size
          for i in range(size):
            n[(i * value) % size] = cards[i]
          cards = deque(n)
  return cards.index(2019)

data = [line.strip() for line in sys.stdin]
aoc.cprint(solve(data))
