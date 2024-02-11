import aoc
import functools
from collections import deque

def get_keys(t, y, x, keybit):
  vnext = deque([(y, x, 0)])
  visited = set()
  keys = []
  while vnext:
    y, x, doors = vnext.popleft()
    if (y, x) in visited:
      continue
    visited.add((y, x))
    if t[y][x].isupper():
      doors |= keybit[t[y][x].lower()]
    if t[y][x].islower():
      keys.append((t[y][x], keybit[t[y][x]], y, x, doors))
      doors |= keybit[t[y][x]]
    for j, i in t.iter_neigh4(y, x):
      if t[j][i] != "#" and (j, i) not in visited:
        vnext.append((j, i, doors))
  return keys

def get_robots(t):
  robots = []
  keys = set()
  for j, i in t.iter_all():
    if t[j][i].isalpha():
      keys.add(t[j][i].lower())
  keybit = {k: (1 << i) for i, k in enumerate(sorted(keys))}
  for j, i in t.iter_all():
    if t[j][i] == "@":
      robots.append((j, i, get_keys(t, j, i, keybit)))
  return robots

def encode(state):
  _, pos, keys = state
  encoded = tuple(aoc.flatten(pos)) + (keys,)
  return encoded

@functools.lru_cache(maxsize=None)
def get_distance(pos, j, i):
  y, x = pos
  vnext = deque([(0, y, x)])
  visited = set()
  while vnext:
    steps, y, x = vnext.popleft()
    if y == j and x == i:
      return steps, (y, x)
    if (y, x) in visited:
      continue
    visited.add((y, x))
    for jj, ii in table.iter_neigh4(y, x):
      if table[jj][ii] != "#":
        vnext.append((steps + 1, jj, ii))
  return None

def get_available(keys, col_keys, cache):
  if col_keys in cache:
    return cache[col_keys]
  out = []
  for name, (robot, bitname, j, i, doors) in keys.items():
    if (bitname & col_keys) > 0:
      continue
    if (doors & col_keys) != doors:
      continue
    out.append((name, (robot, bitname, j, i, doors)))
  cache[col_keys] = out
  return out

def build_keys(robots):
  keys = {}
  all_keys = 0
  for r, (y, x, robot_keys) in enumerate(robots):
    for name, bitname, j, i, doors in robot_keys:
      keys[name] = (r, bitname, j, i, doors)
      all_keys |= bitname
  return keys, all_keys

def solve2(robots, graph):
  keys, all_keys = build_keys(robots)
  state = (0, [(y, x) for y, x, keys in robots], 0)
  vnext = aoc.bq([state], size=7000)
  visited = set()
  cache = {}
  while vnext:
    state = vnext.pop()
    score, pos, col_keys = state
    if col_keys == all_keys:
      return score
    if (ns := encode(state)) in visited:
      continue
    visited.add(ns)
    for name, (robot, bitname, j, i, doors) in get_available(keys, col_keys, cache):
      dist, pos_robot = get_distance(pos[robot], j, i)
      newpos = pos[:]
      newpos[robot] = pos_robot
      encoded_keys = (col_keys | bitname)
      state = (score + dist, newpos, encoded_keys)
      ns = encode(state)
      if ns not in visited:
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
table = t
robots = get_robots(table)
aoc.cprint(solve2(robots, {}))
table = enlarge(t)
robots = get_robots(table)
aoc.cprint(solve2(robots, {}))
