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
  tick = {}
  maxworkers = 5
  fsize = 60
  for w in itertools.count(0):
    print(w, front, tick)
    finished = [worker for worker, time in tick.items() if time == 0]
    for worker in sorted(finished):
      visited.add(worker)
      del tick[worker]
      order.append(worker)
      for nworker in graph[worker]:
        if nworker not in visited and all(k in visited for k in inv[nworker]):
          front.add(nworker)
    while len(tick) < maxworkers and front:
      worker = aoc.first(sorted(front))
      tick[worker] = fsize + ord(worker) - ord('A') + 1
      front.remove(worker)
    for worker in tick:
      tick[worker] -= 1
    if not front and not tick:
      return w

data = [line.strip() for line in sys.stdin]
graph = aoc.ddict(lambda: set())
keys = set()
for line in data:
  q = aoc.retuple("src dst", r".*?tep (.).*? step (.)", line)
  graph[q.src].add(q.dst)
  keys.add(q.src)
  keys.add(q.dst)
aoc.cprint(solve(graph, keys))
