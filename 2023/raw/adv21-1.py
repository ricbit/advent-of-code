import sys
import re
import itertools
import math
import aoc

def walk(t, py, px, n):
  reachable = set([(py, px)])
  for step in range(n):
    newreach = set()
    for j, i in reachable:
      for jj, ii in t.iter_neigh4(j, i):
        if t[jj][ii] == ".": 
          newreach.add((jj, ii))
    reachable = newreach
  return reachable

def find_s(t):
  for j, row in enumerate(t.table):
    if "S" in row:
      i = row.index("S")
      t[j][i] = "."
      return j, i

t = aoc.Table.read()
py, px = find_s(t)
r = walk(t, py, px, 505)
print(len(r))



