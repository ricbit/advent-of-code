import aoc

class Grow:
  def __init__(self, t):
    self.t = t
    self.mask = t.copy()

  def sides(self, t, y, x):
    ans = 0
    for j, i in t.iter_all():
      if t[j][i] != -1:
        continue
      if t[j][i] == -1 and t[j][i-1] == -1 and t[j-1][i] != -1 and t[j-1][i-1] != -1:
        ans -= 1
      if t[j][i] == -1 and t[j][i-1] == -1 and t[j+1][i] != -1 and t[j+1][i-1] != -1:
        ans -= 1
      if t[j][i] == -1 and t[j-1][i] == -1 and t[j][i-1] != -1 and t[j-1][i-1] != -1:
        ans -= 1
      if t[j][i] == -1 and t[j-1][i] == -1 and t[j][i+1] != -1 and t[j-1][i+1] != -1:
        ans -= 1
    return ans

  def grow(self, y, x):
    pnext = [(y, x)]
    visited = set()
    area, perimeter, sides = 0, 0, 0
    tt = self.t.copy()
    sy,sx=y,x
    while pnext:
      y, x = pnext.pop()
      if (y, x) in visited:
        continue
      visited.add((y, x))
      self.mask[y][x] = 0
      tt[y][x] = -1
      area += 1
      perimeter += 4
      sides += 4
      for j, i in self.t.iter_neigh4(y, x):
        if (j, i) in visited:
          perimeter -= 2
          sides -= 2
      for j, i in self.t.iter_neigh4(y, x):
        if self.t[j][i] == self.t[y][x] and self.mask[j][i] != 0:
          pnext.append((j, i))
    return area * perimeter, area*(perimeter + self.sides(tt,sy,sx))

  def solve(self):
    ans1, ans2 = 0, 0
    for j, i in self.t.iter_all():
      if self.mask[j][i] != 0:
        x, y =  self.grow(j, i)
        ans1 += x
        ans2 += y
    return ans1,ans2

data = aoc.Table.read()
part1, part2 = Grow(data.grow(0)).solve()
aoc.cprint(part1)
aoc.cprint(part2)
