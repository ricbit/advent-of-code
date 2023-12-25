import sys
import re
import itertools
import math
import aoc

def build(commands):
  size = 2000
  y, x = 0, 0
  d = {"R": (0 ,1), "L": (0, -1), "U": (-1, 0), "D": (1, 0)}
  points = [(y, x)]
  for vdir, vlen, color in commands:
    dy, dx = d[vdir]
    for i in range(vlen):
      y += dy 
      x += dx
      points.append((y, x))
  miny = min(y for y,x in points)
  minx = min(x for y,x in points)
  points = [(y-miny, x-minx) for y,x in points]
  maxy = max(y for y,x in points)
  maxx = max(x for y,x in points)
  m = [["."] * (1+maxx) for _ in range(1+maxy)]
  for y,x in points:
    m[y][x] = "#"
  y = 1
  x = "".join(m[y]).index("#") + 1
  t = aoc.Table(m)
  vnext = [(y, x)]
  visited = set(vnext)
  while vnext:
    y, x = vnext.pop()
    for j, i in t.iter_neigh4(y, x):
      if m[j][i] == "." and (j, i) not in visited:
        vnext.append((j, i))
        visited.add((j, i))
  ans = 0
  for line in m:
    ans += "".join(line).count("#")
  return ans + len(visited)
  #for line in m:
  #    print( "".join(line))

commands = []
for line in sys.stdin:
  vdir, vlen, color = re.match(r"(\w+) (\d+) \(\#(\w{6})\)", line).groups()
  commands.append((vdir, int(vlen), color))
print(build(commands))
