import sys
import re
from collections import defaultdict
import itertools

def happy(graph, perm):
  ans = 0
  for i in range(len(perm)):
    bef = (i - 1) % len(perm)
    aft = (i + 1) % len(perm)
    ans += graph[perm[i]][perm[bef]]
    ans += graph[perm[i]][perm[aft]]
  return ans

def best(graph):
  return max(happy(graph, perm) for perm in itertools.permutations(graph.keys()))

graph = defaultdict(lambda: defaultdict(lambda: 0))
for line in sys.stdin:
  m = re.match(r"(\w+) would (\w+) (\d+) .* (\w+).", line).groups()
  val = int(m[2]) if m[1] == "gain" else -int(m[2])
  graph[m[0]][m[3]] = val
graph["ricbit"]["ricbit"] = 0
print(best(graph))
