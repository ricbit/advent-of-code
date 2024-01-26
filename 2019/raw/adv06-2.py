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
      frontier.append((k, []))
  bigmap = {}
  while frontier:
    k, path = frontier.popleft()
    bigmap[k] = path
    for v in graph[k]:
      frontier.append((v, path + [k]))
  m = set(bigmap["YOU"]).intersection(set(bigmap["SAN"]))
  print(m)
  lca = max(m, key = lambda x: len(bigmap[x]))
  print(lca)
  a = len(bigmap["YOU"]) - bigmap["YOU"].index(lca)
  b = len(bigmap["SAN"]) - bigmap["SAN"].index(lca)
  return a + b - 2

data = aoc.retuple_read("src dst", r"^(\w+)\)(\w+)$", sys.stdin)
aoc.cprint(solve(data))
