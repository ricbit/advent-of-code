import itertools
import copy
import sys

original_grid = [list(line.strip()) for line in sys.stdin]
original_moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def iter_grid(grid):
  for j in range(len(grid)):
    for i in range(len(grid[0])):
      yield j, i

def valid(grid, j, i):
  return 0 <= j < len(grid) and 0 <= i < len(grid[0])

def enlarge(grid):
  newgrid = []
  newgrid.append(["."] * (len(grid[0]) + 2))
  for line in grid:
    newgrid.append(["."] + line + ["."])
  newgrid.append(["."] * (len(grid[0]) + 2))
  return newgrid

def has_neigh(grid, j, i):
  for dj, di in itertools.product(range(-1, 2), repeat=2):
    if di == dj == 0:
      continue
    if valid(grid, j + dj, i+ di) and grid[j + dj][i + di] == "#":
      return True
  return False

def try_proposal(j, i, grid, moves):
  for index, move in enumerate(moves):
    if move[1] == 0:      
      if valid(grid, j + move[0], i + move[1]):
        empty = all(grid[j + move[0]][i + c] == "." for c in range(-1, 2) 
          if valid(grid, j + move[0], i + c))
        if empty:
          return index
    else:
      if valid(grid, j + move[0], i + move[1]):
        empty = all(grid[j + c][i + move[1]] == "." for c in range(-1, 2)
          if valid(grid, j + c, i + move[1]))
        if empty:
          return index
  return None
    
def step(old_grid, moves):
  grid = enlarge(old_grid)
  proposals = [[None] * len(grid[0]) for _ in grid]
  targets = [[0] * len(grid[0]) for _ in grid]
  for j, i in iter_grid(grid):
    if grid[j][i] == "#" and has_neigh(grid, j, i):
      prop = try_proposal(j, i, grid, moves)
      proposals[j][i] = prop
      if prop is not None:
        targets[j + moves[prop][0]][i + moves[prop][1]] += 1
  elfs = 0
  for j, i in iter_grid(grid):
    prop = proposals[j][i]
    if prop is not None:
      if targets[j + moves[prop][0]][i + moves[prop][1]] == 1:
        elfs += 1
        grid[j][i] = "."
        grid[j + moves[prop][0]][i + moves[prop][1]] = "#"
  move = moves.pop(0)
  moves.append(move)
  return elfs, trim(grid)

def trim(grid):
  ymax, ymin = -1, len(grid) + 1
  xmax, xmin = -1, len(grid[0]) + 1
  for index, line in enumerate(grid):
    if line != ["."] * len(line):
      ymax = max(ymax, index)
      ymin = min(ymin, index)
    if "#" in line:
      xmin = min(xmin, line.index("#"))
      xmax = max(xmax, len(line) - list(reversed(line)).index("#"))
  return [line[xmin:xmax] for line in grid[ymin:ymax + 1]]

def first():
  grid = copy.deepcopy(original_grid)
  moves = copy.deepcopy(original_moves)
  for i in range(10):
    elfs, grid = step(grid, moves)
  grid = trim(grid)
  total = 0
  for j, i in iter_grid(grid):
    if grid[j][i] == ".":
      total += 1
  return total

def second():
  grid = copy.deepcopy(original_grid)
  moves = copy.deepcopy(original_moves)
  steps = 0
  while True:
    elfs, grid = step(grid, moves)
    steps += 1
    if not elfs:
      return steps

print(first())
print(second())
