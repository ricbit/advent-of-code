import sys
import aoc

def simple(jumps, comp):
  pos = 0
  step = 0
  while 0 <= pos < len(jumps):
    npos = pos + jumps[pos]
    if comp(jumps[pos]):
      jumps[pos] -= 1
    else:
      jumps[pos] += 1
    pos = npos
    step += 1
  return step

lines = [int(line.strip()) for line in sys.stdin]
aoc.cprint(simple(lines[:], lambda x: False))
aoc.cprint(simple(lines, lambda x: x >= 3))
