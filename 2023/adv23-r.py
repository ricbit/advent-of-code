import sys
import aoc
import itertools
from collections import *
import copy

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
  start = t[0][1]
  end = t[-1][-2]
  return graph, group_size, start, end

def collapse(graph, sizes):
  new_graph = copy.deepcopy(graph)
  for v1, v2 in itertools.combinations(graph.keys(), 2):
    if len(graph[v1]) == 2 and len(graph[v2]) == 2 and v1 in graph[v2]:
      b = [v for v in graph[v2] if v not in graph[v1] and v != v1][0]
      new_graph[v1].remove(v2)
      new_graph[v1].add(b)
      new_graph[b].remove(v2)
      new_graph[b].add(v1)
      del new_graph[v2]
      sizes[v1] += sizes[v2]
  measure = lambda n: -sizes[n]
  return {k:list(sorted(v, key=measure)) for k, v in new_graph.items()}

class DFS:
  def __init__(self, graph, sizes, start, end):
    self.graph = graph
    self.sizes = sizes
    self.start = start
    self.end = end
    self.visited = set()
    self.best = 0
    self.path = []

  def search(self):
    self.visited.add(self.start)
    return self.dfs_search(self.sizes[self.start], self.start,
      sum(self.sizes) - self.sizes[self.start])

  def remove(self, pos, new_pos):
    removed = [new_pos]
    self.visited.add(new_pos)
    candidates = [pos]
    while candidates:
      base = candidates.pop()
      for node in self.graph[base]:
        if node not in self.visited and node != new_pos:
          if len([n for n in self.graph[node] if n not in self.visited]) == 1:
            removed.append(node)
            self.visited.add(node)
            candidates.append(node)
    return removed

  def dfs_search(self, score, pos, left):
    maxscore = 0
    for new_pos in self.graph[pos]:
      if new_pos == self.end:
        maxscore = max(maxscore, score + self.sizes[self.end])
        if maxscore > self.best:
          self.best = maxscore
          print(self.best - 1, left, self.path)
        break
      if new_pos not in self.visited:
        removed = self.remove(pos, new_pos)
        remlen = sum(sizes[n] for n in removed)
        self.path.append((new_pos, remlen, removed))
        d = self.dfs_search(score + sizes[new_pos], new_pos, left - remlen)
        self.path.pop()
        for node in removed:
          self.visited.remove(node)
        maxscore = max(maxscore, d)
    return maxscore

def draw_graph(graph):
  print("graph x {")
  for k, v in graph.items():
    for vv in v:
      if k < vv:
        print(f"v{k} -- v{vv};")
  print("} ")

t = aoc.Table.read()
groups = build_groups(t)
graph, sizes, start, end = build_graph(t, groups)
graph = collapse(graph, sizes)
for k, v in graph.items():
  print(k, sizes[k], sum(sizes[n] for n in v), [(j,sizes[j]) for j in v])
#draw_graph(graph)
#d = DFS(graph, sizes, start, end)
#print(d.search())

