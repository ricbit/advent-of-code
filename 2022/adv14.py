import sys

def parse():
  walls = []
  for line in sys.stdin:
    wall = []
    for point in line.split("->"):
      j, i = point.split(",")
      wall.append((int(j), int(i)))
    walls.append(wall)
  return walls

def get_bounds(walls):
  min_x = 1e10
  max_x = 0
  max_y = 0
  for wall in walls:
    for x, y in wall:
      min_x = min(min_x, x)
      max_x = max(max_x, x)
      max_y = max(max_y, y)
  return min_x, max_x, max_y

def translate(walls, min_x):
  new_walls = []
  for wall in walls:
    new_wall = []
    for x, y in wall:
      new_wall.append(((x - min_x), y))
    new_walls.append(new_wall)
  return new_walls
  
original_walls = parse()  

def draw_single_wall(current, point, grid):
  cx, cy = current
  px, py = point
  if cx == px:
    for j in range(min(cy, py), max(cy, py) + 1):
      grid[j][cx] = "#"
  elif cy == py:
    for i in range(min(cx, px), max(cx, px) + 1):
      grid[cy][i] = "#"

def draw_walls(grid, walls):
  for wall in walls:
    current = wall[0]
    for point in wall[1:]:
      draw_single_wall(current, point, grid)
      current = point

def dump_grid(grid):
  for line in grid:
    print("".join(line))
  print()

def drop_sand(grid, startx):
  cx, cy = (startx, 0)
  while grid[0][startx] == ".":
    if cy >= len(grid) or cx < 0 or cx >= len(grid[0]):
      return False
    if grid[cy + 1][cx] == ".":
      cy += 1
      continue
    elif grid[cy + 1][cx - 1] == ".":
      cy += 1
      cx -= 1
      continue
    elif grid[cy + 1][cx + 1] == ".":
      cy += 1
      cx += 1
      continue
    else:
      grid[cy][cx] = "o"
      return True
  return False

def first():
  min_x, max_x, max_y = get_bounds(original_walls)
  walls = translate(original_walls, min_x)
  grid = [["."] * (max_x - min_x + 1) for _ in range(max_y + 1)]
  draw_walls(grid, walls)
  count = 0
  while drop_sand(grid, 500 - min_x):
    count += 1
  return count

def second():
  min_x, max_x, max_y = get_bounds(original_walls)
  min_x -= max_y
  max_x += max_y
  max_y += 2
  walls = translate(original_walls, min_x)
  grid = [["."] * (max_x - min_x + 1) for _ in range(max_y + 1)]
  for i in range(len(grid[0])):
    grid[-1][i] = "#"
  draw_walls(grid, walls)
  count = 0
  while drop_sand(grid, 500 - min_x):
    count += 1
  return count
  
print(first())
print(second())
    
