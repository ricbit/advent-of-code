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
  baseline = len(nx.shortest_path(g, (sy, sx), (ey, ex)))
  for y, x in t.iter_all():
    if t[y][x] == "#" and x != 0 and y != 0 and x != t.w - 1 and y != t.h - 1:
      ans = 0
      for j, i in t.iter_neigh4(y, x):
        if t[j][i] == ".":
          g.add_edge((j, i), (y, x))
          ans += 1
      if ans > 0:
        k = len(nx.shortest_path(g, (sy, sx), (ey, ex)))
        if baseline - k >= 100: 
          print(y,x,baseline - k)
          total += 1
        for j, i in t.iter_neigh4(y, x):
          if t[j][i] == ".":
            g.add_edge((j, i), (y, x))
            ans += 1
        g.remove_node((y, x))


  return total

data = aoc.Table.read()
aoc.cprint(solve(data))
