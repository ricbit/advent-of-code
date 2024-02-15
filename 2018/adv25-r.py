import sys
import itertools
import aoc

def solve(data):
  graph = aoc.ddict(lambda: set())
  for a, b in itertools.combinations(range(len(data)), 2):
    if sum(abs(i - j) for i, j in zip(data[a], data[b])) <= 3:
      graph[a].add(b)
      graph[b].add(a)
  free = set(range(len(data)))
  while free:
    group = set()
    start = aoc.first(free)
    vnext = [start]
    while vnext:
      a = vnext.pop()
      if a not in free:
        continue
      group.add(a)
      free.remove(a)
      for b in graph[a]:
        if b in free:
          vnext.append(b)
    yield group

data = [aoc.ints(line.split(",")) for line in sys.stdin]
aoc.cprint(len(list(solve(data))))
