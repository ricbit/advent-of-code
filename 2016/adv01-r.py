import sys
import re
import itertools
import math
import aoc
from collections import *

def parse(d):
  return d[0], int(d[1:])

def traverse_commands(cmd, vdir):
  for turn, size in cmd:
    if turn == "R":
      vdir *= -1j
    else:
      vdir *= 1j
    yield vdir, size

def walk(pos, vdir, cmd):
  for vdir, size in traverse_commands(cmd, vdir):
    pos += vdir * size
  return pos

def walk2(pos, vdir, cmd):
  visited = set([pos])
  for vdir, size in traverse_commands(cmd, vdir):
    for i in range(size):
      pos += vdir
      if pos in visited:
        return pos
      visited.add(pos)
  return pos

cmd = [parse(d) for d in sys.stdin.read().split(", ")]
pos = walk(0, 1j, cmd)
aoc.cprint(int(abs(pos.real) + abs(pos.imag)))
pos = walk2(0, 1j, cmd)
aoc.cprint(int(abs(pos.real) + abs(pos.imag)))

