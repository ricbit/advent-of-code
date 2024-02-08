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

@dataclass(init=False, repr=True)
class Unit:
  size: int
  hp: int
  attack: int
  attack_type: str
  weak: set[str]
  immune: set[str]
  init: int
  ctype: int
  etype: int
  dead: bool

def solve(data):
  return 0

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
    u.weak = set()
    u.immune = set()
    u.ctype = ctype
    u.etype = etype
    u.dead = False
    if q.weaks:
      weaks = q.weaks.strip()[1:-1]
      for weak in weaks.split(";"):
        weak = weak.split(" to ")
        weaklist = (weakness.strip() for weakness in weak[1].split(","))
        if weak[0].strip() == "weak":
          u.weak.update(weaklist)
        else:
          u.immune.update(weaklist)
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
  while not finished(units):
    alive = [unit for unit in units if not unit.dead]
    alive.sort(reverse=True, key=lambda unit: (unit.size * unit.attack, unit.init))
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
    order = [(alive[i].init, i) for i in range(len(alive))]
    order.sort(reverse=True)
    for _, i in order:
      if target[i] is not None and not alive[i].dead:
        a = alive[i]
        b = alive[target[i]]
        dead = damage(a, b) // b.hp
        b.size -= dead
        if b.size <= 0:
          b.dead = True
  print(units)
  return sum(u.size for u in units if not u.dead)

blocks = aoc.line_blocks()
immune = parse_units(blocks[0], 0, 1)
infection = parse_units(blocks[1], 1, 0)
aoc.cprint(simulate(list(itertools.chain(immune, infection))))
