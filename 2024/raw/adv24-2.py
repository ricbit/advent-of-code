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

def dot(nodes, ops, x, y, brange):
  g = nx.DiGraph()
  print("digraph { ")
  for op in ops:
    name = f"{op.b3}_{op.op}"
    g.add_edge(op.b3, op.b1)
    g.add_edge(op.b3, op.b2)
    print(f"{op.b2} -> {name}")
    print(f"{op.b1} -> {name}")
    print(f"{name} -> {op.b3}")
  print("} ")

def run(nodes, ops, x, y, brange, switch):
  smap = {}
  for a, b in switch:
    smap[a] = b
    smap[b] = a
  newops = []
  for op in ops:
    if op.b3 in smap:
      newops.append({"b1": op.b1, "b2": op.b2, "op": op.op, "b3": smap[op.b3]})
    else:
      newops.append({"b1": op.b1, "b2": op.b2, "op": op.op, "b3": op.b3})
  g = nx.DiGraph()
  for op in newops:
    g.add_edge(op["b3"], op["b1"])
    g.add_edge(op["b3"], op["b2"])
  values = {}
  bx = list(reversed("0" * brange + bin(x)[2:]))[:brange]
  by = list(reversed("0" * brange + bin(y)[2:]))[:brange]
  print("".join(str(d % 10) for d in reversed(range(46))))
  print("".join(["0"]+bx[::-1]))
  print("".join(["0"]+by[::-1]))
  for i in range(brange):
    nodes["x%02d" % i] = int(bx[i])
    nodes["y%02d" % i] = int(by[i])
  for node in reversed(list(nx.topological_sort(g))):
    if node in nodes:
      values[node] = nodes[node]
    else:
      for op in newops:
        if op["b3"] == node:
          a = values[op["b1"]]
          b = values[op["b2"]]
          match op["op"]:
            case "AND":
              c = a & b
            case "OR":
              c = a | b
            case "XOR":
              c = a ^ b
          values[op["b3"]] = c
  zs = {int(k[1:]):v for k, v in values.items() if k.startswith("z")}  
  vs = [zs[k] for k in sorted(zs.keys(), reverse=True)]
  print("".join(list(str(v) for v in vs)))
  print()
  #print()

def solve(data):
  bits, ops = data
  nodes = aoc.retuple_read("node bit_", r"(\w+): (\d+)", bits)
  nodes = {n.node: n.bit for n in nodes}
  ops = aoc.retuple_read("b1 op b2 b3", r"(\w+) (\w+) (\w+) -> (\w+)", ops)
  #print(len(ops))
  brange = 45
  bmax = 2 ** brange - 1
  #dot(nodes, ops, 0, 0, brange)
  a = int("".join(["0", "1"] * 20), 2)
  b = int("".join(["1", "0"] * 20), 2)
  #print(a,b) 
  #switch = [("jpj", "z12"), ("vvw", "fqf"), ("rts", "z07")]  
  switch = [("rts", "z07"), ("jpj", "z12"), ("z26", "kgj"), ("vvw", "chv")]
  #switch = []
  run(nodes, ops, 0, 0, brange, switch)
  run(nodes, ops, bmax, bmax, brange, switch)
  run(nodes, ops, a, b, brange, switch)
  f = list(aoc.flatten(switch))
  f.sort()
  return ",".join(f)

data = aoc.line_blocks()
aoc.cprint(solve(data))
