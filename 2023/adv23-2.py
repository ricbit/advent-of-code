import sys
import re
import itertools
import math
import aoc
from collections import *
import copy
import heapq

EMPTY = ".v^<>"

def count(t, y, x):
  ans = 0
  for j, i in t.iter_neigh4(y, x):
    if t[j][i] in EMPTY:
      ans += 1
  return ans

def build_groups(t):
  vnext = [(0, 0, 1, set())]
  groups = {}
  visited = set()
  last_name = 0
  while vnext:
    name, y, x, group = vnext.pop()
    groups[name] = group
    for j, i in t.iter_neigh4(y, x):
      if (j, i) in visited or t[j][i] == "#":
        continue
      if count(t, j, i) <= 2 and count(t, y, x) <= 2:
        visited.add((j, i))
        group.add((j, i))
        vnext.append((name, j, i, group))
      else: 
        group = set([(j, i)])
        visited.add((j, i))
        vnext.append((last_name + 1, j, i, group))
        last_name += 1
  return groups

def build_graph(t, groups): 
  for name, group in groups.items():
    #name = chr(ord('a') + name)
    for j, i in group:
      t[j][i] = name
  graph = defaultdict(lambda: set())
  group_size = Counter()
  for y, x in t.iter_all():
    if t[y][x] == "#":
      continue
    group_size[t[y][x]] += 1
    for j, i in t.iter_neigh4(y, x):
      if t[j][i] != "#" and t[j][i] != t[y][x]:
        graph[t[y][x]].add(t[j][i])
  #print("\n".join("".join(row) for row in t.table))
  #for k, v in graph.items():
  #  print(k, v, group_size[k])
  start = t[0][1]
  end = t[-1][-2]
  #print(start, end)
  return graph, group_size, start, end

def search(graph, sizes, start, end):
  vnext = [(-sizes[start], start, set([start]))]
  paths = []
  maxscore = 0
  while vnext:
    score, cur, visited = heapq.heappop(vnext)
    if cur == end:
      paths.append(score)
      maxscore = max(maxscore, -score-1)
      print(maxscore,visited)
      continue
    for new_pos in graph[cur]:
      if new_pos in visited:
        continue
      new_visited = visited.copy()
      new_visited.add(new_pos)
      heapq.heappush(vnext,(score - sizes[new_pos], new_pos, new_visited))
  return max(paths) - 1

t = aoc.Table.read()
groups = build_groups(t)
graph, sizes, start, end = build_graph(t, groups)
print(search(graph, sizes, start, end))

