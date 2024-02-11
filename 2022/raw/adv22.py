import sys
import re
import copy
import networkx as nx
import itertools
import math
import json

def parse():
  original_tiles = []
  for line in sys.stdin:
    if not line.strip():
      break
    original_tiles.append(line.strip("\n"))
  maxlen = max(len(line) for line in original_tiles)
  tiles = [(line + " " * maxlen)[:maxlen] for line in original_tiles]
  path = input()
  return tiles, path

def find_start(tiles):
  space = re.search(r"^(\s+)", tiles[0])
  return 0, len(space.group(1))

directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def decode_path(path):
  curdir = 0
  decoded = re.split(r"([RL])", path)
  for command in decoded:
    match command:
      case "R":
        yield 1
        #curdir = (curdir + 1) % 4
      case "L":
        yield 3
        #curdir = (curdir + 3) % 4
      case steps:
        for _ in range(int(steps) - 1):
          #yield curdir
          yield 0

def find_next(tiles, pos, delta):
  y, x = pos
  dy, dx = delta
  sy, sx = len(tiles), len(tiles[0])
  while True:
    y = (y + dy + sy) % sy
    x = (x + dx + sx) % sx
    if tiles[y][x] != " ":
      return y, x

dirsymbol = [">", "v", "<", "^"]
sample_dice = "9909 1239 9945".split()
sample_edges = "5324 2045 3410 5420 5123 0143".split()
sample_flow = "0101 0311 0020 1123 0033 2022".split()

def first(tiles, path):
  pos = find_start(tiles)
  tcopy = [list(line) for line in tiles]
  for curdir in decode_path(path):
    nextpos = find_next(tiles, pos, directions[curdir])
    if tiles[nextpos[0]][nextpos[1]] != "#":
      tcopy[pos[0]][pos[1]] = dirsymbol[curdir]
      #print("\n".join("".join(line) for line in tcopy))
      #print()
      pos = nextpos
  return 1000 * (pos[0] + 1) + 4 * (pos[1] + 1) + curdir

def get_face(tiles, pos, dice, size):
  y, x = pos[0] // size, pos[1] // size
  return int(sample_dice[y][x])

gety = lambda pos: pos[0]
getx = lambda pos: pos[1]
puty = lambda pos, y: (y, pos[1])
putx = lambda pos, x: (pos[0], x)
fromedge = [gety, getx, gety, getx]
toedge = [puty, putx, puty, putx]

def toint(array):
  return [[int(x) for x in line] for line in array]

def dump(dice, pos):
  dice = copy.deepcopy(dice)
  dice[pos[0]][pos[1]] = "E"
  print("\n".join("".join(line) for line in dice))
  print()

def basepos(dice, face, size):
  for j, line in enumerate(dice):
    if face in line:
      return [j * size, line.index(face) * size]

def second(tiles, path, dice, edges, flow):
  dice = toint(dice)
  edges = toint(edges)
  flow = toint(flow)
  size = int((len(tiles) * len(tiles[0]) // 12) ** 0.5)
  pos = find_start(tiles)
  tcopy = [list(line) for line in tiles]
  prevface = 0
  curdir = 0
  for deltadir in decode_path(path):  
    curdir = (curdir + deltadir) % 4
    nextpos = find_next(tiles, pos, directions[curdir])
    face = get_face(tiles, nextpos, dice, size)
    print("trying curdir %d face %d" % (curdir, face))
    dump(tcopy, pos)
    if face != prevface:
      face = edges[prevface][curdir]
      newdir = flow[prevface][curdir]
      hold = curdir % 2
      oldbase = basepos(dice, prevface, size)
      nextpos = basepos(dice, face, size)      
      print(nextpos)
      nextpos[newdir % 2] += pos[hold] - oldbase[hold]
      nextpos[1 - (newdir % 2)] += 0 if newdir < 2 else size - 1
      print("moving to face %d newdir %d nextpos %s" % (face, newdir, nextpos))
    if tiles[nextpos[0]][nextpos[1]] != "#":
      tcopy[pos[0]][pos[1]] = dirsymbol[curdir]
      pos = nextpos
    prevface = face            

def find_line_runs(line):
  last = " "
  count = 0
  for cur in line:
    if cur != " ":
      count += 1
    elif last != " ":
      yield count
      count = 0
    last = cur
  if count:
    yield count

def find_tiles_runs(tiles):
  for line in tiles:
    yield from find_line_runs(line)
  for i in range(len(tiles[0])):
    tline = [line[i] for line in tiles]
    yield from find_line_runs(tline)

def find_size(tiles):
  return math.gcd(*find_tiles_runs(tiles))

def dump_grid(grid):
  for line in grid:
    print("".join("." if i == 9 else str(i) for i in line))

def build_grid(tiles):
  size = find_size(tiles)
  y, x = len(tiles) // size, len(tiles[0]) // size
  grid, cur = [], 0
  for j in range(y):
    line = []
    for i in range(x):
      if tiles[j * size][i * size] == " ":
        line.append(9)
      else:
        line.append(cur)
        cur += 1
    grid.append(line)
  return size, y, x, grid

def build_cube_graph():
  cube = {}
  for i, j in itertools.product(range(6), repeat=2):
    if i != j and i + j != 5:
      cube.setdefault(i, set()).add(j)
  return cube

def build_partial_graph(tiles):
  size, y, x, grid = build_grid(tiles)
  dump_grid(grid)
  cube = {}
  valid = lambda j, i: 0 <= j < y and 0 <= i < x
  for j in range(y):
    for i in range(x):
      if grid[j][i] == 9:
        continue
      for dj, di in directions:
        if not valid(j + dj, i + di) or grid[j + dj][i + di] == 9:
          continue
        cube.setdefault(grid[j][i], set()).add(grid[j + dj][i + di])
  return cube

def get_node_match(edge_match):
  node_match = {}
  for (a1, a2), (b1, b2) in edge_match.items():
    node_match[a1] = b1
    node_match[b1] = a1
    node_match[a2] = b2
    node_match[b2] = a2
  return node_match

def dump_connection_graph(graph, node_match):
  nodes = {}
  for n1, n2 in nx.edges(graph):
    nodes.setdefault(node_match[n1], []).append(node_match[n2])
    nodes.setdefault(node_match[n2], []).append(node_match[n1])
  for i in sorted(nodes):
    print(i, nodes[i])

def is_match(a, b, perm):
  for aa, bb in enumerate(perm):
    if 

def find_subgraph_match(a, b):
  for perm in itertools.permutations(range(6)):
    if is_match(a, b, perm):
      return perm

tiles, path = parse()
cube_graph = build_cube_graph()
print(cube_graph)
partial_graph = build_partial_graph(tiles)
print(partial_graph)
print("subgraph match ", subgraph_match(cube_graph, partial_graph))
#iso = nx.algorithms.isomorphism.ISMAGS(cube_graph, partial_graph)
#print(iso.subgraph_is_isomorphic())
#nx.nx_pydot.write_dot(cube_graph, "cube.dot")
#nx.nx_pydot.write_dot(partial_graph, "partial.dot")

def lixo():
    cube_graph = nx.line_graph(original_graph)
    partial_graph = nx.line_graph(build_partial_graph(tiles))
    edge_list = list(nx.generate_edgelist(cube_graph))
    iso = nx.algorithms.isomorphism.GraphMatcher(cube_graph, partial_graph)
    edge_match = list(itertools.islice(iso.subgraph_isomorphisms_iter(), 1))[0]
    print(edge_match)
    node_match = get_node_match(edge_match)
    print(node_match)
    dump_connection_graph(original_graph, node_match)
    #print(first(tiles, path))
    #print(second(tiles, path, sample_dice, sample_edges, sample_flow))
    #print(tiles, path) 
