import sys
import aoc

def part1(t, y, x):
  pnext = [(y, x)]
  visited = set()
  score = 0
  while pnext:
    y, x = pnext[0]
    pnext.pop(0)
    if (y, x) in visited:
      continue
    visited.add((y, x))
    if t[y][x] == 9:
      score += 1
    for j, i in t.iter_neigh4(y, x):
      if t[j][i] == t[y][x] + 1:
        pnext.append((j, i))
  return score

def part2(t, y, x):
  pnext = [((y, x),)]
  trails = set()
  fulltrails = set()
  while pnext:
    tupletrail = pnext[0]
    trail = list(pnext[0])
    pnext.pop(0)
    y, x = trail[-1]
    if tupletrail in trails:
      continue
    trails.add(tupletrail)
    if t[y][x] == 9:
      fulltrails.add(tupletrail)
    for j, i in t.iter_neigh4(y, x):
      if t[j][i] == t[y][x] + 1:
        pnext.append(tuple(trail +[(j, i)]))
  return len(fulltrails)

def solve(t, part):
  ans = 0
  for j, i in t.iter_all():
    if t[j][i] == 0:
      ans += part(t, j, i)
  return ans

lines = sys.stdin.read().splitlines()
data = aoc.Table([[(int(i) if i != "." else -10) for i in j] for j in lines])
aoc.cprint(solve(data, part1))
aoc.cprint(solve(data, part2))

