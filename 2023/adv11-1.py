import sys
import re
import itertools
import math
from aoc import Table

lines = [line.strip() for line in sys.stdin]

def expandx(lines):
  rexpand = []
  for line in lines:
    if line.count(".") == len(line):
      rexpand.append(line)
    rexpand.append(line)
  return rexpand

def transpose(lines):
  rex = []
  for i in range(len(lines[0])):
    rex.append("".join(line[i] for line in lines))
  return rex

mat = transpose(expandx(transpose(expandx(lines)))) 
galaxies = []
for j, row in enumerate(mat):
  for i, c in enumerate(row):
    if c == "#":
      galaxies.append((j, i))

def shortest(sj, si, galaxies):
  dist = []
  for j, i in galaxies:
    dist.append(abs(j - sj) + abs(i - si))
  return sum(dist)

ans = 0
for j, i in galaxies:
  ans += shortest(j, i, galaxies)
print(ans // 2)
      
