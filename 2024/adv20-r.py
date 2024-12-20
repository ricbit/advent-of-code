import aoc

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

class Solver:
  def __init__(self, path, t):
    self.path = path
    self.t = t
    self.distance = build_distance(self.path)

  def solve_from(self, encoded):
    y, x = encoded
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

  def solve(self):
    ans = map(self.solve_from, self.path)
    return [sum(line) for line in zip(*ans)]

t = aoc.Table.read()
path = build_path(t)
part1, part2 = Solver(path, t).solve()
aoc.cprint(part1)
aoc.cprint(part2)
