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
import networkx as nx

def get_side(t):
  s = [[] for _ in range(4)]
  for i in range(t.w):
    s[0].append(t[0][i])
    s[1].append(t[t.h - 1][i])
    s[2].append(t[i][0])
    s[3].append(t[i][t.w - 1])
  cdir = [1j, -1j, -1, 1]
  yield from ((cdir, "".join(side)) for cdir, side in zip(cdir, s))

def build_rotations(original):
  rotated = [original]
  for i in range(3):
    rotated.append(rotated[-1].clock90())
  for i in range(4):
    rotated.append(rotated[i].flipx())
  return rotated

def build_tiles(blocks):
  tiles = {}
  sides = aoc.ddict(set)
  for block in blocks:
    title, *lines = block
    title = aoc.retuple("title_", r".*?(\d+):", title)
    original = aoc.Table([list(line) for line in lines])
    rotated = build_rotations(original)
    tiles[title.title] = rotated
    for rot in rotated:
      for cdir, side in get_side(rot):
        sides[side].add((cdir, title.title))
  return tiles, sides

def find_corners(g):
  for node in g.nodes:
    if len(list(nx.neighbors(g, node))) == 2:
      yield node

def part1(g):
  return math.prod(find_corners(g))

def build_graph(sides):
  g = nx.Graph()
  for side, data in sides.items():
    trimmed = set(b for a, b in data)
    if len(trimmed) == 2:
      g.add_edge(*trimmed)
  return g

def build_rotation_links(g, tiles):
  good_rotations = aoc.ddict(list)
  for a, b in g.edges:
    a, b = min(a, b), max(a, b)
    for (xc, c), (xd, d) in itertools.product(enumerate(tiles[a]), enumerate(tiles[b])):
      if all(x not in [a, b] for x in [xc, xd]):
        for (cdir, ckey), (ddir, dkey) in itertools.product(get_side(c), get_side(d)):
          if cdir == -ddir and ckey == dkey:
            good_rotations[(a, xc)].append((b, xd, cdir))
            good_rotations[(b, xd)].append((a, xc, ddir))
  return good_rotations

def find_right_rotation(start, rotations):
  for rot in range(8):
    (anode, arot, adir), (bnode, brot, bdir) = rotations[start, rot]
    if adir == 1 and bdir == 1j:
      return rot

def build_grid(g, tiles):
  size = int(len(g.nodes) ** 0.5 + 0.5)
  grid = nx.grid_2d_graph(size, size)
  g_to_grid = nx.vf2pp_isomorphism(g, grid, node_label=None)
  grid_to_g = {v: k for k, v in g_to_grid.items()}
  rotations = build_rotation_links(g, tiles)
  start = grid_to_g[(0, 0)]
  rot = find_right_rotation(start, rotations)
  visited = set()
  pnext = [(start, rot, 0)]
  grid = {}
  while pnext:
    node, rot, pos = pnext.pop()
    if (node, rot) in visited:
      continue
    visited.add((node, rot))
    grid[pos] = (node, rot)
    for nnode, nnrot, nndir in rotations[(node, rot)]:
      if nnode != node:
        if (nnode, nnrot) not in visited:
          pnext.append((nnode, nnrot, pos + nndir))
  return size, grid

def shrink_tile(tile):
  newtile = []
  for line in range(1, tile.h - 1):
    newtile.append(tile.table[line][1:tile.w - 1])
  return aoc.Table(newtile)

def build_image(blocksize, grid, tiles):
  tilesize = aoc.first(tiles.values())[0].w - 2
  imagesize = blocksize * tilesize
  image = [[0] * imagesize for _ in range(imagesize)]
  for y in range(blocksize):
    for x in range(blocksize):
      tilename, rot = grid[y * 1j + x]
      tile = shrink_tile(tiles[tilename][rot])
      for j, i in tile.iter_all():
        image[y * tilesize + j][x * tilesize + i] = tile[tile.h - j - 1][i]
  return aoc.Table(image)

monster = [
    "                  # ",
    "#    ##    ##    ###",
    " #  #  #  #  #  #   "
]

def count_monsters(image):
  mh, mw = len(monster), len(monster[0])
  msize = sum(c == "#" for c in aoc.flatten(monster))
  for y, x in image.iter_all():
    if y + mh <= image.h and x + mw <= image.w:
      count = 0
      for j, i in itertools.product(range(mh), range(mw)):
        if monster[j][i] == "#" and image[y + j][x + i] in "#O":
          count += 1
      if count == msize:
        for j, i in itertools.product(range(mh), range(mw)):
          if monster[j][i] == "#":
            image[y + j][x + i] = "O"
  return sum(c == "#" for c in aoc.flatten(image))

def part2(image):
  rotated = build_rotations(image)
  return min(count_monsters(r) for r in rotated)

blocks = aoc.line_blocks()
tiles, sides = build_tiles(blocks)
g = build_graph(sides)
aoc.cprint(part1(g))
size, grid = build_grid(g, tiles)
image = build_image(size, grid, tiles)
aoc.cprint(part2(image))
