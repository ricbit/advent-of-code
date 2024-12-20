import sys
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
import networkx as nx

def printgrid(t, path):
  for j, line in enumerate(t.table):
    out = []
    for i, x in enumerate(line):
      if (j, i) in path:
        out += ["O"]
      else:
        out += t[j][i]
    print("".join(out))
  print()

def solve(t):
  g = nx.Graph()
  sy, sx = t.find("S")
  ey, ex = t.find("E")
  t[sy][sx] = "."
  t[ey][ex] = "."
  valid = set()
  for y, x in t.iter_all():
    if t[y][x] == ".":
      valid.add((y, x))
      for j, i in t.iter_neigh4(y, x):
        if t[j][i] == ".":
          g.add_edge((j, i), (y, x))
  total = 0
  baseline_path = nx.shortest_path(g, (sy, sx), (ey, ex))
  #baseline = len(baseline_path)
  g = nx.DiGraph()
  for a, b in zip(baseline_path, baseline_path[1:]):
    g.add_edge(a, b)
  #visiteid = set()
  hist = Counter()
  distance = {}
  for i, p in enumerate(baseline_path):
    distance[p] = i
  for y, x in t.iter_all(conditional=lambda x: x=="."):
    for j, i in t.iter_all(conditional=lambda x: x=="."):
      d = abs(j-y) + abs(i-x)
      if d <= 1 or d > 20:
        continue
      #path=[(y, x), (j, i)]
      #path.sort()
      #path = tuple(path)
      #if path in visited:
      #  continue
      #visited.add(path)
      #g.add_edge((j, i), (y, x))
      #g.add_edge((y, x), (j, i))
      #p = nx.shortest_path(g, (sy, sx), (ey, ex))
      #k = len(p)
      save = distance[(j,i)] - distance[(y,x)]
      if save <= 0:
        continue
      save -= d
      print((j,i), (y,x),save)
      if save > 100 - 2: 
        #print(y,x,baseline - k - d)
        hist[save] += 1
        #printgrid(t,p)
        total += 1
      #g.remove_edge((j, i), (y, x))
      #g.remove_edge((y, x), (j, i))
  for s in sorted(hist.keys()):
    print(s+ 1,hist[s])
  return total

data = aoc.Table.read()
aoc.cprint(solve(data))
