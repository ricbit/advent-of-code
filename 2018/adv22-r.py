import sys
import aoc
import heapq

def solve(depth, y, x, factor):
  geolevel = aoc.Table([[0] * (factor * x + 1) for _ in range(factor * y + 1)])
  erosion = aoc.Table([[0] * (factor * x + 1) for _ in range(factor * y + 1)])
  regtype = aoc.Table([[0] * (factor * x + 1) for _ in range(factor * y + 1)])
  for j in range(factor * y + 1):
    for i in range(factor * x + 1):
      if j == 0 and i == 0:
        geolevel[j][i] = 0
      elif y == j and i == x:
        geolevel[j][i] = 0
      elif j == 0:
        geolevel[j][i] = i * 16807
      elif i == 0:
        geolevel[j][i] = j * 48271
      else:
        geolevel[j][i] = erosion[j][i-1] * erosion[j-1][i]
      erosion[j][i] = (geolevel[j][i] + depth) % 20183
      regtype[j][i] = erosion[j][i] % 3
  return regtype

def risk(regtype):
  return sum(sum(line) for line in regtype)

def mindist(cave, gy, gx):
  # torch 0  - gear  1  - neither 2
  allowed = {0: set([0, 1]), 1: set([1, 2]), 2: set([0, 2])}
  vnext = [(0, 0, 0, 0)]
  visited = set()
  while vnext:
    score, tool, y, x = heapq.heappop(vnext)
    if (tool, y, x) in visited:
      continue
    if tool == 0 and y == gy and x == gx:
      return score
    visited.add((tool, y, x))
    for t in range(3):
      if t != tool and t in allowed[cave[y][x]]:
        if (t, y, x) not in visited:
          heapq.heappush(vnext, (score + 7, t, y, x))
    for j, i in cave.iter_neigh4(y, x):
      if tool in allowed[cave[j][i]]:
        if (tool, j, i) not in visited:
          heapq.heappush(vnext, (score + 1, tool, j, i))

data = [line.strip() for line in sys.stdin]
depth = int(data[0].split(": ")[1])
x, y = aoc.ints(data[1].split(":")[1].split(","))
cave = solve(depth, y, x, 1)
aoc.cprint(risk(cave))
cave = solve(depth, y, x, 5)
aoc.cprint(mindist(cave, y, x))
