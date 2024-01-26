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
  graph = aoc.ddict(lambda: set())
  for q in data:
    graph[q.src].add(q.dst)
  inv = aoc.invert(graph)
  count = Counter()
  keys = graph.keys()
  count = {k: 0 for k in keys}
  for k, v in inv.items():
    count[k] = len(v)
  frontier = deque()
  for k, v in count.items():
    if not v:
      frontier.append((k, 0))
  ans = 0
  while frontier:
    k, value = frontier.popleft()
    ans += value
    for v in graph[k]:
      frontier.append((v, value + 1))
  return ans

data = aoc.retuple_read("src dst", r"^(\w+)\)(\w+)$", sys.stdin)
aoc.cprint(solve(data))
