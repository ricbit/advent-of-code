import sys
import itertools
import math
import aoc
import networkx as nx

def distance(points):
  p1, p2 = points
  return math.dist(p1, p2), p1, p2

def get_distances(points):
  dist = list(map(distance, itertools.combinations(points, 2)))
  dist.sort()
  return dist

def part1(points, dist):
  g = nx.Graph()
  for v, p1, p2 in dist[:1000]:
    g.add_edge(p1, p2)
  components = [len(c) for c in nx.connected_components(g)]
  components.sort(reverse=True)
  return math.prod(components[:3])

def part2(points, dist):
  g = nx.Graph()
  for p in points:
    g.add_node(p)
  for v, p1, p2 in dist:
    g.add_edge(p1, p2)
    if nx.is_connected(g):
      break
  return p1[0] * p2[0]

data = sys.stdin.readlines()
points = [tuple(map(int, line.split(","))) for line in data]
dist = get_distances(points)
aoc.cprint(part1(points, dist))
aoc.cprint(part2(points, dist))
