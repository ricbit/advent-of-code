import sys
import string
import re
import itertools
import math
import cmath
import aoc
import heapq
import functools
import copy
from collections import Counter, deque
from dataclasses import dataclass
import networkx as nx

def solve(data):
  bits, ops = data
  nodes = aoc.retuple_read("node bit_", r"(\w+): (\d+)", bits)
  nodes = {n.node: n.bit for n in nodes}
  ops = aoc.retuple_read("b1 op b2 b3", r"(\w+) (\w+) (\w+) -> (\w+)", ops)
  print(nodes, ops)
  g = nx.DiGraph()
  for op in ops:
    g.add_edge(op.b3, op.b2)
    g.add_edge(op.b3, op.b1)
  values = {}
  for node in reversed(list(nx.topological_sort(g))):
    if node in nodes:
      values[node] = nodes[node]
    else:
      for op in ops:
        if op.b3 == node:
          a = values[op.b1]
          b = values[op.b2]
          match op.op:
            case "AND":
              c = a & b
            case "OR":
              c = a | b
            case "XOR":
              c = a ^ b
          values[op.b3] = c
  zs = {int(k[1:]):v for k, v in values.items() if k.startswith("z")}
    
  print(values)
  print(zs)
  vs = [zs[k] for k in sorted(zs.keys(), reverse=True)]
  print(vs)
  return int("".join(str(v) for v in vs), 2)

data = aoc.line_blocks()
aoc.cprint(solve(data))
