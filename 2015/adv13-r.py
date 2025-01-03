import sys
import itertools
import aoc

def happy(graph, perm):
  ans = 0
  for i in range(len(perm)):
    bef = (i - 1) % len(perm)
    aft = (i + 1) % len(perm)
    ans += graph[perm[i]][perm[bef]]
    ans += graph[perm[i]][perm[aft]]
  return ans

def best(graph):
  perms = itertools.permutations(graph.keys())
  return max(happy(graph, perm) for perm in perms)

graph = aoc.ddict(lambda: aoc.ddict(lambda: 0))
for line in sys.stdin:
  q = aoc.retuple("src action value_ dst",
    r"(\w+) would (\w+) (\d+) .* (\w+).", line)
  if q.action == "gain":
    graph[q.src][q.dst] = q.value
  else:
    graph[q.src][q.dst] = -q.value
aoc.cprint(best(graph))
graph["ricbit"]["ricbit"] = 0
aoc.cprint(best(graph))
