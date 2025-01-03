import sys
import aoc
from collections import Counter

def fly(horse):
  while True:
    yield (horse.v, horse.time)
    yield (0, horse.rest)

def position(horse, t):
  dist = 0
  for v, dt in fly(horse):
    if dt < t:
      dist += v * dt
      t -= dt
    else:
      dist += v * t
      return dist
  return None

horses = []
for line in sys.stdin:
  horses.append(aoc.retuple("name v_ time_ rest_",
      r"(\w+).*?(\d+).*?(\d+).*?(\d+)", line))
aoc.cprint(max(position(h, 2503) for h in horses))
c = Counter()
for j in range(1, 2503 + 1):
  v = [(position(h, j), i) for i, h in enumerate(horses)]
  v.sort(reverse=True)
  vmax = v[0][0]
  for hh, ii in v:
    if hh == vmax:
      c[ii] += 1
aoc.cprint(max(c.values()))
