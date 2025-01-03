import sys
import aoc
from collections import deque

def grow(t, ball):
  ticks = [ball]
  visited = set(ticks)
  time = 0
  while ticks:
    time += 1
    frontier = set()
    for tick in ticks:
      for j, i in t.iter_neigh4(tick[0], tick[1]):
        if t[j][i] == "." and (j, i) not in visited:
          frontier.add((j, i))
          visited.add((j, i))
    ticks = frontier
  return time - 1

def extract_maze(data):
  offset = data[207]
  size = data[132]
  factor = data[196]
  salt = data[212]
  bally, ballx = data[153], data[146]
  starty, startx = data[1035], data[1034]
  maze = [["#"] * (size + 1) for _ in range(size + 1)]
  for j in range(1, size):
    for i in range(1, size):
      ii, jj = i % 2, j % 2
      addr = offset + (j // 2 + jj - 1) * factor + (i - 1)
      if jj ^ ii:
        maze[j][i] = "#" if data[addr] >= salt else "."
      else:
        maze[j][i] = "#" if jj == ii == 0 else "."
  return aoc.Table(maze), (bally, ballx), (starty, startx)


def shortest(maze, start, goal):
  vnext = deque([(0, start)])
  visited = set()
  while vnext:
    size, pos = vnext.popleft()
    if pos == goal:
      return size
    if pos in visited:
      continue
    visited.add(pos)
    for j, i in maze.iter_neigh4(*pos):
      if maze[j][i] == "." and (j, i) not in visited:
        vnext.append((size + 1, (j, i)))

data = aoc.ints(sys.stdin.read().split(","))
maze, ball, start = extract_maze(data)
aoc.cprint(shortest(maze, start, ball))
aoc.cprint(grow(maze, ball))
