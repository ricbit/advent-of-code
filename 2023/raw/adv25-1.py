import sys
import re
import itertools
import math
import aoc
import random
from collections import *

graph = defaultdict(lambda: [])
#print("graph x { ")
for line in sys.stdin:
  k, v = line.strip().split(":")
  for vv in v.split():
    graph[k].append(vv)
    graph[vv].append(k)
    #print(f"{k} -- {vv}")
    #graph[vv].add(k)
#print("}")

def contract(graph):
  while len(graph) > 2:
    a = random.choice(list(graph.keys()))
    b = random.choice(graph[a])
    print("a", a,graph[a])
    print("b", b,graph[b])
    graph[a].remove(b)
    for neigh in graph[b]:
      if neigh != a:
        print("neigh", neigh,graph[neigh])
        graph[a].append(neigh)
        graph[neigh].remove(b)
        graph[neigh].append(a)
        print("a",a,graph[a])
        print("neigh",neigh,graph[neigh])
    del graph[b]
    print()
  print(graph)

def search(graph):
  start = "xzn"
  vnext = [start]
  visited = set()
  while vnext:
    node = vnext.pop()
    print(node)
    visited.add(node)
    for v in graph[node]:
      if v not in visited and v not in ["qfj", "qqh", "dsr"]:
        vnext.append(v)
  return len(visited), len(graph) - len(visited)

#a,b = search(graph)
contract(graph)
#print(len(graph),a,b)
#print(a*b)
