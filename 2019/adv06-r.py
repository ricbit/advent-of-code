import sys
import aoc
from collections import deque

def topo(data):
  graph = aoc.ddict(lambda: set())
  for q in data:
    graph[q.src].add(q.dst)
  src = set(x.src for x in data).difference(set(x.dst for x in data))
  frontier = deque((x, []) for x in src)
  bigmap = {}
  while frontier:
    k, path = frontier.popleft()
    bigmap[k] = path
    for v in graph[k]:
      frontier.append((v, path + [k]))
  return bigmap

def part1(data):
  bigmap = topo(data)
  return sum(len(x) for x in bigmap.values())

def part2(data):
  src = "YOU"
  dst = "SAN"
  bigmap = topo(data)
  middle = set(bigmap[src]).intersection(set(bigmap[dst]))
  lca = max(middle, key = lambda x: len(bigmap[x]))
  a = len(bigmap[src]) - bigmap[src].index(lca)
  b = len(bigmap[dst]) - bigmap[dst].index(lca)
  return a + b - 2

data = aoc.retuple_read("src dst", r"^(\w+)\)(\w+)$", sys.stdin)
aoc.cprint(part1(data))
aoc.cprint(part2(data))
