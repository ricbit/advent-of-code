import sys
import itertools
import aoc
import multiprocessing

def iter_diamond(t, y, x, d):
  for j in range(max(0, y - d), min(t.h, y + d + 1)):
    dj = abs(j - y)
    for i in range(max(0, x - d + dj), min(t.w, x + d - dj + 1)):
      dist = dj + abs(x - i)
      if 1 < dist <= d:
        yield j, i, dist

def build_path(t):
  sy, sx = t.find("S")
  ey, ex = t.find("E")
  t[sy][sx] = "."
  t[ey][ex] = "."
  pos = (sy, sx)
  path = [pos]
  visited = set(path)
  while pos != (ey, ex):
    for ny, nx in t.iter_neigh4(*pos):
      if t[ny][nx] == "." and (pnext := (ny, nx)) not in visited:
        visited.add(pnext)
        path.append(pnext)
        pos = pnext
        break
  return path

def build_distance(path):
  return {p: i for i, p in enumerate(path)}

class CheatFinder:
  def __init__(self, path, t):
    self.path = path
    self.t = t
    self.distance = build_distance(self.path)

  def solve_from(self, y, x):
    p1, p2 = 0, 0
    for j, i, d in iter_diamond(self.t, y, x, 20):
      if self.t[j][i] != ".":
        continue
      if (save := self.distance[(j, i)] - self.distance[(y, x)]) <= 0:
        continue
      if save - d + 1 >= 100: 
        p1 += d <= 2
        p2 += 1
    return p1, p2

  def find(self, lines):
    ans = [self.solve_from(y, x) for y, x in self.path if y in lines]
    return [sum(line) for line in zip(*ans)]

def solve(encoded):
  grid, lines = encoded
  t = aoc.Table([list(x) for x in grid])
  path = build_path(t)
  part1, part2 = CheatFinder(path, t).find(lines)
  return part1, part2

CPUS = 8
input_grid = sys.stdin.read().splitlines()
height = len(input_grid)
lines = itertools.batched(range(height), height // CPUS + 1)
with multiprocessing.Pool() as pool:
  ans = list(pool.imap(solve, ((input_grid, line) for line in lines)))
part1, part2 = [sum(line) for line in zip(*ans)]
aoc.cprint(part1)
aoc.cprint(part2)

