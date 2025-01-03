import sys
import aoc

def walk(t, y, x, check=True):
  pnext = [(y, x)]
  visited = set()
  score = 0
  while pnext:
    y, x = pnext[0]
    pnext.pop(0)
    if check and (y, x) in visited:
      continue
    visited.add((y, x))
    if t[y][x] == 9:
      score += 1
    for j, i in t.iter_neigh4(y, x):
      if t[j][i] == t[y][x] + 1:
        pnext.append((j, i))
  return score

def solve(t, part, check):
  ans = 0
  for j, i in t.iter_all():
    if t[j][i] == 0:
      ans += part(t, j, i, check)
  return ans

lines = sys.stdin.read().splitlines()
data = aoc.Table([[(int(i) if i != "." else -10) for i in j] for j in lines])
aoc.cprint(solve(data, walk, check=True))
aoc.cprint(solve(data, walk, check=False))
