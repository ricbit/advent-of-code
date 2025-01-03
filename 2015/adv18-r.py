import aoc

def life(m, stuck):
  new = m.copy()
  for j, i in m.iter_all():
    count = sum(1 for jj, ii in m.iter_neigh8(j, i) if m[jj][ii] == "#")
    if m[j][i] == "#":
      new[j][i] = "#" if count in [2, 3] else "."
    else:
      new[j][i] = "#" if count == 3 else "."
  if stuck:
    new[0][0] = "#"
    new[0][-1] = "#"
    new[-1][0] = "#"
    new[-1][-1] = "#"
  return new

def solve(m, stuck):
  for _ in range(100):
    m = life(m, stuck)
  return sum(1 for j, i in m.iter_all() if m[j][i] == "#")

m = aoc.Table.read()
aoc.cprint(solve(m, False))
aoc.cprint(solve(m, True))
