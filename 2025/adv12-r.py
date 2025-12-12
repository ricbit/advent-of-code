# Works for example and input.

import aoc
import functools

class Solver:
  def __init__(self, rotated, required, x, y):
    self.rotated = rotated
    self.required = required
    self.x = x
    self.y = y

  def stamp(self, tt, shape, j, i):
    for jj in range(3):
      for ii in range(3):
        if shape[jj * 3 + ii] == "#":
          if tt[j + jj][i + ii] == "#":
            return False
          tt[j + jj][i + ii] = "#"
    return True

  @functools.cache
  def search(self, grid, pos):
    if pos == len(self.required):
      return True
    batch = lambda grid, i: list(grid[i * self.x:(i + 1) * self.x])
    t = aoc.Table([batch(grid, i) for i in range(self.y)])
    for shape in self.rotated[self.required[pos]]:
      for j in range(1 + self.y - 3):
        for i in range(1 + self.x - 3):
          tt = t.copy()
          if self.stamp(tt, shape, j, i):
            newgrid = "".join(aoc.flatten(tt.table))
            if self.search(newgrid, pos + 1):
              return True
    return False

def rotate(shapes):
  rotated = []
  for shape in shapes:
    unique = set()
    for b in range(4):
      shape = shape.clock90()
      unique.add("".join(aoc.flatten(shape.table)))
      unique.add("".join(aoc.flatten(shape.flipx().table)))
    rotated.append(unique)
  return rotated

def solve(gifts, rotated):
  ans = 0
  for line in gifts:
    gift = aoc.retuple("x_ y_ spec", r"(\d+)x(\d+): (.*)$", line)
    amount = aoc.ints(gift.spec.split())
    required = list(aoc.flatten([i] * a for i, a in enumerate(amount)))
    x = sum(aoc.first(rotated[i]).count("#") for i in required)
    if x > gift.x * gift.y:
      continue
    total_blocks = sum(amount)
    total_available = (gift.x // 3) * (gift.y // 3)
    if total_blocks <= total_available:
      ans += 1
      continue
    s = Solver(rotated, required, gift.x, gift.y)
    if s.search("." * (gift.x * gift.y), 0):
      ans += 1
  return ans

data = aoc.line_blocks()
shapes = [aoc.Table(b[1:]) for b in data[:-1]]
gifts = data[-1]
rotated = rotate(shapes)
aoc.cprint(solve(gifts, rotated))
