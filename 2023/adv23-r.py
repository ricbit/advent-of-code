import sys
import aoc
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

class DFS:
  def __init__(self, graph, sizes, start, end):
    self.graph = graph
    self.sizes = sizes
    self.start = start
    self.end = end
    self.visited = set()

  def search(self):
    self.visited.add(self.start)
    left = sum(self.sizes) - self.sizes[self.start]
    self.available = copy.deepcopy(graph)
    return self.dfs_search(self.sizes[self.start], self.start, left)

  def remove(self, start, chosen):
    for node in self.graph[start]:
      if node != chosen:
        self.available[node].remove(start)

  def reinsert(self, start, chosen):
    for node in self.graph[start]:
      if node != chosen:
        self.available[node].add(start)

  def dfs_search(self, score, pos, left):
    maxscore = 0
    for new_pos in self.available[pos]:
      if new_pos == self.end:
        maxscore = max(maxscore, score + self.sizes[self.end] - 1)
        continue
      if new_pos not in self.visited:
        self.visited.add(new_pos)
        self.remove(pos, new_pos)
        d = self.dfs_search(score + sizes[new_pos], new_pos, left - sizes[new_pos])
        self.reinsert(pos, new_pos)
        self.visited.remove(new_pos)
        maxscore = max(maxscore, d)
    return maxscore

t = aoc.Table.read()
groups = build_groups(t)
graph, sizes, start, end = build_graph(t, groups)
d = DFS(graph, sizes, start, end)
print(d.search())

