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

def part2(values, target):
  vlink = [(v, i, None) for i, v in enumerate(values)]
  vhash = aoc.ddict(lambda: None)
  vhash.update({v: i for i, v in enumerate(values)})
  for _ in range(len(values), target):
    speak, i, prev = vlink[-1]
    if prev is not None:
      new_value = i - prev
      vlink.append((new_value, i + 1, vhash[new_value]))
      vhash[new_value] = i + 1
    else:
      vlink.append((0, i + 1, vhash[0]))
      vhash[0] = i + 1
  return vlink[-1][0]

data = aoc.ints(sys.stdin.read().strip().split(","))
aoc.cprint(part2(data, 2020))
aoc.cprint(part2(data, 30000000))
