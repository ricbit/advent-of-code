import sys
import re
import itertools
import math
from aoc import Table

lines = [line.strip() for line in sys.stdin]

def expandx(lines):
  rexpand = []
  for i, line in enumerate(lines):
    if line.count(".") == len(line):
      rexpand.append(i)
  return rexpand

def transpose(lines):
  rex = []
  for i in range(len(lines[0])):
    rex.append("".join(line[i] for line in lines))
  return rex

galaxies = []
for j, row in enumerate(lines):
  for i, c in enumerate(row):
    if c == "#":
      galaxies.append((j, i))

def shortest(sj, si, galaxies, rows, cols):
  dist = 0
  for j, i in galaxies:
    base = abs(j - sj) + abs(i - si)
    for x in range(min(j, sj), max(j, sj) + 1):
      if x in rows:
        base += 1000000 - 1
    for x in range(min(i, si), max(i, si) + 1):
      if x in cols:
        base += 1000000 - 1
    dist += base
  return dist

rows = expandx(lines)
cols = expandx(transpose(lines))

ans = 0
for j, i in galaxies:
  ans += shortest(j, i, galaxies, rows, cols)
print(ans // 2)


