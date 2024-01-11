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

def check(graph):  
  visited = aoc.ddict(lambda: False)
  while True:
    c = 0
    for src, (cost, dst) in graph.items():
      if not dst:
        visited[src] = True
        c += 1
      else:
        if all(visited[d] for d in dst):
          if len(set(weight(graph, i) for i in dst)) != 1:
            return False
          visited[src] = True
          c += 1
    if c == len(graph):
      return True

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

def parent(graph, wrong):
  for src, (cost, dst) in graph.items():
    if wrong in dst:
      return src
  return None

def weight(graph, src):
  if not graph[src][1]:
    return graph[src][0]
  return graph[src][0] + sum(weight(graph, i) for i in graph[src][1])

def fix(graph, wrong):
  top = parent(graph, wrong)
  if top is None:
    return False
  sons = [weight(graph, i) for i in graph[top][1]]
  if all(a == b for a,b in itertools.combinations(sons, 2)):
    return None
  values = set(sons)
  for v in values:
    vv = v - sum(weight(graph, i) for i in graph[wrong][1])
    graph[wrong] = (vv, graph[wrong][1])
    if check(graph):
      return graph[wrong][0]
  #nsons = [weight(graph, i) for i in graph[top][1]]
  #return all(a == b for a,b in itertools.combinations(nsons, 2))

def find(graph):
  for wrong in graph:
    print(f"-- {wrong}")
    if not graph[wrong][1]:
      continue
    g = copy.deepcopy(graph)
    if (a := fix(g, wrong)) is not None:
      return a

lines = [line.strip() for line in sys.stdin]
graph = {}
for line in lines:
  q = aoc.retuple("src cost_ dst", r"(\w+) \((\d+)\)(?: -> (.*))?", line)
  if q.dst is not None:
    graph[q.src] = (q.cost, q.dst.split(", "))
  else:
    graph[q.src] = (q.cost, [])
aoc.cprint(str(find(graph)))
