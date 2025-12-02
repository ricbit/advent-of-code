import sys
import re
import aoc

def solve(data):
  part1, part2 = 0, 0
  part1_regexp = re.compile(r"^(\d+)\1$")
  part2_regexp = re.compile(r"^(\d+)\1+$")
  for line in data:
    a, b = map(int, line.split("-"))
    for i in range(a, b + 1):
      s = str(i)
      if part1_regexp.match(s):
        part1 += i
      if part2_regexp.match(s):
        part2 += i
  return part1, part2

data = sys.stdin.read().strip().split(",")
part1, part2 = solve(data)
aoc.cprint(part1)
aoc.cprint(part2)
