import sys

grid = [line.strip() for line in sys.stdin]

def find_position(grid, letter):
  for index, line in enumerate(grid):
    if letter in line:
      return (index, line.index(letter))

def get_height(pos):
  j, i = pos
  return grid[j][i]

def value(letter):
  match letter:
    case "S":
      return ord("a")
    case "E":
      return ord("z")
    case _:
      return ord(letter)

def neigh(pos):
  y = [1, -1, 0, 0]
  x = [0, 0, -1, 1]
  for j, i in zip(y, x):
    yield (pos[0] + j, pos[1] + i)

def valid_neigh(pos, limits):
  for j, i in neigh(pos):
    if 0 <= j < limits[0] and 0 <= i < limits[1]:
      yield j, i

def reachable_neigh(pos, limit, height):
  for next_pos in valid_neigh(pos, limit):
    if value(get_height(next_pos)) <= height + 1:
      yield next_pos

def dijkstra(grid, start):
  end = find_position(grid, "E")
  limits = (len(grid), len(grid[0]))
  visited = set()
  visited.add(start)
  current = [(0, start)]
  while current:
    steps, pos = current.pop(0)
    height = value(get_height(pos))
    if pos == end:
      return steps
    for next_pos in reachable_neigh(pos, limits, height):
      if next_pos not in visited:
        visited.add(next_pos)
        current.append((steps + 1, next_pos))
  return None

start = find_position(grid, "S")
print(dijkstra(grid, start))

best = 1e10
limits = (len(grid), len(grid[0]))
for j in range(limits[0]):
  for i in range(limits[1]):
    if value(get_height((j, i))) == ord('a'):
      current = dijkstra(grid, (j, i))
      if current and current < best:
        best = current
print(best)
        
