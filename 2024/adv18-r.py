import sys
import bisect
import itertools
import aoc
import networkx as nx

DIM = 71

def build_grid(data, limit): # limit is inclusive
  grid = nx.grid_2d_graph(DIM, DIM)
  for x, y in itertools.islice(data, limit + 1):
    grid.remove_node((x, y))
  return grid

def part1(data):
  grid = build_grid(data, 1023)
  path = nx.shortest_path(grid, (0, 0), (DIM - 1, DIM - 1))
  steps = len(path) - 1
  return steps

def is_blocked(data, limit):
  grid = build_grid(data, limit)
  return not nx.has_path(grid, (0, 0), (DIM - 1, DIM -1))

def part2(data):
  bounds = list(range(len(data)))
  index = bisect.bisect_left(bounds, True, lo=1024, key=lambda x:is_blocked(data, x))
  return ",".join(str(i) for i in data[index])

data = [aoc.ints(x.split(",")) for x in sys.stdin.read().splitlines()]
aoc.cprint(part1(data))
aoc.cprint(part2(data))
