import sys
import re
from collections import defaultdict

def dfs(graph, visited, src, score):
  visited[src] = True
  if sum(visited.values()) == len(graph):
    visited[src] = False
    return score
  else:
    dists = []
    for (dst, val) in graph[src]:
      if not visited[dst]:
        dists.append(dfs(graph, visited, dst, score + val))
    visited[src] = False
    return max(dists)

def shortest(graph):
  visited = {k: False for k in graph}
  return max(dfs(graph, visited, g, 0) for g in graph.keys())

graph = defaultdict(lambda: set())
for line in sys.stdin:
  src, dst, val = re.match(r"(\w+) to (\w+) = (\d+)", line).groups()
  graph[src].add((dst, int(val)))
  graph[dst].add((src, int(val)))
print(shortest(graph))
