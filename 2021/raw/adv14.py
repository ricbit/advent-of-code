import sys
import itertools
import collections

lines = sys.stdin.readlines()
seed = lines[0].strip()
rules = {}
for line in lines[2:]:
  src, dst = line.strip().split(" -> ")
  rules[src] = dst

def grow(current):
  middle = []
  for s in zip(current, current[1:]):
    middle.append(rules["".join(s)])
  x = itertools.zip_longest(current, middle, fillvalue=" ")
  return "".join(itertools.chain.from_iterable(x)).strip()

for i in range(40):
  seed = grow(seed)

hist = collections.Counter()
for c in seed:
  hist[c] += 1

counts = list(hist.items())
counts.sort(key=lambda x: x[1])
print(counts[-1][1] - counts[0][1])
