import sys
import re
import itertools
import math
import aoc
import copy
import heapq
from collections import *

def all_loadings(old_floor):
  left = list(old_floor)
  for a, b in itertools.combinations(old_floor, 2):
    if (a >> 1) != (b >> 1) and (a & 1) != (b & 1):
      continue
    left.remove(a)
    left.remove(b)
    yield (a, b), tuple(left)
    left.append(a)
    left.append(b)
  for a in old_floor:
    left.remove(a)
    yield (a,), tuple(left)
    left.append(a)

def move_elevator(elevator):
  if elevator > 0:
    yield elevator - 1
  if elevator < 3:
    yield elevator + 1

def valid(floor):
  matches = aoc.ddict(lambda: [])
  for g in floor:
    name, kind = g >> 1, g & 1
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
    ans.append(tuple(sorted(x)))
  return tuple(ans)

def heuristic(floors, score):
  score += 1
  for i, f in enumerate(floors[:3]):
    score += (len(f) + 1) // 2 * (3 - i)
  return score

def canonical(floors):
  floors = ttuple(floors)
  names = {}
  cur = 0
  for line in floors:
    for gg in line:
      n, g = gg >> 1, gg & 1
      if n not in names:
        names[n] = cur
        cur += 2
  new = [[] for _ in range(4)]
  for i in range(4):
    for gg in floors[i]:
      new[i].append(names[gg >> 1] + (gg & 1))
  return ttuple(new)

def simulate(floors):
  elevator = 0
  vnext = [(0, 0, elevator, ttuple(floors))]
  visited = set()
  cc = 0
  while vnext:
    h, score, elevator, floors = heapq.heappop(vnext)
    cc += 1
    if cc % 100 == 0:
      print(len(vnext), h, score, len(visited))
    if finished(floors):
      return score
    visited.add((elevator, floors))
    for move, left in all_loadings(floors[elevator]):
      for e in move_elevator(elevator):
        new_floors = [list(x) for x in floors]
        new_floors[e].extend(move)
        new_floors[elevator] = left
        new_floors = canonical(new_floors)
        if valid(new_floors[e]) and valid(new_floors[elevator]):
          if (e, new_floors) not in visited:
            heapq.heappush(vnext,
                (heuristic(new_floors, score), score + 1, e, new_floors))
            visited.add((e, new_floors))

def rename(old):
  cur = 0
  names = {}
  for line in old:
    for n, g in line:
      if n not in names:
        names[n] = cur
        cur += 2
  new = [[] for _ in range(4)]
  for i in range(4):
    for n, g in old[i]:
      new[i].append(names[n] + (0 if g.startswith("g") else 1))
  return ttuple(new)

ordinals = {"first": 0, "second": 1, "third": 2, "fourth": 3}
floors = [[] for _ in range(4)]
for line in sys.stdin:
  name = ordinals[re.match(r".*?(" + "|".join(ordinals.keys()) + ")", line).group(1)]
  items = re.findall(r"(\w+)(?:-compatible)? (microchip|generator)", line)
  floors[name].extend([tuple(x[:2]) for x in items])
floors[0].append(("el", "ge"))
floors[0].append(("el", "mi"))
floors[0].append(("di", "ge"))
floors[0].append(("di", "mi"))
aoc.cprint(simulate(rename(floors)))

  
