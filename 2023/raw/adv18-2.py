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
  for vdir, vlen in commands:
    dy, dx = d[vdir]
    y += dy * vlen
    x += dx * vlen
    points.append((y, x))
  points.append(points[0])
  area = 0
  for (y1, x1), (y2, x2) in zip(points, points[1:]):
    area += x1 * y2 - x2 * y1
  area /= 2
  for vdir, vlen in commands:
    area += (vlen - 1) / 2
  commands.append(commands[0])
  for (vd1, vl1), (vd2, vl2) in zip(commands, commands[1:]):
    if vd1 == "R" and vd2 == "D":
      area += 3/4
    if vd1 == "R" and vd2 == "U":
      area += 1/4
    if vd1 == "L" and vd2 == "D":
      area += 1/4
    if vd1 == "L" and vd2 == "U":
      area += 3/4
    if vd1 == "D" and vd2 == "L":
      area += 3/4
    if vd1 == "D" and vd2 == "R":
      area += 1/4
    if vd1 == "U" and vd2 == "L":
      area += 1/4
    if vd1 == "U" and vd2 == "R":
      area += 3/4
  return int(area)

def parse_color(color):
  vlen = int(color[:5], 16)
  d = {0: "R", 1: "D", 2: "L", 3: "U"}
  return d[int(color[5])], vlen

commands = []
for line in sys.stdin:
  vdir, vlen, color = re.match(r"(\w+) (\d+) \(\#(\w{6})\)", line).groups()
  commands.append((vdir, int(vlen), parse_color(color)))

p1cmd = [(vdir, vlen) for vdir, vlen, vcolor in commands]
print(build(p1cmd))
p2cmd = [vcolor for vdir, vlen, vcolor in commands]
print(build(p2cmd))



