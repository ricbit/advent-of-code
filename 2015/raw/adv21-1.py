import sys
import re
import itertools
import math
import aoc
from collections import *

sales = """
Weapons:    Cost  Damage  Armor
Dagger        8     4       0
Shortsword   10     5       0
Warhammer    25     6       0
Longsword    40     7       0
Greataxe     74     8       0

Armor:      Cost  Damage  Armor
Leather      13     0       1
Chainmail    31     0       2
Splintmail   53     0       3
Bandedmail   75     0       4
Platemail   102     0       5

Rings:      Cost  Damage  Armor
Damage +1    25     1       0
Damage +2    50     2       0
Damage +3   100     3       0
Defense +1   20     0       1
Defense +2   40     0       2
Defense +3   80     0       3
"""

def parse(weapon):
  for line in weapon.strip().split("\n")[1:]:
    yield aoc.retuple("Item","cost_ damage_ armor_", 
        r"^.*?\s+(\d+)\s+(\d+)\s+(\d+)\s*$", line)

def pc_generator(weapon, armor, rings, Player):
  options = [range(1, 2), range(0, 2), range(0, 3)]
  for w, a, r in itertools.product(*options):
    ww = itertools.combinations(weapon, w)
    aa = itertools.combinations(armor, a)
    rr = itertools.combinations(rings, r)
    for items in itertools.product(ww, aa, rr):
      cost, damage, shield = 0, 0, 0
      for subitem in items:
        for item in subitem:
          cost += item.cost
          damage += item.damage
          shield += item.armor
      yield Player(100, damage, shield), cost

def simulate(player, orc):
  hp = player.hp
  ho = orc.hp
  while True:
    dmg = max(1, player.damage - orc.armor)
    ho -= dmg
    if ho <= 0:
      return False
    dmg = max(1, orc.damage - player.armor)
    hp -= dmg
    if hp <= 0:
      return True

def simulate_all(orc, Player):
  for pc, gold in pc_generator(weapon, armor, rings, Player):
    if simulate(pc, orc):
      yield gold

weapon, armor, rings = sales.split("\n\n")
weapon = list(parse(weapon))
armor = list(parse(armor))
rings = list(parse(rings))
Player = namedtuple("Player", "hp damage armor")
orc_stats = [int(re.search(r"\d+", line).group(0)) for line in sys.stdin]
orc = Player(*orc_stats)
aoc.cprint(max(simulate_all(orc, Player)))

