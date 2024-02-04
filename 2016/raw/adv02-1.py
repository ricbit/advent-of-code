import sys
import re
import itertools
import math
import aoc
from collections import *

DIR = aoc.get_dir("U")

def walk(t, lines):
  j, i = 1, 1
  for cmds in lines:
    for cmd in cmds:
      dj, di = DIR[cmd]
      if t.valid(j + dj, i + di):
        j += dj
        i += di
    yield str(t[j][i])

def walk2(t, lines):
  j, i = 2, 0
  for cmds in lines:
    for cmd in cmds:
      dj, di = DIR[cmd]
      if t.valid(j + dj, i + di) and t[j + dj][i + di] != 0:
        j += dj
        i += di
    yield hex(t[j][i])[2:]

lines = [line.strip() for line in sys.stdin]
t = aoc.Table([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
aoc.cprint("".join(walk(t, lines)))
t = aoc.Table([
  [0, 0, 1, 0, 0],
  [0, 2, 3, 4, 0],
  [5, 6, 7, 8, 9],
  [0, 10, 11, 12, 0],
  [0, 0, 13, 0, 0]
])
aoc.cprint("".join(walk2(t, lines)))

