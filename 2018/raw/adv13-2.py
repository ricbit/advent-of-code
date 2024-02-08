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

def solve(data):
  t = aoc.Table(data)
  cars = []
  CDIR = {">": 1, "<": -1, "^": -1j, "v": +1j}
  CTURN = [-1j, 1, 1j]
  for j, i in t.iter_all():
    if t[j][i] in aoc.DIRECTIONS2.keys():
      cars.append([j, i, j * 1j + i, CDIR[t[j][i]], 0, True])
      if t.valid(j - 1, i) and t[j - 1][i] == "-":
        t[j][i] = "-"
      elif t.valid(j + 1, i) and t[j + 1][i] == "-":
        t[j][i] = "-"
      elif t.valid(j, i - 1) and t[j][i - 1] == "|":
        t[j][i] = "|"
      elif t.valid(j, i + 1) and t[j][i + 1] == "|":
        t[j][i] = "|"
      elif t.valid(j - 1, i) and t[j - 1][i] == "|":
        t[j][i] = "|"
      elif t.valid(j + 1, i) and t[j + 1][i] == "|":
        t[j][i] = "|"
      elif t.valid(j, i - 1) and t[j][i - 1] == "-":
        t[j][i] = "-"
      elif t.valid(j, i + 1) and t[j][i + 1] == "-":
        t[j][i] = "-"
      elif t.valid(j, i - 1) and t[j][i - 1] == " ":
        t[j][i] = "|"
  for tick in itertools.count(0):
    #if tick > 30:
    #  return "abort"
    cars.sort()
    for i in range(len(cars)):
      if not cars[i][5]:
        continue
      cars[i][2] += cars[i][3]
      cars[i][0] = int(cars[i][2].imag)
      cars[i][1] = int(cars[i][2].real)
      for j in range(len(cars)):
        if i != j and cars[i][5] and cars[j][5]:
          if cars[i][0] == cars[j][0] and cars[i][1] == cars[j][1]:
            #return f"{cars[i][1]},{cars[i][0]}"
            cars[i][5] = False
            cars[i][0] = -i
            cars[j][5] = False
            cars[j][0] = -j
            break
      match t[cars[i][0]][cars[i][1]]:
        case "/":
          cars[i][3] *= 1j
          cars[i][3] = cars[i][3].conjugate()
        case "\\":
          cars[i][3] *= -1j
          cars[i][3] = cars[i][3].conjugate()
        case "+":
          cars[i][3] *= CTURN[cars[i][4] % 3]
          cars[i][4] += 1
      #print(i, cars[i][3])
    if sum(cars[i][5] for i in range(len(cars))) == 1:
      for i in range(len(cars)):
        if cars[i][5]:
          return f"{cars[i][1]},{cars[i][0]}"
    continue
    for j in range(len(t.table)):
      line = []
      for i in range(len(t.table[0])):
        for k, (cj, ci, cc, cdir, cturn) in enumerate(cars):
          if cj == j and ci == i:
            line.append(str(k))
            break
        else:
          line.append(t[j][i])
      print("".join(line))
    print()
  return 0

data = [list(line.strip("\n")) for line in sys.stdin]
aoc.cprint(solve(data))
