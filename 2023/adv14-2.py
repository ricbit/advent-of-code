import sys
import re
import itertools
import math
import aoc

def rotate(table):
  rot = []
  for i in range(table.w):
    r = []
    for j in range(table.h):
      r.append(table[table.h - j - 1][i])
    rot.append("".join(r))
  return aoc.Table(rot)

def scroll(table):
  for t in range(table.h): 
    for j, i in table.iter_all(lambda x: x == "O"):
      if j > 0 and table[j - 1][i] == ".":
        table[j][i], table[j - 1][i] = table[j - 1][i], table[j][i]

def score(table):
  ans = 0
  for j, row in enumerate(table.table):
    for i,c in enumerate(row):
      if c == "O":
        ans += table.h - j
  return ans

def turn(t):
  table = t
  for i in range(4):
    scroll(table)
    table = rotate(table)
  return table

def thash(table):
  return "".join("".join(row) for row in table.table)

table = aoc.Table(sys.stdin)

def search(table):
  visited = {}
  vtable = []
  for pos in itertools.count():
    t = thash(table)
    vtable.append(score(table))
    print(pos)
    if t not in visited:
      visited[t] = pos
      table = turn(table)
    else:
      period = pos - visited[t]
      n = 1000000000
      k= (n - visited[t])  % period + visited[t]
      return vtable[k]
      break

print(search(table))
#for line in table.table:
#  print( "".join(line))


