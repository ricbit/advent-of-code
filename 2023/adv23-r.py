import sys
import re
import itertools
import math
import aoc
from collections import *
import copy
import heapq
import mip

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
  vnext = [(-sizes[start], start, 1 << start)]
  maxscore = 0
  while vnext:
    score, cur, visited = heapq.heappop(vnext)
    if cur == end:
      if maxscore < -score - 1:
        maxscore = -score - 1
        continue
    for new_pos in graph[cur]:
      if ((1 << new_pos) & visited) > 0:
        continue
      new_visited = visited + (1 << new_pos)
      heapq.heappush(vnext,(score - sizes[new_pos], new_pos, new_visited))
  return maxscore

def dfs_search(graph, sizes, score, pos, end, visited):
  maxscore = 0
  for new_pos in graph[pos]:
    if new_pos == end:
      #print(visited)
      return score + sizes[end] - 1
    if new_pos not in visited:
      visited.add(new_pos)
      d = dfs_search(graph, sizes, score + sizes[new_pos], new_pos, end, visited)
      visited.remove(new_pos)
      maxscore = max(maxscore, d)
  return maxscore

def dfs(graph, sizes, start, end):
  return dfs_search(graph, sizes, sizes[start], start, end, set([start]))

def mip_solve(graph, sizes, start, end):
  model = mip.Model(sense=mip.MAXIMIZE)
  model.verbose = 1
  nodes = len(graph)
  paths = {}
  for name in graph:
    paths[name] = [model.add_var(var_type=mip.BINARY, 
        name="g%s_%03d" % (name, i)) for i in range(nodes)] 
  # maximize the distance
  pairs = itertools.product(graph.keys(), range(nodes))
  product = (paths[name][i] * sizes[name] for name, i in pairs)
  model.objective = mip.maximize(mip.xsum(product))
  # only one path at each position
  for name in graph:
    model += mip.xsum(paths[name][i] for i in range(nodes)) <= 1
  # only one path at each time
  for i in range(nodes):
    model += mip.xsum(paths[name][i] for name in graph) <= 1
  # start must be first
  model += paths[start][0] == 1
  for i in range(1, nodes):
    model += paths[start][i] == 0
  # no paths after end
  for i in range(1, nodes - 1):
    model += (paths[end][i] * nodes * nodes + 
        mip.xsum(paths[name][j] for name in graph for j in range(i + 1, nodes))
        <= nodes * nodes)
  # all positions filled in before end
  for i in range(1, nodes - 1):
    for j in range(i):
      model += -1 * paths[end][i] + mip.xsum(paths[name][j] for name in graph) >= 0
  # only connected paths
  for name1, name2 in itertools.product(graph, repeat=2):
    for i in range(nodes - 1):
      if name1 != name2 and name2 not in graph[name1]:
        model += paths[name1][i] + paths[name2][i + 1] <= 1
  model.max_solutions = 3
  status = model.optimize()
  solution = [var.name for var in model.vars if var.x > 0.5]
  solution.sort(key=lambda v: v.split("_")[1])
  print(solution)
  model.write("mip.lp")
  return model.objective_value

t = aoc.Table.read()
groups = build_groups(t)
graph, sizes, start, end = build_graph(t, groups)
print(dfs(graph, sizes, start, end))

