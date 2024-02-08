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

def print_soil(soil, wet):
  jjs = [k for k,v in soil.items() if "#" in v.values()]
  iis = set(aoc.flatten(soil[j].keys() for j in jjs if soil[j]))
  ans1, ans2 = 0, 0
  if not jjs:
    return 0
  for j in range(min(jjs), max(jjs) + 1):
    line =[]
    if iis:
      for i in range(min(iis), max(iis) + 1): 
        line.append("|" if (soil[j][i]=="." and (j, i) in wet) else soil[j][i])
        if line[-1] == "~":
          ans1 += 1
        elif line[-1] == "|":
          ans2 += 1
    print("".join(line))
  print()
  return ans1, ans2

def fill_soil(clay, soil):
  for element in clay:
    if element.d1 == "x":
      for j in range(element.begin2, element.end2 + 1):
        soil[j][element.n1] = "#"
    elif element.d1 == "y":
      for i in range(element.begin2, element.end2 + 1):
        soil[element.n1][i] = "#"
  soil[0][500] = "+"

def has_wall(soil, wj, wi, vdir, wet):
  while soil[wj][wi] == ".":
    wet.add((wj, wi + vdir))
    if soil[wj][wi + vdir] == "." and soil[wj + 1][wi + vdir] == ".":
      return False
    wi += vdir
  return True

def fill(soil, wj, wi, vdir):
  while soil[wj][wi + vdir] == ".":
    soil[wj][wi + vdir] = "~"
    wi += vdir
  return True

def walk(soil, wj, wi, vdir):
  while soil[wj][wi] == ".":
    if soil[wj][wi + vdir] == "." and soil[wj + 1][wi + vdir] == ".":
      return wi + vdir
    wi += vdir

def down(soil, wj, wi, wet, ymax, forbidden):
  #print(f"restart {wi} {wj}")
  if (wj, wi) in forbidden:
    return
  forbidden.add((wj, wi))
  while wj <= ymax:
    #print(wj, wi)
    #print_soil(soil, wet)
    wet.add((wj, wi))
    if soil[wj + 1][wi] == ".":
      wj += 1
    else:
      left, right = has_wall(soil, wj, wi, -1, wet), has_wall(soil, wj, wi, +1, wet)
      if left and right:
        fill(soil, wj, wi, -1)
        fill(soil, wj, wi, 1)
        soil[wj][wi] = "~"
      elif (not left) and (not right):
        if wj + 1 <= ymax:
          nwi = walk(soil, wj, wi, -1)
          down(soil, wj + 1, nwi, wet, ymax, forbidden)
          nwi = walk(soil, wj, wi, +1)
          down(soil, wj + 1, nwi, wet, ymax, forbidden)
      elif not left:
        nwi = walk(soil, wj, wi, -1)
        if wj + 1 <= ymax:
          down(soil, wj + 1, nwi, wet, ymax, forbidden)
      elif not right:
        nwi = walk(soil, wj, wi, +1)
        if wj + 1 <= ymax:
          down(soil, wj + 1, nwi, wet, ymax, forbidden)
      return

def simulate_water(soil):
  source = (0, 500)
  wet = set()
  ymax = max(soil.keys())
  aoc.cls()
  aoc.goto0()
  last = -1, -1
  for i in range(10000):
    wj, wi = source
    down(soil, wj, wi, wet, ymax, set())
    ans = print_soil(soil, wet)
    print(i, ans)
    x = ans
    if x == last and x[0] != 0:
      return sum(ans)
    last =x

clay = aoc.retuple_read("d1 n1_ d2 begin2_ end2_", r"(.)=(\d+), (.)=(\d+)\.\.(\d+)")
soil = aoc.ddict(lambda: aoc.ddict(lambda: "."))
fill_soil(clay, soil)
print(simulate_water(soil))
#aoc.cprint(solve(data))
