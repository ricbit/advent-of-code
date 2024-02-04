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

@dataclass(unsafe_hash=True,frozen=True,order=True,eq=True)
class Disk:
  used: int
  avail: int
  value: int

def print_table(n):
  for j in range(len(n)):
    line = []
    for i in range(len(n[0])):
      line.append("%10s" % (f"{n[j][i].used}/{n[j][i].avail}{'*' if n[j][i].value else ' '}"))
    print(" ".join(line))
  print()

def where(nnn):
  for j in range(len(nnn)):
    for i in range(len(nnn[0])):
      if nnn[j][i].value == 1:
        return j, i

def hole(nnn):
  for j in range(len(nnn)):
    for i in range(len(nnn[0])):
      if nnn[j][i].used == 0:
        return j, i

def heuristic(nnn):
  y, x = where(nnn)
  pj, pi = hole(nnn)
  if pj + 3 >= len(nnn):     
    d = abs(pj) + (abs(pi)) * 2000
  else:
    d = abs(pj - y) + abs(pi - x)
  return x + y + d

def ttuple(x):
  return tuple(tuple(i) for i in x)

def assert_ok(nodes):
  useds = (t.used for t in aoc.flatten(nodes))
  maxx = max(t.avail+t.used for t in aoc.flatten(nodes) if t.avail + t.used < 500)
  for i, j in itertools.product(useds, repeat=2):
    if i + j <= maxx and i > 0 and j > 0:
      print(f"bug {i} {j} {maxx}")
      return False
  return True

def search(nodes):
  if not assert_ok(nodes):
    return None
  my, mx = len(nodes), len(nodes[0])
  d = nodes[0][mx - 1]
  nodes[0][mx - 1] = Disk(d.used, d.avail, 1)
  nodes = ttuple(nodes)
  visited = set()
  vnext = [(0, 0, nodes)]
  cc = 0
  aoc.cls()
  while vnext:
    h, score, n = heapq.heappop(vnext)
    if cc % 100 == 0:
      #aoc.goto0()
      #print(h, score, len(vnext), " " * 30)
      #print_table(n)
      pass
    cc += 1
    py, px = where(n)
    hy, hx = hole(n)
    oldstate = (py, px, hy, hx)
    if n[0][0].value == 1:
      return score
    nn = [list(line)[:] for line in n]
    for y, x in itertools.product(range(my), range(mx)):
      if abs(py - y) + abs(px - x) > 40:
        continue
      for j, i in aoc.iter_neigh4(y, x):
        if 0 <= j < my and 0 <= i < mx:
          if n[j][i].avail > n[y][x].used and n[j][i].used == 0:
            nji = n[j][i]
            nyx = n[y][x]
            nn[j][i] = Disk(nji.used + nyx.used, nji.avail - nyx.used, int(nyx.value == 1))
            nn[y][x] = Disk(0, nyx.used + nyx.avail, 0)
            nnn = ttuple(nn)
            #print_table(nnn)
            npy, npx = where(nnn)
            nhy, nhx = hole(nnn)
            state = (npy, npx, nhy, nhx)
            print(f"old {oldstate} to {state}")
            if state not in visited:
              #print(f"{score} : {y} {x} to {j} {i}")
              #print_table(n)
              #print_table(nn)
              heapq.heappush(vnext, (heuristic(nnn) + score + 1, score + 1, nnn))
              visited.add(state)
            nn[j][i] = nji
            nn[y][x] = nyx
  return None
  
def build_node(nodes, j, i):
  n = nodes[(j, i)]
  return Disk(n.used, n.avail, n.value)

def build(nodes):
  mx = 1 + max(t.x for x in nodes.values())
  my = 1 + max(t.y for x in nodes.values())
  n = [[build_node(nodes, j, i) for i in range(mx)] for j in range(my)]
  return n

lines = [line.strip() for line in sys.stdin][2:]
nodes = {}
for line in lines:
  t = aoc.retuple("value_ x_ y_ size_ used_ avail_", 
          r"(.)\S+?(\d+)\S+?(\d+)\s+(\d+).\s+(\d+).\s+(\d+)", "0" + line)
  nodes[(t.y, t.x)] = t
aoc.cprint(search(build(nodes)))
