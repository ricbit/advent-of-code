import itertools
import aoc
import copy
from collections import Counter, deque
from dataclasses import dataclass

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
  for unit in units:
    if unit.y == j and unit.x == i and not unit.dead:
      return unit

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

def move_unit(t, unit):
  t[unit.y][unit.x] = "."
  for pathlen, path in aoc.ifirst(sorted(reachable(t, unit.y, unit.x, unit.enemy))):
    if pathlen:
      j, i = path[0]
      t[j][i] = unit.ctype
      unit.y = j
      unit.x = i
      return
  t[unit.y][unit.x] = unit.ctype

def select_target(t, unit, units):
  for j, i in t.iter_neigh4(unit.y, unit.x):
    if t[j][i] == unit.enemy:
      enemy = search_unit(j, i, units)
      yield ((enemy.hp, enemy.y, enemy.x), enemy)

def supremacy(units):
  count = Counter()
  for unit in units:
    if not unit.dead:
      count[unit.ctype] += unit.hp
  if len(count) == 1:
    return aoc.first(count.items())[1]
  return None

def clear_units(units):
  for unit in units:
    unit.used = False

def has_units(units):
  return any((not unit.used) and (not unit.dead) for unit in units)

def get_next_unit(units):
  avail = []
  for unit in units:
    if (not unit.used) and (not unit.dead):
      avail.append((unit.y, unit.x, unit))
  return min(avail)[2]

def find_units(t, elf_attack):
  for j, i in t.iter_all():
    if t[j][i] in "GE":
      enemy = "G" if t[j][i] == "E" else "E"
      attack = elf_attack if t[j][i] == "E" else 3
      yield Unit(j, i, t[j][i], enemy, 200, attack, False, False)

def solve(original, elf_attack, elf_kills=True):
  units = list(find_units(original, elf_attack))
  t = copy.deepcopy(original)
  for tick in itertools.count(0):
    clear_units(units)
    while has_units(units):
      unit = get_next_unit(units)
      unit.used = True
      move_unit(t, unit)
      targets = sorted(select_target(t, unit, units))
      for _, target in aoc.ifirst(targets):
        target.hp -= unit.attack
        if target.hp <= 0:
          t[target.y][target.x] = "."
          target.dead = True
          if target.ctype == "E" and not elf_kills:
            return None
        if (score := supremacy(units)) is not None:
          kludge = 0 if any((not unit.dead) and (not unit.used) for unit in units) else 1
          return (tick + kludge) * score

def search(t):
  for i in itertools.count(3):
    if (score := solve(t, i, False)) is not None:
      return score

t = aoc.Table.read()
aoc.cprint(solve(t, 3))
aoc.cprint(search(t))
