import sys
import string
import aoc

def part1(data):
  ans = 0
  for block in data:
    ans += len(set("".join(block)))
  return ans

def part2(data):
  ans = 0
  for block in data:
    common = set(string.ascii_lowercase)
    for line in block:
      common.intersection_update(set(line))
    ans += len(common)
  return ans

data = aoc.line_blocks()
aoc.cprint(part1(data))
aoc.cprint(part2(data))
