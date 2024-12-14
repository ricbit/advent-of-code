import math
import aoc
from collections import Counter

def decode(data):
  return data.py, data.px, data.vy, data.vx

def bots(data, ty, tx, n):
  for bot in data:
    y, x, vy, vx = decode(bot)
    y = (y + n * vy) % ty
    x = (x + n * vx) % tx
    yield y, x

def part1(data, ty, tx, n):
  h = Counter()
  for y, x in bots(data, ty, tx, n):
    a = 1 if y < ty // 2 else 0
    b = 2 if y > ty // 2 else 0
    c = 4 if x < tx // 2 else 0
    d = 8 if x > tx // 2 else 0
    if c + d >= 4 and a + b >= 1:
      h[a + b + c + d] += 1
  return math.prod(h.values())

def draw_tree(bots, ty, tx):
  t = [["."] * tx for _ in range(ty)]
  for y, x in bots:
    t[y][x] = "1"
  for line in t:
    print("".join(line))
  print()

def check_tree(data, ty, tx, n):
  m = set()
  for y, x in bots(data, ty, tx, n):
    if (y, x) in m:
      return False
    m.add((y, x))
  if len(m) == len(data):
    #draw_tree(m, ty, tx)
    return True
  return False

def part2(data, ty, tx):
  for n in range(1, 35000):
    if check_tree(data, ty, tx, n):
      return n

data = aoc.retuple_read("px_ py_ vx_ vy_", r"p=(-?\d+),(-?\d+) v=(-?\d+),(-?\d+)")
aoc.cprint(part1(data, 103, 101, 100))
aoc.cprint(part2(data, 103, 101))

