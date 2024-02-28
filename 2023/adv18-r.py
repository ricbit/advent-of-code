import sys
import re
import aoc

DIRECTIONS = aoc.get_dir("U")

def area(commands):
  y, x = 0, 0
  points = [(y, x)]
  perimeter = 0
  for vdir, vlen in commands:
    dy, dx = DIRECTIONS[vdir]
    y += dy * vlen
    x += dx * vlen
    points.append((y, x))
    perimeter += vlen
  return int(aoc.shoelace(points) + perimeter / 2 + 1)

def parse_color(color):
  vlen = int(color[:5], 16)
  d = {0: "R", 1: "D", 2: "L", 3: "U"}
  return d[int(color[5])], vlen

p1cmd, p2cmd = [], []
for line in sys.stdin:
  vdir, vlen, color = re.match(r"(\w+) (\d+) \(#(\w{6})\)", line).groups()
  p1cmd.append((vdir, int(vlen)))
  p2cmd.append(parse_color(color))

aoc.cprint(area(p1cmd))
aoc.cprint(area(p2cmd))
