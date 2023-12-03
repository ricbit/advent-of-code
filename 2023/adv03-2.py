import sys
import re
import itertools
import math

def issymbol(c):
  return (not c.isnumeric()) and c != "."

def search(table, j, i):
  while i >= 0:
    if not table[j][i - 1].isnumeric():
      return j, i
    i -= 1
  return j, i

def number(table, j, i, w):
  ans = 0
  while i < w and table[j][i].isnumeric():
    ans = ans * 10 + int(table[j][i])
    i += 1
  return ans

table = [x.strip() for x in sys.stdin.readlines()]
w, h = len(table[0]), len(table)
ans = 0
for j in range(h):
  for i in range(w):
    if issymbol(table[j][i]):
      visited = set()
      gear = 1
      for jj in range(-1, 2):
        for ii in range(-1, 2):
          if j + jj < 0 or j + jj >= h or i + ii < 0 or i + ii >= w:
            continue
          if table[j + jj][i + ii].isnumeric():
            nj, ni = search(table, j + jj, i + ii)
            if (nj, ni) not in visited:
              visited.add((nj, ni))
              gear *= number(table, nj, ni, w)
      if len(visited) == 2:
        ans += gear
print(ans)
      

