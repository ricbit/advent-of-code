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

def get_side(t):
  s = [[] for _ in range(4)]
  for i in range(t.w):
    s[0].append(t[0][i])
    s[1].append(t[t.h - 1][i])
    s[2].append(t[i][0])
    s[3].append(t[i][t.w - 1])
  yield from ("".join(side) for side in s)

def solve(blocks):
  tiles = []
  sides = aoc.ddict(set)
  for block in blocks:
    title, *lines = block
    title = aoc.retuple("title_", r".*?(\d+):", title)
    original = aoc.Table([list(line) for line in lines])
    rotated = [original]
    for i in range(3):
      rotated.append(rotated[-1].clock90())
    for i in range(4):
      rotated.append(rotated[i].flipx())
    tiles.append((title, rotated))
    for rot in rotated:
      for side in get_side(rot):
        sides[side].add(title.title)
  g = nx.Graph()
  for side in sides.values():
    if len(side) == 2:
      g.add_edge(*side)
  #nx.nx_agraph.write_dot(g, 'p20.dot')
  ans = 1
  for node in g.nodes:
    if len(list(nx.neighbors(g, node))) == 2:
      ans *= node
  return ans

blocks= aoc.line_blocks()
aoc.cprint(solve(blocks))
