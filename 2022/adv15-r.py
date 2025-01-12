import re
import sys
import aoc
  
limit = 4000000
lines = sys.stdin.readlines()
data = []
for line in lines:
  search = re.search(r"x=(-?\d+).*y=(-?\d+).*x=(-?\d+).*y=(-?\d+)", line)
  sx, sy, bx, by = [int(i) for i in search.groups()]
  data.append((sx, sy, bx, by))

def forbidden(data, y):
  reachable = []
  for sx, sy, bx, by in data:
    delta = abs(sx - bx) + abs(sy - by)
    dx = delta - (abs(sy - y))
    if dx <= 0:
      continue
    if not reachable:
      reachable.append(aoc.Interval(sx - dx, dx + sx))
    else:
      union = aoc.Interval(sx - dx, dx + sx)
      goal, diff = [], []
      for r in reachable:
        inter = list(union.inter(r))
        if inter:
          goal.append(aoc.first(union.union(r)))
        else:
          diff.append(r)
      if len(goal) == 0:
        reachable.append(union)
      else:
        if len(goal) > 1:
          goal = [aoc.first(goal[0].union(goal[1]))]
        reachable = list(sorted(goal + diff))
  return reachable

def part1(data):
  intervals = forbidden(data, 2000000)
  return sum(len(interval) - 1 for interval in intervals)

def part2(data):
  for y in range(0, limit + 1):
    if y % 1000 == 0:
      print(y)
    components = forbidden(data, y)
    if len(components) > 1:
      for a, b in zip(components, components[1:]):
        if b.begin - a.end >= 1:
          print(y + 4000000 * ((int(b.begin) + int(a.end)) // 2))
          return

aoc.cprint(part1(data))
#aoc.cprint(part2(data))
