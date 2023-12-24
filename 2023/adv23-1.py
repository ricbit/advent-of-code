import sys
import re
import itertools
import math
import aoc
from collections import *
import copy

def search(t):
  vnext = [(0, 0, 1, set())]
  paths = []
  while vnext:
    score, y, x, visited = vnext.pop(0)
    for j, i in t.iter_neigh4(y, x):
      if (j, i) in visited:
        continue
      if (j, i) == (t.h - 1, t.w - 2):
        paths.append(1 + len(visited))
        continue
      dj = j - y
      di = i - x
      if t[j][i] in ".v^<>" and (t[y][x] == "." or
          (t[y][x] == ">" and di == 1 and dj == 0) or
          (t[y][x] == "<" and di == -1 and dj == 0) or
          (t[y][x] == "^" and di == 0 and dj == -1) or
          (t[y][x] == "v" and di == 0 and dj == 1)):
        visited2 = visited.copy()
        visited2.add((j, i))
        vnext.append((score + 1, j, i, visited2))
  return max(paths)

t = aoc.Table.read()
print(search(t))
def lixo(): 
  for path in search(t):
    tt = aoc.Table(copy.deepcopy(t.table)  )
    for j, i in path:
      tt[j][i] = "O"
    print(len(path))
    print("\n".join("".join(row) for row in tt.table))
    print()

