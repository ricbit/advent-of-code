import sys
import re
import aoc

def dfs(graph, visited, src, score, choose):
  visited[src] = True
  if sum(visited.values()) == len(graph):
    visited[src] = False
    return score
  dists = []
  for (dst, val) in graph[src]:
    if not visited[dst]:
      dists.append(dfs(graph, visited, dst, score + val, choose))
  visited[src] = False
  return choose(dists)

def walk(graph, choose):
  visited = {k: False for k in graph}
  return choose(dfs(graph, visited, g, 0, choose) for g in graph.keys())

graph = aoc.ddict(lambda: set())
for line in sys.stdin:
  src, dst, val = re.match(r"(\w+) to (\w+) = (\d+)", line).groups()
  graph[src].add((dst, int(val)))
  graph[dst].add((src, int(val)))
aoc.cprint(walk(graph, min))
aoc.cprint(walk(graph, max))
