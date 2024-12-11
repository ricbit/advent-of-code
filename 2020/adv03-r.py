import sys
import aoc

def count(t, sy, sx):
  y, x = 0, 0
  ans = 0
  while y < t.h - 1:
    y += sy
    x = (x + sx) % t.w
    if t[y][x] == "#":
      ans += 1
  return ans

def solve(data):
  slopes = [(1,1), (1,3), (1,5), (1,7), (2,1)]
  ans = 1
  for sy, sx in slopes:
    ans *= count(data, sy, sx)
  return ans

data = aoc.Table.read()
aoc.cprint(count(data, 1, 3))
aoc.cprint(solve(data))
