import sys
import aoc
from collections import deque

DIRS = {"U": 0, "D": 1, "L": 2, "R": 3}

DD = aoc.get_dir("U")

def isopen(path, name):
  doors = [(ord(i) > ord("a")) for i in aoc.md5(path)[:4]]
  return doors[DIRS[name]]

def search(seed):
  vnext = deque([(0, 0, seed)])
  while vnext:
    y, x, path = vnext.popleft()
    if (y, x) == (3, 3):
      yield path
      continue
    for name, (dj, di) in DD.items():
      j, i = y + dj, x + di
      if i < 0 or j < 0 or i > 3 or j > 3:
        continue
      if isopen(path, name):
        vnext.append((j, i, path + name))

seed = sys.stdin.read().strip()
paths = list(search(seed))
aoc.cprint(paths[0][len(seed):])
aoc.cprint(len(paths[-1]) - len(seed))

