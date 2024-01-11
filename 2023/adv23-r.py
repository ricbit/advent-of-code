import aoc
import itertools
from collections import defaultdict, Counter, deque
import copy
from multiprocessing import Pool
import numpy

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
  sizes = [0] * (max(group_size) + 1)
  for k, v in group_size.items():
    sizes[k] = v
  return graph, sizes, start, end

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
  return {k: list(sorted(v, key=measure)) for k, v in new_graph.items()}

class DFS:
  def __init__(self, graph, sizes, start, end, visited=None, final=None):
    self.graph = graph
    self.sizes = sizes
    self.start = start
    self.end = end
    self.visited = visited if visited is not None else [False] * len(self.sizes)
    self.best = 0
    self.final = final if final is not None else self.populate_final()

  def populate_final(self):
    final = {}
    for g in self.graph[self.end]:
      final[g] = self.end
    for a in list(final.keys()):
      for b in self.graph[a]:
        final[b] = a
    return final

  def search(self):
    self.visited[self.start] = True
    yield from self.dfs_search(self.sizes[self.start], self.start)

  def fast_exit(self, score, pos):
    while pos != self.end:
      score += self.sizes[pos]
      pos = self.final[pos]
    return score + self.sizes[self.end]

  def dfs_search(self, score, pos):
    maxscore = 0
    for new_pos in self.graph[pos]:
      if new_pos in self.final:
        maxscore = max(maxscore, self.fast_exit(score, new_pos))
        continue
      if not self.visited[new_pos]:
        self.visited[new_pos] = True
        d = self.dfs_search(score + self.sizes[new_pos], new_pos)
        self.visited[new_pos] = False
        maxscore = max(maxscore, d)
    return maxscore

  def dfs_shallow(self, score, pos, steps):
    if steps == 15:
      clone = DFS(self.graph, self.sizes, self.start, self.end, self.visited[:])
      yield (score, pos, clone)
      return
    for new_pos in self.graph[pos]:
      if not self.visited[new_pos]:
        removed = []
        for g in self.graph[pos]:
          if not self.visited[g]:
            self.visited[g] = True
            removed.append(g)
        yield from self.dfs_shallow(score + self.sizes[new_pos], new_pos, steps + 1)
        for node in removed:
          self.visited[node] = False

  def shallow_search(self):
    self.visited[self.start] = True
    maxscore = 0
    paths = self.dfs_shallow(self.sizes[self.start], self.start, 0)
    with Pool(8) as p:
      maxscore = max(p.starmap(dfs_deep, paths))
    return maxscore

def dfs_deep(score, pos, g):
  return g.dfs_search(score, pos)

def draw_graph(graph, path):
  print("graph x {")
  for k in path:
    print(f"v{k} [shape=doublecircle]")
  for k, v in graph.items():
    for vv in v:
      if k < vv:
        print(f"v{k} -- v{vv};")
  print("} ")

def maxplus(graph):
  k = max(graph.keys())
  a = numpy.zeros((k, k))
  a += numpy.inf
  print(a)
  return 0


t = aoc.Table.read()
groups = build_groups(t)
graph, sizes, start, end = build_graph(t, groups)
graph = collapse(graph, sizes)
#for k, v in graph.items():
#  print(k, sizes[k], sum(sizes[n] for n in v), [(j, sizes[j]) for j in v])
#draw_graph(graph)
#d = DFS(graph, sizes, start, end)
#print(d.shallow_search())
print(maxplus(graph, sizes))
