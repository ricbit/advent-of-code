import sys
import string
import aoc
import multiprocessing
from collections import deque

grid = aoc.Table([line.strip() for line in sys.stdin])

def get_height(pos):
  j, i = pos
  return grid[j][i]

value_dict = {c: ord(c) for c in string.ascii_lowercase}
value_dict['S'] = ord('a')
value_dict['E'] = ord('z')

def reachable_neigh(pos, height):
  for j, i in grid.iter_neigh4(*pos):
    if value_dict[grid[j][i]] <= height + 1:
      yield (j, i)

def dijkstra(grid, start, end):
  visited = set()
  visited.add(start)
  current = deque([(0, start)])
  while current:
    steps, (j, i) = current.popleft()
    height = value_dict[grid[j][i]]
    for next_pos in reachable_neigh((j, i), height):
      if next_pos not in visited:
        visited.add(next_pos)
        current.append((steps + 1, next_pos))
        if next_pos == end:
          return steps + 1
  return None

def dijkstra_grid(pos):
  return dijkstra(grid, pos, end)

start = grid.find("S")
end = grid.find("E")
aoc.cprint(dijkstra(grid, start, end))

valid = []
for j, i in grid.iter_all():
  if value_dict[grid[j][i]] == ord('a'):
    valid.append((j, i))

with multiprocessing.Pool() as pool:
  best = pool.imap_unordered(dijkstra_grid, valid)
  aoc.cprint(min(b for b in best if b is not None))
