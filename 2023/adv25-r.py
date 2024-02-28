import sys
import random
import aoc
import networkx as nx

def read_graph():
  graph = nx.Graph()
  nodes = set()
  for line in sys.stdin:
    a, links = line.strip().split(":")
    nodes.add(a)
    for b in links.split():
      nodes.add(b)
      graph.add_edge(a, b, capacity=1)
  return graph, list(nodes)

def find_mincut(graph, nodes):
  while True:
    a, b = random.sample(nodes, 2)
    cut, (x, y) = nx.minimum_cut(graph, a, b)
    if len(x) != 1 and len(y) != 1:
      return len(x) * len(y)

graph, nodes = read_graph()
aoc.cprint(find_mincut(graph, nodes))
