import sys
import aoc

def original_path(t):
  for j, i in t.iter_all():
    if t[j][i] == "^":
      start = j * 1j + i
      t[j][i] = "."
      break
  vdir = -1j
  visited, pos = set(), start
  while t.cvalid(pos):
    visited.add((pos, vdir))
    while t.cvalid(pos + vdir) and t.get(pos + vdir) == "#":
      vdir *= 1j
    pos += vdir
  return visited, start

def is_loop(t, start):
  pos = start
  vdir = -1j
  visited = set()
  while t.cvalid(pos) and (pos, vdir) not in visited:
    visited.add((pos, vdir))
    while t.cvalid(pos + vdir) and t.get(pos + vdir) == "#":
      vdir *= 1j
    pos += vdir
  return t.cvalid(pos)

def find_blockers(t, visited, start):
  ans = 0
  for cpos in set(cpos for cpos, vdir in visited):
    t.put(cpos, "#")
    if is_loop(t, start):
      ans += 1
    t.put(cpos, ".")
  return ans

t = aoc.Table.read()
visited, start = original_path(t)
aoc.cprint(len(set(cpos for cpos, vdir in visited)))
aoc.cprint(find_blockers(t, visited, start))
