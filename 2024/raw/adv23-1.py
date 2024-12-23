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

def solve(lines):
  g = nx.Graph()
  for src, dst in lines:
    g.add_edge(src, dst)
  ans = 0
  uniq = set()
  for x in nx.find_cliques(g):
    x = list(x)
    if len(x) >= 3 and any(y.startswith("t") for y in x):
      for kk in itertools.combinations(x, 3):
        kk = tuple(kk)
        if any(y for y in kk if y.startswith("t")):
          print("this ", kk)
          uniq.add(kk)
          ans += 1
  return len(uniq)

# not 1621
data = [s.strip().split("-") for s in sys.stdin.read().splitlines()]
aoc.cprint(solve(data))
