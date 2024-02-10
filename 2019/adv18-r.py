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
    if t[y][x].islower():
      doors |= keybit[t[y][x].lower()]
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
  _, _, pos, _, keys = state
  pos = ",".join(str(i) for i in aoc.flatten(pos))
  return pos + str(keys)

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

def get_available(keys, col_keys):
  for name, (robot, bitname, j, i, doors) in keys.items():
    if (bitname & col_keys) > 0:
      continue
    if (doors & col_keys) != doors:
      continue
    yield name, (robot, bitname, j, i, doors)

def is_key_alive(keys, col_keys, y, x):
  if table[y][x].islower():
    return (keys[table[y][x]][1] & col_keys) == 0
  else:
    return False

def dfs(pos, col_keys, keys, visited, graph):
  visited.add(pos)
  y, x = pos
  branches = []
  for dist, (j, i) in graph[(y, x)]:
    if (j, i) not in visited:
      branches.append((dist, dfs((j, i), col_keys, keys, visited, graph)))
  if not branches:
    #print(pos, is_key_alive(keys, col_keys, y, x), 0)
    return is_key_alive(keys, col_keys, y, x), 0
  beyond = sum((dist1 + dist2 for dist1, (alive, dist2) in branches if alive)) #, default=0)
  self_alive = any(alive for _, (alive, _) in branches) or is_key_alive(keys, col_keys, y, x)
  #print(pos, self_alive, beyond)
  return self_alive, beyond

def heuristic(pos, col_keys, keys, robot, graph):
  #return 0
  #print("----",bin(col_keys), table[pos[0]][pos[1]])
  return dfs(pos, col_keys, keys, set(), graph)[0]
  ans = 0
  for name, (r, bitname, j, i, doors) in keys.items():
    if (bitname & col_keys) == 0 and robot == r:
      ans = max(ans, get_distance(tuple(pos), j, i)[0])
  return ans

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
  hh = [heuristic((y, x), 0, keys, r, graph) for r, (y, x, robot_keys) in enumerate(robots)]
  state = (sum(hh), 0, [(y, x) for y, x, keys in robots], hh, 0)
  vnext = aoc.bq([state], size = 8000)
  visited = set() #[encode(state)])
  ticks = 0
  while vnext:
    state = vnext.pop()
    old_hsum, score, pos, hh, col_keys = state
    ticks += 1
    if ticks % 100 == 0:
      print(ticks, score, old_hsum, len(vnext), len(visited))
    if col_keys == all_keys:
      return score
    if encode(state) in visited:
      continue
    visited.add(encode(state))
    for name, (robot, bitname, j, i, doors) in get_available(keys, col_keys):
      dist, pos_robot = get_distance(pos[robot], j, i)
      newpos = pos[:]
      newpos[robot] = pos_robot
      encoded_keys = (col_keys | bitname)
      new_hh = hh[:]
      new_hh[robot] = heuristic(newpos[robot], encoded_keys, keys, robot, graph)
      state = (score + dist + sum(new_hh), score + dist, newpos, new_hh, encoded_keys)
      ns = encode(state)
      if ns not in visited:
        vnext.push(state)
        #visited.add(ns)
  return None

def enlarge(t):
  for j, i in t.iter_all():
    if t[j][i] == "@":
      t[j - 1][i - 1: i + 2] = ["@", "#", "@"]
      t[j + 0][i - 1: i + 2] = ["#", "#", "#"]
      t[j + 1][i - 1: i + 2] = ["@", "#", "@"]
      return t

def deletable(j, i):
  return (not table[j][i].islower()) and table[j][i] != "@"

def reduce_graph(graph):
  changed = False
  erased = [(j, i) for j, i in graph if len(graph[(j, i)]) == 1 and deletable(j, i)]
  for node in erased:
    dist, dst = aoc.first(graph[node])
    graph[dst].remove((dist, node))
    del graph[node]
    changed = True
  double = [(j, i) for j, i in graph if len(graph[(j, i)]) == 2 and deletable(j, i)]
  for node in double:
    if len(node) != 2:
      continue
    (da, a), (db, b) = graph[node]
    if a in graph and b in graph:
      graph[a].remove((da, node))
      graph[b].remove((db, node))
      graph[a].add((da + db, b))
      graph[b].add((da + db, a))
      del graph[node]
      changed = True
  return changed

def shrink(graph):
  for node, children in graph.items():
    if len(children) == 4:
      save = children.copy()
      for dist, child in save:
        for subdist, subchild in graph[child]:
          if node != subchild:
            graph[node].add((subdist, subchild))
          graph[subchild].add((subdist, node))
          graph[subchild].remove((dist, child))
      for dist, child in save:
        del graph[child]
      return graph

def create_graph():
  graph = aoc.ddict(lambda: set())
  for j, i in table.iter_all(lambda x: x != "#"):
    for jj, ii in t.iter_neigh4(j, i, lambda x: x != "#"):
      graph[(j, i)].add((1, (jj, ii)))
  while reduce_graph(graph):
    pass
  return graph
  #return shrink(graph)

def write_dot(graph):
  f = open("graph.18.dot", "wt")
  f.write("graph maze {\n")
  for j, i in graph:
    src = f"g{j}_{i}"
    f.write(f'{src} [label="{table[j][i]}"];\n')
  for j, i in graph:
    for size, (jj, ii) in graph[(j, i)]:
      src = f"g{j}_{i}"
      dst = f"g{jj}_{ii}"
      if src < dst:
        f.write(f'{src} -- {dst} [label="{size}"];\n')
  f.write("}")
  f.close()
  return 0

t = aoc.Table.read()
table =  enlarge(t)
graph = create_graph()
write_dot(graph)
robots = get_robots(table)
aoc.cprint(solve2(robots, graph))
