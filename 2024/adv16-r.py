import aoc
import networkx as nx

def build_graph(t):
  sy, sx = t.find("S")
  ey, ex = t.find("E")
  t[sy][sx] = "."
  t[ey][ex] = "."
  empty = lambda x: x == "."
  g = nx.DiGraph()
  for y, x in t.iter_all(conditional = empty):
    pos = y * 1j + x
    for pdir in [1, -1, 1j, -1j]:
      for turn in [1j, -1j]:
        g.add_edge((pos, pdir), (pos, pdir * turn), weight=1000)
      if empty(t.get(pos + pdir)):
        g.add_edge((pos, pdir), (pos + pdir, pdir), weight=1)
  for pdir in [1, -1, 1j, -1j]:
    g.add_edge((ey * 1j + ex, pdir), "goal", weight=0)
  g.add_edge("start", (sy * 1j + sx, 1), weight = 0)
  return g

def part1(g):
  path = nx.shortest_path(g, "start", "goal", "weight")
  ans = 0
  for a, b in zip(path, path[1:]):
    if a[0] == b[0]:
      ans += 1000
    else:
      ans += 1
  return ans - 2

def part2(g):
  paths = nx.all_shortest_paths(g, "start", "goal", "weight")
  p2 = set()
  for path in paths:
    p2.update(node[0] for node in path)
  return len(p2) - 2

data = aoc.Table.read()
graph = build_graph(data)
aoc.cprint(part1(graph))
aoc.cprint(part2(graph))
