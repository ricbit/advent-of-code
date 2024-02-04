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

def newencode(state):
  _, _, pos, _, keys = state
  pos = ",".join(",".join(str(i) for i in pair) for pair in pos)
  keys = str(keys)
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
      return steps, (y, x)
    if (y, x) in visited:
      continue
    visited.add((y, x))
    for jj, ii in t.iter_neigh4(y, x):
      if t[jj][ii] != "#":
        vnext.append((steps + 1, jj, ii))
  return None

def get_available(keys, col_keys):
  for name, (robot, bitname, j, i, doors) in keys.items():
    if (bitname & col_keys) > 0:
      continue
    if (doors & col_keys) != doors:
      continue
    yield name, (robot, bitname, j, i, doors)

def heuristic(pos, col_keys, keys, robot):
  ans = []
  for name, (r, bitname, j, i, doors) in keys.items():
    if (bitname & col_keys) == 0 and robot == r:
      ans.append(get_distance(tuple(pos), j, i))
  return max((steps for steps, _ in ans), default = 0)

def solve2(t, robots):
  global table
  table = t
  keys = {}
  all_keys = 0
  for r, (y, x, robot_keys) in enumerate(robots):
    for name, bitname, j, i, doors in robot_keys:
      keys[name] = (r, bitname, j, i, doors)
      all_keys |= bitname
  hh = [heuristic((y, x), 0, keys, r) for r, (y, x, robot_keys) in enumerate(robots)]
  state = (sum(hh), 0, [(y, x) for y, x, keys in robots], hh, 0)
  vnext = aoc.bq([state], size = 3000)
  visited = set()
  ticks = 0
  while vnext:
    state = vnext.pop()
    old_hsum, score, pos, hh, col_keys = state
    ticks += 1
    if ticks % 10000 == 0:
      print(ticks, score, old_hsum, len(vnext), len(visited))
    if col_keys == all_keys:
      return score
    visited.add(newencode(state))
    for name, (robot, bitname, j, i, doors) in get_available(keys, col_keys):
      dist, pos_robot = get_distance(pos[robot], j, i)
      newpos = pos[:]
      newpos[robot] = pos_robot
      encoded_keys = (col_keys | bitname)
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