import sys
import aoc

DIR = aoc.get_dir("U")

def traverse(t, lines, j, i, extra=lambda t, y, x: True):
  for cmds in lines:
    for cmd in cmds:
      dj, di = DIR[cmd]
      if t.valid(j + dj, i + di) and extra(t, j + dj, i + di):
        j += dj
        i += di
    yield t[j][i]

def walk(t, lines):
  j, i = 1, 1
  for item in traverse(t, lines, j, i):
    yield str(item)

def walk2(t, lines):
  j, i = 2, 0
  for item in traverse(t, lines, j, i, extra=lambda t, y, x: t[y][x] != 0):
    yield hex(item)[2:].upper()

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

