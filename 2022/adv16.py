import more_itertools
import itertools
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

def max_bound(graph, visited, time_left, agents):
  closed = []
  for index, node in enumerate(graph):
    if (1 << index) & visited == 0:
      closed.append(index)
  closed.sort(reverse=True, key=lambda i: graph[i].rate)
  chunked = more_itertools.chunked(closed, agents)
  total = 0
  for chunk, best_case in zip(chunked, tick(time_left)):
    rates = sum(graph[c].rate for c in chunk)
    total += rates * best_case
  return total

def dump(graph, max_rate, rate, opened, pos, time, old_id, new_id):
  opened_list = []
  for node in graph:
    if (1 << node.number) & opened != 0:
      opened_list.append(node.name)
  opened_names = " ".join(opened_list)
  nodes = " ".join(graph[n].name for n in pos)
  params = (new_id, nodes, max_rate, rate, time, opened_names, old_id)
  print("%d: Node [%s], rate %d (%d), time %d, opened [%s] from %d" % params)

def get_start(graph):
  for i, node in enumerate(graph):
    if node.name == "AA":
      return i

def iter_single(graph, opened, node, time):
  mask = 1 << node
  if mask & opened == 0 and graph[node].rate > 0:
    yield (mask, graph[node].rate * (time - 1), node)
  for link in graph[node].links:
    yield (0, 0, link)

def no_repeats(group):
  for a, b in zip(group, group[1:]):
    if a == b:
      return False
  return True

def product(groups):
  if len(groups) == 1:
    yield from ([elem] for elem in groups[0])
  else:
    for elem in groups[0]:
      for tail in product(groups[1:]):
        yield list(itertools.chain([elem], tail))

def canonical_events(chain):
  for group_tuple in product(chain):
    group = list(group_tuple)
    group.sort(key=lambda x: x[2])
    if no_repeats(group):
      yield tuple(group)

def dump_group(graph, group):
  groups = []
  for mask, delta, link  in group:
    groups.append("(%d %d %s)" % (mask, delta, graph[link].name))
  print(" ".join(groups))

def search(graph, agents, limit):
  start = get_start(graph)
  pos = tuple([start] * agents)
  events = [(-max_bound(graph, 0, limit, agents), 0, 0, pos, limit)]
  visited = {}
  minbound = 0
  while events:
    max_rate, rate, opened, pos, time = heapq.heappop(events)
    max_rate, rate = -max_rate, -rate
    if time == 0 or max_rate < minbound:
      continue
    chain = []
    for node in pos:
      chain.append(list(iter_single(graph, opened, node, time)))
    canonical = set(canonical_events(chain))
    for group in canonical:
      new_opened = opened
      next_rate = rate
      new_pos = []
      for mask, delta_rate, link in group:
        new_opened |= mask
        next_rate += delta_rate
        new_pos.append(link)
      new_bound = max_bound(graph, new_opened, time - 1, agents) + next_rate
      if new_bound > minbound:
        if next_rate > visited.get((new_opened, tuple(new_pos)), -1):
          next_node = (
            -new_bound, -next_rate, new_opened, new_pos, time - 1)
          minbound = max(minbound, next_rate)
          heapq.heappush(events, next_node)
          visited[(new_opened, tuple(new_pos))] = next_rate
  return minbound

graph = parse()
print(search(graph, 1, 30))
print(search(graph, 2, 26))
