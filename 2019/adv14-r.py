import sys
import math
import aoc
import bisect
from collections import deque

def solve(graph, fuels):
  vnext = deque(["FUEL"])
  cost = 0
  left = aoc.ddict(lambda: 0)
  needed = aoc.ddict(lambda: 0)
  needed["FUEL"] = fuels
  while vnext:
    name = vnext.popleft()
    if name == "ORE":
      cost += needed[name]
      needed[name] = 0
      continue
    if left[name] >= needed[name]:
      left[name] -= needed[name]
      needed[name] = 0
      continue
    if needed[name] == 0:
      continue
    needed[name] -= left[name]
    minsize, resources = graph[name]
    requests = math.ceil(needed[name] / minsize)
    left[name] = minsize * requests - needed[name]
    needed[name] = 0
    for res_size, res_name in resources:
      needed[res_name] += res_size * requests
      vnext.append(res_name)
  return cost

def search(graph, cargo):
  solve_key = lambda x: solve(graph, x)
  return bisect.bisect_right(range(cargo), cargo, key=solve_key) - 1

data = [line.strip() for line in sys.stdin]
graph = {}
for line in data:
  all_resources, goal = line.split(" => ")
  goal_size, goal_name = goal.strip().split()
  resources = []
  for res in all_resources.split(","):
    res_size, res_name = res.strip().split()
    resources.append((int(res_size), res_name))
  graph[goal_name] = (int(goal_size), resources)
aoc.cprint(solve(graph, 1))
aoc.cprint(search(graph, 1000000000000))
