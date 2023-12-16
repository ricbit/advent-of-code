import sys
import re
import itertools
import math
import aoc

def count(m, pos, vdir):
    tiles = [(pos, vdir)]
    visited = set()
    while tiles:  
      pos, vdir = tiles.pop()
      pos += vdir
      x, y = int(pos.real), int(pos.imag)
      vx, vy = int(vdir.real), int(vdir.imag)
      if not m.valid(y, x):
        continue
      if (y,x,vy,vx) in visited:
        continue
      visited.add((y,x,vy,vx))
      if m[y][x] == ".":
        tiles.append((pos, vdir))
      elif m[y][x] == "|":
        if vdir.imag == 0:
          tiles.append((pos, 1J))
          tiles.append((pos, -1J))
        else:
          tiles.append((pos, vdir))
      elif m[y][x] == "-":
        if vdir.real == 0:
          tiles.append((pos, 1))
          tiles.append((pos, -1))
        else:
          tiles.append((pos, vdir))
      elif m[y][x] == "\\":
        if vdir.imag == 0:
          tiles.append((pos, vdir * 1J))
        else:
          tiles.append((pos, vdir * -1J))
      elif m[y][x] == "/":
        if vdir.imag == 0:
          tiles.append((pos, vdir * -1J))
        else:
          tiles.append((pos, vdir * 1J))

    v = set([(y,x) for y,x,vy,vx in visited])
    ans = 0
    for j in range(m.h):
      r = []
      for i in range(m.w):
        if (j, i) in v:
          r.append("*")
          ans += 1
        else:
          r.append(".")
    return ans

def all_rays(m):
  for j in range(m.h):
    yield count(m, -1 + j * 1J, 1)
    yield count(m, m.w + j * 1J, -1)
  for i in range(m.w):
    yield count(m, -1J + i, 1J)
    yield count(m, m.h * 1J + i, -1J)
    

m = aoc.Table.read()
print(count(m,-1,1))
print(max(all_rays(m)))

