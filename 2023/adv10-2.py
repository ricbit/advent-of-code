import sys
import re
import itertools
import math
import heapq

mat = [list(line.strip()) for line in sys.stdin]
sy, sx = len(mat), len(mat[0])

def finds(mat):
  print(mat)
  for j in range(sy):
    for i in range(sx):
      if mat[j][i] == 'S':
        return j, i

dirs = {
  "|": [(1, 0), (-1, 0)],
  "-": [(0, 1), (0, -1)],
  "7": [(1, 0), (0, -1)],
  "L": [(-1, 0), (0, 1)],
  "J": [(-1, 0), (0, -1)],
  "F": [(1, 0), (0, 1)]
}

py, px = finds(mat)
visited = set((py, px))
nextp = [(0, py, px)]
mat[py][px] = "L"
maxd = 0
while nextp:
  d, py, px = heapq.heappop(nextp)
  if d > maxd:
    maxd = d
  (aj, ai), (bj, bi) = dirs[mat[py][px]]
  if (py + aj, px + ai) not in visited:
    visited.add((py + aj, px + ai))
    heapq.heappush(nextp, (d + 1, py + aj, px + ai))
  if (py + bj, px + bi) not in visited:
    visited.add((py + bj, px + bi))
    heapq.heappush(nextp, (d + 1, py + bj, px + bi))
for j in range(sy):
  for i in range(sx):
    if (j, i) not in visited:
      mat[j][i] = '.'
print(maxd)
ans = 0
for row in mat:
  interior = 0
  r = []
  row =  ("".join(row).replace("-","")
  .replace("F7","")
  .replace("LJ", "")
  .replace("FJ","|")
  .replace("L7","|"))
  for c in row:
    if c == "|"
      interior += 1
    r.append(interior % 2)
    if interior % 2 == 1 and c == ".":
      ans += 1
print(ans)
  


