import heapq
import sys
import copy
from dataclasses import dataclass

grid = [list(line.strip()) for line in sys.stdin]

def iter_grid(grid):
  for j in range(len(grid)):
    for i in range(len(grid[0])):
      yield j, i

wind_type = {">": (0, 1), "<": (0, -1), "^": (-1, 0), "v": (1, 0)}
wind_code = {v:k for k, v in wind_type.items()}

@dataclass(init=False, repr=True)
class Valley:
  start: tuple[int]
  end: tuple[int]
  wind: list[tuple[int]]
  h: int
  w: int
  grid: list[list[int]]
  minpath: int

def parse_grid(grid):
  wind = []
  for j, i in iter_grid(grid):
    if grid[j][i] not in "#.":
      dj, di = wind_type[grid[j][i]]
      wind.append((j, i, dj, di))
  valley = Valley()
  valley.start = (0, grid[0].index("."))
  valley.end = (len(grid) - 1, grid[-1].index("."))
  valley.wind = wind
  valley.h = len(grid)
  valley.w = len(grid[0])
  valley.grid = grid
  minpath = abs(valley.start[0] - valley.end[0])
  minpath += abs(valley.start[1] - valley.end[1])
  valley.minpath = minpath
  return valley

valley = parse_grid(grid)

def iter_wind(valley, wind):
  new_wind = []
  for current, base in zip(wind, valley.wind):
    j, i = current
    sj, si, dj, di = base
    j = (j - 1 + dj) % (valley.h - 2) + 1
    i = (i - 1 + di) % (valley.w - 2) + 1
    new_wind.append((j, i))
  return new_wind

def dump_valley(valley, pos, wind):
  grid = [["."] * valley.w for _ in range(valley.h)]
  for j in range(valley.h):
    grid[j][0] = grid[j][-1] = "#"
  for i in range(valley.w):
    grid[0][i] = grid[-1][i] = "#"
    grid[valley.start[0]][valley.start[1]] = "."
    grid[valley.end[0]][valley.end[1]] = "."  
  for original, current in zip(valley.wind, wind):
    sj, si, dj, di = original
    j, i = current
    if grid[j][i] == ".":
      grid[j][i] = wind_code[(dj, di)]
    elif not grid[j][i].isdigit():
      grid[j][i] = "2"
    else:
      grid[j][i] = str(int(grid[j][i]) + 1)
  grid[pos[0]][pos[1]] = "E"
  print("\n".join("".join(line) for line in grid))
  print()

directions = [(1, 0), (0, 1), (-1, 0), (0, -1), (0, 0)]

def iter_player(valley, pos, wind):
  for dj, di in directions:
    nj, ni = pos[0] + dj, pos[1] + di
    if any(wj == nj and wi == ni for wj, wi in wind):
      continue
    if 0 <= nj < valley.h and 0 <= ni < valley.w:      
      if grid[nj][ni] != "#":
        yield nj, ni

def score(valley, state, goal, nj, ni):
  minpath = valley.minpath * (goal - state - 1)
  if state % 2 == 0:
    fj, fi = valley.end[0], valley.end[1]
  else:
    fj, fi = valley.start[0], valley.start[1]
  return abs(nj - fj) + abs(ni - fi) + minpath

def change_state(valley, state, pos):
  if state % 2 == 0 and pos == valley.end:
    state += 1
  elif state % 2 == 1 and pos == valley.start:
    state += 1
  return state

def search(valley, goal):
  maxscore = score(valley, 0, goal, valley.start[0], valley.start[1])
  start = (maxscore, 0, 0, valley.start)
  visited = set((0, 0, valley.start))
  events = [start]
  wind_cache = {0: [(j, i) for j, i, dj, di in valley.wind]}
  minscore = 0
  vis, drop = 0, 0
  while events:
    maxscore, time, state, pos = heapq.heappop(events)
    vis += 1
    if maxscore < minscore:
      drop += 1
      continue
    if time not in wind_cache:
      wind_cache[time] = iter_wind(valley, wind_cache[time - 1])
    wind = wind_cache[time]
    if vis % 1000 == 0:
      print(vis, drop, state, maxscore, minscore)
    newstate = change_state(valley, state, pos)
    if newstate == goal:
      return time - 1
    time += 1
    minscore = max(minscore, time)
    for nj, ni in iter_player(valley, pos, wind):
      nscore = time + score(valley, newstate, goal, nj, ni)
      npos = (nscore, time, newstate, (nj, ni))
      if (time, newstate, (nj, ni)) not in visited:
        visited.add((time, newstate, (nj, ni)))
        heapq.heappush(events, npos)
  return None
      
def first():
  print(search(valley, 1))

def second():
  print(search(valley, 3))

first()
second()
