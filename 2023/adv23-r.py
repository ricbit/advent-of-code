import aoc
import itertools
from collections import defaultdict, Counter
import copy

EMPTY = ".v^<>"

def direct_search(t):
  vnext = [(0, 0, 1, set())]
  paths = []
  while vnext:
    score, y, x, visited = vnext.pop(0)
    for j, i in t.iter_neigh4(y, x):
      if (j, i) in visited:
        continue
      if (j, i) == (t.h - 1, t.w - 2):
        paths.append(1 + len(visited))
        continue
      dj = j - y
      di = i - x
      if t[j][i] in ".v^<>" and (t[y][x] == "." or
          (t[y][x] == ">" and di == 1 and dj == 0) or
          (t[y][x] == "<" and di == -1 and dj == 0) or
          (t[y][x] == "^" and di == 0 and dj == -1) or
          (t[y][x] == "v" and di == 0 and dj == 1)):
        visited2 = visited.copy()
        visited2.add((j, i))
        vnext.append((score + 1, j, i, visited2))
  return max(paths)

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
  return {k: list(sorted(v, key=measure)) for k, v in new_graph.items()}

class DFS:
  def __init__(self, graph, sizes, start, end):
    self.graph = graph
    self.sizes = [0] * (max(sizes) + 1)
    for k, v in sizes.items():
      self.sizes[k] = v
    self.start = start
    self.end = end
    self.visited = [False] * len(self.sizes)
    self.used = [False] * len(self.sizes)
    self.best = 0
    self.path = []
    self.best_path = []

  def search(self):
    self.visited[self.start] = True
    self.used[self.start] = True
    left = sum(self.sizes) - self.sizes[self.start]
    return self.dfs_search(self.sizes[self.start], self.start, left)

  def dfs_search(self, score, pos, left):
    maxscore = 0
    if score + left < self.best:
      return 0
    for new_pos in self.graph[pos]:
      if new_pos == self.end:
        maxscore = max(maxscore, score + self.sizes[self.end])
        if maxscore > self.best:
          self.best = maxscore
          self.best_path = self.path[:]
        break
      if not self.visited[new_pos]:
        self.visited[new_pos] = True
        remlen = 0
        self.path.append(new_pos)
        d = self.dfs_search(score + self.sizes[new_pos], new_pos, left - remlen)
        self.visited[new_pos] = False
        self.path.pop()
        maxscore = max(maxscore, d)
    return maxscore

t = aoc.Table.read()
aoc.cprint(direct_search(t))
groups = build_groups(t)
graph, sizes, start, end = build_graph(t, groups)
graph = collapse(graph, sizes)
d = DFS(graph, sizes, start, end)
aoc.cprint(d.search() - 1)
