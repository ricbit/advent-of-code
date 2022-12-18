import itertools
import sys

cubes = []
for line in sys.stdin.readlines():
  cubes.append([int(x) for x in line.strip().split(",")])

size = 22
grid = [[[0] * size for i in range(size)] for j in range(size)]
for cube in cubes:
  grid[cube[0] + 1][cube[1] + 1][cube[2] + 1] = 1

def walk(grid, pos):
  dirs = [(0, 0, 1), (0, 0, -1), (0, 1, 0), (0, -1, 0), (1, 0, 0), (-1, 0, 0)]
  for delta in dirs:
    npos = [x + y for x, y in zip(pos, delta)]
    if all(0 <= p < size for p in npos):
      yield tuple(npos)

def floodfill(grid):
  visited = set()
  visited.add((0, 0, 0))
  events = [(0, 0, 0)]
  grid[0][0][0] = 2
  while events:
    pos = events.pop(0)
    for npos in walk(grid, pos):
      if npos in visited:
        continue
      visited.add(npos)      
      a, b, c = npos
      if grid[a][b][c] == 0:
        grid[a][b][c] = 2
        events.append(npos)      
      elif grid[a][b][c] == 1:
        grid[a][b][c] = 3

def count(grid, solid, exterior):
  faces = 0
  for a, b, c in itertools.product(range(size), repeat=3):
    if grid[a][b][c] in solid:
      for x, y, z in walk(grid, (a, b, c)):
        if grid[x][y][z] in exterior:
          faces += 1
  return faces

floodfill(grid)
print(count(grid, [1, 3], [0, 2]))
print(count(grid, [3], [2]))

