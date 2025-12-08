import sys
import networkx as nx
import string
import re
import itertools
import math
import cmath
import aoc
import heapq
import functools
import copy
from collections import Counter, deque
from dataclasses import dataclass

def distance(p1, p2):
  return sum((a - b) ** 2 for a, b in zip(p1, p2)) ** 0.5

def find_min(dist):
  mindist = 1e17
  for (p1, p2), v in dist.items():
    if v < mindist:
      mindist = v
      start = (p1, p2)
  del dist[start]
  return (start, mindist)

def solve(points):
  dist = {}
  for p1, p2 in itertools.combinations(points, 2):
    dist[(p1, p2)] = distance(p1, p2)
  race = []
  for p1, p2 in itertools.combinations(points, 2):
    race.append((distance(p1, p2), p1, p2))
  race.sort()
  g = nx.Graph()
  for v, p1, p2 in race[:1000]:
    g.add_edge(p1, p2)
  x = [len(k) for k in nx.connected_components(g)]
  x.sort(reverse=True)
  return math.prod(x[:3])


  x = ([len(x) for x in circuits])
  x.sort(reverse=True)
  for c in circuits:
    print(c)
  return math.prod(x[:3])

data = sys.stdin.readlines()
data = [tuple(map(int, line.split(","))) for line in data]
print(data)
aoc.cprint(solve(data))
