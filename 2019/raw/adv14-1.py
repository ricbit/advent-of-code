import sys
import string
import re
import itertools
import math
import cmath
import aoc
import heapq
import functools
import copy
from collections import Counter, deque
from dataclasses import dataclass

def solve(graph):
  vnext = deque(["FUEL"])
  cost = 0
  left = aoc.ddict(lambda: 0)
  needed = aoc.ddict(lambda: 0)
  needed["FUEL"] = 1
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
    print(f"to build {requests} requests of {name}")
    for res_size, res_name in resources:
      needed[res_name] += res_size * requests
      vnext.append(res_name)
      print(f"  i need {res_size * requests} {res_name}")
    print(f"left {left}\n")
  return cost

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
aoc.cprint(solve(graph))
