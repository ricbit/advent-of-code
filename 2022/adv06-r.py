import sys
import aoc

def solve(lines, distinct):
  for line in lines:
    for index in range(len(line.strip()) - distinct):
      if len(set(line[index:index + distinct])) == distinct:
        return index + distinct
      
lines = [line.strip() for line in sys.stdin]
aoc.cprint(solve(lines, 4))
aoc.cprint(solve(lines, 14))
