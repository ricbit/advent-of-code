import sys
import itertools
import aoc

def solve(data):
  pos = 0
  while pos < len(data):
    if data[pos] == 1:
      a, b, c = data[pos + 1: pos + 4]
      data[c] = data[a] + data[b]
      pos += 4
    elif data[pos] == 2:
      a, b, c = data[pos + 1: pos + 4]
      data[c] = data[a] * data[b]
      pos += 4
    elif data[pos] == 99:
      break
  return data[0]

def part2(data):
  for a, b in itertools.product(range(50), repeat=2):
    data = original_data[:]
    data[1] = a
    data[2] = b
    solve(data)
    if data[0] == 19690720:
      return data[1] * 100 + data[2]

def part1(data):
  data = data[:]
  data[1] = 12
  data[2] = 2
  return solve(data)

original_data = [int(i) for i in sys.stdin.read().split(",")]
aoc.cprint(part1(original_data))
aoc.cprint(part2(original_data))
