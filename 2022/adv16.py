import re
import sys
from dataclasses import dataclass
import heapq

lines = sys.stdin.readlines()

@dataclass(init=False, repr=True)
class Node:
  number: int
  name: str
  rate: int
  links: list[int]

def parse():
  graph = []
  names = {}
  links = []
  for i, line in enumerate(lines):
    valve = re.search(r"Valve (\w+).*rate=(\d+).*valves? (.*)$", line)
    names[valve.group(1)] = i
    node = Node()
    node.number = i
    node.name = valve.group(1)
    node.rate = int(valve.group(2))
    node.links = []
    links.append([link.strip() for link in valve.group(3).strip().split(",")])
    graph.append(node)
  for node, link in zip(graph, links):
    for p in link:
      node.links.append(names[p])
  return graph

def tick(time):
  while time > 0:
    yield time
    time -= 2

def max_bound(graph, visited, time_left):
  closed = []
  for index, node in enumerate(graph):
    if (1 << index) & visited == 0:
      closed.append(index)
  closed.sort(reverse=True, key=lambda i: graph[i].rate)
  total = 0
  for index, best_case in zip(closed, tick(time_left)):
    total += graph[index].rate * best_case
  return total

def dump(graph, max_rate, rate, opened, current_node, time):
  opened_list = []
  for node in graph:
    if (1 << node.number) & opened != 0:
      opened_list.append(node.name)
  opened_names = " ".join(opened_list)
  params = (graph[current_node].name, max_rate, rate, time, opened_names)
  print("Node %s, rate %d (%d), time %d, opened [%s]" % params)

def get_start(graph):
  for i, node in enumerate(graph):
    if node.name == "AA":
      return i

def iter_single(graph, max_rate, rate, opened, node, time):
  mask = 1 << node
  if mask & opened == 0 and graph[node].rate > 0:
    yield (mask, node)
  for link in graph[node].links:
    yield (0, link)

def search(graph, agents):
  limit = 30
  max_rate = max(node.rate for node in graph) * (limit + 1)
  events = []
  start = get_start(graph)
  heapq.heappush(events, (-max_bound(graph, 0, limit), 0, 0, start, limit))
  visited = {}
  minbound = 0
  while events:
    max_rate, rate, opened, node, time = heapq.heappop(events)
    max_rate, rate = -max_rate, -rate
    if time == 0 or max_rate < minbound:
      continue
    dump(graph, max_rate, rate, opened, node, time)
    mask = 1 << node
    # open valve
    if mask & opened == 0 and graph[node].rate > 0:
      new_opened = opened | mask
      next_rate = rate + graph[node].rate * (time - 1)
      new_bound = max_bound(graph, new_opened, time - 1) + next_rate
      if new_bound >= minbound:
        if next_rate > visited.get((new_opened, node), -1):
          next_node = (-new_bound, -next_rate, new_opened, node, time - 1)
          minbound = max(minbound, next_rate)
          heapq.heappush(events, next_node)
          visited[(new_opened, node)] = next_rate
    # move
    new_bound = max_bound(graph, opened, time - 1) + rate
    if new_bound < minbound:
      continue
    for link in graph[node].links:
      if rate > visited.get((opened, link), -1):
        next_node = (-new_bound, -rate, opened, link, time - 1)
        minbound = max(minbound, rate)
        heapq.heappush(events, next_node)
        visited[(opened, link)] = rate
  return minbound

graph = parse()
print(search(graph, 1))
