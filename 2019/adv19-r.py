import sys
import numpy as np
import itertools
import math
import aoc
from aoc.refintcode import IntCode

def check(j, i, data):
  cpu = IntCode(data)
  state = 0
  while cpu.run():
    match cpu.state:
      case cpu.INPUT:
        if state == 0:
          cpu.input = i
          state = 1
        elif state == 1:
          cpu.input = j
          state = 2
      case cpu.OUTPUT:
        state = 0
        return cpu.output

def part1(data):
  ans = 0
  first, last = 0, 0
  size = 7
  for j in range(size):
    line = []
    for i in range(size + 2):
      line.append(check(j, i, data))
    count = line.count(1)
    ans += count
    if count == 2:
      first = line.index(1)
      last = len(line) - line[::-1].index(1)
  first_array = []
  last_array = []
  outer = aoc.Interval(0, 49)
  for j in range(size, 50):
    while check(j, first, data) == 0:
      first += 1
    last += 1
    while check(j, last, data) == 1:
      last += 1
    last -= 1
    for m in outer.inter(aoc.Interval(first, last)):
      ans += m.end - m.begin + 1
    first_array.append(first)
    last_array.append(last)
  genpoly = lambda array : 49 * np.polyfit(list(range(size, 50)), array, 1)
  first_poly = genpoly(first_array)
  last_poly = genpoly(last_array)
  return ans, first_poly[0], last_poly[0]

def part2(data, first, last):
  x = (99 * first * (49 + last)) / 49 / (last - first)
  y = int(math.floor(49 / first * x))
  x = int(math.floor(x))
  while check(y, x, data) == 0:
    x += 1
  size = 100
  for j in itertools.count(y + 1):
    while check(j, x, data) == 0:
      x += 1
    if check(j - size + 1, x + size - 1, data) == 1:
      return j - size + 1 + 10000 * x

data = aoc.ints(sys.stdin.read().split(","))
beam_size, first, last = part1(data)
aoc.cprint(beam_size)
aoc.cprint(part2(data, first, last))

