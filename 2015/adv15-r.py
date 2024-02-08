import aoc
import re
import sys

def comps(n, limit, size):
  if size == 1:
    if 0 <= n < limit:
      yield [n]
  else:
    for i in range(limit):
      for seq in comps(n - i, limit, size - 1):
        yield [i] + seq

def sample(ing, perm, goal=None):
  count = 1
  if goal:
    calories = sum(v[4] * mult for mult, (name, v) in zip(perm, ing))
    if calories != 500:
      return 0
  for i in range(0, 4):
    fac = sum(v[i] * mult for mult, (name, v) in zip(perm, ing))
    fac = 0 if fac < 0 else fac
    count *= fac
  return count

ing = []
for line in sys.stdin:
  name, ingr = line.split(":")
  values = [int(i) for i in re.findall(r"-?\d+", ingr)]
  ing.append((name, values))

def search(ing, goal=None):
  return max(sample(ing, x, goal) for x in comps(100, 101, 4))

aoc.cprint(search(ing))
aoc.cprint(search(ing, 500))

