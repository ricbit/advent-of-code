import sys
import aoc

def single_component(graph, visited, nodes, start):
  vnext = [start]
  before = len(nodes)
  while vnext:
    q = vnext.pop()
    if q in visited:
      continue
    visited.add(q)
    nodes.remove(q)
    for d in graph[q]:
      if d not in visited:
        vnext.append(d)
  return before - len(nodes)

def all_components(graph):
  nodes = set(graph.keys())
  visited = set()
  while nodes:
    yield single_component(graph, visited, nodes, aoc.first(nodes))

graph = aoc.ddict(lambda: set())
lines = [line.strip() for line in sys.stdin]
for line in lines:
  q = aoc.retuple("src_ dst", r"(\d+) <-> (.*)", line)
  for d in q.dst.split(", "):
    d = int(d)
    graph[d].add(q.src)
    graph[q.src].add(d)
aoc.cprint(single_component(graph, set(), set(graph.keys()), 0))
aoc.cprint(len(list(all_components(graph))))
