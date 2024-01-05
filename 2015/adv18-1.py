import sys
import re
import itertools
import math
import aoc
from collections import *

def life(m):
  new = m.copy()
  for j, i in m.iter_all():
    count = sum(1 for jj, ii in m.iter_neigh8(j, i) if m[jj][ii] == "#")
    if m[j][i] == "#":
      new[j][i] = "#" if count in [2, 3] else "."
    else:
      new[j][i] = "#" if count == 3 else "."
  new[0][0] = "#"
  new[0][-1] = "#"
  new[-1][0] = "#"
  new[-1][-1] = "#"
  return new

m = aoc.Table.read()
m[0][0] = "#"
m[0][-1] = "#"
m[-1][0] = "#"
m[-1][-1] = "#"
for i in range(100):
  m = life(m)
aoc.cprint(sum(1 for j, i in m.iter_all() if m[j][i] == "#"))
