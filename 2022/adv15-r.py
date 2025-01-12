import re
import sys
import aoc
import z3

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

def zabs(x):
  return z3.If(x >= 0, x, -x)

def part2(data):
  x = z3.Int('x')
  y = z3.Int('y')
  constr = [0 <= x, x <= 4000000, 0 <= y, y <= 4000000]
  for sx, sy, bx, by in data:
    constr.append(zabs(sx - x) + zabs(sy - y) > zabs(sx - bx) + zabs(sy - by))
  s = z3.Solver()
  s.add(z3.And(*constr))
  s.check()
  m = s.model()
  xm = int(str(m.evaluate(x)))
  ym = int(str(m.evaluate(y)))
  return xm * 4000000 + ym

aoc.cprint(part1(data))
aoc.cprint(part2(data))
