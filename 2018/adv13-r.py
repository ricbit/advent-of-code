import sys
import itertools
import aoc
import copy
from dataclasses import dataclass

@dataclass(init=True, order=True)
class Car:
  y: int
  x: int
  cpos: complex
  cdir: complex
  state: int
  active: bool

CDIR = aoc.get_cdir(">")

def get_cars(t):
  cars = []
  for j, i in t.iter_all():
    if t[j][i] in CDIR.keys():
      cars.append(Car(j, i, j * 1j + i, CDIR[t[j][i]], 0, True))
  return cars

def collision(cars, i, j):
  if i != j and cars[j].active:
    if cars[i].y == cars[j].y and cars[i].x == cars[j].x:
      return True
  return False

def solve(data, abort):
  t = aoc.Table(data)
  cars = get_cars(t)
  CTURN = [-1j, 1, 1j]
  for tick in itertools.count(0):
    cars.sort()
    for i in range(len(cars)):
      if not cars[i].active:
        continue
      cars[i].cpos += cars[i].cdir
      cars[i].y = int(cars[i].cpos.imag)
      cars[i].x = int(cars[i].cpos.real)
      for j in range(len(cars)):
        if collision(cars, i, j):
          if abort:
            return f"{cars[i].x},{cars[i].y}"
          cars[i].active = False
          cars[i].y = -i
          cars[j].active = False
          cars[j].y = -j
          break
      match t[cars[i].y][cars[i].x]:
        case "/":
          cars[i].cdir = (cars[i].cdir * 1j).conjugate()
        case "\\":
          cars[i].cdir = (cars[i].cdir * -1j).conjugate()
        case "+":
          cars[i].cdir *= CTURN[cars[i].state % 3]
          cars[i].state += 1
    active_cars = [i for i in range(len(cars)) if cars[i].active]
    if len(active_cars) == 1:
      return f"{cars[active_cars[0]].x},{cars[active_cars[0]].y}"

data = [list(line.strip("\n")) for line in sys.stdin]
aoc.cprint(solve(copy.deepcopy(data), True))
aoc.cprint(solve(data, False))
