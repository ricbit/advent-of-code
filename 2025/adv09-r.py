import sys
import itertools
import aoc

def area(p1, p2):
  return (1 + abs(p1[0] - p2[0])) * (1 + abs(p1[1] - p2[1]))

def part1(points):
  max_rect = 0
  for p1, p2 in itertools.combinations(points, 2):
    max_rect = max(max_rect, area(p1, p2))
  return max_rect

def fill(t, sides):
  for j, line in enumerate(sides):
    winding, last_side, pos = 0, 0, 0
    for i, side in sorted(line.items()):
      if winding > 0:
        for ii in range(pos, i):
          t[j][ii] = "x"
      if side != last_side:
        winding += side
        last_side = side
      pos = i

def draw_h_line(t, p1, p2, inverse):
  j = inverse[p1[0]]
  p1i = inverse[p1[1]]
  p2i = inverse[p2[1]]
  for i in range(min(p1i, p2i), 1 + max(p1i, p2i)):
    t[j][i] = "x"

def draw_v_line(t, p1, p2, inverse, sides, clockwise):
  i = inverse[p1[1]]
  p1j = inverse[p1[0]]
  p2j = inverse[p2[0]]
  for j in range(min(p1j, p2j), 1 + max(p1j, p2j)):
    t[j][i] = "x"
    sides[j][i] = clockwise * aoc.sgn(p1j - p2j)

def build_sides(t, points, inverse):
  clockwise = aoc.sgn(aoc.shoelace(points))
  sides = [{} for _ in range(t.h)]
  for p1, p2 in zip(points, points[1:] + [points[0]]):
    if p1[0] == p2[0]:
      draw_h_line(t, p1, p2, inverse)
    else:
      draw_v_line(t, p1, p2, inverse, sides, clockwise)
  return sides

def part2(points):
  reduced = sorted(set([p[0] for p in points] + [p[1] for p in points]))
  inverse = {v: i for i, v in enumerate(reduced)}
  pmax = max(inverse.values()) + 1
  t = aoc.Table([["."] * pmax for _ in range(pmax)])
  sides = build_sides(t, points, inverse)
  fill(t, sides)
  ms = aoc.MatrixSum(t)
  max_rect = 0
  for p1, p2 in itertools.combinations(points, 2):
    p1j, p1i = inverse[p1[0]], inverse[p1[1]]
    p2j, p2i = inverse[p2[0]], inverse[p2[1]]
    y1, y2 = min(p1j, p2j), max(p1j, p2j)
    x1, x2 = min(p1i, p2i), max(p1i, p2i)
    if ms.sum(y1, y2, x1, x2) == 0:
      max_rect = max(max_rect, area(p1, p2))
  return max_rect

data = sys.stdin.readlines()
points = [aoc.ints(line.split(",")) for line in data]
aoc.cprint(part1(points))
aoc.cprint(part2(points))
