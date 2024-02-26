import sys
import itertools
import aoc
from aoc.refintcode import IntCode

def part2(data):
  for a, b in itertools.product(range(80), repeat=2):
    data = original_data[:]
    data[1] = a
    data[2] = b
    cpu = IntCode(data)
    cpu.run()
    if cpu.data[0] == 19690720:
      return cpu.data[1] * 100 + cpu.data[2]

def part1(data):
  data = data[:]
  data[1] = 12
  data[2] = 2
  cpu = IntCode(data)
  cpu.run()
  return cpu.data[0]

original_data = aoc.ints(sys.stdin.read().split(","))
aoc.cprint(part1(original_data))
aoc.cprint(part2(original_data))
