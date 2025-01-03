import sys
import aoc

line = sys.stdin.read().strip()

def solve(line, offset):
  total, n = 0, len(line)
  for i, digit in enumerate(line):
    if digit == line[(i + offset) % n]:
      total += int(digit)
  return total

aoc.cprint(solve(line, 1))
aoc.cprint(solve(line, len(line) // 2))
