import re
import sys
from interval import interval
  
limit = 4000000
lines = sys.stdin.readlines()
data = []
for line in lines:
  search = re.search(r"x=(-?\d+).*y=(-?\d+).*x=(-?\d+).*y=(-?\d+)", line)
  sx, sy, bx, by = [int(i) for i in search.groups()]
  data.append((sx, sy, bx, by))

def search():
  for y in range(0, limit + 1):
    if y % 1000 == 0:
      print(y)
    empty = interval()
    for sx, sy, bx, by in data:
      delta = abs(sx - bx) + abs(sy - by)
      dx = delta - (abs(sy - y))
      if dx <= 0:
        continue
      empty = interval.union([empty, interval[sx - dx, dx + sx]])
    components = list(empty.components)
    if len(components) > 1:
      for a, b in zip(components, components[1:]):
        if b[0][0] - a[0][1] > 1:
          print(y + 4000000 * ((int(b[0][0]) + int(a[0][1])) // 2))
          return

search()
