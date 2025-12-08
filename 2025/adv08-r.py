import sys
import math
import aoc
import networkx as nx

def get_distances(points):
  dist = []
  points.sort()
  for p1 in range(len(points)):
    for p2 in range(p1 + 1, min(len(points), p1 + 200)):
      dist.append((math.dist(points[p1], points[p2]), p1, p2))
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
  uf = nx.utils.UnionFind(range(len(points)))
  for v, p1, p2 in dist:
    uf.union(p1, p2)
    if uf.weights[uf.parents[p1]] == len(points):
      return points[p1][0] * points[p2][0]

data = sys.stdin.readlines()
points = [tuple(map(int, line.split(","))) for line in data]
dist = get_distances(points)
aoc.cprint(part1(points, dist))
aoc.cprint(part2(points, dist))
