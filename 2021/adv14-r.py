import aoc
from collections import Counter

def solve(seed, rules, steps):
  count = Counter()
  for a, b in zip(seed, seed[1:]):
    count[a + b] += 1
  for _ in range(steps):
    newcount = Counter()
    for (a, b), c in count.items():
      x = rules[a + b]
      newcount[a + x] += c
      newcount[x + b] += c
    count = newcount
  element = Counter()
  for (a, b), c in count.items():
    element[a] += c
    element[b] += c
  element[seed[0]] += 1
  element[seed[-1]] += 1
  return (max(element.values()) - min(element.values())) // 2

data = aoc.line_blocks()
seed = data[0][0]
rules = {}
for line in data[1]:
  q = aoc.retuple("src dst", r"(.\w+) -> (.)", line)
  rules[q.src] = q.dst
aoc.cprint(solve(seed, rules, 10))
aoc.cprint(solve(seed, rules, 40))
