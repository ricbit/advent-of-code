import sys
import re
import itertools
import math
import aoc
import heapq
import functools
import copy
from collections import *
from dataclasses import dataclass

def wrong_slot(pos, slots, i):
  for name, frogs in zip("ABCD", pos):
    for fy, fx, value in frogs:
      if 2 <= fy <= 3 and fx == i and fx != slots[name]:
        return True
  return False

def occupied(y, x, j, i, pos):
  for frogs in pos:
    for fy, fx, value in frogs:
      if (j, i) == (fy, fx):
        return True
  return False

def possible(m, pos, slots, name, y, x, value):
  if value > 1:
    return []
  vnext = aoc.bq([(0, y, x)])
  visited = set()
  allowed = []
  #print(f"from {name} {y} {x} {value}")
  while vnext:
    score, y, x = vnext.pop()
    #print(f"try {y} {x}")
    for j, i in m.iter_neigh4(y, x, lambda c: c != "#"):
      #print(f"check {j} {i}")
      if (j, i) not in visited:
        #print(f"enter {j} {i}")
        if occupied(y, x, j, i, pos):
          continue
        #print(f"noc {j} {i}")
        vnext.push((score + 1, j, i))
        visited.add((j, i))
        if j == 1 and i in slots.values():
          continue
        if j == 1 and value == 1:
          continue
        if i in slots.values() and i != slots[name]:
          continue
        if i == slots[name]:
          if wrong_slot(pos, slots, i): 
            continue
        allowed.append((score + 1, j, i, value + 1 if value == 0 else 1))
  #print(allowed)
  return allowed

def finished(npos, slots):
  for name, frogs in zip("ABCD", npos):
    c = 0
    for fy, fx, value in frogs:
      if fx == slots[name] and fy in [2, 3]:
        c += 1
    if c != 2:
      return False
  return True

def print_table(m, pos, slots):
  lines = []
  for j in range(len(m.table)):
    line = []
    for i in range(len(m.table[0])):
      line.append("." if m[j][i] in "ABCD" else m[j][i])
    lines.append(line)
  for nf, (name, frogs) in enumerate(zip("ABCD", pos)):
    for nff, (fy, fx, value) in enumerate(frogs): 
      lines[fy][fx] = name
  return "\n".join("".join(line) for line in lines)

def canonize(npos):
  ans = []
  for frog in npos:
    ans.append(tuple(sorted(frog)))
  return tuple(ans)

def heuristic(pos, slots, cost):
  ans = 0
  return ans
  for name, frogs in zip("ABCD", pos):
    for fy, fx, value in frogs:
      ans += abs(fx - slots[name]) * cost[name]
  return ans


def search(m, pos, slots):
  pos = tuple(tuple(v) for k, v in sorted(pos.items()))
  cost = dict(zip("ABCD", [1, 10, 100, 1000]))
  vnext = [(heuristic(pos, slots, cost), 0, pos, "")]
  visited = set()
  c = 0
  while vnext:
    h, score, pos, path = heapq.heappop(vnext)
    if c % 100 == 0:
      print(score, pos, len(vnext))
    c += 1
    if finished(pos, slots):
      print(path)
      return score
    #print_table(m, pos, slots)
    for nf, (name, frogs) in enumerate(zip("ABCD", pos)):
      for nff, (fy, fx, value) in enumerate(frogs): 
        for nscore, j, i, nvalue in possible(m, pos, slots, name, fy, fx, value):
          npos = [list(b) for b in pos]
          npos[nf][nff] = (j, i, nvalue)
          npos = canonize(npos)
          if npos not in visited:
            s = score + nscore * cost[name] 
            heapq.heappush(vnext, (s, s, npos, path + "\n\n" + print_table(m, npos, slots)))
            #heapq.heappush(vnext, ((heuristic(pos, slots, cost) + s, s, npos)))
            visited.add(npos)

def get_pos(m):
  pos = aoc.ddict(lambda: [])
  for j, i in m.iter_all():
    print(j, i)
    if m[j][i].isupper():
      pos[m[j][i]].append((j, i, 0))
  slots = []
  for i in range(len(m[3])):
    if m[3][i].isupper():
      slots.append(i)
      m[2][i] = m[3][i] = "."
  return pos, dict(zip("ABCD", slots))

lines = [line.rstrip() for line in sys.stdin]
w = max(len(line) for line in lines)
lines = [list((line + " " * w)[:w]) for line in lines]
for line in lines:
  print(line)
m = aoc.Table(lines)
pos, slots = get_pos(m)
print(search(m, pos, slots))
