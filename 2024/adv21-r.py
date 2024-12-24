import sys
import itertools
import aoc
import functools

number = {
    "7": (0, 0), "8": (0, 1), "9": (0, 2),
    "4": (1, 0), "5": (1, 1), "6": (1, 2),
    "1": (2, 0), "2": (2, 1), "3": (2, 2),
                 "0": (3, 1), "A": (3, 2)
}

small = {        "^": (0, 1), "A": (0, 2),
    "<": (1, 0), "v": (1, 1), ">": (1, 2)
}

class Solver:
  def __init__(self, max_depth):
    self.max_depth = max_depth

  def simulate(self, line, py, px, gapy, gapx):
    d = aoc.get_dir("^")
    for c in line:
      if c == "A":
        continue
      dy, dx = d[c]
      py += dy
      px += dx
      if py == gapy and px == gapx:
        return False
    return True

  @functools.cache
  def small_step(self, py, px, ny, nx, depth):
    dy, dx = ny - py, nx - px
    best = []
    for perm in itertools.permutations(range(4)):
      ans = []
      for p in perm:
        if p == 0:
          if dx > 0:
            ans.extend([">"] * abs(dx))
        if p == 1:
          if dy > 0:
            ans.extend(["v"] * abs(dy))
        if p == 2:
          if dx < 0:
            ans.extend(["<"] * abs(dx))
        if p == 3:
          if dy < 0:
            ans.extend(["^"] * abs(dy))
      ans.append("A")
      ans = "".join(ans)
      gapy, gapx = (0, 0) if depth >= 0 else (3, 0)
      if self.simulate(ans, py, px, gapy, gapx):
        best.append(self.walk_line(ans, depth + 1))
    return min(best)

  def walk_line(self, line, depth):
    if depth == self.max_depth:
      return len(line)
    table = small if depth >= 0 else number
    py, px = table["A"]
    size = 0
    for c in line:
      ny, nx = table[c] 
      size += self.small_step(py, px, ny, nx, depth)
      py, px = ny, nx
    return size

def solve(data, max_depth):
  ans = 0
  solver = Solver(max_depth)
  for line in data:
    n = solver.walk_line(line, -1)
    ans += n * int(line[:3])
  return ans

data = sys.stdin.read().splitlines()
aoc.cprint(solve(data, 2))
aoc.cprint(solve(data, 25))
