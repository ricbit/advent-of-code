import aoc
import sys

ops = sys.stdin.read().strip()
basement = None
level = 0
for i, c in enumerate(ops):
  if c == "(":
    level += 1
  elif c == ")":
    level -= 1
  if level == -1 and basement is None:
    basement = i + 1
aoc.cprint(level)
aoc.cprint(basement)
