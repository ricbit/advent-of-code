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
  return 0

data = sys.stdin.read().strip()
layers = []
size = 25 * 6
for i in range(len(data) // size):
  layers.append(data[size * i : size * i + size])
m = min(layers, key=lambda x:x.count("0"))
aoc.cprint(m.count("1") * m.count("2"))
