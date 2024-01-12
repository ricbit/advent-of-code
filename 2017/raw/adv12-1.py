import sys
import re
import itertools
import math
import aoc
import heapq
import functools
import copy
from collections import *
from dataclasses import dataclass

def walk(graph, start):
  vnext = [start]
  visited = set()
  while vnext:
    q = vnext.pop()
    if q in visited:
      continue
    visited.add(q)
    for d in graph[q]:
      if d not in visited:
        vnext.append(d)
  return len(visited)



graph = aoc.ddict(lambda: set())
lines = [line.strip() for line in sys.stdin]
for line in lines:
  q = aoc.retuple("src_ dst", r"(\d+) <-> (.*)", line)
  for d in q.dst.split(", "):
    d = int(d)
    graph[d].add(q.src)
    graph[q.src].add(d)
aoc.cprint(walk(graph, 0))
