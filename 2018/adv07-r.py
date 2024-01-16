import sys
import itertools
import aoc

def solve1(graph, keys):
  inv = aoc.invert(graph)
  front = set(k for k in keys if len(inv[k]) == 0)
  visited = set()
  while front:
    worker = aoc.first(sorted(front))
    front.remove(worker)
    visited.add(worker)
    yield worker
    for dst in graph[worker]:
      if dst not in visited and all(w in visited for w in inv[dst]):
        front.add(dst)

def solve2(graph, keys):
  inv = aoc.invert(graph)
  front = set(k for k in keys if len(inv[k]) == 0)
  visited, tick = set(), {}
  maxworkers, fsize = 5, 60
  for w in itertools.count(0):
    finished = [worker for worker, time in tick.items() if time == 0]
    for worker in sorted(finished):
      visited.add(worker)
      del tick[worker]
      for nworker in graph[worker]:
        if nworker not in visited and all(w in visited for w in inv[nworker]):
          front.add(nworker)
    while len(tick) < maxworkers and front:
      worker = aoc.first(sorted(front))
      tick[worker] = fsize + ord(worker) - ord('A') + 1
      front.remove(worker)
    for worker in tick:
      tick[worker] -= 1
    if not front and not tick:
      return w

data = [line.strip() for line in sys.stdin]
graph = aoc.ddict(lambda: set())
keys = set()
for line in data:
  q = aoc.retuple("src dst", r".*?tep (.).*? step (.)", line)
  graph[q.src].add(q.dst)
  keys.add(q.src)
  keys.add(q.dst)
aoc.cprint("".join(solve1(graph, keys)))
aoc.cprint(solve2(graph, keys))
