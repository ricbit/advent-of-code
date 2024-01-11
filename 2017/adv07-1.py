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

def root(graph):  
  visited = aoc.ddict(lambda: False)
  while True:
    c = 0
    for src, dst in graph.items():
      if not dst:
        visited[src] = True
        c += 1
      else:
        if all(visited[d] for d in dst):
          if not visited[src]:
            last = src
          visited[src] = True
          c += 1
    if c == len(graph):
      return last


lines = [line.strip() for line in sys.stdin]
graph = {}
for line in lines:
  q = aoc.retuple("src cost_ dst", r"(\w+) \((\d+)\)(?: -> (.*))?", line)
  graph[q.src] = []
  if q.dst is not None:
    graph[q.src].extend(q.dst.split(", "))
print(graph)
aoc.cprint(root(graph))
