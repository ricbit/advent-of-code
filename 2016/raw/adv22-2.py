import sys
import re
import itertools
import math
import aoc
import heapq
import functools
import copy
from collections import deque
from dataclasses import dataclass

def heuristic(py, px, hy, hx):
  return py + px + abs(hy - py) + abs(hx - px)

def search(nodes, hy, hx):
  my, mx = len(nodes), len(nodes[0])
  py, px = 0, mx - 1
  vnext = aoc.bqueue([(heuristic(py, px, hy, hx), 0, py, px, hy, hx)])
  visited = set([(py, px, hy, hx)])
  while vnext:
    h, score, py, px, hy, hx = vnext.pop()
    if py == 0 and px == 0:
      return score
    for j, i in aoc.iter_neigh4(hy, hx):
      if j < 0 or i < 0 or j >= my or i >= mx:
        continue
      if nodes[j][i] == "#":
        continue
      if j == py and i == px:
        if (hy, hx, j, i) in visited:
          continue
        state = (heuristic(hy, hx, j, i) + score + 1, score + 1, hy, hx, j, i)
        vnext.push(state)
        visited.add((hy, hx, j, i))
      else:
        if (py, px, j, i) in visited:
          continue
        state = (heuristic(py, px, j, i) + score + 1, score + 1, py, px, j, i)
        vnext.push(state)
        visited.add((py, px, j, i))
  return None
  
def build_node(nodes, j, i):
  n = nodes[(j, i)]
  return "#" if n.avail + n.used > 500 else "."

def build(nodes):
  mx = 1 + max(t.x for x in nodes.values())
  my = 1 + max(t.y for x in nodes.values())
  for j in range(my):
    for i in range(mx):
      if nodes[(j, i)].used == 0:
        hy, hx = j, i
  n = [[build_node(nodes, j, i) for i in range(mx)] for j in range(my)]
  return n, hy, hx

lines = [line.strip() for line in sys.stdin][2:]
nodes = {}
for line in lines:
  t = aoc.retuple("value_ x_ y_ size_ used_ avail_", 
          r"(.)\S+?(\d+)\S+?(\d+)\s+(\d+).\s+(\d+).\s+(\d+)", "0" + line)
  nodes[(t.y, t.x)] = t
aoc.cprint(search(*build(nodes)))
