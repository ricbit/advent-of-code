import itertools
import aoc
import copy
from collections import Counter
from dataclasses import dataclass

@dataclass(init=False, repr=True, unsafe_hash=True)
class Unit:
  size: int
  hp: int
  attack: int
  attack_type: str
  weak: tuple[str]
  immune: tuple[str]
  init: int
  ctype: int
  etype: int
  dead: bool

def parse_units(block, ctype, etype):
  units = []
  for line in block[1:]:
    q = aoc.retuple("size_ hp_ weaks atk_ atktype init_",
        r"(\d+).*?(\d+)[^(]*?((?:\(.*\))?)[^(]*?(\d+) (\w+) .*?(\d+)", line)
    u = Unit()
    u.size = q.size
    u.hp = q.hp
    u.attack = q.atk
    u.attack_type = q.atktype
    u.init = q.init
    u.ctype = ctype
    u.etype = etype
    u.dead = False
    u.weak = tuple()
    u.immune = tuple()
    if q.weaks:
      weaks = q.weaks.strip()[1:-1]
      for weak in weaks.split(";"):
        weak = weak.split(" to ")
        weaklist = (weakness.strip() for weakness in weak[1].split(","))
        if weak[0].strip() == "weak":
          u.weak = tuple(weaklist)
        else:
          u.immune = tuple(weaklist)
    units.append(u)
  return units

def damage(a, b):
  power = a.size * a.attack
  if a.attack_type in b.immune:
    return 0
  if a.attack_type in b.weak:
    return power * 2
  return power

def finished(units):
  unit_types = Counter()
  for unit in units:
    if not unit.dead:
      unit_types[unit.ctype] += 1
  return len(unit_types) == 1

def simulate(units):
  visited = set()
  while not finished(units):
    alive = [unit for unit in units if not unit.dead]
    alive.sort(reverse=True, key=lambda unit: (unit.size * unit.attack, unit.init))
    if tuple(alive) in visited:
      return False
    visited.add(tuple(alive))
    chosen = [False] * len(alive)
    target = [None] * len(alive)
    for a, unit in enumerate(alive):
      enemies = []
      for b, enemy in enumerate(alive):
        if enemy.ctype != unit.ctype and not chosen[b] and not enemy.dead:
          enemies.append((enemy, b))
      if enemies:
        enemy, b = max(enemies, key=lambda enemy:
          (damage(unit, enemy[0]), enemy[0].size * enemy[0].attack, enemy[0].init))
        if damage(unit, enemy) > 0:
          target[a] = b
          chosen[b] = True
    for i in sorted(range(len(alive)), reverse=True, key=lambda q: alive[q].init):
      if target[i] is not None and not alive[i].dead:
        a = alive[i]
        b = alive[target[i]]
        dead = damage(a, b) // b.hp
        b.size -= dead
        if b.size <= 0:
          b.dead = True
  return any(unit.ctype == 0 and not unit.dead for unit in units)

def find_boost(units):
  for i in itertools.count(1):
    boosted = copy.deepcopy(units)
    for unit in boosted:
      if unit.ctype == 0:
        unit.attack += i
    if simulate(boosted):
      return units_alive(boosted)

def units_alive(units):
  return sum(u.size for u in units if not u.dead)

def single(units):
  units = copy.deepcopy(units)
  simulate(units)
  return units_alive(units)

blocks = aoc.line_blocks()
immune = parse_units(blocks[0], 0, 1)
infection = parse_units(blocks[1], 1, 0)
units = list(itertools.chain(immune, infection))
aoc.cprint(single(units))
aoc.cprint(find_boost(units))
