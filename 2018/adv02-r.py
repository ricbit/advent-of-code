import sys
import itertools
import aoc
from collections import Counter

def find(a, b):
  count = 0
  for i in range(len(a)):
    if a[i] != b[i]:
      last = a[i]
      count += 1
  if count == 1:
    return a[:a.index(last)] + a[a.index(last) + 1:]
  return None

def check(line, n):
  c = Counter()
  for x in line:
    c[x] += 1
  return n in c.values()

lines = [line.strip() for line in sys.stdin]
has2 = sum(check(line, 2) for line in lines)
has3 = sum(check(line, 3) for line in lines)
aoc.cprint(has2 * has3)
for a, b in itertools.combinations(lines, 2):
  if c := find(a, b):
    aoc.cprint(c)
    break
