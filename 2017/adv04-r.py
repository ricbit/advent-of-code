import sys
import aoc

lines = [line.strip() for line in sys.stdin]
ans1, ans2 = 0, 0
for line in lines:
  words = line.split()
  if len(words) == len(set(words)):
    ans1 += 1
  words = ["".join(sorted(w)) for w in words]
  if len(words) == len(set(words)):
    ans2 += 1
aoc.cprint(ans1)
aoc.cprint(ans2)
