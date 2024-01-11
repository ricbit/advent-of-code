import sys
import aoc
from collections import *

line = sys.stdin.read().strip()

ans = 0
for a, b in zip(line, line[1:] + line[0]):
  if a == b:
    ans += int(a)
aoc.cprint(ans)

ans = 0
n = len(line)
for i, a in enumerate(line):
  if a == line[(i + n // 2) % n]:
    ans += int(a)
aoc.cprint(ans)
  
