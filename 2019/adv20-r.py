import sys
import aoc
from collections import deque

def iter_codes(t):
  for j, i in t.iter_all():
    if t[j][i].isupper() and t[j + 1][i].isupper():
      if t[j - 1][i] == ".":        
        yield t[j][i] + t[j + 1][i], j - 1, i
      else:
        yield t[j][i] + t[j + 1][i], j + 2, i
    if t[j][i].isupper() and t[j][i + 1].isupper():
      if t[j][i - 1] == ".":
        yield t[j][i] + t[j][i + 1], j, i - 1
      else:
        yield t[j][i] + t[j][i + 1], j, i + 2

def build_maze(t):
  codes = aoc.ddict(lambda: [])
  teleport = {}
  for code, j, i in iter_codes(t):
    codes[code].append((j, i))
  start, end = None, None
  for code, portals in codes.items():
    if len(portals) == 2:
      a, b = portals
      teleport[a] = b
      teleport[b] = a
    elif code == "AA":
      start = portals[0]
    elif code == "ZZ":
      end = portals[0]
  return teleport, start, end

def solve(t, teleport, start, end, add):
  visited = set()
  vnext = deque([(0, 0, start)])
  yborder = [3, t.h - 4]
  xborder = [3, t.w - 4]
  while vnext:
    score, level, (y, x) = vnext.popleft()
    if (level, (y, x)) == (0, end):
      return score
    if (level, y, x) in visited:
      continue
    visited.add((level, y, x))
    for j, i in t.iter_neigh4(y, x):
      if t[j][i] == "." and (level, j, i) not in visited:
        vnext.append((score + 1, level, (j, i)))
    if (y, x) in teleport:
      j, i = teleport[(y, x)]
      if (y in yborder) or (x in xborder):
        if ((add(level, - 1), j, i) not in visited) and (level > add(-1, 1)):
          vnext.append((score + 1, add(level, -1), (j, i)))
      else:
        if (add(level, + 1), j, i) not in visited:
          vnext.append((score + 1, add(level, +1), (j, i)))

def build_table(lines):
  t = aoc.Table([list(line) for line in lines])
  return t.grow(" ")

t = build_table([line.rstrip("\n") for line in sys.stdin])
teleport, start, end = build_maze(t)
aoc.cprint(solve(t, teleport, start, end, lambda a, b: a))
aoc.cprint(solve(t, teleport, start, end, lambda a, b: a + b))
