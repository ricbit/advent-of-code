import sys
import string
import re
import itertools
import math
import cmath
import aoc
import heapq
import functools
import copy
from collections import Counter, deque
from dataclasses import dataclass
from aoc.refintcode import IntCode

def get_keys(t, y, x):
  vnext = deque([(0, y, x, [])])
  visited = {}
  keys = []
  while vnext:
    steps, y, x, doors = vnext.popleft()
    if (y, x) in visited:
      continue
    visited[(y, x)] = steps
    if t[y][x].isupper():
      doors = doors[:] + [t[y][x]]
    if t[y][x].islower():
      keys.append((t[y][x], y, x, doors))
    for j, i in t.iter_neigh4(y, x):
      if t[j][i] != "#" and (j, i) not in visited:
        vnext.append((steps + 1, j, i, doors))
  return keys

def get_robots(t):
  robots = []
  for j, i in t.iter_all():
    if t[j][i] == "@":
      robots.append((j, i, get_keys(t, j, i)))
  return robots

def newencode(state):
  _, _, pos, _, keys = state
  pos = ",".join(",".join(str(i) for i in pair) for pair in pos)
  keys = "".join(sorted(keys))
  return pos + keys

table = None

@functools.lru_cache(maxsize=None)
def get_distance(pos, j, i):
  y, x = pos
  vnext = deque([(0, y, x)])
  visited = set()
  while vnext:
    steps, y, x = vnext.popleft()
    if y == j and x == i:
      del vnext
      return steps, (y, x)
    if (y, x) in visited:
      continue
    visited.add((y, x))
    for jj, ii in t.iter_neigh4(y, x):
      if t[jj][ii] != "#":
        vnext.append((steps + 1, jj, ii))
  return None

def get_available(keys, col_keys):
  for name, (robot, j, i, doors) in keys.items():
    if name in col_keys:
      continue
    if any(door.lower() not in col_keys for door in doors):
      continue
    yield name, (robot, j, i, doors)

def heuristic(pos, col_keys, keys, robot):
  ans = []
  for name, (r, j, i, doors) in keys.items():
    if name not in col_keys and robot == r:
      ans.append(get_distance(tuple(pos), j, i))
  return max((steps for steps, _ in ans), default = 0)

def solve2(t, robots):
  global table
  table = t
  keys = {}
  for r, (y, x, robot_keys) in enumerate(robots):
    for name, j, i, doors in robot_keys:
      keys[name] = (r, j, i, doors)
  hh = [heuristic((y, x), "", keys, r) for r, (y, x, robot_keys) in enumerate(robots)]
  state = (sum(hh), 0, [(y, x) for y, x, keys in robots], hh, "")
  vnext = aoc.bq([state], size = 3000)
  visited = set()
  ticks = 0
  while vnext:
    state = vnext.pop()
    old_hsum, score, pos, hh, col_keys = state
    ticks += 1
    if ticks % 10000 == 0:
      print(ticks, score, old_hsum, len(vnext), len(visited))
    if len(col_keys) == len(keys):
      return score
    visited.add(newencode(state))
    for name, (robot, j, i, doors) in get_available(keys, col_keys):
      dist, pos_robot = get_distance(pos[robot], j, i)
      newpos = pos[:]
      newpos[robot] = pos_robot
      encoded_keys = "".join(sorted(col_keys + name))
      new_hh = hh[:]
      new_hh[robot] = heuristic(newpos[robot], encoded_keys, keys, robot)
      state = (score + dist + sum(new_hh), score + dist, newpos, new_hh, encoded_keys)
      if newencode(state) not in visited:
        vnext.push(state)
  return None

def enlarge(t):
  for j, i in t.iter_all():
    if t[j][i] == "@":
      t[j - 1][i - 1: i + 2] = ["@", "#", "@"]
      t[j + 0][i - 1: i + 2] = ["#", "#", "#"]
      t[j + 1][i - 1: i + 2] = ["@", "#", "@"]
      return t

t = aoc.Table.read()
lt = enlarge(t)
robots = get_robots(lt)
aoc.cprint(solve2(lt, robots))
