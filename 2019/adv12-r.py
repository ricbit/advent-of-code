import sys
import itertools
import math
import aoc

def get_state(planet, coord):
  state = []
  for p in planet:
    state.append(p[0][coord])
    state.append(p[1][coord])
  return tuple(state)

def compare_state(planet, coord, state):
  n = 0
  for p in planet:
    if p[0][coord] != state[n]:
      return False
    if p[1][coord] != state[n + 1]:
      return False
    n += 2
  return True

def step(planet, coord):
  for a, b in itertools.combinations(planet, 2):
    if a[0][coord] < b[0][coord]:
      a[1][coord] += 1
      b[1][coord] -= 1
    elif a[0][coord] > b[0][coord]:
      a[1][coord] -= 1
      b[1][coord] += 1
  for p in planet:
    p[0][coord] += p[1][coord]

def simulate2(planet, coord):
  state = get_state(planet, coord)
  for tick in itertools.count(0):
    step(planet, coord)
    if compare_state(planet, coord, state):
      return tick + 1

def simulate1(planet, ticks):
  for tick in range(ticks):
    for d in range(3):
      step(planet, d)
    energy = sum(sum(abs(d) for d in p[0]) * sum(abs(d) for d in p[1]) for p in planet)
  return energy

data = aoc.retuple_read("x_ y_ z_", r"<x=(.*?), y=(.*?), z=(.*?)>", sys.stdin)
planets = [[[p.x, p.y, p.z], [0, 0, 0]] for p in data]
aoc.cprint(simulate1(planets, 1000))
values = [simulate2(planets, i) for i in range(3)]
aoc.cprint(math.lcm(*values))
