import sys
import aoc

def sliding(lines, n):
  ans = 0
  for batch in zip(*(lines[x:] for x in range(n - 1, -1, -1))):
    if sum(batch[:-1]) > sum(batch[1:]):
      ans += 1
  return ans

lines = aoc.ints(sys.stdin.read().split())
aoc.cprint(sliding(lines, 2))
aoc.cprint(sliding(lines, 4))
