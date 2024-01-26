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

def get(layers, y, x):
  for layer in layers:
    c = layer[y * 25 + x]
    if c != "2":
      return "." if c == "0" else "#"
  return "0"

data = sys.stdin.read().strip()
layers = []
size = 25 * 6
for i in range(len(data) // size):
  layers.append(data[size * i : size * i + size])
m = min(layers, key=lambda x:x.count("0"))
aoc.cprint(m.count("1") * m.count("2"))
base = [[0] * 25 for _ in range(6)]
for j in range(6):
  line = []
  for i in range(25):
    line.append(get(layers, j, i))
  print("".join(line))
