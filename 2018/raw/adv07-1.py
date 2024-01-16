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

def solve(graph, keys):
  inv = aoc.ddict(lambda: set())
  for k, v in graph.items():
    for vv in v:
      inv[vv].add(k)
  front = set(k for k in keys if len(inv[k]) == 0)
  visited = set()
  order = []
  while front:
    x = aoc.first(sorted(front))
    front.remove(x)
    visited.add(x)
    order.append(x)
    for dst in graph[x]:
      if dst not in visited and all(x in visited for x in inv[dst]):
        front.add(dst)
  return "".join(order)

data = [line.strip() for line in sys.stdin]
graph = aoc.ddict(lambda: set())
keys = set()
for line in data:
  q = aoc.retuple("src dst", r".*?tep (.).*? step (.)", line)
  graph[q.src].add(q.dst)
  keys.add(q.src)
  keys.add(q.dst)
aoc.cprint(solve(graph, keys))
