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
  g = nx.DiGraph()
  for line in data:
    for node in line.dst.split():
      g.add_edge(line.src, node)
  return len(list(nx.all_simple_paths(g, "you", "out")))

data = aoc.retuple_read("src dst", r"(\w+): (.*)$")
aoc.cprint(solve(data))
