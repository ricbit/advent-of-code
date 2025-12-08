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
  for p in points:
    g.add_node(p)
  pos = 0
  while True:
    v, p1, p2 = race[pos]
    pos += 1
    g.add_edge(p1, p2)
    print(p1, p2)
    if nx.is_connected(g):
      print(g)
      break
  return p1[0] * p2[0]


data = sys.stdin.readlines()
data = [tuple(map(int, line.split(","))) for line in data]
print(data)
aoc.cprint(solve(data))
