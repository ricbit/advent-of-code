import itertools
import aoc
import networkx as nx

def solve(data):
  g = nx.Graph()
  for edge in data:
    g.add_edge(edge.src, edge.dst)
  unique = set()
  big = set()
  valid = lambda clique: any(x.startswith("t") for x in clique)
  for clique in nx.find_cliques(g):
    big.add(",".join(sorted(clique)))
    if len(clique) >= 3 and valid(clique):
      for small in itertools.combinations(clique, 3):
        small = tuple(sorted(small))
        if valid(small):
          unique.add(small)
  return len(unique), max(big, key=lambda x: len(x))

data = aoc.retuple_read("src dst", r"(\w+)-(\w+)")
part1, part2 = solve(data)
aoc.cprint(part1)
aoc.cprint(part2)
