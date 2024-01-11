import sys
import itertools
import aoc
from collections import *

lines = [line.strip() for line in sys.stdin]
ans1, ans2 = 0, 0
for line in lines:
  numbers = [int(i) for i in line.strip().split()]
  ans1 += max(numbers) - min(numbers)
  for a in itertools.combinations(numbers, 2):
    if max(a) % min(a) == 0:
      ans2 += max(a) // min(a)
aoc.cprint(ans1)
aoc.cprint(ans2)
