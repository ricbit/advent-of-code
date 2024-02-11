import re
import aoc

values = re.findall(r"x=(-?\d+)..(-?\d+), y=(-?\d+)..(-?\d+)\s*$", input())
xmin, xmax, ymin, ymax = [int(i) for i in values[0]]

def xpositions(vx0, xmin, xmax):
  x, v, i = 0, vx0, 0
  while True:
    x += v
    v -= 1
    i += 1
    if xmin <= x <= xmax:
      yield i, x
    if v < 0 or x > xmax:
      return

def simulation(vx0, vy0):
  x, y, vx, vy = 0, 0, vx0, vy0
  while True:
    yield x, y
    x += vx
    if vx > 0:
      vx -= 1
    y += vy
    vy -= 1

def complete(vx0, vy0, xmin, xmax, ymin, ymax):
  for x, y in simulation(vx0, vy0):
    if y < ymin:
      return
    yield x, y

def valid(vx0, vy0, xmin, xmax, ymin, ymax):
  for x, y in complete(vx0, vy0, xmin, xmax, ymin, ymax):
    if xmin <= x <= xmax and ymin <= y <= ymax:
      yield x, y

def bound(vx0, vy0, xmin, xmax, ymin, ymax):
  for x, y in valid(vx0, vy0, xmin, xmax, ymin, ymax):
    return True
  return False

def findymax(vx0, vy0, xmin, xmax, ymin, ymax):
  if not bound(vx0, vy0, xmin, xmax, ymin, ymax):
    return 0
  ylist = [y for x, y in complete(vx0, vy0, xmin, xmax, ymin, ymax)]
  return max(ylist) if ylist else 0

def solve1():
  ans = ymin
  for v0 in range(1, xmax + 1):
    for j in range(-300, 300):
      ans = max(ans, findymax(v0, j, xmin, xmax, ymin, ymax))
  return ans

def solve2():
  ans = 0
  for v0 in range(1, xmax + 1):
    for j in range(-100, 100):
      if bound(v0, j, xmin, xmax, ymin, ymax):
        ans += 1
  return ans

aoc.cprint(solve1())
aoc.cprint(solve2())
