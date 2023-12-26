import re
import heapq
import aoc

mat = aoc.Table.read()

def find_s(mat):
  for j, i in mat.iter_all(lambda x: x == 'S'):
    return j, i

dirs = {
  "|": [(1, 0), (-1, 0)],
  "-": [(0, 1), (0, -1)],
  "7": [(1, 0), (0, -1)],
  "L": [(-1, 0), (0, 1)],
  "J": [(-1, 0), (0, -1)],
  "F": [(1, 0), (0, 1)]
}

def check(y, x, visited, nextp, distance):
  if (y, x) not in visited:
    visited.add((y, x))
    heapq.heappush(nextp, (distance, y, x))

def build_loop(mat):
  initial_y, initial_x = find_s(mat)
  mat[initial_y][initial_x] = "L" # hardcoded
  visited = set((initial_y, initial_x))
  nextp = [(0, initial_y, initial_x)]
  distances = []
  while nextp:
    distance, py, px = heapq.heappop(nextp)
    distances.append(distance)
    (aj, ai), (bj, bi) = dirs[mat[py][px]]
    check(py + aj, px + ai, visited, nextp, distance + 1)
    check(py + bj, px + bi, visited, nextp, distance + 1)
  return visited, max(distances)

def erase_not_loop(mat, visited):
  for j, i in mat.iter_all():
    if (j, i) not in visited:
      mat[j][i] = '.'

def count_area(mat):
  ans = 0
  for row in mat.table:
    interior = 0
    row = re.sub(r"F-*7|L-*J", "", "".join(row))
    row = re.sub(r"F-*J|L-*7", "|", row)
    for c in row:
      if c == "|":
        interior += 1
      if interior % 2 == 1 and c == ".":
        ans += 1
  return ans

visited, max_distance = build_loop(mat)
print(max_distance)
erase_not_loop(mat, visited)
print(count_area(mat))
