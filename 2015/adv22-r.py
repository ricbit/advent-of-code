import sys
import re
import aoc
import heapq
import copy
from dataclasses import dataclass

@dataclass(init=False, order=True, unsafe_hash=True)
class State:
  orchp: int
  pchp: int = 50
  mana: int = 500
  timer: (int, int, int, int, int) = (0, 0, 0, 0, 0)
  orcdmg: int

magics = [
  ("Magic Missile", 53, 0),
  ("Drain", 73, 0),
  ("Shield", 113, 6),
  ("Poison", 173, 6),
  ("Recharge", 229, 5)
]

def simulate(orchp, orcdmg, bleeding):
  start = State()
  start.orchp = orchp
  start.orcdmg = orcdmg
  vnext = [(0, start, [])]
  visited = set()
  while vnext:
    spent, state, path = heapq.heappop(vnext)
    if state in visited:
      continue
    visited.add(state)
    for i, (name, cost, maxtimer) in enumerate(magics):
      new_state = copy.deepcopy(state)
      new_state.pchp -= bleeding
      if new_state.pchp <= 0:
        continue
      new_spent = spent
      timer = list(new_state.timer)
      new_path = path[:] + [name]
      if state.mana >= cost:
        match i:
          case 0: 
            new_state.orchp -= 4
            new_spent += cost
            new_state.mana -= cost
          case 1:
            new_state.orchp -= 2
            new_state.pchp += 2
            new_spent += cost
            new_state.mana -= cost
          case 2 | 3 | 4:
            if timer[i] == 0:
              timer[i] = maxtimer
              new_spent += cost
              new_state.mana -= cost
            else:
              continue
      else:
        continue
      if timer[3] > 0:
        new_state.orchp -= 3
      if timer[4] > 0:
        new_state.mana += 101
      if new_state.orchp <= 0:
        return new_spent
      for i in range(5):
        timer[i] = max(0, timer[i] - 1)
      # orc round
      if timer[3] > 0:
        new_state.orchp -= 3
      if timer[4] > 0:
        new_state.mana += 101
      if new_state.orchp <= 0:
        return new_spent
      armor = 7 if timer[2] > 0 else 0
      for i in range(5):
        timer[i] = max(0, timer[i] - 1)
      dmg = max(1, new_state.orcdmg - armor)
      new_state.pchp -= dmg
      if new_state.pchp > 0:
        new_state.timer = tuple(timer)
        if new_state not in visited:
          heapq.heappush(vnext, (new_spent, new_state, new_path))

lines = [line.strip() for line in sys.stdin]
orchp = int(re.match(r".*?(\d+)", lines[0]).groups()[0])
orcdmg = int(re.match(r".*?(\d+)", lines[1]).groups()[0])
aoc.cprint(simulate(orchp, orcdmg, 0))
aoc.cprint(simulate(orchp, orcdmg, 1))

