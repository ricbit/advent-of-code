import aoc

class Regions:
  def __init__(self, t):
    self.t = t
    self.mask = t.copy()

  def common_sides(self, visited):
    ans = 0
    for j, i in visited:
      # Left neighbour
      if (j, i - 1) in visited:
        for jj in [j - 1, j + 1]:
          if (jj, i) not in visited and (jj, i - 1) not in visited:
            ans += 1
      # Up neighbour
      if (j - 1, i) in visited:
        for ii in [i - 1, i + 1]:
          if (j, ii) not in visited and (j - 1, ii) not in visited:
            ans += 1
    return ans

  def grow(self, y, x):
    pnext = [(y, x)]
    visited = set()
    area, perimeter = 0, 0
    while pnext:
      y, x = pnext.pop()
      if (y, x) in visited:
        continue
      visited.add((y, x))
      self.mask[y][x] = 0
      area += 1
      perimeter += 4
      for j, i in self.t.iter_neigh4(y, x):
        if (j, i) in visited:
          perimeter -= 2
        elif self.t[j][i] == self.t[y][x]:
          pnext.append((j, i))
    return area * perimeter, area * (perimeter - self.common_sides(visited))

  def solve(self):
    ans1, ans2 = 0, 0
    for j, i in self.t.iter_all():
      if self.mask[j][i] != 0:
        x, y =  self.grow(j, i)
        ans1 += x
        ans2 += y
    return ans1, ans2

data = aoc.Table.read()
part1, part2 = Regions(data.grow(0)).solve()
aoc.cprint(part1)
aoc.cprint(part2)
