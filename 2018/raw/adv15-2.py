import sys
import string
import re
import itertools
import math
import aoc
import heapq
import functools
import copy
from collections import Counter, deque
from dataclasses import dataclass

#+7

@dataclass(init=True, repr=True, order=True)
class Unit:
  y: int
  x: int
  ctype: str
  enemy: str
  hp: int
  attack: int
  dead: bool
  used: bool

def search_unit(j, i, units):
  for k in range(len(units)):
    if units[k].y == j and units[k].x == i and not units[k].dead:
      return k

def reachable(t, y, x, enemy):
  vnext = deque([(y, x, [])])
  visited = set()
  while vnext:
    y, x, path = vnext.popleft()
    if (y, x) in visited:
      continue
    visited.add((y, x))
    if any(t[j][i] == enemy for j, i in t.iter_neigh4(y, x)):
      yield (len(path), path)
    for j, i in sorted(t.iter_neigh4(y, x)):
      if (j, i) not in visited and t[j][i] == ".":
        vnext.append((j, i, path + [(j, i)]))

def move_unit(t, units, ku):
  unit = units[ku]
  if unit.dead:
    return
  t[unit.y][unit.x] = "."
  paths = list(reachable(t, unit.y, unit.x, unit.enemy))
  if paths:
    path = min(paths)
    if path and path[0]:
      j, i = path[1][0]
      t[j][i] = unit.ctype
      units[ku].y = j
      units[ku].x = i
      return
  t[unit.y][unit.x] = unit.ctype

def select_target(t, unit, units):
  for j, i in t.iter_neigh4(unit.y, unit.x):
    if t[j][i] == unit.enemy:
      enemy = search_unit(j, i, units)
      if units[enemy].dead:
        continue
      yield (units[enemy].hp, units[enemy].y, units[enemy].x, enemy)

def supremacy(units):
  count = Counter()
  for unit in units:
    if not unit.dead:
      count[unit.ctype] += unit.hp
  if len(count) == 1:
    return aoc.first(count.items())[1]
  return None

def tprint(t):
  for line in t.table:
    print("".join(line))
  print()

def clear_units(units):
  for i in range(len(units)):
    units[i].used= False

def has_units(units):
  return any((not unit.used) and (not unit.dead) for unit in units)

def get_next_unit(units):
  avail = []
  for i, unit in enumerate(units):
    if (not unit.used) and (not unit.dead):
      avail.append((unit.y, unit.x, i, unit))
  return min(avail)[2:4]

def solve(original, elf_attack, elf_kills=True):
  units = []
  t = copy.deepcopy(t)
  for j, i in t.iter_all():
    if t[j][i] in "GE":
      enemy = "G" if t[j][i] == "E" else "E"
      attack = elf_attack if t[j][i] == "E" else 3
      units.append(Unit(j, i, t[j][i], enemy, 200, attack, False, False))
  for tick in itertools.count(0):
    clear_units(units)
    while has_units(units):
      ku, unit = get_next_unit(units)
      units[ku].used = True
      move_unit(t, units, ku)
      targets = list(select_target(t, unit, units))
      if targets:
        target = min(targets)[3]
        #print(f"{unit} attacks {units[target]}")
        units[target].hp -= unit.attack
        if units[target].hp <= 0:
          tprint(t)
          t[units[target].y][units[target].x] = "."
          units[target].dead = True
          if units[target].ctype == "E" and not elf_kills:
            return None
          #print("---")
          #for unit in units:
          #  print(unit)
        if (score := supremacy(units)) is not None:
          #tprint(t)
          #print(tick, score)
          kludge = 0 if any((not unit.dead) and (not unit.used) for unit in units) else 1
          for unit in units:
            if not unit.dead:
              print(unit)
          return (tick + kludge) * score

def search(t):
  for i in itertools.count(3):
    if (score := solve(t, i, False)) is not None:
      return score

t = aoc.Table.read()
aoc.cprint(solve(t, 3))
aoc.cprint(search(t))
