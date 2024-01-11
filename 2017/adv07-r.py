import sys
import aoc
from collections import deque

def toposort(graph):
  front = deque([k for k, v in graph.items() if not v[1]])
  count = {k: len(v[1]) for k, v in graph.items()}
  reverse = {d: src for src, (_, dst) in graph.items() for d in dst}
  while front:
    yield (src := front.popleft())
    dst = reverse.get(src, None)
    if dst is not None:
      count[dst] -= 1
      if not count[dst]:
        front.append(dst)

def check(graph):
  weight = {}
  for node in toposort(graph):
    if not graph[node][1]:
      weight[node] = graph[node][0]
    else:
      sons = [weight[s] for s in graph[node][1]]
      if len(set(sons)) != 1:
        return False
      weight[node] = graph[node][0] + sum(sons)
  return True

def weight(graph, src):
  if not graph[src][1]:
    return graph[src][0]
  return graph[src][0] + sum(weight(graph, i) for i in graph[src][1])

def fix(graph, reverse, wrong):
  if (top := reverse[wrong]) is None:
    return None
  sons = [weight(graph, i) for i in graph[top][1]]
  values = set(sons)
  if len(values) == 1:
    return None
  for value in values:
    fixed_value = value - sum(weight(graph, i) for i in graph[wrong][1])
    saved_value = graph[wrong][0]
    graph[wrong] = (fixed_value, graph[wrong][1])
    worked = check(graph)
    graph[wrong] = (saved_value, graph[wrong][1])
    if worked:
      return fixed_value

def find(graph):
  reverse = {d: src for src, (_, dst) in graph.items() for d in dst}
  for wrong in graph:
    if (value := fix(graph, reverse, wrong)) is not None:
      return value

lines = [line.strip() for line in sys.stdin]
graph = {}
for line in lines:
  q = aoc.retuple("src cost_ dst", r"(\w+) \((\d+)\)(?: -> (.*))?", line)
  if q.dst is not None:
    graph[q.src] = (q.cost, q.dst.split(", "))
  else:
    graph[q.src] = (q.cost, [])
aoc.cprint(list(toposort(graph))[-1])
aoc.cprint(find(graph))
