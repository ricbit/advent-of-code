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

def check(window, value):
  for x in window:
    if (value - x) in window and value != 2 * x:
      return True
  return False

def find_number(data, preamble):
  window = set(data[:preamble])
  for i in range(preamble, len(data)):
    if not check(window, data[i]):
      return data[i]
    window.remove(data[i - preamble])
    window.add(data[i])

def part2(data, number):
  csum = []
  acc = 0
  for x in data:
    csum.append(acc + x)
    acc += x
  dsum = {x: index for index, x in enumerate(csum)}
  for i, x in enumerate(csum):
    if (x - number) in csum:
      print(x, i, dsum[x - number])
      seq = data[dsum[x - number] + 1:i + 1]
      return min(seq) + max(seq)

data = aoc.ints(sys.stdin.read().splitlines())
preamble = 25
number = find_number(data, preamble)
aoc.cprint(number)
aoc.cprint(part2(data, number))
