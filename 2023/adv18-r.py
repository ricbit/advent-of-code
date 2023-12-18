import sys
import re

def shoelace(points):
  area = 0
  for (y1, x1), (y2, x2) in zip(points, points[1:] + [points[0]]):
    area += x1 * y2 - x2 * y1
  return area / 2

def area(commands):
  y, x = 0, 0
  d = {"R": (0, 1), "L": (0, -1), "U": (-1, 0), "D": (1, 0)}
  points = [(y, x)]
  for vdir, vlen in commands:
    dy, dx = d[vdir]
    y += dy * vlen
    x += dx * vlen
    points.append((y, x))
  return int(shoelace(points) + sum(vlen for vdir, vlen in commands) / 2 + 1)

def parse_color(color):
  vlen = int(color[:5], 16)
  d = {0: "R", 1: "D", 2: "L", 3: "U"}
  return d[int(color[5])], vlen

p1cmd, p2cmd = [], []
for line in sys.stdin:
  vdir, vlen, color = re.match(r"(\w+) (\d+) \(#(\w{6})\)", line).groups()
  p1cmd.append((vdir, int(vlen)))
  p2cmd.append(parse_color(color))

print(area(p1cmd))
print(area(p2cmd))
