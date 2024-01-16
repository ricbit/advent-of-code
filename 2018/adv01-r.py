import sys
import itertools
import aoc

line = aoc.ints(sys.stdin.readlines())
aoc.cprint(sum(line))
seen = set([0])
for freq in itertools.accumulate(itertools.cycle(line)):
  if freq in seen:
    aoc.cprint(freq)
    break
  seen.add(freq)
