import sys
import re
import itertools
import math
import aoc
import copy
import heapq
from collections import *

def all_loadings(old_floor):
  floor = [list(x) for x in old_floor]
  for a, b in itertools.combinations(floor, 2):
    if a[1] == "generator" and b[1] == "microchip" and a[0] != b[0]:
      continue
    left = floor[:]
    left.remove(a)
    left.remove(b)
    yield (a, b), tuple(left)
  for a in floor:
    left = floor[:]
    left.remove(a)
    yield (a,), tuple(left)

def move_elevator(elevator):
  if elevator > 0:
    yield elevator - 1
  if elevator < 3:
    yield elevator + 1

def valid(floor):
  matches = aoc.ddict(lambda: [])
  for name, kind in floor:
    matches[name].append(kind)
  unmatched = set()
  for name, kinds in matches.items():
    if len(kinds) == 1:
      unmatched.add(kinds[0])
  return len(unmatched) < 2

def print_floor(floors):
  for i in reversed(range(4)):
    print(i, floors[i])
  print()

def finished(floors):
  return sum(len(floor) for floor in floors[:3]) == 0

def ttuple(floors):
  ans = []
  for x in floors:
    y = (tuple(k) for k in x)
    ans.append(tuple(sorted(y)))
  return tuple(ans)
  #return tuple(tuple(tuple(y) for y in sorted(x)) for x in floors)

def heuristic(floors, score):
  score += 1
  for i, f in enumerate(floors[:3]):
    score += (len(f) + 1) // 2 * (3 - i)
  return score

def simulate(floors):
  elevator = 0
  vnext = [(0, 0, elevator, ttuple(floors))]
  visited = set()
  cc = 0
  while vnext:
    h, score, elevator, floors = heapq.heappop(vnext)
    cc += 1
    if cc % 100 == 0:
      print(len(vnext), h, score)
    if finished(floors):
      #for plan in path:
      #  print_floor(plan)
      return score
    visited.add((elevator, floors))
    for move, left in all_loadings(floors[elevator]):
      for e in move_elevator(elevator):
        new_floors = [list(x) for x in floors]
        new_floors[e].extend(move)
        new_floors[elevator] = left
        new_floors = ttuple(new_floors)
        if valid(new_floors[e]) and valid(new_floors[elevator]):
          if (e, new_floors) not in visited:
            heapq.heappush(vnext,
                (heuristic(new_floors, score), score + 1, e, new_floors))
            visited.add((e, new_floors))
      
ordinals = {"first": 0, "second": 1, "third": 2, "fourth": 3}
floors = [[] for _ in range(4)]
for line in sys.stdin:
  name = ordinals[re.match(r".*?(" + "|".join(ordinals.keys()) + ")", line).group(1)]
  items = re.findall(r"(\w+)(?:-compatible)? (microchip|generator)", line)
  floors[name].extend([tuple(x[:2]) for x in items])
aoc.cprint(simulate(ttuple(floors)))

  
